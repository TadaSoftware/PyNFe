#!/usr/bin/env python
# *-* encoding: utf8 *-*
"""Pins the ``<qrCode>`` host of every UF whose branch reads a host prefix.

The GO fix (DEV-2468) routed those branches through ``webservices.qrcode_host`` so the QR
host can no longer be taken from the authorizer keys. These tests lock the resulting URLs
for SP, AM, BA and MG in both environments, which is what makes the refactor verifiable as
byte-identical outside GO.

``urlChave`` is asserted here only as the value that pairs with each of those QR hosts; the
field's own registry, property tests and non-regression set live in
``test_nfce_urlchave_por_uf.py``.
"""

import unittest

from lxml import etree

from pynfe.processamento.serializacao import SerializacaoQrcode
from pynfe.utils.flags import CODIGOS_ESTADOS, NAMESPACE_NFE, NAMESPACE_SIG

TP_AMB_PRODUCAO = "1"
TP_AMB_HOMOLOGACAO = "2"

# uf -> (prefixo esperado do qrCode, urlChave esperada) por ambiente.
ESPERADO = {
    "SP": {
        TP_AMB_PRODUCAO: (
            "https://www.nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?",
            "https://www.nfce.fazenda.sp.gov.br/consulta",
        ),
        TP_AMB_HOMOLOGACAO: (
            "https://www.homologacao.nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/"
            "ConsultaQRCode.aspx?",
            "https://www.homologacao.nfce.fazenda.sp.gov.br/consulta",
        ),
    },
    "AM": {
        TP_AMB_PRODUCAO: (
            "https://sistemas.sefaz.am.gov.br/nfceweb/consultarNFCe.jsp?",
            "https://sistemas.sefaz.am.gov.br/nfceweb/formConsulta.do",
        ),
        TP_AMB_HOMOLOGACAO: (
            "https://sistemas.sefaz.am.gov.br/nfceweb-hom/consultarNFCe.jsp?",
            "https://sistemas.sefaz.am.gov.br/nfceweb/formConsulta.do",
        ),
    },
    "BA": {
        TP_AMB_PRODUCAO: (
            "http://nfe.sefaz.ba.gov.br/servicos/nfce/qrcode.aspx?",
            # ACBr [NFCe_BA_P] URL-ConsultaNFCe_2.00; o hinternet e o valor de homologacao,
            # emitido em producao ate DEV-2468.
            "http://www.sefaz.ba.gov.br/nfce/consulta",
        ),
        TP_AMB_HOMOLOGACAO: (
            "http://hnfe.sefaz.ba.gov.br/servicos/nfce/qrcode.aspx?",
            "http://hinternet.sefaz.ba.gov.br/nfce/consulta",
        ),
    },
    "MG": {
        TP_AMB_PRODUCAO: (
            "https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml",
            "https://nfce.fazenda.mg.gov.br/portalnfce",
        ),
        TP_AMB_HOMOLOGACAO: (
            "https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml",
            "https://hnfce.fazenda.mg.gov.br/portalnfce",
        ),
    },
}


def _nfe(uf, tp_amb):
    cuf = CODIGOS_ESTADOS[uf]
    chave = cuf + "0" * 42
    xml = (
        f'<NFe xmlns="{NAMESPACE_NFE}">'
        f'<infNFe Id="NFe{chave}">'
        f"<ide><cUF>{cuf}</cUF><dhEmi>2025-01-14T12:00:00-03:00</dhEmi>"
        f"<tpAmb>{tp_amb}</tpAmb></ide>"
        f"<dest><CPF>12345678900</CPF></dest>"
        f"<total><ICMSTot><vNF>10.00</vNF></ICMSTot></total>"
        f"</infNFe>"
        f'<Signature xmlns="{NAMESPACE_SIG}"><SignedInfo><Reference>'
        f"<DigestValue>ABCDEF==</DigestValue>"
        f"</Reference></SignedInfo></Signature>"
        f"</NFe>"
    )
    return etree.fromstring(xml.encode())


class QrcodeHostsPorUfTestCase(unittest.TestCase):
    def test_hosts_de_qrcode_e_urlchave(self):
        for uf, ambientes in ESPERADO.items():
            for tp_amb, (prefixo_qr, url_chave_esperada) in ambientes.items():
                with self.subTest(uf=uf, tpAmb=tp_amb):
                    nfe, qrcode = SerializacaoQrcode().gerar_qrcode(
                        "000001", "CSC123", _nfe(uf, tp_amb), return_qr=True
                    )
                    url_chave = nfe.find("infNFeSupl").find("urlChave").text
                    self.assertTrue(
                        qrcode.startswith(prefixo_qr),
                        f"{uf}/{tp_amb}: qrCode deveria comecar com {prefixo_qr}, veio {qrcode}",
                    )
                    self.assertEqual(url_chave, url_chave_esperada)


if __name__ == "__main__":
    unittest.main()
