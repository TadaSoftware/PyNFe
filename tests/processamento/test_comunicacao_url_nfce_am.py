#!/usr/bin/env python
# *-* encoding: utf8 *-*
"""Regression tests for the AM NFC-e WEBSERVICE host (autorizador, not consulta portal).

Same defect class as GO (DEV-2468): ``NFCE["AM"]["HTTPS"]`` carried the consultation-portal
prefix ``https://sistemas.`` while the endpoint paths already embed the ``nfce.`` subdomain,
so every AM NFC-e webservice URL resolved to ``sistemas.nfce.sefaz.am.gov.br`` — a host that
does not exist (NXDOMAIN), i.e. AM emission could not even open a connection. Two independent
facts settle the correct prefix:

- ``NFCE["AM"]["HOMOLOGACAO"] = "https://hom"`` concatenates to ``homnfce.sefaz.am.gov.br``,
  which resolves and demands a client certificate (TLS alert 42 with "Acceptable client
  certificate CA names", cert ``CN=*.sefaz.am.gov.br``, ``O=SECRETARIA DE ESTADO DA FAZENDA
  SEFAZ``) — the mTLS SOAP signature. So the webservice paths are meant to be prefixed with
  the scheme only, and production must be ``https://`` → ``nfce.sefaz.am.gov.br``, which shows
  the same certificate and the same client-certificate demand.
- ``sistemas.sefaz.am.gov.br`` completes the TLS handshake with no client certificate and a
  plain ``CN=sistemas.sefaz.am.gov.br`` cert — it is the public portal, correct for
  ``<qrCode>`` and wrong for SOAP.

The QR host stays on ``https://sistemas.`` via ``QR_HOST``; the byte-identity of AM's
``<qrCode>``/``<urlChave>`` is locked in ``tests/test_nfce_qrcode_hosts_por_uf.py``.
"""

import unittest

from pynfe.processamento.comunicacao import ComunicacaoSefaz
from pynfe.utils.webservices import NFCE, qrcode_host

CONSULTAS = ["AUTORIZACAO", "STATUS", "EVENTOS", "INUTILIZACAO", "CHAVE", "RECIBO"]

HOST_AUTORIZADOR_PRODUCAO = "nfce.sefaz.am.gov.br"
HOST_AUTORIZADOR_HOMOLOGACAO = "homnfce.sefaz.am.gov.br"

URL_AUTORIZACAO_PRODUCAO = "https://nfce.sefaz.am.gov.br/nfce-services/services/NfeAutorizacao4"
URL_AUTORIZACAO_HOMOLOGACAO = (
    "https://homnfce.sefaz.am.gov.br/nfce-services/services/NfeAutorizacao4"
)


def _comunicacao(homologacao):
    return ComunicacaoSefaz(
        uf="am",
        certificado="./tests/certificado.pfx",
        certificado_senha=bytes("123456", "utf-8"),
        homologacao=homologacao,
    )


class UrlWebserviceNFCeAmTestCase(unittest.TestCase):
    def test_autorizacao_producao_aponta_para_autorizador(self):
        url = _comunicacao(homologacao=False)._get_url(modelo="nfce", consulta="AUTORIZACAO")
        self.assertEqual(url, URL_AUTORIZACAO_PRODUCAO)

    def test_autorizacao_homologacao_aponta_para_autorizador(self):
        url = _comunicacao(homologacao=True)._get_url(modelo="nfce", consulta="AUTORIZACAO")
        self.assertEqual(url, URL_AUTORIZACAO_HOMOLOGACAO)

    def test_host_de_webservice_e_o_mesmo_em_todas_as_consultas(self):
        for homologacao, host_esperado in (
            (False, HOST_AUTORIZADOR_PRODUCAO),
            (True, HOST_AUTORIZADOR_HOMOLOGACAO),
        ):
            comunicacao = _comunicacao(homologacao=homologacao)
            for consulta in CONSULTAS:
                url = comunicacao._get_url(modelo="nfce", consulta=consulta)
                self.assertEqual(
                    url.split("/")[2],
                    host_esperado,
                    f"host de {consulta} (homologacao={homologacao}) divergiu do autorizador",
                )

    def test_webservice_nunca_usa_host_do_portal_de_consulta(self):
        for homologacao in (False, True):
            comunicacao = _comunicacao(homologacao=homologacao)
            for consulta in CONSULTAS:
                url = comunicacao._get_url(modelo="nfce", consulta=consulta)
                self.assertNotIn("sistemas.", url, f"{consulta} aponta para o portal de consulta")

    def test_chaves_de_qr_e_de_webservice_de_am_sao_distintas(self):
        self.assertEqual(qrcode_host("AM", producao=True), "https://sistemas.")
        self.assertNotEqual(NFCE["AM"]["HTTPS"], NFCE["AM"]["QR_HOST"])


if __name__ == "__main__":
    unittest.main()
