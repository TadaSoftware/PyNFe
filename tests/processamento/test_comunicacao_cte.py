import unittest
from unittest.mock import MagicMock
from pynfe.processamento.comunicacao import ComunicacaoCTe
from pynfe.utils import etree


class TestComunicacaoCTe(unittest.TestCase):
    """
    Testa a classe ComunicacaoCTe
    """

    def test_consulta(self):
        chave = "35190912345678000123570010000000011000000018"
        url_esperada = "https://url.ficticia/consulta"
        resposta_mock = "<resposta>ok</resposta>"

        comunicacao = ComunicacaoCTe(
            uf="rs",
            certificado="./tests/certificado.pfx",
            certificado_senha=bytes("123456", "utf-8"),
            homologacao=True,
        )
        comunicacao._versao = "3.00"
        comunicacao._ambiente = 1
        comunicacao._get_url = MagicMock(return_value=url_esperada)
        comunicacao._construir_xml_soap = MagicMock(
            side_effect=lambda metodo, xml: f"<soap>{etree.tostring(xml).decode()}</soap>"
        )
        comunicacao._post = MagicMock(return_value=resposta_mock)

        resposta = comunicacao.consulta(chave)
        xml_gerado = comunicacao._construir_xml_soap.call_args[0][1]
        chave_extraida = xml_gerado.find(".//{*}chCTe").text

        comunicacao._get_url.assert_called_once_with("CONSULTA")
        comunicacao._construir_xml_soap.assert_called_once()
        comunicacao._post.assert_called_once_with(
            url_esperada, f"<soap>{etree.tostring(xml_gerado).decode()}</soap>"
        )
        self.assertEqual(resposta, resposta_mock)
        self.assertEqual(chave_extraida, chave)
        self.assertEqual(xml_gerado.find(".//{*}tpAmb").text, "1")
        self.assertEqual(xml_gerado.find(".//{*}xServ").text, "CONSULTAR")
        self.assertTrue(xml_gerado.tag.endswith("consSitCTe"))
        self.assertIn("xmlns", xml_gerado.attrib)


if __name__ == "__main__":
    unittest.main()
