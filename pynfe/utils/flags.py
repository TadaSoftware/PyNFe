# -*- coding: utf-8 -*-

NAMESPACE_NFE = "http://www.portalfiscal.inf.br/nfe"
NAMESPACE_SIG = "http://www.w3.org/2000/09/xmldsig#"
NAMESPACE_SOAP = "http://www.w3.org/2003/05/soap-envelope"
NAMESPACE_XSI = "http://www.w3.org/2001/XMLSchema-instance"
NAMESPACE_XSD = "http://www.w3.org/2001/XMLSchema"
NAMESPACE_METODO = "http://www.portalfiscal.inf.br/nfe/wsdl/"

NAMESPACE_SOAP_NFSE = "http://schemas.xmlsoap.org/soap/envelope/"
NAMESPACE_BETHA = "http://www.betha.com.br/e-nota-contribuinte-ws"

NAMESPACE_MDFE = "http://www.portalfiscal.inf.br/mdfe"
NAMESPACE_MDFE_METODO = "http://www.portalfiscal.inf.br/mdfe/wsdl/"
MODELO_MDFE = "58"
VERSAO_MDFE = "3.00"

VERSAO_PADRAO = "4.00"

NAMESPACE_CTE = "http://www.portalfiscal.inf.br/cte"
NAMESPACE_CTE_METODO = "http://www.portalfiscal.inf.br/cte/wsdl/"
VERSAO_CTE = "3.00"

VERSAO_QRCODE = "2"

TIPOS_DOCUMENTO = (
    "CNPJ",
    "CPF",
)

XSD_FOLDER_NFE = "pynfe/data/XSDs/NF-e"
XSD_NFE = "nfe_v4.00.xsd"
XSD_NFE_PROCESSADA = "procNFe_v4.00.xsd"
XSD_PD_CANCELAR_NFE = "procCancNFe_v1.07.xsd"
XSD_PD_INUTILIZAR_NFE = "procInutNFe_v1.07.xsd"

XSD_FOLDER_MDFE = "pynfe/data/XSDs/MDF-e"
XSD_MDFE = "mdfe_v3.00.xsd"
XSD_MDFE_PROCESSADA = "procMDFe_v3.00.xsd"


ICMS_TIPOS_TRIBUTACAO = (
    ("00", "ICMS 00 - Tributada integralmente"),
    ("02", "ICMS 02 - Tributação monofásica própria sobre combustíveis"),
    ("10", "ICMS 10 - Tributada com cobranca do ICMS por substituicao tributaria"),
    (
        "15",
        "ICMS 15 - Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis",
    ),
    ("20", "ICMS 20 - Com reducao da base de calculo"),
    (
        "30",
        ("ICMS 30 - Isenta ou nao tributada e com cobranca do ICMS por substituicao tributaria"),
    ),
    ("40", "ICMS 40 - Isenta"),
    ("41", "ICMS 41 - Nao tributada"),
    ("50", "ICMS 50 - Suspensao"),
    ("51", "ICMS 51 - Diferimento"),
    ("53", "ICMS 53 - Tributação monofásica sobre combustíveis com recolhimento diferido"),
    ("60", "ICMS 60 - Cobrado anteriormente por substituicao tributaria"),
    ("61", "ICMS 61 - Tributação monofásica sobre combustíveis cobrada anteriormente"),
    (
        "70",
        ("ICMS 70 - Com reducao da base de calculo e cobranca do ICMS por substituicao tributaria"),
    ),
    ("90", "ICMS 90 - Outras"),
    ("101", "ICMS 101 - Tributação ICMS pelo Simples Nacional, CSOSN=101"),
    (
        "102",
        "ICMS 102 - Tributação ICMS pelo Simples Nacional, CSOSN=102, 103, 300 ou 400",
    ),
    ("201", "ICMS 201 - Tributação ICMS pelo Simples Nacional, CSOSN=201"),
    ("202", "ICMS 202 - Tributação ICMS pelo Simples Nacional, CSOSN=202 ou 203"),
    ("500", "ICMS 500 - Tributação ICMS pelo Simples Nacional, CSOSN=500"),
    ("900", "ICMS 900 - Tributação ICMS pelo Simples Nacional, CSOSN=900"),
    (
        "ST",
        (
            "ICMS ST - Grupo de informação do ICMS ST devido para a UF de destino, nas"
            " operações interestaduais de produtos que tiveram retenção antecipada de"
            " ICMS por ST na UF do remetente. Repasse via Substituto Tributário."
        ),
    ),
)

