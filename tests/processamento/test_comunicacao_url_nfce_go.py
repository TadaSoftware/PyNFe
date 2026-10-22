#!/usr/bin/env python
# *-* encoding: utf8 *-*
"""Regression tests for the GO NFC-e WEBSERVICE host (autorizador, not consulta portal).

GO serves the public consultation portal (``nfeweb.sefaz.go.gov.br``, destination of
``<qrCode>``) and the SOAP authorizer (``nfe.sefaz.go.gov.br``) from
different hosts. Pointing the webservice URL at the consultation portal does NOT produce
a SEFAZ rejeicao: the portal answers a BigIP redirect plus HTML, so the invoice never gets
a verdict at all and every emission fails as a transport error. These tests pin the
authorizer host for NFC-e to the same host used for NF-e, and keep the QR host separate.
See DEV-2468.
"""

import unittest

from pynfe.processamento.comunicacao import ComunicacaoSefaz
from pynfe.utils.webservices import NFCE, NFE, qrcode_host

CONSULTAS = ["AUTORIZACAO", "STATUS", "EVENTOS", "INUTILIZACAO", "CHAVE"]

URL_AUTORIZACAO_PRODUCAO = "https://nfe.sefaz.go.gov.br/nfe/services/NFeAutorizacao4?wsdl"
URL_AUTORIZACAO_HOMOLOGACAO = "https://homolog.sefaz.go.gov.br/nfe/services/NFeAutorizacao4?wsdl"


def _comunicacao(homologacao):
    return ComunicacaoSefaz(
        uf="go",
        certificado="./tests/certificado.pfx",
        certificado_senha=bytes("123456", "utf-8"),
        homologacao=homologacao,
    )


class UrlWebserviceNFCeGoTestCase(unittest.TestCase):
    def test_autorizacao_producao_aponta_para_autorizador(self):
        url = _comunicacao(homologacao=False)._get_url(modelo="nfce", consulta="AUTORIZACAO")
        self.assertEqual(url, URL_AUTORIZACAO_PRODUCAO)

    def test_autorizacao_homologacao_aponta_para_autorizador(self):
        url = _comunicacao(homologacao=True)._get_url(modelo="nfce", consulta="AUTORIZACAO")
        self.assertEqual(url, URL_AUTORIZACAO_HOMOLOGACAO)

    def test_nfce_usa_o_mesmo_host_da_nfe(self):
        for homologacao in (False, True):
            nfce = _comunicacao(homologacao=homologacao)
            nfe = _comunicacao(homologacao=homologacao)
            for consulta in CONSULTAS:
                url_nfce = nfce._get_url(modelo="nfce", consulta=consulta)
                url_nfe = nfe._get_url(modelo="nfe", consulta=consulta)
                self.assertEqual(
                    url_nfce.split("/")[2],
                    url_nfe.split("/")[2],
                    f"host de {consulta} (homologacao={homologacao}) divergiu entre nfce e nfe",
                )

    def test_webservice_nunca_usa_host_do_portal_de_consulta(self):
        for homologacao in (False, True):
            comunicacao = _comunicacao(homologacao=homologacao)
            for consulta in CONSULTAS:
                url = comunicacao._get_url(modelo="nfce", consulta=consulta)
                self.assertNotIn("nfeweb", url, f"{consulta} aponta para o portal de consulta")


class QrcodeHostTestCase(unittest.TestCase):
    def test_go_mantem_host_do_portal_de_consulta(self):
        self.assertEqual(qrcode_host("GO", producao=True), "https://nfeweb.")
        self.assertEqual(qrcode_host("GO", producao=False), "https://nfewebhomolog.")

    def test_uf_sem_host_de_qr_cai_no_host_de_webservice(self):
        self.assertEqual(qrcode_host("SE", producao=True), NFCE["SE"]["HTTPS"])
        self.assertEqual(qrcode_host("SE", producao=False), NFCE["SE"]["HOMOLOGACAO"])

    def test_sp_e_am_mantem_o_host_de_qr_historico(self):
        # SP e AM tinham o host de QR montado a partir da chave de webservice; os literais
        # abaixo travam a equivalencia byte a byte apos a separacao das chaves. Sao literais
        # de proposito: derivar o esperado de NFCE[uf]["HTTPS"] tornaria a trava vazia
        # justamente quando essa chave for corrigida.
        self.assertEqual(qrcode_host("SP", producao=True), "https://www.")
        self.assertEqual(qrcode_host("SP", producao=False), "https://www.homologacao.")
        self.assertEqual(qrcode_host("AM", producao=True), "https://sistemas.")
        self.assertEqual(qrcode_host("AM", producao=False), "https://sistemas.")

    def test_chaves_de_qr_e_de_webservice_de_go_sao_distintas(self):
        self.assertEqual(NFCE["GO"]["HTTPS"], NFE["GO"]["HTTPS"])
        self.assertEqual(NFCE["GO"]["HOMOLOGACAO"], NFE["GO"]["HOMOLOGACAO"])
        self.assertNotEqual(NFCE["GO"]["HTTPS"], NFCE["GO"]["QR_HOST"])
        self.assertNotEqual(NFCE["GO"]["HOMOLOGACAO"], NFCE["GO"]["QR_HOST_HOMOLOGACAO"])


if __name__ == "__main__":
    unittest.main()
