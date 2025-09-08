#!/usr/bin/env python
# *-* encoding: utf8 *-*

import unittest

from pynfe.utils import (
    so_numeros,
    obter_pais_por_codigo,
    normalizar_municipio,
    obter_codigo_por_municipio,
    obter_municipio_por_codigo,
    obter_uf_por_codigo,
    formatar_decimal,
    remover_acentos,
    carregar_arquivo_municipios,
)
from lxml import etree
from pynfe.utils.descompactar import DescompactaGzip


class UtilsTestCase(unittest.TestCase):
    # so_numeros
    def test_so_numeros_none(self):
        self.assertEqual(so_numeros(None), "")

    def test_so_numeros_valor_int(self):
        self.assertEqual(so_numeros(223), "223")

    def test_so_numeros_valor_string(self):
        self.assertEqual(so_numeros("223"), "223")

    def test_so_numeros_com_letras_e_numeros(self):
        self.assertEqual(so_numeros("aa223bb"), "223")

    def test_so_numeros_somente_com_letras(self):
        self.assertEqual(so_numeros("aabbccdd"), "")

    # obter_pais_por_codigo
    def test_obter_pais_por_codigo_brasil(self):
        self.assertEqual(obter_pais_por_codigo("1058"), "Brasil")

    def test_obter_pais_por_codigo__informar_vazio_e_retornar_brasil(self):
        self.assertEqual(obter_pais_por_codigo(""), "Brasil")

    def test_obter_pais_por_codigo__informar_none_e_retornar_brasil(self):
        self.assertEqual(obter_pais_por_codigo(None), "Brasil")

    def test_obter_pais_por_codigo_paisesbaixos(self):
        self.assertEqual(obter_pais_por_codigo("5738"), "PAISES BAIXOS (HOLANDA)")

    def test_obter_pais_por_codigo_reino_unido(self):
        self.assertEqual(obter_pais_por_codigo("6289"), "REINO UNIDO")

    def test_obter_pais_por_codigo_ilhas_cayman(self):
        self.assertEqual(obter_pais_por_codigo("1376"), "CAYMAN, ILHAS")

    # normalizar_municipio
    def test_normalizar_municipio_acento_til_na_letra_a(self):
        self.assertEqual(normalizar_municipio("São Paulo"), "SAO PAULO")

    def test_normalizar_municipio_cedilha_e_acento_til_na_letra_o(self):
        self.assertEqual(normalizar_municipio("Monções"), "MONCOES")

    def test_normalizar_municipio_acento_agudo_na_letra_a(self):
        self.assertEqual(normalizar_municipio("Cuiabá"), "CUIABA")

    def test_normalizar_municipio_acento_agudo_na_letra_e(self):
        self.assertEqual(normalizar_municipio("Avaré"), "AVARE")

    def test_normalizar_municipio_acento_agudo_na_letra_i(self):
        self.assertEqual(normalizar_municipio("Aguaí"), "AGUAI")

    def test_normalizar_municipio_acento_agudo_na_letra_o(self):
        self.assertEqual(normalizar_municipio("Altinópolis"), "ALTINOPOLIS")

    def test_normalizar_municipio_acento_agudo_na_letra_u(self):
        self.assertEqual(normalizar_municipio("Cabreúva"), "CABREUVA")

    def test_normalizar_municipio_acento_circunflexo_na_letra_a(self):
        self.assertEqual(normalizar_municipio("Alvinlândia"), "ALVINLANDIA")

    def test_normalizar_municipio_acento_circunflexo_na_letra_e(self):
        self.assertEqual(
            normalizar_municipio("Governador Eugênio Barros"),
            "GOVERNADOR EUGENIO BARROS",
        )

    def test_normalizar_municipio_acento_circunflexo_na_letra_o(self):
        self.assertEqual(normalizar_municipio("Santo Antônio de Posse"), "SANTO ANTONIO DE POSSE")

    def test_normalizar_municipio_apostrofo(self):
        self.assertEqual(normalizar_municipio("Lambari D'Oeste"), "LAMBARI DOESTE")

    # obter_codigo_por_municipio
    def test_obter_codigo_por_municipio_saopaulo_3550308(self):
        self.assertEqual(obter_codigo_por_municipio("São Paulo", "SP"), "3550308")

    def test_fail_obter_codigo_por_municipio_saopaulo_3550308(self):
        self.assertNotEqual(obter_codigo_por_municipio("São Paulo", "SP"), "0000000")

    def test_obter_codigo_por_municipio_curitiba_4106902(self):
        self.assertEqual(obter_codigo_por_municipio("Curitiba", "PR"), "4106902")

    def test_fail_obter_codigo_por_municipio_curitiba_4106902(self):
        self.assertNotEqual(obter_codigo_por_municipio("Curitiba", "PR"), "0000000")

    # obter_municipio_por_codigo
    def test_obter_municipio_por_codigo_saopaulo_3550308(self):
        self.assertEqual(obter_municipio_por_codigo("3550308", "SP"), "São Paulo")

    def test_obter_municipio_por_codigo_saopaulo_3550308_normalizado(self):
        self.assertEqual(obter_municipio_por_codigo("3550308", "SP", True), "SAO PAULO")

    def test_obter_municipio_por_codigo_curitiba_4106902(self):
        self.assertEqual(obter_municipio_por_codigo("4106902", "PR"), "Curitiba")

    def test_obter_municipio_por_codigo_curitiba_4106902_normalizado(self):
        self.assertEqual(obter_municipio_por_codigo("4106902", "PR", True), "CURITIBA")

    def test_fail_obter_municipio_por_codigo_saopaulo_3550308(self):
        with self.assertRaises(Exception):
            obter_municipio_por_codigo("0000000", "SP")
        self.assertRaises(ValueError)

    # obter_uf_por_codigo
    def test_obter_uf_por_codigo_ro_11(self):
        self.assertEqual(obter_uf_por_codigo("11"), "RO")

    def test_obter_uf_por_codigo_ac_12(self):
        self.assertEqual(obter_uf_por_codigo("12"), "AC")

    def test_obter_uf_por_codigo_am_13(self):
        self.assertEqual(obter_uf_por_codigo("13"), "AM")

    def test_obter_uf_por_codigo_rr_14(self):
        self.assertEqual(obter_uf_por_codigo("14"), "RR")

    def test_obter_uf_por_codigo_pa_15(self):
        self.assertEqual(obter_uf_por_codigo("15"), "PA")

    def test_obter_uf_por_codigo_ap_16(self):
        self.assertEqual(obter_uf_por_codigo("16"), "AP")

    def test_obter_uf_por_codigo_to_17(self):
        self.assertEqual(obter_uf_por_codigo("17"), "TO")

    def test_obter_uf_por_codigo_ma_21(self):
        self.assertEqual(obter_uf_por_codigo("21"), "MA")

    def test_obter_uf_por_codigo_pi_22(self):
        self.assertEqual(obter_uf_por_codigo("22"), "PI")

    def test_obter_uf_por_codigo_ce_23(self):
        self.assertEqual(obter_uf_por_codigo("23"), "CE")

    def test_obter_uf_por_codigo_rn_24(self):
        self.assertEqual(obter_uf_por_codigo("24"), "RN")

    def test_obter_uf_por_codigo_pb_25(self):
        self.assertEqual(obter_uf_por_codigo("25"), "PB")

    def test_obter_uf_por_codigo_pe_26(self):
        self.assertEqual(obter_uf_por_codigo("26"), "PE")

    def test_obter_uf_por_codigo_al_27(self):
        self.assertEqual(obter_uf_por_codigo("27"), "AL")

    def test_obter_uf_por_codigo_se_28(self):
        self.assertEqual(obter_uf_por_codigo("28"), "SE")

    def test_obter_uf_por_codigo_ba_29(self):
        self.assertEqual(obter_uf_por_codigo("29"), "BA")

    def test_obter_uf_por_codigo_mg_31(self):
        self.assertEqual(obter_uf_por_codigo("31"), "MG")

    def test_obter_uf_por_codigo_es_32(self):
        self.assertEqual(obter_uf_por_codigo("32"), "ES")

    def test_obter_uf_por_codigo_rj_33(self):
        self.assertEqual(obter_uf_por_codigo("33"), "RJ")

    def test_obter_uf_por_codigo_pr_41(self):
        self.assertEqual(obter_uf_por_codigo("41"), "PR")

    def test_obter_uf_por_codigo_sc_42(self):
        self.assertEqual(obter_uf_por_codigo("42"), "SC")

    def test_obter_uf_por_codigo_rs_43(self):
        self.assertEqual(obter_uf_por_codigo("43"), "RS")

    def test_obter_uf_por_codigo_ms_50(self):
        self.assertEqual(obter_uf_por_codigo("50"), "MS")

    def test_obter_uf_por_codigo_mt_51(self):
        self.assertEqual(obter_uf_por_codigo("51"), "MT")

    def test_obter_uf_por_codigo_go_52(self):
        self.assertEqual(obter_uf_por_codigo("52"), "GO")

    def test_obter_uf_por_codigo_df_53(self):
        self.assertEqual(obter_uf_por_codigo("53"), "DF")

    def test_obter_uf_por_codigo_an_91(self):
        self.assertEqual(obter_uf_por_codigo("91"), "AN")

    # formatar_decimal
    def test_formatar_decimal_1(self):
        self.assertEqual(formatar_decimal(1), "1.00")

    def test_formatar_decimal_1_0(self):
        self.assertEqual(formatar_decimal(1.0), "1.00")

    def test_formatar_decimal_1_00(self):
        self.assertEqual(formatar_decimal(1.00), "1.00")

    def test_formatar_decimal_1_01(self):
        self.assertEqual(formatar_decimal(1.01), "1.01")

    def test_formatar_decimal_1_011(self):
        self.assertEqual(formatar_decimal(1.011), "1.011")

    # remover_acentos
    def test_remover_acentos_com_acento(self):
        self.assertEqual(remover_acentos("á"), "a")
        self.assertEqual(remover_acentos("é"), "e")
        self.assertEqual(remover_acentos("í"), "i")
        self.assertEqual(remover_acentos("ó"), "o")
        self.assertEqual(remover_acentos("ú"), "u")

        self.assertEqual(remover_acentos("â"), "a")
        self.assertEqual(remover_acentos("ê"), "e")
        self.assertEqual(remover_acentos("ô"), "o")

        self.assertEqual(remover_acentos("à"), "a")
        self.assertEqual(remover_acentos("ã"), "a")
        self.assertEqual(remover_acentos("õ"), "o")

        self.assertEqual(remover_acentos("a"), "a")
        self.assertEqual(remover_acentos("b"), "b")
        self.assertEqual(remover_acentos("c"), "c")