ICMS_ORIGENS = (
    (0, "Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8. "),
    (1, "Estrangeira - Importação direta, exceto a indicada no código 6."),
    (2, "Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7."),
    (
        3,
        (
            "Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e"
            " inferior ou igual a 70%."
        ),
    ),
    (
        4,
        (
            "Nacional, cuja produção tenha sido feita em conformidade com os processos"
            " produtivos básicos de que tratam as legislações citadas nos Ajustes."
        ),
    ),
    (
        5,
        ("Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%. "),
    ),
    (
        6,
        (
            "Estrangeira - Importação direta, sem similar nacional, constante em lista"
            " da CAMEX e gás natural. "
        ),
    ),
    (
        7,
        (
            "Estrangeira - Adquirida no mercado interno, sem similar nacional,"
            " constante em lista da CAMEX e gás natural."
        ),
    ),
    (8, "Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%."),
)

ICMS_MODALIDADES = (
    (0, "Margem Valor Agregado"),
    (1, "Pauta (valor)"),
    (2, "Preco Tabelado Max. (valor)"),
    (3, "Valor da Operacao"),
)

ICMS_ST_MODALIDADES = (
    (0, "Preço tabelado ou máximo sugerido"),
    (1, "Lista Negativa (valor)"),
    (2, "Lista Positiva (valor)"),
    (3, "Lista Neutra (valor)"),
    (4, "Margem Valor Agregado (%)"),
    (5, "Pauta (valor)"),
    (6, "Valor da Operação"),
)

ICMS_MOTIVO_DESONERACAO = (
    (1, "Táxi"),
    (3, "Produtor Agropecuário"),
    (4, "Frotista/Locadora"),
    (5, "Diplomático/Consular"),
    (
        6,
        (
            "Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio"
            " (Resolução 714/88 e 790/94 – CONTRAN e suas alterações)"
        ),
    ),
    (7, "SUFRAMA"),
    (8, "Venda a órgão Público"),
    (9, "Outros"),
    (10, "Deficiente Condutor"),
    (11, "Deficiente não condutor"),
    (16, "Olimpíadas Rio 2016"),
    (90, "Solicitado pelo Fisco"),
)

NF_STATUS = (
    "Em Digitacao",
    "Validada",
    "Assinada",
    "Em processamento",
    "Autorizada",
    "Rejeitada",
    "Cancelada",
)

MDFE_STATUS = (
    "Em Digitacao",
    "Validada",
    "Assinada",
    "Em processamento",
    "Autorizada",
    "Rejeitada",
    "Cancelada",
    "Encerrada",
)

NF_TIPOS_DOCUMENTO = (
    (0, "Entrada"),
    (1, "Saida"),
)

NF_PROCESSOS_EMISSAO = (
    (0, "Emissão de NF-e com aplicativo do contribuinte"),
    (1, "Emissão de NF-e avulsa pelo Fisco"),
    (
        2,
        (
            "Emissão de NF-e avulsa, pelo contribuinte com seu certificado digital,"
            " através do site do Fisco"
        ),
    ),
    (3, "Emissão NF-e pelo contribuinte com aplicativo fornecido pelo Fisco"),
)

NF_TIPOS_IMPRESSAO_DANFE = (
    (1, "Retrato"),
    (2, "Paisagem"),
)

NF_FORMAS_PAGAMENTO = (
    (0, "Pagamento a vista"),
    (1, "Pagamento a prazo"),
    (2, "Outros"),
)

NF_FORMAS_EMISSAO = (
    (1, "Normal"),
    (2, "Contingencia"),
    (3, "Contingencia com SCAN"),
    (4, "Contingencia via DPEC"),
    (5, "Contingencia FS-DA"),
)

NF_FINALIDADES_EMISSAO = (
    (1, "NF-e normal"),
    (2, "NF-e complementar"),
    (3, "NF-e de ajuste"),
    (4, "NF-e de Devolução"),
    (5, "NF-e de Débito"),
    (6, "NF-e de Crédito"),
)

NF_REFERENCIADA_TIPOS = (
    "Nota Fiscal eletronica",
    "Nota Fiscal",
    "Nota Fiscal produtor",
    "Conhecimento de frete",
    "Cupom Fiscal",
)

NF_PRODUTOS_ESPECIFICOS = (
    "Veiculo",
    "Medicamento",
    "Armamento",
    "Combustivel",
)

NF_AMBIENTES = (
    (1, "Producao"),
    (2, "Homologacao"),
)

