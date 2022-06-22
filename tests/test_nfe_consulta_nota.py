import unittest
from unittest.mock import patch

from pynfe.processamento.comunicacao import ComunicacaoSefaz
from pynfe.utils.flags import NAMESPACE_NFE
from lxml import etree

from tests.mocks.fake_xml import (
    FakeConsultaNotaAutorizada,
    FakeConsultaNotaComRejeicao
)
from tests.mocks.valid_xml import (
    ConsultaNotaAutorizada,
    ConsultaNotaComRejeicao
)


class ConsultaNotaTestCase(unittest.TestCase):

    path_certificado = 'certificado.pfx'
    senha_certificado = b'123456'
    homologacao = True
    uf = '51'  # 51=MT
    ns = {'ns': NAMESPACE_NFE}

    @patch(
        'pynfe.processamento.comunicacao.ComunicacaoSefaz.consulta_nota',
        return_value=FakeConsultaNotaAutorizada()
    )
    def test_retorno_da_consulta_nota_autorizada(self, mock_consulta_nota_autorizada):

        xml_retorno_esperado = ConsultaNotaAutorizada.__str__(self)

        nota = ComunicacaoSefaz(
            uf=self.uf,
            certificado=self.path_certificado,
            certificado_senha=self.senha_certificado,
            homologacao=self.homologacao
        )

        # Testa se o mock foi chamado -> False
        self.assertFalse(mock_consulta_nota_autorizada.called)

        # Chama o status_servico() para mockar em mock_status_servico()
        chave = '35100610142785000190551100000000014259062380'
        resposta = nota.consulta_nota('nfe', chave)

        # Testa se o mock foi chamado -> True
        self.assertTrue(mock_consulta_nota_autorizada.called)

        # Tratamento da resposta XML
        resp = etree.fromstring(resposta.content)
        resultado = etree.tostring(resp, encoding='unicode')

        # Testa se o XML é o mesmo
        self.assertEqual(xml_retorno_esperado, resultado)

        # Testa campos específicos do retorno
        raiz = resp.xpath('ns:protNFe', namespaces=self.ns)[0]
        xml_status = raiz.xpath('ns:infProt/ns:cStat', namespaces=self.ns)[0].text
        xml_motivo = raiz.xpath('ns:infProt/ns:xMotivo', namespaces=self.ns)[0].text
        xml_chave = raiz.xpath('ns:infProt/ns:chNFe', namespaces=self.ns)[0].text
        self.assertEqual('100', xml_status)
        self.assertEqual('Autorizado o uso da NF-e', xml_motivo)
        self.assertEqual(chave, xml_chave)

    @patch(
        'pynfe.processamento.comunicacao.ComunicacaoSefaz.consulta_nota',
        return_value=FakeConsultaNotaComRejeicao()
    )
    def test_retorno_da_consulta_nota_com_rejeicao(self, mock_consulta_nota_com_rejeicao):

        xml_retorno_esperado = ConsultaNotaComRejeicao.__str__(self)

        nota = ComunicacaoSefaz(
            uf=self.uf,
            certificado=self.path_certificado,
            certificado_senha=self.senha_certificado,
            homologacao=self.homologacao
        )

        # Testa se o mock foi chamado -> False
        self.assertFalse(mock_consulta_nota_com_rejeicao.called)

        # Chama o status_servico() para mockar em mock_status_servico()
        chave = '35100610142785000190551100000000014259062380'
        resposta = nota.consulta_nota('nfe', chave)

        # Testa se o mock foi chamado -> True
        self.assertTrue(mock_consulta_nota_com_rejeicao.called)

        # Tratamento da resposta XML
        resp = etree.fromstring(resposta.content)
        resultado = etree.tostring(resp, encoding='unicode')

        # Testa se o XML é o mesmo
        self.assertEqual(xml_retorno_esperado, resultado)

        # Testa campos específicos do retorno
        xml_status = resp.xpath('ns:cStat', namespaces=self.ns)[0].text
        xml_motivo = resp.xpath('ns:xMotivo', namespaces=self.ns)[0].text
        xml_chave = resp.xpath('ns:chNFe', namespaces=self.ns)[0].text
        self.assertEqual('217', xml_status)
        self.assertEqual('Rejeicao: NF-e nao consta na base de dados da SEFAZ', xml_motivo)
        self.assertEqual(chave, xml_chave)


if __name__ == '__main__':
    unittest.main()
