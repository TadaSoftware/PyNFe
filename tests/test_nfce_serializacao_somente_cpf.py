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

    def preenche_destinatario(self):
        self.cliente = Cliente(
            indicador_ie=9,
            tipo_documento="CPF",  # CPF ou CNPJ
            numero_documento="12345678900",  # numero do cpf ou cnpj
        )
        return self.cliente

    def preenche_notafiscal_produto(self):
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
            informacoes_adicionais="Informações adicionais",
        )

        self.notafiscal.adicionar_responsavel_tecnico(
            cnpj="99999999000199",
            contato="Teste PyNFe",
            email="pynfe@pynfe.io",
            fone="11912341234",
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

    def grupo_ide_test(self):
        uf = self.xml_assinado.xpath("//ns:ide/ns:cUF", namespaces=self.ns)[0].text
        natureza_operacao = self.xml_assinado.xpath(
            "//ns:ide/ns:natOp", namespaces=self.ns
        )[0].text
        modelo = self.xml_assinado.xpath("//ns:ide/ns:mod", namespaces=self.ns)[0].text
        serie = self.xml_assinado.xpath("//ns:ide/ns:serie", namespaces=self.ns)[0].text
        numero_nf = self.xml_assinado.xpath("//ns:ide/ns:nNF", namespaces=self.ns)[
            0
        ].text
        data_emissao = self.xml_assinado.xpath("//ns:ide/ns:dhEmi", namespaces=self.ns)[
            0
        ].text
        tipo_documento = self.xml_assinado.xpath(
            "//ns:ide/ns:tpNF", namespaces=self.ns
        )[0].text
        indicador_destino = self.xml_assinado.xpath(
            "//ns:ide/ns:idDest", namespaces=self.ns
        )[0].text
        municipio = self.xml_assinado.xpath("//ns:ide/ns:cMunFG", namespaces=self.ns)[
            0
        ].text
        tipo_impressao_danfe = self.xml_assinado.xpath(
            "//ns:ide/ns:tpImp", namespaces=self.ns
        )[0].text
        forma_emissao = self.xml_assinado.xpath(
            "//ns:ide/ns:tpEmis", namespaces=self.ns
        )[0].text
        tipo_ambiente = self.xml_assinado.xpath(
            "//ns:ide/ns:tpAmb", namespaces=self.ns
        )[0].text
        finalidade_emissao = self.xml_assinado.xpath(
            "//ns:ide/ns:finNFe", namespaces=self.ns
        )[0].text
        cliente_final = self.xml_assinado.xpath(
            "//ns:ide/ns:indFinal", namespaces=self.ns
        )[0].text
        indicador_presencial = self.xml_assinado.xpath(
            "//ns:ide/ns:indPres", namespaces=self.ns
        )[0].text
        processo_emissao = self.xml_assinado.xpath(
            "//ns:ide/ns:procEmi", namespaces=self.ns
        )[0].text

        self.assertEqual(uf, "41")
        self.assertEqual(natureza_operacao, "VENDA")
        self.assertEqual(modelo, "65")
        self.assertEqual(serie, "1")
        self.assertEqual(numero_nf, "111")
        self.assertEqual(data_emissao, "2021-01-14T12:00:00+00:00")
        self.assertEqual(tipo_documento, "1")
        self.assertEqual(indicador_destino, "1")
        self.assertEqual(municipio, "4118402")
        self.assertEqual(tipo_impressao_danfe, "1")
        self.assertEqual(forma_emissao, "1")
        self.assertEqual(tipo_ambiente, "2")
        self.assertEqual(finalidade_emissao, "1")
        self.assertEqual(cliente_final, "1")
        self.assertEqual(indicador_presencial, "1")
        self.assertEqual(processo_emissao, "0")

    def dados_emitente_test(self):
        razao_social = self.xml_assinado.xpath(
            "//ns:emit/ns:xNome", namespaces=self.ns
        )[0].text
        nome_fantasia = self.xml_assinado.xpath(
            "//ns:emit/ns:xFant", namespaces=self.ns
        )[0].text
        cnpj = self.xml_assinado.xpath("//ns:emit/ns:CNPJ", namespaces=self.ns)[0].text
        codigo_de_regime_tributario = self.xml_assinado.xpath(
            "//ns:emit/ns:CRT", namespaces=self.ns
        )[0].text
        inscricao_estadual = self.xml_assinado.xpath(
            "//ns:emit/ns:IE", namespaces=self.ns
        )[0].text
        inscricao_municipal = self.xml_assinado.xpath(
            "//ns:emit/ns:IM", namespaces=self.ns
        )[0].text
        cnae_fiscal = self.xml_assinado.xpath("//ns:emit/ns:CNAE", namespaces=self.ns)[
            0
        ].text
        endereco_logradouro = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:xLgr", namespaces=self.ns
        )[0].text
        endereco_numero = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:nro", namespaces=self.ns
        )[0].text
        endereco_bairro = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:xBairro", namespaces=self.ns
        )[0].text
        endereco_municipio = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:xMun", namespaces=self.ns
        )[0].text
        endereco_uf = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:UF", namespaces=self.ns
        )[0].text
        endereco_cep = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:CEP", namespaces=self.ns
        )[0].text
        endereco_pais = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:xPais", namespaces=self.ns
        )[0].text

        self.assertEqual(
            razao_social, "NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL"
        )
        self.assertEqual(nome_fantasia, "Nome Fantasia da Empresa")
        self.assertEqual(cnpj, "99999999000199")
        self.assertEqual(codigo_de_regime_tributario, "3")
        self.assertEqual(inscricao_estadual, "9999999999")
        self.assertEqual(inscricao_municipal, "12345")
        self.assertEqual(cnae_fiscal, "9999999")
        self.assertEqual(endereco_logradouro, "Rua da Paz")
        self.assertEqual(endereco_numero, "666")
        self.assertEqual(endereco_bairro, "Sossego")
        self.assertEqual(endereco_municipio, "Paranavai")
        self.assertEqual(endereco_uf, "PR")
        self.assertEqual(endereco_cep, "87704000")
        self.assertEqual(endereco_pais, "Brasil")

    def dados_destinatario_test(self):
        indicador_ie = self.xml_assinado.xpath(
            "//ns:dest/ns:indIEDest", namespaces=self.ns
        )[0].text
        numero_documento = self.xml_assinado.xpath(
            "//ns:dest/ns:CPF", namespaces=self.ns
        )[0].text
        self.assertEqual(indicador_ie, "9")
        self.assertEqual(numero_documento, "12345678900")
        self.assertNotEqual(numero_documento, "123")

    def total_e_produto_test(self):
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

        # Impostos
        # ICMS
        orig = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:orig", namespaces=self.ns
        )[0].text
        CST = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:CST", namespaces=self.ns
        )[0].text
        modBC = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:modBC", namespaces=self.ns
        )[0].text
        vBC = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:vBC", namespaces=self.ns
        )[0].text
        pICMS = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:pICMS", namespaces=self.ns
        )[0].text
        vICMS = self.xml_assinado.xpath(
            "//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:vICMS", namespaces=self.ns
        )[0].text
        pFCP = None
        vFCP = None

        self.assertEqual(orig, "0")
        self.assertEqual(CST, "00")
        self.assertEqual(modBC, "0")
        self.assertEqual(vBC, "0")
        self.assertEqual(pICMS, "0.00")
        self.assertEqual(vICMS, "0.00")
        self.assertEqual(pFCP, None)
        self.assertEqual(vFCP, None)

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
        self.assertEqual(vPIS, "0.00")
        self.assertEqual(vCOFINS, "0.00")
        self.assertEqual(vOutro, "0.00")
        self.assertEqual(vNF, "117.00")
        self.assertEqual(vTotTrib, "1.01")

    def test_notafiscal_produto_cst00(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.dados_emitente_test()
        self.dados_destinatario_test()
        self.total_e_produto_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()


if __name__ == "__main__":
    unittest.main()
