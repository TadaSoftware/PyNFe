import unittest

import re
import pyxb.namespace

from pynfe.entidades.notafiscal import NotaFiscalServico
from tests.test_nfse_serializacao import SerializacaoNFSeTest


class SerializacaoNFSeGinfesTestCase(unittest.TestCase):
    def test_notafiscal_geral(self):
        nfse = SerializacaoNFSeTest.get_notafiscal_servico()
        nfse_xml = SerializacaoNFSeTest.serializa_nfse(nfse, 'ginfes')

        # TODO: assinatura digital
        # config = SerializacaoNFSeTest.get_config()
        # nfse_xml_assinado = SerializacaoNFSeTest.assina_xml(config, nfse_xml)

        self.maxDiff = None
        result = self._get_nfse_esperada(nfse)

        nfse_xml = self._ajusta_xml_test(nfse_xml)
        result = self._ajusta_xml_test(nfse_xml)

        # Teste do conteúdo das tags do XML
        self.assertEqual(nfse_xml, result)

        # Testa a validação do XML com os schemas XSD
        # SerializacaoNFSeTest.validacao_com_xsd_do_xml_gerado_sem_processar(
        #     nfse_xml,
        #     nfse_xml_assinado,
        #     'servico_enviar_lote_rps_envio_v03.xsd',
        #     'pynfe/data/XSDs/NFS-e/Ginfes'
        # )

        # Limpa o Namespace para não gerar conflito com outros testes
        pyxb.namespace.Namespace._Namespace__Registry.clear()

    # a serialização gera os atributos xmlns:ns1 e xmlns:ns2
    # da tag ns1:EnviarLoteRpsEnvio em ordem randômica (!!!)
    def _ajusta_xml_test(self, xml: str) -> str:
        return re.sub(r'<(ns1:EnviarLoteRpsEnvio)[^>]*>', r'<\1>', xml)

    def _get_nfse_esperada(self, nfse: NotaFiscalServico) -> str:
        return SerializacaoNFSeTest.strip_xml(f"""
            <?xml version="1.0" ?>
            <ns1:EnviarLoteRpsEnvio xmlns:ns1="http://www.ginfes.com.br/servico_enviar_lote_rps_envio_v03.xsd" xmlns:ns2="http://www.ginfes.com.br/tipos_v03.xsd">
                <ns1:LoteRps Id="1">
                    <ns2:NumeroLote>1</ns2:NumeroLote>
                    <ns2:Cnpj>99999999999999</ns2:Cnpj>
                    <ns2:InscricaoMunicipal>000000</ns2:InscricaoMunicipal>
                    <ns2:QuantidadeRps>1</ns2:QuantidadeRps>
                    <ns2:ListaRps>
                    <ns2:Rps>
                        <ns2:InfRps Id="50">
                        <ns2:IdentificacaoRps>
                            <ns2:Numero>50</ns2:Numero>
                            <ns2:Serie>A1</ns2:Serie>
                            <ns2:Tipo>1</ns2:Tipo>
                        </ns2:IdentificacaoRps>
                        <ns2:DataEmissao>{nfse.data_emissao.isoformat()[:19]}</ns2:DataEmissao>
                        <ns2:NaturezaOperacao>1</ns2:NaturezaOperacao>
                        <ns2:OptanteSimplesNacional>1</ns2:OptanteSimplesNacional>
                        <ns2:IncentivadorCultural>2</ns2:IncentivadorCultural>
                        <ns2:Status>1</ns2:Status>
                        <ns2:Servico>
                            <ns2:Valores>
                            <ns2:ValorServicos>100.0</ns2:ValorServicos>
                            <ns2:ValorDeducoes>10.0</ns2:ValorDeducoes>
                            <ns2:ValorPis>10.0</ns2:ValorPis>
                            <ns2:ValorCofins>10.0</ns2:ValorCofins>
                            <ns2:ValorInss>10.0</ns2:ValorInss>
                            <ns2:ValorIr>10.0</ns2:ValorIr>
                            <ns2:ValorCsll>10.0</ns2:ValorCsll>
                            <ns2:IssRetido>1</ns2:IssRetido>
                            <ns2:ValorIss>10.0</ns2:ValorIss>
                            <ns2:ValorIssRetido>10.0</ns2:ValorIssRetido>
                            <ns2:OutrasRetencoes>10.0</ns2:OutrasRetencoes>
                            <ns2:BaseCalculo>10.0</ns2:BaseCalculo>
                            <ns2:Aliquota>10.0</ns2:Aliquota>
                            <ns2:ValorLiquidoNfse>10.0</ns2:ValorLiquidoNfse>
                            <ns2:DescontoIncondicionado>10.0</ns2:DescontoIncondicionado>
                            <ns2:DescontoCondicionado>10.0</ns2:DescontoCondicionado>
                            </ns2:Valores>
                            <ns2:ItemListaServico>0101</ns2:ItemListaServico>
                            <ns2:CodigoCnae>6201501</ns2:CodigoCnae>
                            <ns2:CodigoTributacaoMunicipio>1234</ns2:CodigoTributacaoMunicipio>
                            <ns2:Discriminacao>Mensalidade</ns2:Discriminacao>
                            <ns2:CodigoMunicipio>3149309</ns2:CodigoMunicipio>
                        </ns2:Servico>
                        <ns2:Prestador>
                            <ns2:Cnpj>99999999999999</ns2:Cnpj>
                            <ns2:InscricaoMunicipal>000000</ns2:InscricaoMunicipal>
                        </ns2:Prestador>
                        <ns2:Tomador>
                            <ns2:IdentificacaoTomador>
                            <ns2:CpfCnpj>
                                <ns2:Cnpj>99999999999999</ns2:Cnpj>
                            </ns2:CpfCnpj>
                            <ns2:InscricaoMunicipal>1234</ns2:InscricaoMunicipal>
                            </ns2:IdentificacaoTomador>
                            <ns2:RazaoSocial>NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL</ns2:RazaoSocial>
                            <ns2:Endereco>
                            <ns2:Endereco>Rua tal</ns2:Endereco>
                            <ns2:Numero>0</ns2:Numero>
                            <ns2:Complemento>Ao lado de lugar nenhum</ns2:Complemento>
                            <ns2:Bairro>Centro</ns2:Bairro>
                            <ns2:CodigoMunicipio>123</ns2:CodigoMunicipio>
                            <ns2:Uf>MG</ns2:Uf>
                            <ns2:Cep>33257010</ns2:Cep>
                            </ns2:Endereco>
                            <ns2:Contato>
                            <ns2:Telefone>12365478945</ns2:Telefone>
                            <ns2:Email>nome@email.com.br</ns2:Email>
                            </ns2:Contato>
                        </ns2:Tomador>
                        </ns2:InfRps>
                    </ns2:Rps>
                    </ns2:ListaRps>
                </ns1:LoteRps>
            </ns1:EnviarLoteRpsEnvio>
        """)


if __name__ == "__main__":
    unittest.main()
