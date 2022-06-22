import unittest
from unittest.mock import patch

from pynfe.processamento.comunicacao import ComunicacaoSefaz
from pynfe.utils.flags import NAMESPACE_NFE
from lxml import etree

from tests.mocks.fake_xml import FakeConsultaServico
from tests.mocks.valid_xml import ConsultaServico


class ConsultaServicoTestCase(unittest.TestCase):

    path_certificado = 'certificado.pfx'
    senha_certificado = b'123456'
    homologacao = True
    uf = '51'  # 51=MT
    ns = {'ns': NAMESPACE_NFE}

    @patch(
        'pynfe.processamento.comunicacao.ComunicacaoSefaz.status_servico',
        return_value=FakeConsultaServico()
    )
    def test_retorno_da_consulta_do_servico(self, mock_status_servico):

        xml_retorno_esperado = ConsultaServico.__str__(self)

        consulta_servico = ComunicacaoSefaz(
            uf=self.uf,
            certificado=self.path_certificado,
            certificado_senha=self.senha_certificado,
            homologacao=self.homologacao
        )

        # Testa se o mock foi chamado -> False
        self.assertFalse(mock_status_servico.called)

        # Chama o status_servico() para mockar em mock_status_servico()
        resposta = consulta_servico.status_servico('nfe')

        # Testa se o mock foi chamado -> True
        self.assertTrue(mock_status_servico.called)

        # Tratamento da resposta XML
        resp = etree.fromstring(resposta.content)
        resultado = etree.tostring(resp, encoding='unicode')

        # Testa se o XML é o mesmo
        self.assertEqual(xml_retorno_esperado, resultado)

        # Testa campos específicos do retorno
        xml_status = resp.xpath('ns:cStat', namespaces=self.ns)[0].text
        xml_motivo = resp.xpath('ns:xMotivo', namespaces=self.ns)[0].text
        self.assertEqual('107', xml_status)
        self.assertEqual('Servico em Operacao', xml_motivo)


if __name__ == '__main__':
    unittest.main()
