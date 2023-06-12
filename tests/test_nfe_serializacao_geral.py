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

    def preenche_notafiscal_produto_cst00(self):
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
            icms_modalidade="00",
            icms_origem=0,
            icms_csosn="",
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
            ipi_valor_ipi_dev=Decimal("10.00"),
            pdevol=Decimal("1.00"),
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
        data_saida_entrada = self.xml_assinado.xpath(
            "//ns:ide/ns:dhSaiEnt", namespaces=self.ns
        )[0].text
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
        self.assertEqual(modelo, "55")
        self.assertEqual(serie, "1")
        self.assertEqual(numero_nf, "111")
        self.assertEqual(data_emissao, "2021-01-14T12:00:00+00:00")
        self.assertEqual(data_saida_entrada, "2021-01-14T13:10:20+00:00")
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
        razao_social = self.xml_assinado.xpath(
            "//ns:dest/ns:xNome", namespaces=self.ns
        )[0].text
        email = self.xml_assinado.xpath("//ns:dest/ns:email", namespaces=self.ns)[
            0
        ].text
        numero_documento = self.xml_assinado.xpath(
            "//ns:dest/ns:CPF", namespaces=self.ns
        )[0].text
        indicador_ie = self.xml_assinado.xpath(
            "//ns:dest/ns:indIEDest", namespaces=self.ns
        )[0].text
        endereco_logradouro = self.xml_assinado.xpath(
            "//ns:dest/ns:enderDest/ns:xLgr", namespaces=self.ns
        )[0].text
        endereco_numero = self.xml_assinado.xpath(
            "//ns:dest/ns:enderDest/ns:nro", namespaces=self.ns
        )[0].text
        endereco_complemento = self.xml_assinado.xpath(
            "//ns:dest/ns:enderDest/ns:xCpl", namespaces=self.ns
        )[0].text
        endereco_bairro = self.xml_assinado.xpath(
            "//ns:dest/ns:enderDest/ns:xBairro", namespaces=self.ns
        )[0].text
        endereco_municipio = self.xml_assinado.xpath(
            "//ns:dest/ns:enderDest/ns:xMun", namespaces=self.ns
        )[0].text
        endereco_uf = self.xml_assinado.xpath(
            "//ns:dest/ns:enderDest/ns:UF", namespaces=self.ns
        )[0].text
        endereco_cep = self.xml_assinado.xpath(
            "//ns:dest/ns:enderDest/ns:CEP", namespaces=self.ns
        )[0].text
        endereco_pais = self.xml_assinado.xpath(
            "//ns:dest/ns:enderDest/ns:xPais", namespaces=self.ns
        )[0].text
        endereco_telefone = self.xml_assinado.xpath(
            "//ns:dest/ns:enderDest/ns:fone", namespaces=self.ns
        )[0].text

        self.assertEqual(razao_social, "JOSE DA SILVA")
        self.assertEqual(email, "email@email.com")
        self.assertEqual(numero_documento, "12345678900")
        self.assertEqual(indicador_ie, "9")
        self.assertEqual(endereco_logradouro, "Rua dos Bobos")
        self.assertEqual(endereco_numero, "Zero")
        self.assertEqual(endereco_complemento, "Ao lado de lugar nenhum")
        self.assertEqual(endereco_bairro, "Aquele Mesmo")
        self.assertEqual(endereco_municipio, "Brasilia")
        self.assertEqual(endereco_uf, "DF")
        self.assertEqual(endereco_cep, "12345123")
        self.assertEqual(endereco_pais, "Brasil")
        self.assertEqual(endereco_telefone, "11912341234")

    def notas_produtor_referenciadas_test(self):
        ref_1 = self.xml_assinado.xpath(
            "//ns:ide/ns:NFref/ns:refNFP/ns:nNF", namespaces=self.ns
        )[0].text
        ref_2 = self.xml_assinado.xpath(
            "//ns:ide/ns:NFref/ns:refNFP/ns:nNF", namespaces=self.ns
        )[1].text

        self.assertEqual(ref_1, "999999998")
        self.assertEqual(ref_2, "999999999")

    def notas_referenciadas_test(self):
        chave_1 = self.xml_assinado.xpath(
            "//ns:ide/ns:NFref/ns:refNFe", namespaces=self.ns
        )[0].text
        chave_2 = self.xml_assinado.xpath(
            "//ns:ide/ns:NFref/ns:refNFe", namespaces=self.ns
        )[1].text

        self.assertEqual(chave_1, "12345678901234567890123456789012345678900001")
        self.assertEqual(chave_2, "12345678901234567890123456789012345678900002")

    def responsavel_tecnico_test(self):
        cnpj = self.xml_assinado.xpath("//ns:infRespTec/ns:CNPJ", namespaces=self.ns)[
            0
        ].text
        contato = self.xml_assinado.xpath(
            "//ns:infRespTec/ns:xContato", namespaces=self.ns
        )[0].text
        email = self.xml_assinado.xpath("//ns:infRespTec/ns:email", namespaces=self.ns)[
            0
        ].text
        fone = self.xml_assinado.xpath("//ns:infRespTec/ns:fone", namespaces=self.ns)[
            0
        ].text

        self.assertEqual(cnpj, "99999999000199")
        self.assertEqual(contato, "Teste PyNFe")
        self.assertEqual(email, "pynfe@pynfe.io")
        self.assertEqual(fone, "11912341234")

    def digestvalue_da_assinatura_test(self):
        DigestValue = self.xml_assinado.xpath(
            "//ns:Signature//ns:SignedInfo/ns:Reference/ns:DigestValue",
            namespaces=self.ns_sig,
        )[0].text
        self.assertTrue(len(DigestValue) > 0)

    def test_notafiscal_geral(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_cst00()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.dados_emitente_test()
        self.dados_destinatario_test()
        self.notas_referenciadas_test()
        self.responsavel_tecnico_test()
        self.digestvalue_da_assinatura_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()


if __name__ == "__main__":
    unittest.main()