class DescompactaGzipUtils(unittest.TestCase):
    def test_descompacta_string_gzip(self):
        gzip_str = "H4sIAAAAAAAACrPJS0u1K0ktLklVKKgEsm30QQIABhWzIhYAAAA="
        esperado = "<nfe>teste pynfe</nfe>"

        descompacta_gzip = DescompactaGzip.descompacta(gzip_str)
        resultado_str = etree.tostring(descompacta_gzip).decode("utf-8")

        self.assertEqual(resultado_str, esperado)


class CidadesTestCase(unittest.TestCase):
    """
    Testar quantidade de cidades por UF
    pelo arquivos MunIBGE-UFXX.txt

    """

    def test_quantidade_cidades_ac(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=12)), 22)

    def test_quantidade_cidades_al(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=27)), 102)

    def test_quantidade_cidades_ap(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=16)), 16)

    def test_quantidade_cidades_am(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=13)), 62)

    def test_quantidade_cidades_ba(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=29)), 417)

    def test_quantidade_cidades_ce(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=23)), 184)

    def test_quantidade_cidades_df(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=53)), 1)

    def test_quantidade_cidades_es(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=32)), 78)

    def test_quantidade_cidades_go(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=52)), 246)

    def test_quantidade_cidades_ma(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=21)), 217)

    def test_quantidade_cidades_mt(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=51)), 142)

    def test_quantidade_cidades_ms(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=50)), 79)

    def test_quantidade_cidades_mg(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=31)), 853)

    def test_quantidade_cidades_pa(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=15)), 144)

    def test_quantidade_cidades_pb(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=25)), 223)

    def test_quantidade_cidades_pr(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=41)), 399)

    def test_quantidade_cidades_pe(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=26)), 185)

    def test_quantidade_cidades_pi(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=22)), 224)

    def test_quantidade_cidades_rj(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=33)), 92)

    def test_quantidade_cidades_rn(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=24)), 167)

    def test_quantidade_cidades_rs(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=43)), 497)

    def test_quantidade_cidades_ro(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=11)), 52)

    def test_quantidade_cidades_rr(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=14)), 15)

    def test_quantidade_cidades_sc(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=42)), 295)

    def test_quantidade_cidades_sp(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=35)), 645)

    def test_quantidade_cidades_se(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=28)), 75)

    def test_quantidade_cidades_to(self):
        self.assertEqual(len(carregar_arquivo_municipios(uf=17)), 139)

    def test_quantidade_total_cidades(self):
        """
        Carregar todos os arquivos
        e verificar a quantidade total de cidades

        """
        total = 0
        lista_de_codigos_uf = [
            11,
            12,
            13,
            14,
            15,
            16,
            17,  # Norte
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,  # Nordeste
            31,
            32,
            33,
            35,  # Sudeste
            41,
            42,
            43,  # Sul
            50,
            51,
            52,
            53,  # Centro-Oeste
        ]
        for uf in lista_de_codigos_uf:
            total += len(carregar_arquivo_municipios(uf=uf))

        self.assertEqual(total, 5571)


if __name__ == "__main__":
    unittest.main()