IPI_TIPOS_TRIBUTACAO = (
    ("00", "IPI 00 - Entrada com recuperacao de credito"),
    ("01", "IPI 01 - Entrada tributada com aliquota zero"),
    ("02", "IPI 02 - Entrada isenta"),
    ("03", "IPI 03 - Entrada nao-tributada"),
    ("04", "IPI 04 - Entrada imune"),
    ("05", "IPI 05 - Entrada com suspensao"),
    ("49", "IPI 49 - Outras entradas"),
    ("50", "IPI 50 - Saida tributada"),
    ("51", "IPI 51 - Saida tributada com aliquota zero"),
    ("52", "IPI 52 - Saida isenta"),
    ("53", "IPI 53 - Saida nao-tributada"),
    ("54", "IPI 54 - Saida imune"),
    ("55", "IPI 55 - Saida com suspensao"),
    ("99", "IPI 99 - Outas saidas"),
)

IPI_TIPOS_CALCULO = (
    "Percentual",
    "Em Valor",
)

PIS_TIPOS_TRIBUTACAO = (
    (
        "01",
        (
            "PIS 01 - Operação Tributável - Base de cálculo = valor da operação"
            " alíquota normal (cumulativo/não cumulativo)"
        ),
    ),
    (
        "02",
        (
            "PIS 02 - Operação Tributável - Base de cálculo = valor da operação"
            " (alíquota diferenciada)"
        ),
    ),
    (
        "03",
        (
            "PIS 03 - Operacao Tributavel - Base de cálculo = quantidade vendida x"
            " alíquota por unidade de produto)"
        ),
    ),
    ("04", "PIS 04 - Operacao Tributavel - Tributacao Monofasica - (Aliquota Zero)"),
    ("06", "PIS 06 - Operacao Tributavel - Aliquota Zero"),
    ("07", "PIS 07 - Operacao Isenta da Contribuicao"),
    ("08", "PIS 08 - Operacao sem Indidencia da Contribuicao"),
    ("09", "PIS 09 - Operacao com Suspensao da Contribuicao"),
    ("49", "PIS 49 - Outras Operações de Saída"),
    (
        "50",
        (
            "PIS 50 - Operação com Direito a Crédito - Vinculada Exclusivamente a"
            " Receita Tributada no Mercado Interno"
        ),
    ),
    (
        "51",
        (
            "PIS 51 - Operação com Direito a Crédito - Vinculada Exclusivamente a"
            " Receita Não Tributada no Mercado Interno"
        ),
    ),
    (
        "52",
        (
            "PIS 52 - Operação com Direito a Crédito – Vinculada Exclusivamente a"
            " Receita de Exportação"
        ),
    ),
    (
        "53",
        (
            "PIS 53 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas"
            " e Não-Tributadas no Mercado Interno"
        ),
    ),
    (
        "54",
        (
            "PIS 54 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas"
            " no Mercado Interno e de Exportação"
        ),
    ),
    (
        "55",
        (
            "PIS 55 - Operação com Direito a Crédito - Vinculada a Receitas Não"
            " Tributadas no Mercado Interno e de Exportação"
        ),
    ),
    (
        "56",
        (
            "PIS 56 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas"
            " e Não Tributadas no Mercado Interno, e de Exportação"
        ),
    ),
    (
        "60",
        (
            "PIS 60 - Crédito Presumido - Operação de Aquisição Vinculada"
            " Exclusivamente a Receita Tributada no Mercado Interno"
        ),
    ),
    (
        "61",
        (
            "PIS 61 - Crédito Presumido - Operação de Aquisição Vinculada"
            " Exclusivamente a Receita Não Tributada no Mercado Interno"
        ),
    ),
    (
        "62",
        (
            "PIS 62 - Crédito Presumido - Operação de Aquisição Vinculada"
            " Exclusivamente a Receita de Exportação"
        ),
    ),
    (
        "63",
        (
            "PIS 63 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas"
            " Tributadas e Não-Tributadas no Mercado Interno"
        ),
    ),
    (
        "64",
        (
            "PIS 64 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas"
            " Tributadas no Mercado Interno e de Exportação"
        ),
    ),
    (
        "65",
        (
            "PIS 65 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas"
            " Não Tributadas no Mercado Interno e de Exportação"
        ),
    ),
    (
        "66",
        (
            "PIS 66 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas"
            " Tributadas e Não-Tributadas no Mercado Interno, e de Exportação"
        ),
    ),
    ("67", "PIS 67 - Crédito Presumido - Outras Operações"),
    ("70", "PIS 70 - Operação de Aquisição sem Direito a Crédito"),
    ("71", "PIS 71 - Operação de Aquisição com Isenção"),
    ("72", "PIS 72 - Operação de Aquisição com Suspensão"),
    ("73", "PIS 73 - Operação de Aquisição a Alíquota Zero"),
    ("74", "PIS 74 - Operação de Aquisição; sem Incidência da Contribuição"),
    ("75", "PIS 75 - Operação de Aquisição por Substituição Tributária"),
    ("98", "PIS 98 - Outras Operações de Entrada"),
    ("99", "PIS 99 - Outras operacoes"),
)

