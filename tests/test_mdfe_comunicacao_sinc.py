#!/usr/bin/env python
# *-* encoding: utf8 *-*
"""Testes do envio sincrono do MDF-e (MDFeRecepcaoSinc) e da serializacao do valePed."""

import base64
import gzip
import unittest
from decimal import Decimal
from unittest import mock

from pynfe.entidades.manifesto import (
    ManifestoCondutor,
    ManifestoRodoviario,
    ManifestoVeiculoTracao,
)
from pynfe.processamento.comunicacao import ComunicacaoMDFe
from pynfe.processamento.serializacao import SerializacaoMDFe
from pynfe.utils import etree
from pynfe.utils.flags import NAMESPACE_MDFE

NS = {"ns": NAMESPACE_MDFE}


def _fake_response(status_code, text):
    response = mock.Mock()
    response.status_code = status_code
    response.text = text
    response.content = text.encode("utf-8")
    return response


def _soap_response(ret_mdfe_xml):
    return (
        '<?xml version="1.0" encoding="utf-8"?>'
        '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
        "<soap:Body>"
        '<mdfeRecepcaoResult xmlns="http://www.portalfiscal.inf.br/mdfe/wsdl/MDFeRecepcaoSinc">'
        + ret_mdfe_xml
        + "</mdfeRecepcaoResult>"
        "</soap:Body>"
        "</soap:Envelope>"
    )


def _manifesto_assinado_fake():
    mdfe = etree.Element("MDFe", xmlns=NAMESPACE_MDFE)
    inf = etree.SubElement(
        mdfe, "infMDFe", Id="MDFe51210199999999000199580009200000000011000000008"
    )
    etree.SubElement(inf, "ide")
    return mdfe


class ComunicacaoMDFeRecepcaoSincTestCase(unittest.TestCase):
    def setUp(self):
        self.con = ComunicacaoMDFe("rj", "certificado.pfx", "senha", homologacao=True)
        self.manifesto = _manifesto_assinado_fake()

    def test_envelope_sinc_envia_mdfe_gzip_base64_como_texto(self):
        """O servico sincrono exige o MDFe gzip+base64 como texto de mdfeDadosMsg."""
        with mock.patch.object(self.con, "_post") as post:
            post.return_value = _fake_response(400, "")
            self.con.autorizacao(self.manifesto, ind_sinc=1)

        (url, envelope), kwargs = post.call_args
        self.assertIn("RecepcaoSinc", url)
        self.assertEqual(kwargs.get("content_type"), b"application/soap+xml; charset=utf-8;")

        dados_msg = envelope.xpath("//*[local-name()='Body']/*[local-name()='mdfeDadosMsg']")[0]
        # sem envelope enviMDFe/idLote e sem elementos filhos
        self.assertEqual(len(dados_msg), 0)
        payload = gzip.decompress(base64.b64decode(dados_msg.text))
        self.assertEqual(payload, etree.tostring(self.manifesto))
        raiz_payload = etree.fromstring(payload)
        self.assertEqual(etree.QName(raiz_payload).localname, "MDFe")

    def test_sinc_autorizado_retorna_mdfe_proc(self):
        ret = (
            '<retMDFe versao="3.00" xmlns="http://www.portalfiscal.inf.br/mdfe">'
            "<tpAmb>2</tpAmb><cUF>33</cUF><cStat>104</cStat><xMotivo>Lote processado</xMotivo>"
            '<protMDFe versao="3.00"><infProt><tpAmb>2</tpAmb><cStat>100</cStat>'
            "<xMotivo>Autorizado o uso do MDF-e</xMotivo>"
            "<nProt>933210000000000</nProt></infProt></protMDFe>"
            "</retMDFe>"
        )
        with mock.patch.object(self.con, "_post") as post:
            post.return_value = _fake_response(200, _soap_response(ret))
            resultado = self.con.autorizacao(self.manifesto, ind_sinc=1)

        self.assertEqual(resultado[0], 0)
        proc = resultado[1]
        self.assertEqual(etree.QName(proc).localname, "mdfeProc")
        self.assertEqual(
            proc.xpath("ns:protMDFe/ns:infProt/ns:cStat", namespaces=NS)[0].text, "100"
        )
        self.assertEqual(len(proc.xpath("*[local-name()='MDFe']")), 1)

    def test_sinc_rejeicao_nivel_retmdfe_sem_protmdfe(self):
        """Rejeicao 580 (falha de schema do modal) vem sem protMDFe."""
        ret = (
            '<retMDFe versao="3.00" xmlns="http://www.portalfiscal.inf.br/mdfe">'
            "<tpAmb>2</tpAmb><cUF>33</cUF><cStat>580</cStat>"
            "<xMotivo>Rejeição: Falha no Schema XML específico para o modal</xMotivo>"
            "</retMDFe>"
        )
        with mock.patch.object(self.con, "_post") as post:
            post.return_value = _fake_response(200, _soap_response(ret))
            resultado = self.con.autorizacao(self.manifesto, ind_sinc=1)

        self.assertEqual(resultado[0], 1)
        ret_mdfe = resultado[1]
        self.assertEqual(etree.QName(ret_mdfe).localname, "retMDFe")
        self.assertEqual(ret_mdfe.xpath("ns:cStat", namespaces=NS)[0].text, "580")

    def test_sinc_rejeicao_nivel_protmdfe(self):
        ret = (
            '<retMDFe versao="3.00" xmlns="http://www.portalfiscal.inf.br/mdfe">'
            "<tpAmb>2</tpAmb><cUF>33</cUF><cStat>104</cStat><xMotivo>Lote processado</xMotivo>"
            '<protMDFe versao="3.00"><infProt><tpAmb>2</tpAmb><cStat>204</cStat>'
            "<xMotivo>Rejeição: Duplicidade de MDF-e</xMotivo></infProt></protMDFe>"
            "</retMDFe>"
        )
        with mock.patch.object(self.con, "_post") as post:
            post.return_value = _fake_response(200, _soap_response(ret))
            resultado = self.con.autorizacao(self.manifesto, ind_sinc=1)

        self.assertEqual(resultado[0], 1)
        ret_mdfe = resultado[1]
        self.assertEqual(etree.QName(ret_mdfe).localname, "retMDFe")
        self.assertEqual(
            ret_mdfe.xpath("ns:protMDFe/ns:infProt/ns:cStat", namespaces=NS)[0].text, "204"
        )

    def test_sinc_http_400_corpo_vazio_retorna_response_crua(self):
        with mock.patch.object(self.con, "_post") as post:
            post.return_value = _fake_response(400, "")
            resultado = self.con.autorizacao(self.manifesto, ind_sinc=1)

        self.assertEqual(resultado[0], 1)
        self.assertIs(resultado[1], post.return_value)

    def test_sinc_corpo_nao_parseavel_retorna_response_crua(self):
        with mock.patch.object(self.con, "_post") as post:
            post.return_value = _fake_response(200, "isso nao e xml")
            resultado = self.con.autorizacao(self.manifesto, ind_sinc=1)

        self.assertEqual(resultado[0], 1)
        self.assertIs(resultado[1], post.return_value)


