#!/usr/bin/env python
# *-* encoding: utf8 *-*
"""Regression tests for the Goias (GO) NFC-e ``<qrCode>`` host.

Informe Tecnico 2025.003 moved the GO NFC-e QR Code host from the old
``nfe.sefaz.go.gov.br`` / ``homolog.sefaz.go.gov.br`` subdomains to
``nfeweb.sefaz.go.gov.br`` (producao) and ``nfewebhomolog.sefaz.go.gov.br``
(homologacao). Emitting with the old host triggers SEFAZ rejeicao 395
("Informado QR-Code para NFC-e com formato invalido"). These tests pin the
``<qrCode>`` base so the host can never silently regress to the rejected
subdomain again. See DEV-2177.

The ``<urlChave>`` is deliberately NOT asserted against this host: IT 2025.003
defines only the QR Code address, and emitting it as ``urlChave`` is what made GO
reject 878. That field has its own registry and its own tests in
``test_nfce_urlchave_por_uf.py`` (DEV-2468).
"""

import unittest

from lxml import etree

from pynfe.processamento.serializacao import SerializacaoQrcode
from pynfe.utils.flags import NAMESPACE_NFE, NAMESPACE_SIG

# cUF for Goias.
CUF_GO = "52"
# Producao = 1, Homologacao = 2 (NFe ide/tpAmb).
TP_AMB_PRODUCAO = "1"
TP_AMB_HOMOLOGACAO = "2"

QRCODE_HOST_PRODUCAO = "https://nfeweb.sefaz.go.gov.br/"
QRCODE_HOST_HOMOLOGACAO = "https://nfewebhomolog.sefaz.go.gov.br/"


class QrcodeGoNFCeTestCase(unittest.TestCase):
    """Exercises ``SerializacaoQrcode.gerar_qrcode`` for the GO branch."""

    def _build_nfe_go(self, tp_amb):
        """Build a minimal signed-NFe etree for GO with the fields gerar_qrcode reads."""
        chave = CUF_GO + "0" * 42  # 44-digit access key starting with cUF 52.
        xml = (
            f'<NFe xmlns="{NAMESPACE_NFE}">'
            f'<infNFe Id="NFe{chave}">'
            f"<ide>"
            f"<cUF>{CUF_GO}</cUF>"
            f"<dhEmi>2025-01-14T12:00:00-03:00</dhEmi>"
            f"<tpAmb>{tp_amb}</tpAmb>"
            f"</ide>"
            f"<dest><CPF>12345678900</CPF></dest>"
            f"<total><ICMSTot><vNF>10.00</vNF></ICMSTot></total>"
            f"</infNFe>"
            f'<Signature xmlns="{NAMESPACE_SIG}">'
            f"<SignedInfo><Reference>"
            f"<DigestValue>ABCDEF==</DigestValue>"
            f"</Reference></SignedInfo>"
            f"</Signature>"
            f"</NFe>"
        )
        return etree.fromstring(xml.encode())

    def _gerar(self, tp_amb):
        nfe = self._build_nfe_go(tp_amb)
        nfe, qrcode = SerializacaoQrcode().gerar_qrcode("000001", "CSC123", nfe, return_qr=True)
        supl = nfe.find("infNFeSupl")
        self.assertIsNotNone(supl, "infNFeSupl deve ser inserido")
        url_chave = supl.find("urlChave").text
        # qrCode esta dentro de CDATA; o valor retornado por gerar_qrcode e o mesmo texto.
        return qrcode, url_chave

    def test_qrcode_producao_usa_host_nfeweb(self):
        qrcode, _ = self._gerar(TP_AMB_PRODUCAO)
        self.assertTrue(
            qrcode.startswith(QRCODE_HOST_PRODUCAO),
            f"qrCode de producao deve comecar com {QRCODE_HOST_PRODUCAO}, veio: {qrcode}",
        )
        # Garante que nao reverteu para o subdominio rejeitado (rejeicao 395).
        self.assertNotIn("https://nfe.sefaz.go.gov.br", qrcode)

    def test_qrcode_homologacao_usa_host_nfewebhomolog(self):
        qrcode, _ = self._gerar(TP_AMB_HOMOLOGACAO)
        self.assertTrue(
            qrcode.startswith(QRCODE_HOST_HOMOLOGACAO),
            f"qrCode de homologacao deve comecar com {QRCODE_HOST_HOMOLOGACAO}, veio: {qrcode}",
        )
        self.assertNotIn("https://homolog.sefaz.go.gov.br", qrcode)


if __name__ == "__main__":
    unittest.main()