PIS_TIPOS_CALCULO = IPI_TIPOS_CALCULO

COFINS_TIPOS_TRIBUTACAO = (
    (
        "01",
        (
            "COFINS 01 - Operação Tributável - Base de cálculo = valor da operação"
            " alíquota normal (cumulativo/não cumulativo)"
        ),
    ),
    (
        "02",
        (
            "COFINS 02 - Operação Tributável - Base de cálculo = valor da operação"
            " (alíquota diferenciada)"
        ),
    ),
    (
        "03",
        (
            "COFINS 03 - Operacao Tributavel - Base de cálculo = quantidade vendida x"
            " alíquota por unidade de produto)"
        ),
    ),
    ("04", "COFINS 04 - Operacao Tributavel - Tributacao Monofasica - (Aliquota Zero)"),
    ("06", "COFINS 06 - Operacao Tributavel - Aliquota Zero"),
    ("07", "COFINS 07 - Operacao Isenta da Contribuicao"),
    ("08", "COFINS 08 - Operacao sem Indidencia da Contribuicao"),
    ("09", "COFINS 09 - Operacao com Suspensao da Contribuicao"),
    ("49", "COFINS 49 - Outras Operações de Saída"),
    (
        "50",
        (
            "COFINS 50 - Operação com Direito a Crédito - Vinculada Exclusivamente a"
            " Receita Tributada no Mercado Interno"
        ),
    ),
    (
        "51",
        (
            "COFINS 51 - Operação com Direito a Crédito - Vinculada Exclusivamente a"
            " Receita Não Tributada no Mercado Interno"
        ),
    ),
    (
        "52",
        (
            "COFINS 52 - Operação com Direito a Crédito – Vinculada Exclusivamente a"
            " Receita de Exportação"
        ),
    ),
    (
        "53",
        (
            "COFINS 53 - Operação com Direito a Crédito - Vinculada a Receitas"
            " Tributadas e Não-Tributadas no Mercado Interno"
        ),
    ),
    (
        "54",
        (
            "COFINS 54 - Operação com Direito a Crédito - Vinculada a Receitas"
            " Tributadas no Mercado Interno e de Exportação"
        ),
    ),
    (
        "55",
        (
            "COFINS 55 - Operação com Direito a Crédito - Vinculada a Receitas Não"
            " Tributadas no Mercado Interno e de Exportação"
        ),
    ),
    (
        "56",
        (
            "COFINS 56 - Operação com Direito a Crédito - Vinculada a Receitas"
            " Tributadas e Não Tributadas no Mercado Interno, e de Exportação"
        ),
    ),
    (
        "60",
        (
            "COFINS 60 - Crédito Presumido - Operação de Aquisição Vinculada"
            " Exclusivamente a Receita Tributada no Mercado Interno"
        ),
    ),
    (
        "61",
        (
            "COFINS 61 - Crédito Presumido - Operação de Aquisição Vinculada"
            " Exclusivamente a Receita Não Tributada no Mercado Interno"
        ),
    ),
    (
        "62",
        (
            "COFINS 62 - Crédito Presumido - Operação de Aquisição Vinculada"
            " Exclusivamente a Receita de Exportação"
        ),
    ),
    (
        "63",
        (
            "COFINS 63 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas"
            " Tributadas e Não-Tributadas no Mercado Interno"
        ),
    ),
    (
        "64",
        (
            "COFINS 64 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas"
            " Tributadas no Mercado Interno e de Exportação"
        ),
    ),
    (
        "65",
        (
            "COFINS 65 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas"
            " Não Tributadas no Mercado Interno e de Exportação"
        ),
    ),
    (
        "66",
        (
            "COFINS 66 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas"
            " Tributadas e Não-Tributadas no Mercado Interno, e de Exportação"
        ),
    ),
    ("67", "COFINS 67 - Crédito Presumido - Outras Operações"),
    ("70", "COFINS 70 - Operação de Aquisição sem Direito a Crédito"),
    ("71", "COFINS 71 - Operação de Aquisição com Isenção"),
    ("72", "COFINS 72 - Operação de Aquisição com Suspensão"),
    ("73", "COFINS 73 - Operação de Aquisição a Alíquota Zero"),
    ("74", "COFINS 74 - Operação de Aquisição; sem Incidência da Contribuição"),
    ("75", "COFINS 75 - Operação de Aquisição por Substituição Tributária"),
    ("98", "COFINS 98 - Outras Operações de Entrada"),
    ("99", "COFINS 99 - Outras operacoes"),
)

