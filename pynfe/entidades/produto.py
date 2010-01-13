# -*- coding: utf-8 -*-
from base import Entidade
from pynfe.utils.flags import ICMS_TIPOS_TRIBUTACAO, ICMS_ORIGENS, ICMS_MODALIDADES

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

        super(Produto, self).__init__(*args, **kwargs)

    def __str__(self):
        return ' '.join([self.codigo, self.descricao])

    def adicionar_icms(self, **kwargs):
        u"""Adiciona uma instancia de ICMS a lista de ICMS do produto"""
        self.icms.append(ProdutoICMS(**kwargs))

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

