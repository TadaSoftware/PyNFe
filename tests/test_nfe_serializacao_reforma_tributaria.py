#!/usr/bin/env python
# *-* encoding: utf8 *-*

"""Tests for Reforma Tributaria IBS/CBS serialization (NT 2025.002-RTC).

Note: IS (Imposto Seletivo) is not yet in the SEFAZ schema (starts 2027).
IS entity fields are preserved for future use but not serialized to XML.
"""

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
    """Tests for IBSCBS (Reforma Tributaria) XML serialization per NT 2025.002-RTC."""

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

    def _base_product_kwargs(self):
        """Common product kwargs without reforma tributaria fields."""
        return dict(
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
        )

    def _serializar_e_assinar(self):
        serializador = SerializacaoXML(_fonte_dados, homologacao=self.homologacao)
        xml = serializador.exportar()
        a1 = AssinaturaA1(self.certificado, self.senha)
        return a1.assinar(xml)

    # ------------------------------------------------------------------
    # Test 1: CST 000 — full regular taxation with IBS UF/Mun split
    # ------------------------------------------------------------------
    def test_cst000_ibscbs_tributacao_integral(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        kwargs = self._base_product_kwargs()
        kwargs.update(
            ibscbs_cst="000",
            ibscbs_c_class_trib="000001",
            ibscbs_vbc=Decimal("1000.00"),
            ibscbs_p_ibs_uf=Decimal("0.1000"),
            ibscbs_v_ibs_uf=Decimal("1.00"),
            ibscbs_p_ibs_mun=Decimal("0.0000"),
            ibscbs_v_ibs_mun=Decimal("0.00"),
            ibscbs_v_ibs=Decimal("1.00"),
            ibscbs_p_cbs=Decimal("0.9000"),
            ibscbs_v_cbs=Decimal("9.00"),
        )
        nf.adicionar_produto_servico(**kwargs)
        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=1000.00, ind_pag=0)

        xml = self._serializar_e_assinar()

        # <IBSCBS> is direct child of <imposto> (no impostoMisto wrapper)
        ibscbs = xml.xpath("//ns:det/ns:imposto/ns:IBSCBS", namespaces=self.ns)
        self.assertEqual(len(ibscbs), 1)

        # No impostoMisto wrapper
        imposto_misto = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto", namespaces=self.ns)
        self.assertEqual(len(imposto_misto), 0)

        # CST is 3-digit
        cst = xml.xpath("//ns:IBSCBS/ns:CST", namespaces=self.ns)[0].text
        self.assertEqual(cst, "000")

        # cClassTrib present
        cclass = xml.xpath("//ns:IBSCBS/ns:cClassTrib", namespaces=self.ns)[0].text
        self.assertEqual(cclass, "000001")

        # Shared vBC at gIBSCBS level
        vbc = xml.xpath("//ns:IBSCBS/ns:gIBSCBS/ns:vBC", namespaces=self.ns)[0].text
        self.assertEqual(vbc, "1000.00")

        # gIBSUF
        p_ibs_uf = xml.xpath("//ns:IBSCBS/ns:gIBSCBS/ns:gIBSUF/ns:pIBSUF", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(p_ibs_uf, "0.1000")
        v_ibs_uf = xml.xpath("//ns:IBSCBS/ns:gIBSCBS/ns:gIBSUF/ns:vIBSUF", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(v_ibs_uf, "1.00")

        # gIBSMun
        p_ibs_mun = xml.xpath("//ns:IBSCBS/ns:gIBSCBS/ns:gIBSMun/ns:pIBSMun", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(p_ibs_mun, "0.0000")
        v_ibs_mun = xml.xpath("//ns:IBSCBS/ns:gIBSCBS/ns:gIBSMun/ns:vIBSMun", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(v_ibs_mun, "0.00")

        # vIBS total
        v_ibs = xml.xpath("//ns:IBSCBS/ns:gIBSCBS/ns:vIBS", namespaces=self.ns)[0].text
        self.assertEqual(v_ibs, "1.00")

        # gCBS
        p_cbs = xml.xpath("//ns:IBSCBS/ns:gIBSCBS/ns:gCBS/ns:pCBS", namespaces=self.ns)[0].text
        self.assertEqual(p_cbs, "0.9000")
        v_cbs = xml.xpath("//ns:IBSCBS/ns:gIBSCBS/ns:gCBS/ns:vCBS", namespaces=self.ns)[0].text
        self.assertEqual(v_cbs, "9.00")

        # IS NOT emitted in XML (schema not ready until 2027)
        is_tag = xml.xpath("//ns:det/ns:imposto/ns:IS", namespaces=self.ns)
        self.assertEqual(len(is_tag), 0)

    # ------------------------------------------------------------------
    # Test 2: CST 222 — isenção (no vBC, values zero)
    # ------------------------------------------------------------------
    def test_cst222_isencao_sem_valores(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        kwargs = self._base_product_kwargs()
        kwargs.update(
            codigo="002",
            descricao="Produto isento reforma tributaria",
            quantidade_comercial=Decimal("1"),
            valor_unitario_comercial=Decimal("50.00"),
            valor_total_bruto=Decimal("50.00"),
            quantidade_tributavel=Decimal("1"),
            valor_unitario_tributavel=Decimal("50.00"),
            ibscbs_cst="222",
            ibscbs_c_class_trib="000002",
        )
        nf.adicionar_produto_servico(**kwargs)
        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=50.00, ind_pag=0)

        xml = self._serializar_e_assinar()

        # IBSCBS present even if exempt
        ibscbs = xml.xpath("//ns:det/ns:imposto/ns:IBSCBS", namespaces=self.ns)
        self.assertEqual(len(ibscbs), 1)

        # CST present
        cst = xml.xpath("//ns:IBSCBS/ns:CST", namespaces=self.ns)[0].text
        self.assertEqual(cst, "222")

        # cClassTrib present
        cclass = xml.xpath("//ns:IBSCBS/ns:cClassTrib", namespaces=self.ns)[0].text
        self.assertEqual(cclass, "000002")

        # No gIBSCBS group (CST 222 is not in taxable CSTs)
        gibscbs = xml.xpath("//ns:IBSCBS/ns:gIBSCBS", namespaces=self.ns)
        self.assertEqual(len(gibscbs), 0)

        # No IS group
        is_group = xml.xpath("//ns:det/ns:imposto/ns:IS", namespaces=self.ns)
        self.assertEqual(len(is_group), 0)

    # ------------------------------------------------------------------
    # Test 3: No reforma data — IBSCBS not emitted
    # ------------------------------------------------------------------
    def test_sem_reforma_tributaria_sem_ibscbs(self):
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

        # IBSCBS should NOT exist
        ibscbs = xml.xpath("//ns:det/ns:imposto/ns:IBSCBS", namespaces=self.ns)
        self.assertEqual(len(ibscbs), 0)

        # No impostoMisto either
        imposto_misto = xml.xpath("//ns:det/ns:imposto/ns:impostoMisto", namespaces=self.ns)
        self.assertEqual(len(imposto_misto), 0)

        # No IBSCBSTot
        ibscbs_tot = xml.xpath("//ns:total/ns:IBSCBSTot", namespaces=self.ns)
        self.assertEqual(len(ibscbs_tot), 0)

    # ------------------------------------------------------------------
    # Test 4: Multiple products — totals accumulation with split IBS
    # ------------------------------------------------------------------
    def test_totais_acumulacao_multiplos_produtos(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        base = self._base_product_kwargs()

        # Product 1: vBC=1000, IBS UF=1.00, IBS Mun=0.50, IBS=1.50, CBS=9.00
        p1 = dict(base)
        p1.update(
            codigo="004",
            descricao="Produto 1 reforma",
            ibscbs_cst="000",
            ibscbs_c_class_trib="000001",
            ibscbs_vbc=Decimal("1000.00"),
            ibscbs_p_ibs_uf=Decimal("0.1000"),
            ibscbs_v_ibs_uf=Decimal("1.00"),
            ibscbs_p_ibs_mun=Decimal("0.0500"),
            ibscbs_v_ibs_mun=Decimal("0.50"),
            ibscbs_v_ibs=Decimal("1.50"),
            ibscbs_p_cbs=Decimal("0.9000"),
            ibscbs_v_cbs=Decimal("9.00"),
        )
        nf.adicionar_produto_servico(**p1)

        # Product 2: vBC=500, IBS UF=0.50, IBS Mun=0.25, IBS=0.75, CBS=4.50
        p2 = dict(base)
        p2.update(
            codigo="005",
            descricao="Produto 2 reforma",
            quantidade_comercial=Decimal("5"),
            valor_unitario_comercial=Decimal("100.00"),
            valor_total_bruto=Decimal("500.00"),
            quantidade_tributavel=Decimal("5"),
            valor_unitario_tributavel=Decimal("100.00"),
            ibscbs_cst="000",
            ibscbs_c_class_trib="000001",
            ibscbs_vbc=Decimal("500.00"),
            ibscbs_p_ibs_uf=Decimal("0.1000"),
            ibscbs_v_ibs_uf=Decimal("0.50"),
            ibscbs_p_ibs_mun=Decimal("0.0500"),
            ibscbs_v_ibs_mun=Decimal("0.25"),
            ibscbs_v_ibs=Decimal("0.75"),
            ibscbs_p_cbs=Decimal("0.9000"),
            ibscbs_v_cbs=Decimal("4.50"),
        )
        nf.adicionar_produto_servico(**p2)

        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=1500.00, ind_pag=0)

        xml = self._serializar_e_assinar()

        # Totals in IBSCBSTot (NOT ICMSTot)
        ibscbs_tot = xml.xpath("//ns:total/ns:IBSCBSTot", namespaces=self.ns)
        self.assertEqual(len(ibscbs_tot), 1)

        # vBCIBSCBS = sum of all ibscbs_vbc = 1000 + 500 = 1500
        v_bc = xml.xpath("//ns:IBSCBSTot/ns:vBCIBSCBS", namespaces=self.ns)[0].text
        self.assertEqual(v_bc, "1500.00")

        # Accumulated: IBS UF=1.50, IBS Mun=0.75, IBS=2.25, CBS=13.50
        v_ibs_uf = xml.xpath("//ns:IBSCBSTot/ns:gIBS/ns:gIBSUF/ns:vIBSUF", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(v_ibs_uf, "1.50")

        v_ibs_mun = xml.xpath("//ns:IBSCBSTot/ns:gIBS/ns:gIBSMun/ns:vIBSMun", namespaces=self.ns)[
            0
        ].text
        self.assertEqual(v_ibs_mun, "0.75")

        v_ibs = xml.xpath("//ns:IBSCBSTot/ns:gIBS/ns:vIBS", namespaces=self.ns)[0].text
        self.assertEqual(v_ibs, "2.25")

        v_cbs = xml.xpath("//ns:IBSCBSTot/ns:gCBS/ns:vCBS", namespaces=self.ns)[0].text
        self.assertEqual(v_cbs, "13.50")

    # ------------------------------------------------------------------
    # Test 5: Mixed legacy (ICMS/PIS/COFINS) + reform (IBSCBS) coexistence
    # ------------------------------------------------------------------
    def test_misto_legacy_icms_pis_cofins_com_ibscbs(self):
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
            # Reform IBSCBS (coexisting during transition)
            ibscbs_cst="010",
            ibscbs_c_class_trib="000003",
            ibscbs_vbc=Decimal("200.00"),
            ibscbs_p_ibs_uf=Decimal("4.4250"),
            ibscbs_v_ibs_uf=Decimal("8.85"),
            ibscbs_p_ibs_mun=Decimal("4.4250"),
            ibscbs_v_ibs_mun=Decimal("8.85"),
            ibscbs_v_ibs=Decimal("17.70"),
            ibscbs_p_cbs=Decimal("4.4000"),
            ibscbs_v_cbs=Decimal("8.80"),
        )

        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=200.00, ind_pag=0)

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

        # Reform IBSCBS also present (as direct child of imposto)
        ibscbs = xml.xpath("//ns:det/ns:imposto/ns:IBSCBS", namespaces=self.ns)
        self.assertEqual(len(ibscbs), 1)

        cst = xml.xpath("//ns:IBSCBS/ns:CST", namespaces=self.ns)[0].text
        self.assertEqual(cst, "010")

        # No IS in XML
        is_group = xml.xpath("//ns:det/ns:imposto/ns:IS", namespaces=self.ns)
        self.assertEqual(len(is_group), 0)

    # ------------------------------------------------------------------
    # Test 6: vNF does NOT include IBS/CBS (prohibited in 2025-2026)
    # ------------------------------------------------------------------
    def test_vnf_nao_inclui_ibs_cbs(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        kwargs = self._base_product_kwargs()
        kwargs.update(
            ibscbs_cst="000",
            ibscbs_c_class_trib="000001",
            ibscbs_vbc=Decimal("1000.00"),
            ibscbs_p_ibs_uf=Decimal("0.1000"),
            ibscbs_v_ibs_uf=Decimal("1.00"),
            ibscbs_p_ibs_mun=Decimal("0.0000"),
            ibscbs_v_ibs_mun=Decimal("0.00"),
            ibscbs_v_ibs=Decimal("1.00"),
            ibscbs_p_cbs=Decimal("0.9000"),
            ibscbs_v_cbs=Decimal("9.00"),
        )
        nf.adicionar_produto_servico(**kwargs)
        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=1000.00, ind_pag=0)

        xml = self._serializar_e_assinar()

        # vNF should be 1000.00 (product value only, NO IBS/CBS)
        vnf = xml.xpath("//ns:total/ns:ICMSTot/ns:vNF", namespaces=self.ns)[0].text
        self.assertEqual(vnf, "1000.00")

        # IBS/CBS totals should NOT be inside ICMSTot
        vcbs_in_icmstot = xml.xpath("//ns:ICMSTot/ns:vCBS", namespaces=self.ns)
        self.assertEqual(len(vcbs_in_icmstot), 0)
        vibs_in_icmstot = xml.xpath("//ns:ICMSTot/ns:vIBS", namespaces=self.ns)
        self.assertEqual(len(vibs_in_icmstot), 0)

    # ------------------------------------------------------------------
    # Test 7: Totals in IBSCBSTot, NOT in ICMSTot
    # ------------------------------------------------------------------
    def test_totais_em_ibscbstot_nao_icmstot(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        kwargs = self._base_product_kwargs()
        kwargs.update(
            ibscbs_cst="000",
            ibscbs_c_class_trib="000001",
            ibscbs_vbc=Decimal("1000.00"),
            ibscbs_p_ibs_uf=Decimal("5.0000"),
            ibscbs_v_ibs_uf=Decimal("50.00"),
            ibscbs_p_ibs_mun=Decimal("3.0000"),
            ibscbs_v_ibs_mun=Decimal("30.00"),
            ibscbs_v_ibs=Decimal("80.00"),
            ibscbs_p_cbs=Decimal("8.8000"),
            ibscbs_v_cbs=Decimal("88.00"),
        )
        nf.adicionar_produto_servico(**kwargs)
        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=1000.00, ind_pag=0)

        xml = self._serializar_e_assinar()

        # IBSCBSTot is a sibling of ICMSTot under <total>
        ibscbs_tot = xml.xpath("//ns:total/ns:IBSCBSTot", namespaces=self.ns)
        self.assertEqual(len(ibscbs_tot), 1)

        # Verify vBCIBSCBS (required first child)
        self.assertEqual(
            xml.xpath("//ns:IBSCBSTot/ns:vBCIBSCBS", namespaces=self.ns)[0].text,
            "1000.00",
        )

        # Verify nested gIBS structure
        self.assertEqual(
            xml.xpath("//ns:IBSCBSTot/ns:gIBS/ns:gIBSUF/ns:vIBSUF", namespaces=self.ns)[0].text,
            "50.00",
        )
        self.assertEqual(
            xml.xpath("//ns:IBSCBSTot/ns:gIBS/ns:gIBSMun/ns:vIBSMun", namespaces=self.ns)[0].text,
            "30.00",
        )
        self.assertEqual(
            xml.xpath("//ns:IBSCBSTot/ns:gIBS/ns:vIBS", namespaces=self.ns)[0].text,
            "80.00",
        )

        # Verify nested gCBS structure
        self.assertEqual(
            xml.xpath("//ns:IBSCBSTot/ns:gCBS/ns:vCBS", namespaces=self.ns)[0].text,
            "88.00",
        )

        # Verify vDif and vDevTrib are present (required, zero for now)
        self.assertEqual(
            xml.xpath("//ns:IBSCBSTot/ns:gIBS/ns:gIBSUF/ns:vDif", namespaces=self.ns)[0].text,
            "0.00",
        )
        self.assertEqual(
            xml.xpath("//ns:IBSCBSTot/ns:gCBS/ns:vDif", namespaces=self.ns)[0].text,
            "0.00",
        )

    # ------------------------------------------------------------------
    # Test 8: IS entity fields stored but NOT serialized to XML
    # ------------------------------------------------------------------
    def test_is_entity_stored_but_not_in_xml(self):
        """IS (Imposto Seletivo) starts in 2027. Entity fields are stored
        but _serializar_is is not called until schema supports it."""
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)

        kwargs = self._base_product_kwargs()
        kwargs.update(
            ibscbs_cst="000",
            ibscbs_c_class_trib="000001",
            ibscbs_vbc=Decimal("1000.00"),
            ibscbs_p_ibs_uf=Decimal("0.1000"),
            ibscbs_v_ibs_uf=Decimal("1.00"),
            ibscbs_p_ibs_mun=Decimal("0.0000"),
            ibscbs_v_ibs_mun=Decimal("0.00"),
            ibscbs_v_ibs=Decimal("1.00"),
            ibscbs_p_cbs=Decimal("0.9000"),
            ibscbs_v_cbs=Decimal("9.00"),
            # IS fields stored in entity
            is_cst_selec="01",
            is_c_class_trib="010001",
            is_vbc=Decimal("1000.00"),
            is_aliquota=Decimal("1.0000"),
            is_valor=Decimal("10.00"),
        )
        nf.adicionar_produto_servico(**kwargs)
        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=1000.00, ind_pag=0)

        # Verify entity fields are stored
        produto = nf.produtos_e_servicos[0]
        self.assertEqual(produto.is_cst_selec, "01")
        self.assertEqual(produto.is_c_class_trib, "010001")
        self.assertEqual(produto.is_vbc, Decimal("1000.00"))
        self.assertEqual(produto.is_aliquota, Decimal("1.0000"))
        self.assertEqual(produto.is_valor, Decimal("10.00"))

        # IS totals accumulated internally
        self.assertEqual(nf.totais_is, Decimal("10.00"))

        xml = self._serializar_e_assinar()

        # But IS is NOT in the XML output
        is_tag = xml.xpath("//ns:det/ns:imposto/ns:IS", namespaces=self.ns)
        self.assertEqual(len(is_tag), 0)

        # ISTot not emitted (IS not in schema yet)
        is_tot = xml.xpath("//ns:total/ns:ISTot", namespaces=self.ns)
        self.assertEqual(len(is_tot), 0)

    # ------------------------------------------------------------------
    # Test 9: cMunFGIBS emitted in <ide> header
    # ------------------------------------------------------------------
    def test_cmunfgibs_emitido_no_ide(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)
        nf.municipio_fato_gerador_ibs = "4118402"

        kwargs = self._base_product_kwargs()
        kwargs.update(
            ibscbs_cst="000",
            ibscbs_c_class_trib="000001",
            ibscbs_vbc=Decimal("1000.00"),
            ibscbs_p_ibs_uf=Decimal("0.1000"),
            ibscbs_v_ibs_uf=Decimal("1.00"),
            ibscbs_p_ibs_mun=Decimal("0.0000"),
            ibscbs_v_ibs_mun=Decimal("0.00"),
            ibscbs_v_ibs=Decimal("1.00"),
            ibscbs_p_cbs=Decimal("0.9000"),
            ibscbs_v_cbs=Decimal("9.00"),
        )
        nf.adicionar_produto_servico(**kwargs)
        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=1000.00, ind_pag=0)

        xml = self._serializar_e_assinar()

        # cMunFGIBS should be present in <ide>
        cmunfgibs = xml.xpath("//ns:ide/ns:cMunFGIBS", namespaces=self.ns)
        self.assertEqual(len(cmunfgibs), 1)
        self.assertEqual(cmunfgibs[0].text, "4118402")

        # cMunFGIBS should come after cMunFG
        ide = xml.xpath("//ns:ide", namespaces=self.ns)[0]
        tags = [child.tag.split("}")[-1] for child in ide]
        cmunfg_idx = tags.index("cMunFG")
        cmunfgibs_idx = tags.index("cMunFGIBS")
        self.assertGreater(cmunfgibs_idx, cmunfg_idx)

    # ------------------------------------------------------------------
    # Test 10: cMunFGIBS NOT emitted when not set
    # ------------------------------------------------------------------
    def test_cmunfgibs_nao_emitido_quando_vazio(self):
        emitente = self._emitente()
        cliente = self._cliente()
        nf = self._nota_fiscal(emitente, cliente)
        # municipio_fato_gerador_ibs not set (empty string default)

        kwargs = self._base_product_kwargs()
        nf.adicionar_produto_servico(**kwargs)
        nf.adicionar_pagamento(t_pag="01", x_pag="Dinheiro", v_pag=1000.00, ind_pag=0)

        xml = self._serializar_e_assinar()

        # cMunFGIBS should NOT be present
        cmunfgibs = xml.xpath("//ns:ide/ns:cMunFGIBS", namespaces=self.ns)
        self.assertEqual(len(cmunfgibs), 0)


if __name__ == "__main__":
    unittest.main()
