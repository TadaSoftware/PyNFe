import unittest

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscalServico
from pynfe.entidades.servico import Servico
from pynfe.processamento.serializacao import SerializacaoNfse
from pynfe.utils import obter_codigo_por_municipio
from pynfe.utils.flags import (
    CODIGO_BRASIL,
)
from decimal import Decimal
import datetime
import re
import pyxb.namespace


class SerializacaoNFSeBethaTestCase(unittest.TestCase):
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
            municipio_incidencia=obter_codigo_por_municipio(
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
        serializador = SerializacaoNfse('betha')
        xml = serializador.gerar(self.preenche_notafiscal_servico())
        return xml

    # TODO: assinatura digital
    # def assina_xml(self):
    #     a1 = AssinaturaA1(self.certificado, self.senha)
    #     xml = a1.assinar(self.serializa_nfse(), True)
    #     return xml

    # TODO: Testa a validação do XML com os schemas XSD
    # def validacao_com_xsd_do_xml_gerado_sem_processar(self):
    #     validacao = Validacao()
    #     xsd_nfse = validacao.get_xsd(
    #         xsd_file='nfse_v202.xsd', xsd_folder='pynfe/data/XSDs/NFS-e/Betha'
    #     )

    #     validacao.validar_etree(
    #         xml_doc=etree.fromstring(self.xml), xsd_file=xsd_nfse, use_assert=True
    #         # TODO: assinatura digital
    #         # xml_doc=self.xml_assinado, xsd_file=xsd_nfse, use_assert=True
    #     )

    def get_nfse_esperada(self) -> str:
        xml = f"""
            <?xml version="1.0" ?>
            <GerarNfseEnvio xmlns:ns1="http://www.betha.com.br/e-nota-contribuinte-ws">
                <ns1:Rps>
                    <ns1:InfDeclaracaoPrestacaoServico Id="50">
                        <ns1:Rps>
                            <ns1:IdentificacaoRps>
                                <ns1:Numero>50</ns1:Numero>
                                <ns1:Serie>A1</ns1:Serie>
                                <ns1:Tipo>1</ns1:Tipo>
                            </ns1:IdentificacaoRps>
                            <ns1:DataEmissao>{self.notafiscal.data_emissao.strftime("%Y-%m-%d")}</ns1:DataEmissao>
                            <ns1:Status>1</ns1:Status>
                        </ns1:Rps>
                        <ns1:Competencia>{self.notafiscal.data_emissao.strftime("%Y-%m-%d")}</ns1:Competencia>
                        <ns1:Servico>
                            <ns1:Valores>
                                <ns1:ValorServicos>100.0</ns1:ValorServicos>
                            </ns1:Valores>
                            <ns1:IssRetido>1</ns1:IssRetido>
                            <ns1:ItemListaServico>0101</ns1:ItemListaServico>
                            <ns1:Discriminacao>Mensalidade</ns1:Discriminacao>
                            <ns1:CodigoMunicipio>3149309</ns1:CodigoMunicipio>
                            <ns1:ExigibilidadeISS>0</ns1:ExigibilidadeISS>
                            <ns1:MunicipioIncidencia>3149309</ns1:MunicipioIncidencia>
                        </ns1:Servico>
                        <ns1:Prestador>
                            <ns1:CpfCnpj>
                                <ns1:Cnpj>99999999999999</ns1:Cnpj>
                            </ns1:CpfCnpj>
                            <ns1:InscricaoMunicipal>000000</ns1:InscricaoMunicipal>
                        </ns1:Prestador>
                        <ns1:Tomador>
                            <ns1:RazaoSocial>NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL</ns1:RazaoSocial>
                            <ns1:Endereco>
                                <ns1:Endereco>Rua tal</ns1:Endereco>
                                <ns1:Numero>0</ns1:Numero>
                                <ns1:Bairro>Centro</ns1:Bairro>
                                <ns1:CodigoMunicipio>123</ns1:CodigoMunicipio>
                                <ns1:Uf>MG</ns1:Uf>
                                <ns1:CodigoPais>1058</ns1:CodigoPais>
                                <ns1:Cep>33257010</ns1:Cep>
                            </ns1:Endereco>
                        </ns1:Tomador>
                        <ns1:OptanteSimplesNacional>1</ns1:OptanteSimplesNacional>
                        <ns1:IncentivoFiscal>2</ns1:IncentivoFiscal>
                    </ns1:InfDeclaracaoPrestacaoServico>
                </ns1:Rps>
            </GerarNfseEnvio>
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

        # Teste do conteúdo das tags do XML
        self.assertEqual(self.xml, result)

        # TODO: Testa a validação do XML com os schemas XSD
        # self.validacao_com_xsd_do_xml_gerado_sem_processar()

        # Limpa o Namespace para não gerar conflito com outros testes
        pyxb.namespace.Namespace._Namespace__Registry.clear()


if __name__ == "__main__":
    unittest.main()
