# -*- coding: utf-8 -*-

TIPOS_DOCUMENTO = (
    'CNPJ',
    'CPF',
)

ICMS_TIPOS_TRIBUTACAO = (
    ('00', 'ICMS 00 - Tributada integralmente'),
    ('10', 'ICMS 10 - Tributada com cobranca do ICMS por substituicao tributaria'),
    ('20', 'ICMS 20 - Com reducao da base de calculo'),
    ('30', 'ICMS 30 - Isenta ou nao tributada e com cobranca do ICMS por substituicao tributaria'),
    ('40', 'ICMS 40 - Isenta'),
    ('41', 'ICMS 41 - Nao tributada'),
    ('50', 'ICMS 50 - Suspensao'),
    ('51', 'ICMS 51 - Diferimento'),
    ('60', 'ICMS 60 - Cobrado anteriormente por substituicao tributaria'),
    ('70', 'ICMS 70 - Com reducao da base de calculo e cobranca do ICMS por substituicao tributaria'),
    ('90', 'ICMS 90 - Outras'),
)

ICMS_ORIGENS = (
    'Nacional',
    'Estrangeira - Importacao Direta',
    'Estrangeira - Adquirida no Mercado Interno',
)

ICMS_MODALIDADES = (
    'Margem Valor Agregado',
    'Pauta (valor)',
    'Preco Tabelado Max. (valor)',
    'Valor da Operacao',
)

NF_STATUS = (
    'Em Digitacao',
    'Validada',
    'Assinada',
    'Em processamento',
    'Autorizada',
    'Rejeitada',
    'Cancelada',
)

NF_TIPOS_DOCUMENTO = (
    (0, 'Entrada'),
    (1, 'Saida'),
)

NF_TIPOS_IMPRESSAO_DANFE = (
    'Retrato',
    'Paisagem',
)

NF_FORMAS_PAGAMENTO = (
    (0, 'Pagamento a vista'),
    (1, 'Pagamento a prazo'),
    (2, 'Outros'),
)

NF_FORMAS_EMISSAO = (
    'Normal',
    'Contingencia',
    'Contingencia com SCAN',
    'Contingencia via DPEC',
    'Contingencia FS-DA',
)

NF_FINALIDADES_EMISSAO = (
    (1, 'NF-e normal'),
    (2, 'NF-e complementar'),
    (3, 'NF-e de ajuste'),
)

NF_REFERENCIADA_TIPOS = (
    'Nota Fiscal eletronica',
    'Nota Fiscal',
)

NF_PRODUTOS_ESPECIFICOS = (
    'Veiculo',
    'Medicamento',
    'Armamento',
    'Combustivel',
)

IPI_TIPOS_TRIBUTACAO = (
    ('00', 'IPI 00 - Entrada com recuperacao de credito'),
    ('01', 'IPI 01 - Entrada tributada com aliquota zero'),
    ('02', 'IPI 02 - Entrada isenta'),
    ('03', 'IPI 03 - Entrada nao-tributada'),
    ('04', 'IPI 04 - Entrada imune'),
    ('05', 'IPI 05 - Entrada com suspensao'),
    ('49', 'IPI 49 - Outras entradas'),
    ('50', 'IPI 50 - Saida tributada'),
    ('51', 'IPI 51 - Saida tributada com aliquota zero'),
    ('52', 'IPI 52 - Saida isenta'),
    ('53', 'IPI 53 - Saida nao-tributada'),
    ('54', 'IPI 54 - Saida imune'),
    ('55', 'IPI 55 - Saida com suspensao'),
    ('99', 'IPI 99 - Outas saidas'),
)

IPI_TIPOS_CALCULO = (
    'Percentual',
    'Em Valor',
)

PIS_TIPOS_TRIBUTACAO = (
    ('01', 'PIS 01 - Operacao Tributavel - Base de Calculo = Valor da Operacao Aliquota...'), # FIXME
    ('02', 'PIS 02 - Operacao Tributavel - Base de Calculo = Valor da Operacao (Aliquota...'), # FIXME
    ('03', 'PIS 03 - Operacao Tributavel - Base de Calculo = Quantidade Vendida x Aliquota...'), # FIXME
    ('04', 'PIS 04 - Operacao Tributavel - Tributacao Monofasica - (Aliquota Zero)'),
    ('06', 'PIS 06 - Operacao Tributavel - Aliquota Zero'),
    ('07', 'PIS 07 - Operacao Isenta da Contribuicao'),
    ('08', 'PIS 08 - Operacao sem Indidencia da Contribuicao'),
    ('09', 'PIS 09 - Operacao com Suspensao da Contribuicao'),
    ('99', 'PIS 99 - Outras operacoes'),
)

PIS_TIPOS_CALCULO = IPI_TIPOS_CALCULO

COFINS_TIPOS_TRIBUTACAO = (
    ('00', 'COFINS 01 - Operacao Tributavel - Base de Calculo = Valor da Operacao Aliquota...'), # FIXME
    ('02', 'COFINS 02 - Operacao Tributavel - Base de Calculo = Valor da Operacao (Aliquota...'), # FIXME
    ('03', 'COFINS 03 - Operacao Tributavel - Base de Calculo = Quantidade Vendida x Aliquota...'), # FIXME
    ('04', 'COFINS 04 - Operacao Tributavel - Tributacao Monofasica - (Aliquota Zero)'),
    ('06', 'COFINS 06 - Operacao Tributavel - Aliquota Zero'),
    ('07', 'COFINS 07 - Operacao Isenta da Contribuicao'),
    ('08', 'COFINS 08 - Operacao sem Indidencia da Contribuicao'),
    ('09', 'COFINS 09 - Operacao com Suspensao da Contribuicao'),
    ('99', 'COFINS 99 - Outras operacoes'),
)

COFINS_TIPOS_CALCULO = IPI_TIPOS_CALCULO


