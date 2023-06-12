#!/usr/bin/env python
# *-* encoding: utf8 *-*

import unittest

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscal
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.processamento.serializacao import SerializacaoXML
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.processamento.validacao import Validacao
from pynfe.utils.flags import (
    CODIGO_BRASIL,
    NAMESPACE_NFE,
    NAMESPACE_SIG,
    XSD_FOLDER_NFE,
    XSD_NFE,
    XSD_NFE_PROCESSADA,
)
from decimal import Decimal
import datetime


class SerializacaoNFeTestCase(unittest.TestCase):
    """
    Imprimir o XML completo:
        print(etree.tostring(self.xml_assinado))

    """

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
        self.xsd_nfe = self.validacao.get_xsd(
            xsd_file=XSD_NFE, xsd_folder=XSD_FOLDER_NFE
        )

    def preenche_emitente(self):
        self.emitente = Emitente(
            razao_social="NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL",
            nome_fantasia="Nome Fantasia da Empresa",
            cnpj="99999999000199",  # cnpj apenas números
            codigo_de_regime_tributario="1",  # 1 para simples nacional ou 3 para normal
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

    def preenche_destinatario(self):
        self.cliente = Cliente(
            razao_social="JOSE DA SILVA",
            tipo_documento="CPF",  # CPF ou CNPJ
            email="email@email.com",
            numero_documento="12345678900",  # numero do cpf ou cnpj
            indicador_ie=9,  # 9=Não contribuinte
            endereco_logradouro="Rua dos Bobos",
            endereco_numero="Zero",
            endereco_complemento="Ao lado de lugar nenhum",
            endereco_bairro="Aquele Mesmo",
            endereco_municipio="Brasilia",
            endereco_uf="DF",
            endereco_cep="12345123",
            endereco_pais=CODIGO_BRASIL,
            endereco_telefone="11912341234",
        )
        return self.cliente

    def preenche_notafiscal_produto_csosn102(self):
        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf="PR",
            natureza_operacao="VENDA",  # venda, compra, transferência, devolução, etc
            forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
            tipo_pagamento=1,
            modelo=55,  # 55=NF-e; 65=NFC-e
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
            totais_tributos_aproximado=Decimal("21.06"),
        )

        self.notafiscal.adicionar_produto_servico(
            codigo="000328",  # id do produto
            descricao="Produto teste",
            ncm="99999999",
            # cest='0100100',  # NT2015/003
            ean="1234567890121",
            cfop="5102",
            unidade_comercial="UN",
            quantidade_comercial=Decimal("12"),  # 12 unidades
            valor_unitario_comercial=Decimal("9.75"),  # preço unitário
            valor_total_bruto=Decimal("117.00"),  # preço total
            unidade_tributavel="UN",
            quantidade_tributavel=Decimal("12"),
            valor_unitario_tributavel=Decimal("9.75"),
            ean_tributavel="SEM GTIN",
            ind_total=1,
            icms_modalidade="103",
            icms_origem=0,
            icms_csosn="103",
            icms_aliquota=0,  # Alíquota aplicável de cálculo do crédito (Simples Nacional).
            icms_credito=0,
            pis_modalidade="51",
            cofins_modalidade="51",
            pis_valor_base_calculo=Decimal("117.00"),
            pis_aliquota_percentual=Decimal("0.65"),
            pis_valor=Decimal("0.76"),
            cofins_valor_base_calculo=Decimal("117.00"),
            cofins_aliquota_percentual=Decimal("3.00"),
            cofins_valor=Decimal("3.51"),
            valor_tributos_aprox="21.06",
            numero_pedido="12345",
            numero_item="1",
            nfci="12345678-AAAA-FFFF-1234-000000000000",
            informacoes_adicionais="Informações adicionais",
            ipi_valor_ipi_dev=Decimal("0.00"),
            pdevol=Decimal("0.00"),
        )
        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso="12345678901234567890123456789012345678900001"
        )
        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso="12345678901234567890123456789012345678900002"
        )

        self.notafiscal.adicionar_responsavel_tecnico(
            cnpj="99999999000199",
            contato="Teste PyNFe",
            email="pynfe@pynfe.io",
            fone="11912341234",
        )

    def serializa_nfe(self):
        serializador = SerializacaoXML(_fonte_dados, homologacao=self.homologacao)
        return serializador.exportar()

    def assina_xml(self):
        a1 = AssinaturaA1(self.certificado, self.senha)
        return a1.assinar(self.xml)

    def validacao_com_xsd_do_xml_gerado_sem_processar(self):
        self.validacao.validar_etree(
            xml_doc=self.xml_assinado, xsd_file=self.xsd_nfe, use_assert=True
        )

    def total_e_produto_csosn102_test(self):
        # Produto
        cProd = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:cProd", namespaces=self.ns
        )[0].text
        cEAN = self.xml_assinado.xpath("//ns:det/ns:prod/ns:cEAN", namespaces=self.ns)[
            0
        ].text
        xProd = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:xProd", namespaces=self.ns
        )[0].text
        NCM = self.xml_assinado.xpath("//ns:det/ns:prod/ns:NCM", namespaces=self.ns)[
            0
        ].text

        CEST = None
        indEscala = None
        CFOP = self.xml_assinado.xpath("//ns:det/ns:prod/ns:CFOP", namespaces=self.ns)[
            0
        ].text
        uCom = self.xml_assinado.xpath("//ns:det/ns:prod/ns:uCom", namespaces=self.ns)[
            0
        ].text
        qCom = self.xml_assinado.xpath("//ns:det/ns:prod/ns:qCom", namespaces=self.ns)[
            0
        ].text
        vUnCom = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:vUnCom", namespaces=self.ns
        )[0].text
        vProd = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:vProd", namespaces=self.ns
        )[0].text
        cEANTrib = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:cEANTrib", namespaces=self.ns
        )[0].text
        uTrib = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:uTrib", namespaces=self.ns
        )[0].text
        qTrib = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:qTrib", namespaces=self.ns
        )[0].text
        vUnTrib = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:vUnTrib", namespaces=self.ns
        )[0].text
        indTot = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:indTot", namespaces=self.ns
        )[0].text
        xPed = self.xml_assinado.xpath("//ns:det/ns:prod/ns:xPed", namespaces=self.ns)[
            0
        ].text
        nItemPed = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:nItemPed", namespaces=self.ns
        )[0].text
        nFCI = self.xml_assinado.xpath("//ns:det/ns:prod/ns:nFCI", namespaces=self.ns)[
            0
        ].text

        self.assertEqual(cProd, "000328")
        self.assertEqual(cEAN, "1234567890121")
        self.assertEqual(xProd, "Produto teste")
        self.assertEqual(NCM, "99999999")
        self.assertEqual(CEST, None)
        self.assertEqual(indEscala, None)
        self.assertEqual(CFOP, "5102")
        self.assertEqual(uCom, "UN")
        self.assertEqual(qCom, "12")
        self.assertEqual(vUnCom, "9.7500000000")
        self.assertEqual(vProd, "117.00")
        self.assertEqual(cEANTrib, "SEM GTIN")
        self.assertEqual(uTrib, "UN")
        self.assertEqual(qTrib, "12")
        self.assertEqual(vUnTrib, "9.7500000000")
        self.assertEqual(indTot, "1")
        self.assertEqual(xPed, "12345")
        self.assertEqual(nItemPed, "1")
        self.assertEqual(nFCI, "12345678-AAAA-FFFF-1234-000000000000")

        # Impostos
        # ICMS
        orig = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:ICMS/ns:ICMSSN102/ns:orig", namespaces=self.ns
        )[0].text
        CSOSN = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:ICMS/ns:ICMSSN102/ns:CSOSN", namespaces=self.ns
        )[0].text

        self.assertEqual(orig, "0")
        self.assertEqual(CSOSN, "103")

        # CSOSN 103 gera a tag 102
        CSOSN103 = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:ICMS/ns:ICMSSN103/ns:CSOSN", namespaces=self.ns
        )
        self.assertEqual(CSOSN103, [])

        # PIS
        CST_PIS = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:PIS/ns:PISOutr/ns:CST", namespaces=self.ns
        )[0].text
        self.assertEqual(CST_PIS, "51")

        # COFINS
        CST_COFINS = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:COFINS/ns:COFINSOutr/ns:CST", namespaces=self.ns
        )[0].text
        self.assertEqual(CST_COFINS, "51")

        # Informações Adicionais do produto
        infAdProd = self.xml_assinado.xpath(
            "//ns:det/ns:infAdProd", namespaces=self.ns
        )[0].text
        self.assertEqual(infAdProd, "Informacoes adicionais")

        # Totalizadores
        vBC = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vBC", namespaces=self.ns
        )[0].text
        vICMS = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vICMS", namespaces=self.ns
        )[0].text
        vICMSDeson = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vICMSDeson", namespaces=self.ns
        )[0].text
        vFCP = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vFCP", namespaces=self.ns
        )[0].text
        vBCST = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vBCST", namespaces=self.ns
        )[0].text
        vST = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vST", namespaces=self.ns
        )[0].text
        vFCPST = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vFCPST", namespaces=self.ns
        )[0].text
        vFCPSTRet = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vFCPSTRet", namespaces=self.ns
        )[0].text
        vProd = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vProd", namespaces=self.ns
        )[0].text
        vFrete = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vFrete", namespaces=self.ns
        )[0].text
        vSeg = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vSeg", namespaces=self.ns
        )[0].text
        vDesc = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vDesc", namespaces=self.ns
        )[0].text
        vII = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vII", namespaces=self.ns
        )[0].text
        vIPI = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vIPI", namespaces=self.ns
        )[0].text
        vIPIDevol = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vIPIDevol", namespaces=self.ns
        )[0].text
        vPIS = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vPIS", namespaces=self.ns
        )[0].text
        vCOFINS = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vCOFINS", namespaces=self.ns
        )[0].text
        vOutro = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vOutro", namespaces=self.ns
        )[0].text
        vNF = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vNF", namespaces=self.ns
        )[0].text
        vTotTrib = self.xml_assinado.xpath(
            "//ns:total/ns:ICMSTot/ns:vTotTrib", namespaces=self.ns
        )[0].text

        self.assertEqual(vBC, "0.00")
        self.assertEqual(vICMS, "0.00")
        self.assertEqual(vICMSDeson, "0.00")
        self.assertEqual(vFCP, "0.00")
        self.assertEqual(vBCST, "0.00")
        self.assertEqual(vST, "0.00")
        self.assertEqual(vFCPST, "0.00")
        self.assertEqual(vFCPSTRet, "0.00")
        self.assertEqual(vProd, "117.00")
        self.assertEqual(vFrete, "0.00")
        self.assertEqual(vSeg, "0.00")
        self.assertEqual(vDesc, "0.00")
        self.assertEqual(vII, "0.00")
        self.assertEqual(vIPI, "0.00")
        self.assertEqual(vIPIDevol, "0.00")
        self.assertEqual(vPIS, "0.76")
        self.assertEqual(vCOFINS, "3.51")
        self.assertEqual(vOutro, "0.00")
        self.assertEqual(vNF, "117.00")
        self.assertEqual(vTotTrib, "21.06")

    def test_notafiscal_produto_csosn102(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_csosn102()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.total_e_produto_csosn102_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()


if __name__ == "__main__":
    unittest.main()