COFINS_TIPOS_CALCULO = IPI_TIPOS_CALCULO

# =============================================
# Reforma Tributaria - IVA Dual (EC 132/2023)
# =============================================

# CST para IBSCBS (IBS + CBS) — NT 2025.002-RTC (3-digit codes)
IBS_CBS_TIPOS_TRIBUTACAO = (
    ("000", "Tributação integral"),
    ("010", "Tributação com alíquota reduzida"),
    ("100", "Tributação com suspensão"),
    ("110", "Imunidade — exportação"),
    ("200", "Tributação com diferimento"),
    ("222", "Isenção"),
    ("300", "Não incidência"),
    ("400", "Tributação por substituição"),
    ("410", "Tributação com alíquota zero"),
    ("510", "Tributação integral — regime específico"),
    ("600", "Tributação monofásica — incidência padrão"),
    ("620", "Tributação monofásica — demais operações"),
    ("800", "Crédito presumido"),
    ("810", "Crédito presumido — ZFM"),
    ("900", "Outros"),
)

# CST para IS (Imposto Seletivo) — CSTSelec (NT 2025.002-RTC)
IS_TIPOS_TRIBUTACAO = (
    ("01", "Tributada integralmente"),
    ("02", "Tributada com redução"),
    ("03", "Isenção"),
    ("04", "Imunidade"),
    ("05", "Suspensão"),
    ("06", "Diferimento"),
    ("90", "Outros"),
)

MODALIDADES_FRETE = (
    (0, "0 - Contratação por conta do Remetente (CIF)"),
    (1, "1 - Por conta do destinatário"),
    (2, "2 - Contratação por conta de Terceiros"),
    (3, "3 - Transporte Próprio por conta do Remetente"),
    (4, "4 - Transporte Próprio por conta do Destinatário"),
    (9, "9 - Sem Ocorrência de Transporte"),
)

ORIGENS_PROCESSO = (
    "SEFAZ",
    "Justica federal",
    "Justica estadual",
    "Secex/RFB",
    "Outros",
)

CODIGO_BRASIL = "1058"

CODIGOS_ESTADOS = {
    "RO": "11",
    "AC": "12",
    "AM": "13",
    "RR": "14",
    "PA": "15",
    "AP": "16",
    "TO": "17",
    "MA": "21",
    "PI": "22",
    "CE": "23",
    "RN": "24",
    "PB": "25",
    "PE": "26",
    "AL": "27",
    "SE": "28",
    "BA": "29",
    "MG": "31",
    "ES": "32",
    "RJ": "33",
    "SP": "35",
    "PR": "41",
    "SC": "42",
    "RS": "43",
    "MS": "50",
    "MT": "51",
    "GO": "52",
    "DF": "53",
    "AN": "91",
    "EX": "99",
}

BANDEIRA_CARTAO = (
    ("01", "Visa"),
    ("02", "MasterCard"),
    ("03", "AmericanExpress"),
    ("04", "Sorocred"),
    ("05", "DinersClub"),
    ("06", "Elo"),
    ("07", "Hipercard"),
    ("08", "Aura"),
    ("09", "Cabal"),
    ("10", "Alelo"),
    ("11", "BanesCard"),
    ("12", "CalCard"),
    ("13", "Credz"),
    ("14", "Discover"),
    ("15", "GoodCard"),
    ("16", "GrenCard"),
    ("17", "Hiper"),
    ("18", "JcB"),
    ("19", "Mais"),
    ("20", "MaxVan"),
    ("21", "Policard"),
    ("22", "RedeCompras"),
    ("23", "Sodexo"),
    ("24", "ValeCard"),
    ("25", "Verocheque"),
    ("26", "VR"),
    ("27", "Ticket"),
    ("99", "Outros"),
)

FORMAS_PAGAMENTO = (
    ("01", "Dinheiro"),
    ("02", "Cheque"),
    ("03", "Cartao Credito"),
    ("04", "Cartao Debito"),
    ("05", "Credito Loja"),
    ("10", "Vale Alimentacao"),
    ("11", "Vale Refeicao"),
    ("12", "Vale Presente"),
    ("13", "Vale Combustivel"),
    ("14", "Duplicata Mercantil"),
    ("15", "Boleto Bancario"),
    ("17", "Pagamento Instantaneo"),
    ("90", "Sem Pagamento"),
    ("99", "Outro"),
)
