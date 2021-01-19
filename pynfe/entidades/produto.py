# -*- coding: utf-8 -*-
from .base import Entidade
from pynfe.utils.flags import ICMS_TIPOS_TRIBUTACAO, ICMS_ORIGENS, ICMS_MODALIDADES

from decimal import Decimal

class Produto(Entidade):
    """XXX: E provavel que esta entidade sera descartada."""

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

    # - CEST - Código especificador da substituição tributária
    # NT2015/003 http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uXFlhOSgUZc=
    # Tabela https://www.confaz.fazenda.gov.br/anexo-i.pdf
    cest = str()

    cbenef = str()

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

    # - indica se valor do item entra no valor total da nota fiscal 
    # 0=Valor do item (vProd) não compõe o valor total da NF-e 
    # 1=Valor do item (vProd) compõe o valor total da NF-e (vProd)
    ind_total = int()
    
    # # Impostos

    # - IPI
    #  - Classe de Enquadramento (cigarros e bebidas)
    ipi_classe_enquadramento = str()

    #  - Codigo de Enquadramento Legal
    ipi_codigo_enquadramento_legal = str()

    #  - CNPJ do Produtor
    ipi_cnpj_produtor = str()

    # ICMS (Informar apenas um grupo por produto)
    """
    ICMS 00 - Tributada integralmente
    ICMS 10 - Tributada e com cobrança do ICMS por substituição tributária
    ICMS 20 - Tributada e com cobrança do ICMS por substituição tributária
    ICMS 30 - Tributação Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    ICMS 30 - Isenta ou nao tributada e com cobranca do ICMS por substituicao tributaria
    ICMS 40 - Isenta
    ICMS 41 - Nao tributada
    ICMS 50 - Suspensao
    ICMS 51 - Diferimento
    ICMS 60 - Cobrado anteriormente por substituicao tributaria
    ICMS 70 - Com reducao da base de calculo e cobranca do ICMS por substituicao tributaria
    ICMS 90 - Outras
    """

    # Tributos aproximados por item
    valor_tributos_aprox = str()

    icms_modalidade = str()
    icms_origem = int()
    icms_csosn = str()
    icms_aliquota = Decimal()
    icms_credito= Decimal()

    # # PIS
    pis_modalidade = str()
    pis_valor_base_calculo = str()
    pis_aliquota_percentual = str()
    pis_valor = str()

    # # COFINS
    cofins_modalidade = str()
    cofins_valor_base_calculo = str()
    cofins_aliquota_percentual = str()
    cofins_valor = str()

    # # Fundo de Combate a Pobreza
    fcp_base_calculo = Decimal()
    fcp_percentual = Decimal()
    fcp_valor = Decimal()

    # # - ICMS (lista 1 para * / ManyToManyField)
    icms = None
    def adicionar_icms(self, **kwargs):
        """Adiciona uma instancia de ICMS a lista de ICMS do produto"""
        self.icms.append(ProdutoICMS(**kwargs))

    def __init__(self, *args, **kwargs):
        self.icms = []

        super(Produto, self).__init__(*args, **kwargs)

    def __str__(self):
        return ' '.join([self.codigo, self.descricao])

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

