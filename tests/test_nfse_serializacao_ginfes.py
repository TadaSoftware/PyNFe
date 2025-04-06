import unittest

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscalServico
from pynfe.entidades.servico import Servico
from pynfe.processamento.serializacao import SerializacaoNfse
from pynfe.processamento.validacao import Validacao
from pynfe.utils import obter_codigo_por_municipio, etree
from pynfe.utils.flags import (
    CODIGO_BRASIL,
)
from decimal import Decimal
import datetime
import re
import pyxb.namespace


class SerializacaoNFSeGinfesTestCase(unittest.TestCase):
    """
    Imprimir o XML completo:
        print(etree.tostring(self.xml_assinado))

    """

    def setUp(self):
        # TODO: assinatura digital
        # self.certificado = "./tests/certificado.pfx"
        # self.senha = bytes("123456", "utf-8")
        self.homologacao = True

    def preenche_emitente(self):
        self.emitente = Emitente(
            cnpj='99999999999999',
            inscricao_municipal='000000'
        )
        return self.emitente

    def preenche_destinatario(self):
        self.cliente = Cliente(
            razao_social='NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL',
            tipo_documento='CNPJ',                          # CPF ou CNPJ
            # apenas os numeros do CPF ou CNPJ
            numero_documento='99999999999999',
            inscricao_municipal='1234',                     # opcional
            endereco_logradouro='Rua tal',
            endereco_numero='0',
            endereco_complemento='Ao lado de lugar nenhum',  # opcional
            endereco_bairro='Centro',
            endereco_cod_municipio='123',
            endereco_uf='MG',
            endereco_cep='33257010',
            endereco_pais=CODIGO_BRASIL,
            endereco_telefone='12365478945',                # opcional
            email='nome@email.com.br'                       # opcional
        )
        return self.cliente

    def preenche_notafiscal_servico(self):
        self.servico = Servico(
            valor_servico=Decimal('100.00'),
            iss_retido=1,  # 1 - Sim; 2 - Não
            item_lista='0101',
            discriminacao='Mensalidade',
            codigo_municipio=obter_codigo_por_municipio(
                'Pedro Leopoldo', 'MG'),
            # Dados opcionais
            codigo_cnae=6201501,
            codigo_tributacao_municipio='1234',
            valor_deducoes=Decimal('10.00'),
            valor_pis=Decimal('10.00'),
            valor_confins=Decimal('10.00'),
            valor_inss=Decimal('10.00'),
            valor_ir=Decimal('10.00'),
            valor_csll=Decimal('10.00'),
            valor_iss=Decimal('10.00'),
            valor_iss_retido=Decimal('10.00'),
            valor_liquido=Decimal('10.00'),
            outras_retencoes=Decimal('10.00'),
            base_calculo=Decimal('10.00'),
            aliquota=Decimal('10.00'),
            desconto_incondicionado=Decimal('10.00'),
            desconto_condicionado=Decimal('10.00')
        )

        self.notafiscal = NotaFiscalServico(
            identificador='50',
            data_emissao=datetime.datetime.now(),
            servico=self.servico,
            emitente=self.preenche_emitente(),
            cliente=self.preenche_destinatario(),
            # Optante Simples Nacional
            simples=1,     # 1-Sim; 2-Não
            # 1 – Tributação no município 2 - Tributação fora do município 3 - Isenção 4 - Imune
            natureza_operacao=1,
            # 5 –Exigibilidade suspensa por decisão judicial 6 – Exigibilidade suspensa por procedimento administrativo
            # regime_especial=1, # Regime Especial de Tributação: 1 – Microempresa municipal 2 - Estimativa
            # 3 – Sociedade de profissionais 4 – Cooperativa 5 - Microempresário Individual (MEI)
            # 6 - Microempresário e Empresa de Pequeno Porte (ME EPP)
            incentivo=2,   # Incentivador Cultural # 1-Sim; 2-Não
            serie='A1',
            tipo='1'
        )
        return self.notafiscal

    def serializa_nfse(self):
        serializador = SerializacaoNfse('ginfes')
        xml = serializador.gerar_lote(self.preenche_notafiscal_servico())
        return xml

    # TODO: assinatura digital
    # def assina_xml(self):
    #     a1 = AssinaturaA1(self.certificado, self.senha)
    #     xml = a1.assinar(self.serializa_nfse(), True)
    #     return xml

    def validacao_com_xsd_do_xml_gerado_sem_processar(self):
        validacao = Validacao()
        xsd_nfse = validacao.get_xsd(
            xsd_file='servico_enviar_lote_rps_envio_v03.xsd', xsd_folder='pynfe/data/XSDs/NFS-e/Ginfes'
        )

        validacao.validar_etree(
            xml_doc=etree.fromstring(self.xml), xsd_file=xsd_nfse, use_assert=True
            # TODO: assinatura digital
            # xml_doc=self.xml_assinado, xsd_file=xsd_nfse, use_assert=True
        )

    def get_nfse_esperada(self) -> str:
        xml = f"""
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
                        <ns2:DataEmissao>{self.notafiscal.data_emissao.isoformat()[:19]}</ns2:DataEmissao>
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
        """

        return re.sub(r">\s+<", "><", xml.replace("\n", "").strip())

    def test_notafiscal_geral(self):
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()

        self.xml = self.serializa_nfse()
        # TODO: assinatura digital
        # self.xml_assinado = self.assina_xml()

        self.maxDiff = None
        result = self.get_nfse_esperada()

        # a serialização gera os atributos xmlns:ns1 e xmlns:ns2
        # da tag ns1:EnviarLoteRpsEnvio em ordem randômica (!!!)
        xml = re.sub(r'<(ns1:EnviarLoteRpsEnvio)[^>]*>', r'<\1>', self.xml)
        result = re.sub(r'<(ns1:EnviarLoteRpsEnvio)[^>]*>', r'<\1>', result)

        # Teste do conteúdo das tags do XML
        self.assertEqual(xml, result)

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()

        # Limpa o Namespace para não gerar conflito com outros testes
        pyxb.namespace.Namespace._Namespace__Registry.clear()


if __name__ == "__main__":
    unittest.main()
