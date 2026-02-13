#!/usr/bin/env python
# *-* encoding: utf8 *-*

"""Tests for Reforma Tributaria IBS/CBS/IS serialization (EC 132/2023)."""

import datetime
import unittest
from decimal import Decimal

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscal
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.processamento.serializacao import SerializacaoXML
from pynfe.utils.flags import CODIGO_BRASIL, NAMESPACE_NFE


class ReformaTributariaSerializacaoTestCase(unittest.TestCase):
    """Tests for IBS/CBS/IS (Reforma Tributaria) XML serialization."""

    def setUp(self):
        self.certificado = "./tests/certificado.pfx"
        self.senha = bytes("123456", "utf-8")
        self.uf = "pr"
        self.homologacao = True
        self.ns = {"ns": NAMESPACE_NFE}

    def _emitente(self):
        return Emitente(
            razao_social="NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL",
            nome_fantasia="Empresa Teste",
            cnpj="99999999000199",
            codigo_de_regime_tributario="3",
            inscricao_estadual="9999999999",
            inscricao_municipal="12345",
            cnae_fiscal="9999999",
            endereco_logradouro="Rua da Paz",
            endereco_numero="666",
            endereco_bairro="Sossego",
            endereco_municipio="Paranavaí",
            endereco_uf="PR",
            endereco_cep="87704000",
            endereco_pais=CODIGO_BRASIL,
        )

    def _cliente(self):
        return Cliente(
            razao_social="JOSE DA SILVA",
            tipo_documento="CPF",
            email="email@email.com",
            numero_documento="12345678900",
            indicador_ie=9,
            endereco_logradouro="Rua dos Bobos",
            endereco_numero="Zero",
            endereco_bairro="Aquele Mesmo",
            endereco_municipio="Brasilia",
            endereco_uf="DF",
            endereco_cep="12345123",
            endereco_pais=CODIGO_BRASIL,
        )

    def _nota_fiscal(self, emitente, cliente):
        utc = datetime.timezone.utc
        return NotaFiscal(
            emitente=emitente,
            cliente=cliente,
            uf="PR",
            natureza_operacao="VENDA",
            forma_pagamento=0,
            modelo=55,
            serie="1",
            numero_nf="111",
            data_emissao=datetime.datetime(2026, 1, 15, 12, 0, 0, tzinfo=utc),
            data_saida_entrada=datetime.datetime(2026, 1, 15, 13, 0, 0, tzinfo=utc),
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
            informacoes_adicionais_interesse_fisco="Reforma Tributaria teste",
            totais_tributos_aproximado=Decimal("0.00"),
        )

    def _serializar_e_assinar(self):
        serializador = SerializacaoXML(_fonte_dados, homologacao=self.homologacao)
        xml = serializador.exportar()
        a1 = AssinaturaA1(self.certificado, self.senha)
        return a1.assinar(xml)

    # ------------------------------------------------------------------
    # Test 1: CST 01 - Tributada Integralmente (CBS + IBS + IS)
    # ------------------------------------------------------------------
    def test_cst01_cbs_ibs_is_tributada_integralmente(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        nf.adicionar_produto_servico(
            codigo="001",
            descricao="Produto teste reforma tributaria",
            ncm="99999999",
            ean="SEM GTIN",
            cfop="5102",
            unidade_comercial="UN",
            quantidade_comercial=Decimal("10"),
            valor_unitario_comercial=Decimal("100.00"),
            valor_total_bruto=Decimal("1000.00"),
            unidade_tributavel="UN",
            quantidade_tributavel=Decimal("10"),
            valor_unitario_tributavel=Decimal("100.00"),
            ean_tributavel="SEM GTIN",
            ind_total=1,
            icms_modalidade="00",
            icms_origem=0,
            icms_csosn="",
            pis_modalidade="99",
            cofins_modalidade="99",
            pis_valor_base_calculo=Decimal("0.00"),
            pis_aliquota_percentual=Decimal("0.00"),
            pis_valor=Decimal("0.00"),
            cofins_valor_base_calculo=Decimal("0.00"),
            cofins_aliquota_percentual=Decimal("0.00"),
            cofins_valor=Decimal("0.00"),
            valor_tributos_aprox="0",
            # CBS
            cbs_situacao_tributaria="01",
            cbs_valor_base_calculo=Decimal("1000.00"),
            cbs_aliquota=Decimal("8.8000"),
            cbs_valor=Decimal("88.00"),
            # IBS
            ibs_situacao_tributaria="01",
            ibs_valor_base_calculo=Decimal("1000.00"),
            ibs_aliquota=Decimal("17.7000"),
            ibs_valor=Decimal("177.00"),
            ibs_codigo_municipio_destino="4118402",
            # IS
            is_situacao_tributaria="01",
            is_valor_base_calculo=Decimal("1000.00"),
            is_aliquota=Decimal("1.0000"),
            is_valor=Decimal("10.00"),
        )

        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=1275.00, ind_pag=0)

        xml = self._serializar_e_assinar()

        # impostoMisto group exists
        imposto_misto = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto", namespaces=self.ns)
        self.assertEqual(len(imposto_misto), 1)

        # CBS
        cst_cbs = xml.xpath(
            "//ns:det/ns:imposto/ns:impostoMisto/ns:CBS/ns:CST", namespaces=self.ns
        )[0].text
        self.assertEqual(cst_cbs, "01")

        vbc_cbs = xml.xpath(
            "//ns:det/ns:imposto/ns:impostoMisto/ns:CBS/ns:vBC", namespaces=self.ns
        )[0].text
        self.assertEqual(vbc_cbs, "1000.00")

        pcbs = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:CBS/ns:pCBS", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(pcbs, "8.8000")

        vcbs = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:CBS/ns:vCBS", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(vcbs, "88.00")

        # IBS
        cst_ibs = xml.xpath(
            "//ns:det/ns:imposto/ns:impostoMisto/ns:IBS/ns:CST", namespaces=self.ns
        )[0].text
        self.assertEqual(cst_ibs, "01")

        vbc_ibs = xml.xpath(
            "//ns:det/ns:imposto/ns:impostoMisto/ns:IBS/ns:vBC", namespaces=self.ns
        )[0].text
        self.assertEqual(vbc_ibs, "1000.00")

        pibs = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:IBS/ns:pIBS", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(pibs, "17.7000")

        vibs = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:IBS/ns:vIBS", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(vibs, "177.00")

        cmun = xml.xpath(
            "//ns:det/ns:imposto/ns:impostoMisto/ns:IBS/ns:cMunDest", namespaces=self.ns
        )[0].text
        self.assertEqual(cmun, "4118402")

        # IS
        cst_is = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:IS/ns:CST", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(cst_is, "01")

        vbc_is = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:IS/ns:vBC", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(vbc_is, "1000.00")

        pis_val = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:IS/ns:pIS", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(pis_val, "1.0000")

        vis = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:IS/ns:vIS", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(vis, "10.00")

        # Totals
        vcbs_total = xml.xpath("//ns:total/ns:ICMSTot/ns:vCBS", namespaces=self.ns)[0].text
        self.assertEqual(vcbs_total, "88.00")

        vibs_total = xml.xpath("//ns:total/ns:ICMSTot/ns:vIBS", namespaces=self.ns)[0].text
        self.assertEqual(vibs_total, "177.00")

        vis_total = xml.xpath("//ns:total/ns:ICMSTot/ns:vIS", namespaces=self.ns)[0].text
        self.assertEqual(vis_total, "10.00")

        # vNF includes IBS/CBS/IS
        vnf = xml.xpath("//ns:total/ns:ICMSTot/ns:vNF", namespaces=self.ns)[0].text
        self.assertEqual(vnf, "1275.00")

    # ------------------------------------------------------------------
    # Test 2: CST 03 - Isencao (CBS + IBS isentas, no IS)
    # ------------------------------------------------------------------
    def test_cst03_isencao_sem_valores(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        nf.adicionar_produto_servico(
            codigo="002",
            descricao="Produto isento reforma tributaria",
            ncm="99999999",
            ean="SEM GTIN",
            cfop="5102",
            unidade_comercial="UN",
            quantidade_comercial=Decimal("1"),
            valor_unitario_comercial=Decimal("50.00"),
            valor_total_bruto=Decimal("50.00"),
            unidade_tributavel="UN",
            quantidade_tributavel=Decimal("1"),
            valor_unitario_tributavel=Decimal("50.00"),
            ean_tributavel="SEM GTIN",
            ind_total=1,
            icms_modalidade="00",
            icms_origem=0,
            icms_csosn="",
            pis_modalidade="99",
            cofins_modalidade="99",
            pis_valor_base_calculo=Decimal("0.00"),
            pis_aliquota_percentual=Decimal("0.00"),
            pis_valor=Decimal("0.00"),
            cofins_valor_base_calculo=Decimal("0.00"),
            cofins_aliquota_percentual=Decimal("0.00"),
            cofins_valor=Decimal("0.00"),
            valor_tributos_aprox="0",
            # CBS isenta
            cbs_situacao_tributaria="03",
            # IBS isenta
            ibs_situacao_tributaria="03",
            # No IS
        )

        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=50.00, ind_pag=0)

        xml = self._serializar_e_assinar()

        # impostoMisto group exists (CBS + IBS present even if exempt)
        imposto_misto = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto", namespaces=self.ns)
        self.assertEqual(len(imposto_misto), 1)

        # CBS CST present, no value tags
        cst_cbs = xml.xpath(
            "//ns:det/ns:imposto/ns:impostoMisto/ns:CBS/ns:CST", namespaces=self.ns
        )[0].text
        self.assertEqual(cst_cbs, "03")

        vbc_cbs = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:CBS/ns:vBC", namespaces=self.ns)
        self.assertEqual(len(vbc_cbs), 0)  # No vBC for CST 03

        # IBS CST present, no value tags
        cst_ibs = xml.xpath(
            "//ns:det/ns:imposto/ns:impostoMisto/ns:IBS/ns:CST", namespaces=self.ns
        )[0].text
        self.assertEqual(cst_ibs, "03")

        vbc_ibs = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:IBS/ns:vBC", namespaces=self.ns)
        self.assertEqual(len(vbc_ibs), 0)

        # No IS group
        is_group = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:IS", namespaces=self.ns)
        self.assertEqual(len(is_group), 0)

        # No totals for CBS/IBS/IS (all zero)
        vcbs_total = xml.xpath("//ns:total/ns:ICMSTot/ns:vCBS", namespaces=self.ns)
        self.assertEqual(len(vcbs_total), 0)

    # ------------------------------------------------------------------
    # Test 3: No reforma data - impostoMisto NOT emitted
    # ------------------------------------------------------------------
    def test_sem_reforma_tributaria_sem_imposto_misto(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        nf.adicionar_produto_servico(
            codigo="003",
            descricao="Produto sem reforma",
            ncm="99999999",
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
            icms_csosn="",
            pis_modalidade="51",
            cofins_modalidade="51",
            pis_valor_base_calculo=Decimal("100.00"),
            pis_aliquota_percentual=Decimal("0.65"),
            pis_valor=Decimal("0.65"),
            cofins_valor_base_calculo=Decimal("100.00"),
            cofins_aliquota_percentual=Decimal("3.00"),
            cofins_valor=Decimal("3.00"),
            valor_tributos_aprox="0",
        )

        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=100.00, ind_pag=0)

        xml = self._serializar_e_assinar()

        # impostoMisto should NOT exist
        imposto_misto = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto", namespaces=self.ns)
        self.assertEqual(len(imposto_misto), 0)

        # No reform totals
        vcbs_total = xml.xpath("//ns:total/ns:ICMSTot/ns:vCBS", namespaces=self.ns)
        self.assertEqual(len(vcbs_total), 0)

        vibs_total = xml.xpath("//ns:total/ns:ICMSTot/ns:vIBS", namespaces=self.ns)
        self.assertEqual(len(vibs_total), 0)

    # ------------------------------------------------------------------
    # Test 4: Totals accumulation - multiple products
    # ------------------------------------------------------------------
    def test_totais_acumulacao_multiplos_produtos(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        # Product 1: CBS=88, IBS=177, IS=10
        nf.adicionar_produto_servico(
            codigo="004",
            descricao="Produto 1 reforma",
            ncm="99999999",
            ean="SEM GTIN",
            cfop="5102",
            unidade_comercial="UN",
            quantidade_comercial=Decimal("10"),
            valor_unitario_comercial=Decimal("100.00"),
            valor_total_bruto=Decimal("1000.00"),
            unidade_tributavel="UN",
            quantidade_tributavel=Decimal("10"),
            valor_unitario_tributavel=Decimal("100.00"),
            ean_tributavel="SEM GTIN",
            ind_total=1,
            icms_modalidade="00",
            icms_origem=0,
            icms_csosn="",
            pis_modalidade="99",
            cofins_modalidade="99",
            pis_valor=Decimal("0.00"),
            cofins_valor=Decimal("0.00"),
            valor_tributos_aprox="0",
            cbs_situacao_tributaria="01",
            cbs_valor_base_calculo=Decimal("1000.00"),
            cbs_aliquota=Decimal("8.8000"),
            cbs_valor=Decimal("88.00"),
            ibs_situacao_tributaria="01",
            ibs_valor_base_calculo=Decimal("1000.00"),
            ibs_aliquota=Decimal("17.7000"),
            ibs_valor=Decimal("177.00"),
            is_situacao_tributaria="01",
            is_valor_base_calculo=Decimal("1000.00"),
            is_aliquota=Decimal("1.0000"),
            is_valor=Decimal("10.00"),
        )

        # Product 2: CBS=44, IBS=88.50, IS=5
        nf.adicionar_produto_servico(
            codigo="005",
            descricao="Produto 2 reforma",
            ncm="99999999",
            ean="SEM GTIN",
            cfop="5102",
            unidade_comercial="UN",
            quantidade_comercial=Decimal("5"),
            valor_unitario_comercial=Decimal("100.00"),
            valor_total_bruto=Decimal("500.00"),
            unidade_tributavel="UN",
            quantidade_tributavel=Decimal("5"),
            valor_unitario_tributavel=Decimal("100.00"),
            ean_tributavel="SEM GTIN",
            ind_total=1,
            icms_modalidade="00",
            icms_origem=0,
            icms_csosn="",
            pis_modalidade="99",
            cofins_modalidade="99",
            pis_valor=Decimal("0.00"),
            cofins_valor=Decimal("0.00"),
            valor_tributos_aprox="0",
            cbs_situacao_tributaria="01",
            cbs_valor_base_calculo=Decimal("500.00"),
            cbs_aliquota=Decimal("8.8000"),
            cbs_valor=Decimal("44.00"),
            ibs_situacao_tributaria="01",
            ibs_valor_base_calculo=Decimal("500.00"),
            ibs_aliquota=Decimal("17.7000"),
            ibs_valor=Decimal("88.50"),
            is_situacao_tributaria="01",
            is_valor_base_calculo=Decimal("500.00"),
            is_aliquota=Decimal("1.0000"),
            is_valor=Decimal("5.00"),
        )

        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=1907.50, ind_pag=0)

        xml = self._serializar_e_assinar()

        # Accumulated totals: CBS=132.00, IBS=265.50, IS=15.00
        vcbs_total = xml.xpath("//ns:total/ns:ICMSTot/ns:vCBS", namespaces=self.ns)[0].text
        self.assertEqual(vcbs_total, "132.00")

        vibs_total = xml.xpath("//ns:total/ns:ICMSTot/ns:vIBS", namespaces=self.ns)[0].text
        self.assertEqual(vibs_total, "265.50")

        vis_total = xml.xpath("//ns:total/ns:ICMSTot/ns:vIS", namespaces=self.ns)[0].text
        self.assertEqual(vis_total, "15.00")

        # vNF = 1000 + 500 + 132 + 265.50 + 15 = 1912.50
        # Wait: vNF = sum of (vProd + IBS + CBS + IS) for each product
        # Prod1: 1000 + 177 + 88 + 10 = 1275
        # Prod2: 500 + 88.50 + 44 + 5 = 637.50
        # Total: 1275 + 637.50 = 1912.50
        vnf = xml.xpath("//ns:total/ns:ICMSTot/ns:vNF", namespaces=self.ns)[0].text
        self.assertEqual(vnf, "1912.50")

    # ------------------------------------------------------------------
    # Test 5: Mixed legacy + reform (ICMS/PIS/COFINS + IBS/CBS)
    # ------------------------------------------------------------------
    def test_misto_legacy_icms_pis_cofins_com_ibs_cbs(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        nf.adicionar_produto_servico(
            codigo="006",
            descricao="Produto misto legado e reforma",
            ncm="99999999",
            ean="SEM GTIN",
            cfop="5102",
            unidade_comercial="UN",
            quantidade_comercial=Decimal("1"),
            valor_unitario_comercial=Decimal("200.00"),
            valor_total_bruto=Decimal("200.00"),
            unidade_tributavel="UN",
            quantidade_tributavel=Decimal("1"),
            valor_unitario_tributavel=Decimal("200.00"),
            ean_tributavel="SEM GTIN",
            ind_total=1,
            # Legacy ICMS
            icms_modalidade="00",
            icms_origem=0,
            icms_csosn="",
            icms_valor_base_calculo=Decimal("200.00"),
            icms_aliquota=Decimal("18.00"),
            icms_valor=Decimal("36.00"),
            # Legacy PIS
            pis_modalidade="01",
            pis_valor_base_calculo=Decimal("200.00"),
            pis_aliquota_percentual=Decimal("1.65"),
            pis_valor=Decimal("3.30"),
            # Legacy COFINS
            cofins_modalidade="01",
            cofins_valor_base_calculo=Decimal("200.00"),
            cofins_aliquota_percentual=Decimal("7.60"),
            cofins_valor=Decimal("15.20"),
            valor_tributos_aprox="0",
            # Reform CBS (coexisting during transition)
            cbs_situacao_tributaria="02",
            cbs_valor_base_calculo=Decimal("200.00"),
            cbs_aliquota=Decimal("4.4000"),
            cbs_valor=Decimal("8.80"),
            # Reform IBS (coexisting during transition)
            ibs_situacao_tributaria="02",
            ibs_valor_base_calculo=Decimal("200.00"),
            ibs_aliquota=Decimal("8.8500"),
            ibs_valor=Decimal("17.70"),
        )

        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=226.50, ind_pag=0)

        xml = self._serializar_e_assinar()

        # Legacy ICMS still present
        icms_cst = xml.xpath("//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:CST", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(icms_cst, "00")

        # Legacy PIS still present
        pis_cst = xml.xpath("//ns:det/ns:imposto/ns:PIS/ns:PISAliq/ns:CST", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(pis_cst, "01")

        # Legacy COFINS still present
        cofins_cst = xml.xpath(
            "//ns:det/ns:imposto/ns:COFINS/ns:COFINSAliq/ns:CST", namespaces=self.ns
        )[0].text
        self.assertEqual(cofins_cst, "01")

        # Reform CBS also present
        cbs_cst = xml.xpath(
            "//ns:det/ns:imposto/ns:impostoMisto/ns:CBS/ns:CST", namespaces=self.ns
        )[0].text
        self.assertEqual(cbs_cst, "02")

        # Reform IBS also present
        ibs_cst = xml.xpath(
            "//ns:det/ns:imposto/ns:impostoMisto/ns:IBS/ns:CST", namespaces=self.ns
        )[0].text
        self.assertEqual(ibs_cst, "02")

        # No IS in this test
        is_group = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto/ns:IS", namespaces=self.ns)
        self.assertEqual(len(is_group), 0)


if __name__ == "__main__":
    unittest.main()
