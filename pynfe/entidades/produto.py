# -*- coding: utf-8 -*-
from base import Entidade

from decimal import Decimal

class Produto(Entidade):
    # Dados do Produto
    # - Descricao (obrigatorio)
    descricao = str()

    # - Codigo (obrigatorio) - nao pode ser alterado quando em edicao
    codigo = str()

    # - EAN
    ean = str()

    # - EAN Unid. Tributavel
    ean_unidade_tributavel = str()

    # - EX TIPI
    ex_tipi = str()

    # - Genero
    genero = str()

    # - NCM
    ncm = str()

    # - Unid. Com.
    unidade_comercial = str()

    # - Valor Unitario Com.
    valor_unitario_comercial = Decimal()

    # - Unid. Trib.
    unidade_tributavel = str()

    # - Qtd. Trib.
    quantidade_tributavel = Decimal()

    # - Valor Unitario Trib.
    valor_unitario_tributavel = Decimal()

    # Impostos
    # - ICMS (lista 1 para * / ManyToManyField)
    icms = None

    # - IPI
    #  - Classe de Enquadramento (cigarros e bebidas)
    ipi_classe_enquadramento = str()

    #  - Codigo de Enquadramento Legal
    ipi_codigo_enquadramento_legal = str()

    #  - CNPJ do Produtor
    ipi_cnpj_produtor = str()

    def __init__(self, *args, **kwargs):
        self.icms = []

    def adicionar_icms(self, **kwargs):
        u"""Adiciona uma instancia de ICMS a lista de ICMS do produto"""
        self.icms.append(ProdutoICMS(**kwargs))

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

class ProdutoICMS(Entidade):
    #  - Tipo de Tributacao (seleciona de lista) - ICMS_TIPOS_TRIBUTACAO
    tipo_tributacao = str()

    #  - Origem (seleciona de lista) - ICMS_ORIGENS
    origem = str()

    #  - Modalidade de determinacao da Base de Calculo (seleciona de lista) - ICMS_MODALIDADES
    modalidade = str()

    #  - Aliquota ICMS
    aliquota = Decimal()

    #  - Percentual de reducao da Base de Calculo
    percentual_reducao = Decimal()

    #  - Modalidade de determinacao da Base de Calculo do ICMS ST (seleciona de lista) - ICMS_MODALIDADES
    st_modalidade = str()

    #  - Aliquota ICMS ST
    st_aliquota = Decimal()

    #  - Percentual de reducao do ICMS ST
    st_percentual_reducao = Decimal()

    #  - Percentual da margem de Valor Adicionado ICMS ST
    st_percentual_margem_valor_adicionado = Decimal()