class SerializacaoValePedTestCase(unittest.TestCase):
    def _modal(self, **kwargs):
        condutor = ManifestoCondutor(nome_motorista="JOAO DA SILVA", cpf_motorista="12345678912")
        veiculo_tracao = [
            ManifestoVeiculoTracao(
                cInt="001",
                placa="ABC1234",
                RENAVAM="123456789",
                tara=Decimal("5000"),
                capKG=Decimal("4500"),
                capM3=Decimal("400"),
                proprietario=None,
                condutor=[condutor],
                tpRod="01",
                tpCar="02",
                UF="MT",
            )
        ]
        params = dict(
            rntrc=None,
            ciot=[],
            pedagio=[],
            contratante=[],
            pagamento=None,
            veiculo_tracao=veiculo_tracao,
            veiculo_reboque=[],
        )
        params.update(kwargs)
        return ManifestoRodoviario(**params)

    def _serializar(self, modal):
        serializador = SerializacaoMDFe.__new__(SerializacaoMDFe)
        serializador._versao = "3.00"
        return serializador._serializar_modal_rodoviario(modal, retorna_string=False)

    def test_vale_ped_omitido_sem_disp(self):
        """valePed vazio e rejeitado pelo schema do modal (cStat 580) e deve ser omitido."""
        raiz = self._serializar(self._modal(rntrc="12345678"))
        self.assertEqual(len(raiz.xpath("rodo/infANTT/valePed")), 0)
        self.assertEqual(len(raiz.xpath("rodo/infANTT/RNTRC")), 1)

    def test_inf_antt_omitido_quando_totalmente_vazio(self):
        raiz = self._serializar(self._modal())
        self.assertEqual(len(raiz.xpath("rodo/infANTT")), 0)
        self.assertEqual(len(raiz.xpath("rodo/veicTracao")), 1)


if __name__ == "__main__":
    unittest.main()
