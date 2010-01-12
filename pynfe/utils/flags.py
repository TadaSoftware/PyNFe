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

