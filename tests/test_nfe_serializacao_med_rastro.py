#!/usr/bin/env python
# *-* encoding: utf8 *-*
"""
Testes para o Grupo K - Detalhamento Específico de Medicamentos
e Grupo I80 - Rastreabilidade de Produto

Referências:
- NT 2016.002 - Alteração do leiaute da NF-e (rastro)
- NT 2018.005 - Campo xMotivoIsencao (med)
"""

import datetime
import unittest
from decimal import Decimal

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.entidades.notafiscal import NotaFiscal, NotaFiscalRastro
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.processamento.serializacao import SerializacaoXML
from pynfe.processamento.validacao import Validacao
from pynfe.utils.flags import (
    CODIGO_BRASIL,
    NAMESPACE_NFE,
    XSD_FOLDER_NFE,
    XSD_NFE,
)


class SerializacaoMedicamentoRastreabilidadeTestCase(unittest.TestCase):
    """
    Testes para validar a serialização de Medicamentos (Grupo K) e
    Rastreabilidade de Produtos (Grupo I80).
    """

    def setUp(self):
        self.certificado = "./tests/certificado.pfx"
        self.senha = bytes("123456", "utf-8")
        self.homologacao = True

        self.ns = {"ns": NAMESPACE_NFE}

        self.validacao = Validacao()
        self.xsd_nfe = self.validacao.get_xsd(
            xsd_file=XSD_NFE, xsd_folder=XSD_FOLDER_NFE
        )

    def preenche_emitente(self):
        self.emitente = Emitente(
            razao_social="NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL",
            nome_fantasia="Farmacia Teste LTDA",
            cnpj="99999999000199",
            codigo_de_regime_tributario="3",
            inscricao_estadual="9999999999",
            inscricao_municipal="12345",
            cnae_fiscal="4771701",  # Comércio varejista de produtos farmacêuticos
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
            tipo_documento="CPF",
            email="email@email.com",
            numero_documento="12345678900",
            indicador_ie=9,
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

    def preenche_notafiscal_medicamento_com_rastro(self):
        """Cria uma NF-e com medicamento contendo código ANVISA e rastreabilidade"""
        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2024, 6, 15, 10, 30, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2024, 6, 15, 11, 0, 0, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf="PR",
            natureza_operacao="VENDA",
            modelo=55,
            serie="1",
            numero_nf="12345",
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,
            municipio="4118402",
            tipo_impressao_danfe=1,
            forma_emissao="1",
            cliente_final=1,
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao="1",
            processo_emissao="0",
            transporte_modalidade_frete=9,
        )

        # Adiciona medicamento com código ANVISA e PMC
        produto = self.notafiscal.adicionar_produto_servico(
            codigo="MED001",
            descricao="DIPIRONA SODICA 500MG CX 10 COMP",
            ncm="30049099",  # NCM para medicamentos
            ean="7896000000001",
            cfop="5102",
            unidade_comercial="CX",
            quantidade_comercial=Decimal("5"),
            valor_unitario_comercial=Decimal("8.99"),
            valor_total_bruto=Decimal("44.95"),
            unidade_tributavel="CX",
            quantidade_tributavel=Decimal("5"),
            valor_unitario_tributavel=Decimal("8.99"),
            ean_tributavel="7896000000001",
            ind_total=1,
            icms_modalidade="00",
            icms_origem=0,
            pis_modalidade="07",
            cofins_modalidade="07",
            valor_tributos_aprox="5.00",
            # Grupo K - Medicamento
            med_cProdANVISA="1234567890123",  # Código ANVISA com 13 dígitos
            med_vPMC=Decimal("12.50"),  # Preço Máximo ao Consumidor
        )

        # Adiciona rastreabilidade (lotes)
        produto.adicionar_rastro(
            nLote="LOTE2024001",
            qLote=Decimal("3.000"),
            dFab=datetime.date(2024, 1, 15),
            dVal=datetime.date(2026, 1, 15),
        )

        produto.adicionar_rastro(
            nLote="LOTE2024002",
            qLote=Decimal("2.000"),
            dFab=datetime.date(2024, 2, 20),
            dVal=datetime.date(2026, 2, 20),
            cAgreg="AGR123456",
        )

        self.notafiscal.adicionar_pagamento(
            t_pag="01", x_pag="Dinheiro", v_pag=44.95, ind_pag=0
        )

    def preenche_notafiscal_medicamento_isento(self):
        """Cria uma NF-e com medicamento isento de registro ANVISA"""
        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2024, 6, 15, 10, 30, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2024, 6, 15, 11, 0, 0, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf="PR",
            natureza_operacao="VENDA",
            modelo=55,
            serie="1",
            numero_nf="12346",
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,
            municipio="4118402",
            tipo_impressao_danfe=1,
            forma_emissao="1",
            cliente_final=1,
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao="1",
            processo_emissao="0",
            transporte_modalidade_frete=9,
        )

        # Adiciona medicamento isento de registro ANVISA
        self.notafiscal.adicionar_produto_servico(
            codigo="MED002",
            descricao="PRODUTO FITOTERAPICO TRADICIONAL",
            ncm="30049099",
            ean="7896000000002",
            cfop="5102",
            unidade_comercial="UN",
            quantidade_comercial=Decimal("2"),
            valor_unitario_comercial=Decimal("25.00"),
            valor_total_bruto=Decimal("50.00"),
            unidade_tributavel="UN",
            quantidade_tributavel=Decimal("2"),
            valor_unitario_tributavel=Decimal("25.00"),
            ean_tributavel="7896000000002",
            ind_total=1,
            icms_modalidade="00",
            icms_origem=0,
            pis_modalidade="07",
            cofins_modalidade="07",
            valor_tributos_aprox="5.00",
            # Grupo K - Medicamento isento
            med_cProdANVISA="ISENTO",
            med_xMotivoIsencao="RDC 26/2014 - Fitoterápico tradicional",
            med_vPMC=Decimal("35.00"),
        )

        self.notafiscal.adicionar_pagamento(
            t_pag="01", x_pag="Dinheiro", v_pag=50.00, ind_pag=0
        )

    def serializa_nfe(self):
        serializador = SerializacaoXML(_fonte_dados, homologacao=self.homologacao)
        return serializador.exportar()

    def assina_xml(self):
        a1 = AssinaturaA1(self.certificado, self.senha)
        return a1.assinar(self.xml)

    def validacao_com_xsd_do_xml_gerado(self):
        self.validacao.validar_etree(
            xml_doc=self.xml_assinado, xsd_file=self.xsd_nfe, use_assert=True
        )

    def test_medicamento_com_rastro(self):
        """Testa NF-e de medicamento com código ANVISA e rastreabilidade"""
        # Preenche as classes do pynfe
        self.preenche_emitente()
        self.preenche_destinatario()
        self.preenche_notafiscal_medicamento_com_rastro()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Testa grupo med (inside prod, as product-specific group)
        med_cprodanvisa = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:med/ns:cProdANVISA", namespaces=self.ns
        )[0].text
        med_vpmc = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:med/ns:vPMC", namespaces=self.ns
        )[0].text

        self.assertEqual(med_cprodanvisa, "1234567890123")
        self.assertEqual(med_vpmc, "12.50")

        # Verifica que não existe xMotivoIsencao (não é ISENTO)
        med_xmotivoisencao = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:med/ns:xMotivoIsencao", namespaces=self.ns
        )
        self.assertEqual(len(med_xmotivoisencao), 0)

        # Testa grupo rastro (deve ter 2 lotes)
        rastro_nlote = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:rastro/ns:nLote", namespaces=self.ns
        )
        self.assertEqual(len(rastro_nlote), 2)

        # Primeiro lote
        self.assertEqual(rastro_nlote[0].text, "LOTE2024001")
        rastro_qlote_1 = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:rastro[1]/ns:qLote", namespaces=self.ns
        )[0].text
        rastro_dfab_1 = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:rastro[1]/ns:dFab", namespaces=self.ns
        )[0].text
        rastro_dval_1 = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:rastro[1]/ns:dVal", namespaces=self.ns
        )[0].text
        self.assertEqual(rastro_qlote_1, "3.000")
        self.assertEqual(rastro_dfab_1, "2024-01-15")
        self.assertEqual(rastro_dval_1, "2026-01-15")

        # Segundo lote (com código de agregação)
        self.assertEqual(rastro_nlote[1].text, "LOTE2024002")
        rastro_cagreg_2 = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:rastro[2]/ns:cAgreg", namespaces=self.ns
        )[0].text
        self.assertEqual(rastro_cagreg_2, "AGR123456")

        # Valida contra o XSD
        self.validacao_com_xsd_do_xml_gerado()

    def test_medicamento_isento_anvisa(self):
        """Testa NF-e de medicamento isento de registro ANVISA"""
        # Preenche as classes do pynfe
        self.preenche_emitente()
        self.preenche_destinatario()
        self.preenche_notafiscal_medicamento_isento()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Testa grupo med com ISENTO (inside prod)
        med_cprodanvisa = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:med/ns:cProdANVISA", namespaces=self.ns
        )[0].text
        med_xmotivoisencao = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:med/ns:xMotivoIsencao", namespaces=self.ns
        )[0].text
        med_vpmc = self.xml_assinado.xpath(
            "//ns:det/ns:prod/ns:med/ns:vPMC", namespaces=self.ns
        )[0].text

        self.assertEqual(med_cprodanvisa, "ISENTO")
        self.assertEqual(med_xmotivoisencao, "RDC 26/2014 - Fitoterapico tradicional")
        self.assertEqual(med_vpmc, "35.00")

        # Valida contra o XSD
        self.validacao_com_xsd_do_xml_gerado()

    def test_notafiscal_rastro_entidade(self):
        """Testa a criação da entidade NotaFiscalRastro"""
        rastro = NotaFiscalRastro(
            nLote="LOTE123",
            qLote=Decimal("10.500"),
            dFab=datetime.date(2024, 1, 1),
            dVal=datetime.date(2025, 12, 31),
            cAgreg="AGREG001",
        )

        self.assertEqual(rastro.nLote, "LOTE123")
        self.assertEqual(rastro.qLote, Decimal("10.500"))
        self.assertEqual(rastro.dFab, datetime.date(2024, 1, 1))
        self.assertEqual(rastro.dVal, datetime.date(2025, 12, 31))
        self.assertEqual(rastro.cAgreg, "AGREG001")

    def test_produto_adicionar_rastro(self):
        """Testa o método adicionar_rastro do NotaFiscalProduto"""
        self.preenche_emitente()
        self.preenche_destinatario()

        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2024, 6, 15, 10, 30, 0, tzinfo=utc)

        notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf="PR",
            natureza_operacao="VENDA",
            modelo=55,
            serie="1",
            numero_nf="99999",
            data_emissao=data_emissao,
            tipo_documento=1,
            municipio="4118402",
            tipo_impressao_danfe=1,
            forma_emissao="1",
            cliente_final=1,
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao="1",
            processo_emissao="0",
            transporte_modalidade_frete=9,
        )

        produto = notafiscal.adicionar_produto_servico(
            codigo="PROD001",
            descricao="Produto com rastreabilidade",
            ncm="12345678",
            ean="SEM GTIN",
            cfop="5102",
            unidade_comercial="UN",
            quantidade_comercial=Decimal("1"),
            valor_unitario_comercial=Decimal("100.00"),
            valor_total_bruto=Decimal("100.00"),
            unidade_tributavel="UN",
            quantidade_tributavel=Decimal("1"),
            valor_unitario_tributavel=Decimal("100.00"),
            ean_tributavel="SEM GTIN",
            ind_total=1,
            icms_modalidade="00",
            icms_origem=0,
            pis_modalidade="07",
            cofins_modalidade="07",
            valor_tributos_aprox="10.00",
        )

        # Adiciona múltiplos rastros
        rastro1 = produto.adicionar_rastro(
            nLote="LOTE_A",
            qLote=Decimal("0.500"),
            dFab=datetime.date(2024, 3, 1),
            dVal=datetime.date(2025, 3, 1),
        )

        rastro2 = produto.adicionar_rastro(
            nLote="LOTE_B",
            qLote=Decimal("0.500"),
            dFab=datetime.date(2024, 4, 1),
            dVal=datetime.date(2025, 4, 1),
        )

        # Verifica que os rastros foram adicionados
        self.assertEqual(len(produto.rastro), 2)
        self.assertIsInstance(rastro1, NotaFiscalRastro)
        self.assertIsInstance(rastro2, NotaFiscalRastro)
        self.assertEqual(produto.rastro[0].nLote, "LOTE_A")
        self.assertEqual(produto.rastro[1].nLote, "LOTE_B")


if __name__ == "__main__":
    unittest.main()
