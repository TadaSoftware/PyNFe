#!/usr/bin/env python
# *-* encoding: utf8 *-*

import datetime
import unittest
from decimal import Decimal

from pynfe.entidades.emitente import Emitente
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.entidades.notafiscal import NotaFiscal
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.processamento.serializacao import SerializacaoXML
from pynfe.processamento.validacao import Validacao
from pynfe.utils.flags import (
    CODIGO_BRASIL,
    NAMESPACE_NFE,
    NAMESPACE_SIG,
    XSD_FOLDER_NFE,
    XSD_NFE,
    XSD_NFE_PROCESSADA,
)


class SerializacaoNFeTestCase(unittest.TestCase):
    def setUp(self):
        self.certificado = "./tests/certificado.pfx"
        self.senha = bytes("123456", "utf-8")
        self.uf = "pr"
        self.homologacao = True

        self.ns = {"ns": NAMESPACE_NFE}
        self.ns_sig = {"ns": NAMESPACE_SIG}

        self.validacao = Validacao()
        self.xsd_procNFe = self.validacao.get_xsd(
            xsd_file=XSD_NFE_PROCESSADA, xsd_folder=XSD_FOLDER_NFE
        )
        self.xsd_nfe = self.validacao.get_xsd(xsd_file=XSD_NFE, xsd_folder=XSD_FOLDER_NFE)

    def preenche_emitente(self):
        self.emitente = Emitente(
            razao_social="NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL",
            nome_fantasia="Nome Fantasia da Empresa",
            cnpj="99999999000199",  # cnpj apenas números
            codigo_de_regime_tributario="3",  # 1 para simples nacional ou 3 para normal
            inscricao_estadual="9999999999",  # numero de IE da empresa
            inscricao_municipal="12345",
            cnae_fiscal="9999999",  # cnae apenas números
            endereco_logradouro="Rua da Paz",
            endereco_numero="666",
            endereco_bairro="Sossego",
            endereco_municipio="Paranavaí",
            endereco_uf="PR",
            endereco_cep="87704000",
            endereco_pais=CODIGO_BRASIL,
        )
        return self.emitente

    def preenche_notafiscal_produto(self, quantidade):
        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=None,
            uf="PR",
            natureza_operacao="VENDA",  # venda, compra, transferência, devolução, etc
            forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
            modelo=65,  # 55=NF-e; 65=NFC-e
            serie="1",
            numero_nf="111",  # Número do Documento Fiscal.
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,  # 0=entrada; 1=saida
            municipio="4118402",  # Código IBGE do Município
            tipo_impressao_danfe=1,  # 1=DANFE normal
            forma_emissao="1",  # 1=Emissão normal (não em contingência);
            cliente_final=1,  # 0=Normal;1=Consumidor final;
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao="1",  # 1=NF-e normal
            processo_emissao="0",  # 0=Emissão de NF-e com aplicativo do contribuinte;
            transporte_modalidade_frete=1,
            informacoes_adicionais_interesse_fisco="Mensagem complementar",
            totais_tributos_aproximado=Decimal("1.01"),
            valor_troco=Decimal("3.00"),
        )

        self.notafiscal.adicionar_produto_servico(
            codigo="000328",  # id do produto
            descricao="Produto teste",
            ncm="99999999",
            # cest='0100100',  # NT2015/003
            ean="1234567890121",
            cfop="5102",
            unidade_comercial="UN",
            quantidade_comercial=Decimal(quantidade),
            valor_unitario_comercial=Decimal("0.00"),
            valor_total_bruto=Decimal("0.00"),
            unidade_tributavel="UN",
            quantidade_tributavel=Decimal(quantidade),
            valor_unitario_tributavel=Decimal("0.00"),
            ean_tributavel="SEM GTIN",
            ind_total=1,
            icms_modalidade="00",
            icms_origem=0,
            icms_csosn="",
            pis_modalidade="51",
            cofins_modalidade="51",
            pis_valor_base_calculo=Decimal("0.00"),
            pis_aliquota_percentual=Decimal("0.00"),
            pis_valor=Decimal("0.00"),
            cofins_valor_base_calculo=Decimal("0.00"),
            cofins_aliquota_percentual=Decimal("0.00"),
            cofins_valor=Decimal("0.00"),
            valor_tributos_aprox="1.01",
        )

    def serializa_nfe(self):
        serializador = SerializacaoXML(
            fonte_dados=_fonte_dados, homologacao=self.homologacao, so_cpf=True
        )
        return serializador.exportar()

    def assina_xml(self):
        a1 = AssinaturaA1(self.certificado, self.senha)
        return a1.assinar(self.xml)

    def validacao_com_xsd_do_xml_gerado_sem_processar(self):
        self.validacao.validar_etree(
            xml_doc=self.xml_assinado, xsd_file=self.xsd_nfe, use_assert=True
        )

    def test_notafiscal_produto_com_vnf_e_vprod_com_duas_casas_decimais(self):
        quantidade = 1.123456
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.notafiscal = self.preenche_notafiscal_produto(quantidade)

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        qCom = self.xml_assinado.xpath("//ns:det/ns:prod/ns:qCom", namespaces=self.ns)[0].text
        qTrib = self.xml_assinado.xpath("//ns:det/ns:prod/ns:qTrib", namespaces=self.ns)[0].text

        self.assertEqual(qCom, "1.1235")
        self.assertEqual(qTrib, "1.1235")


if __name__ == "__main__":
    unittest.main()
