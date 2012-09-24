# -*- coding: utf-8 -*-

NAMESPACE_NFE = 'http://www.portalfiscal.inf.br/nfe'
NAMESPACE_SIG = 'http://www.w3.org/2000/09/xmldsig#'
NAMESPACE_SOAP = 'http://www.w3.org/2003/05/soap-envelope'

VERSAO_PADRAO = '1.01'

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
    (0, 'Nacional'),
    (1, 'Estrangeira - Importacao Direta'),
    (2, 'Estrangeira - Adquirida no Mercado Interno'),
)

ICMS_MODALIDADES = (
    (0, 'Margem Valor Agregado'),
    (1, 'Pauta (valor)'),
    (2, 'Preco Tabelado Max. (valor)'),
    (3, 'Valor da Operacao'),
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

NF_PROCESSOS_EMISSAO = (
    (0, u'Emissão de NF-e com aplicativo do contribuinte'),
    (1, u'Emissão de NF-e avulsa pelo Fisco'),
    (2, u'Emissão de NF-e avulsa, pelo contribuinte com seu certificado digital, através do site do Fisco'),
    (3, u'Emissão NF-e pelo contribuinte com aplicativo fornecido pelo Fisco'),
)

NF_TIPOS_IMPRESSAO_DANFE = (
    (1, 'Retrato'),
    (2, 'Paisagem'),
)

NF_FORMAS_PAGAMENTO = (
    (0, 'Pagamento a vista'),
    (1, 'Pagamento a prazo'),
    (2, 'Outros'),
)

NF_FORMAS_EMISSAO = (
    (1, 'Normal'),
    (2, 'Contingencia'),
    (3, 'Contingencia com SCAN'),
    (4, 'Contingencia via DPEC'),
    (5, 'Contingencia FS-DA'),
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

NF_AMBIENTES = (
    (1, 'Producao'),
    (2, 'Homologacao'),
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
    ('01', 'COFINS 01 - Operacao Tributavel - Base de Calculo = Valor da Operacao Aliquota...'), # FIXME
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

MODALIDADES_FRETE = (
    (0, '0 - Por conta do emitente'),
    (1, '1 - Por conta do destinatario'),
)

ORIGENS_PROCESSO = (
    'SEFAZ',
    'Justica federal',
    'Justica estadual',
    'Secex/RFB',
    'Outros',
)

CODIGO_BRASIL = '1058'

CODIGOS_ESTADOS = {
    'RO': '11',
    'AC': '12',
    'AM': '13',
    'RR': '14',
    'PA': '15',
    'AP': '16',
    'TO': '17',
    'MA': '21',
    'PI': '22',
    'CE': '23',
    'RN': '24',
    'PB': '25',
    'PE': '26',
    'AL': '27',
    'SE': '28',
    'BA': '29',
    'MG': '31',
    'ES': '32',
    'RJ': '33',
    'SP': '35',
    'PR': '41',
    'SC': '42',
    'RS': '43',
    'MS': '50',
    'MT': '51',
    'GO': '52',
    'DF': '53',
}


