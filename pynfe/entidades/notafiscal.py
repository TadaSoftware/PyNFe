from base import Entidade
from pynfe.utils.flags import NF_STATUS

from decimal import Decimal

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

class NotaFiscal(Entidade):
    status = NF_STATUS[0]

    # Nota Fisca eletronica
    # - Modelo (formato: NN)
    modelo = str()

    # - Serie (obrigatorio - formato: NNN)
    serie = str()

    # - Numero NF (obrigatorio)
    numero_nf = str()

    # - Data da Emissao (obrigatorio)
    data_emissao = None

    # - Natureza da Operacao (obrigatorio)
    natureza_operacao = str()

    # - Tipo do Documento (obrigatorio - seleciona de lista) - NF_TIPOS_DOCUMENTO
    tipo_documento = int()

    # - Tipo impressao DANFE (obrigatorio - seleciona de lista) - NF_TIPOS_IMPRESSAO_DANFE
    tipo_impressao_danfe = str()

    # - Data de saida/entrada
    data_saida_entrada = None

    # - Forma de pagamento  (obrigatorio - seleciona de lista) - NF_FORMAS_PAGAMENTO
    forma_pagamento = str()

    # - Forma de emissao (obrigatorio - seleciona de lista) - NF_FORMAS_EMISSAO
    forma_emissao = str()

    # - Finalidade de emissao (obrigatorio - seleciona de lista) - NF_FINALIDADES_EMISSAO
    finalidade_emissao = int()

    # - UF
    uf = str()

    # - Municipio de ocorrencia
    municipio = str()

    # - Digest value da NF-e (somente leitura)
    digest_value = None

    # - Valor total da nota (somente leitura)
    valor_total_nota = Decimal()

    # - Valor ICMS da nota (somente leitura)
    valor_icms_nota = Decimal()

    # - Valor ICMS ST da nota (somente leitura)
    valor_icms_st_nota = Decimal()

    # - Protocolo (somente leitura)
    protocolo = str()

    # - Data (somente leitura)
    data = None

    # - Notas Fiscais Referenciadas (lista 1 para * / ManyToManyField)
    notas_fiscais_referenciadas = None

    # - Emitente (CNPJ ???)
    emitente = None

    # - Destinatario/Remetente
    #  - Identificacao (seleciona de Clientes)
    destinatario_remetente = None

    # - Endereco (ver se pode copiar do Cliente)
    #  - Logradouro (obrigatorio)
    destinatario_endereco_logradouro = str()

    #  - Numero (obrigatorio)
    destinatario_endereco_numero = str()

    #  - Complemento
    destinatario_endereco_complemento = str()

    #  - Bairro (obrigatorio)
    destinatario_endereco_bairro = str()

    #  - CEP
    destinatario_endereco_cep = str()

    #  - Pais (seleciona de lista)
    destinatario_endereco_pais = 'BRASIL'

    #  - UF (obrigatorio)
    destinatario_endereco_uf = str()

    #  - Municipio (obrigatorio)
    destinatario_endereco_municipio = str()

    #  - Telefone
    destinatario_endereco_telefone = str()

    # - Local Retirada/Entrega
    #  - Local de retirada diferente do emitente (Sim/Nao)
    local_retirada_diferente_emitente = False

    #  - Local de entrega diferente do destinatario (Sim/Nao)
    local_entrega_diferente_destinatario = False

    # - Produtos e Servicos (lista 1 para * / ManyToManyField)
    produtos_servicos = None

    def __init__(self, *args, **kwargs):
        self.notas_fiscais_referenciadas = []
        self.produtos_servicos = []

        super(NotaFiscal, self).__init__(*args, **kwargs)

    def adicionar_nota_fiscal_referenciada(self, **kwargs):
        u"""Adiciona uma instancia de Nota Fisca referenciada"""
        self.notas_fiscais_referenciadas.append(NotaFiscalReferenciada(**kwargs))

    def adicionar_produto_servico(self, **kwargs):
        u"""Adiciona uma instancia de Produto"""
        self.produtos_servicos.append(NotaFiscalProduto(**kwargs))


class NotaFiscalReferenciada(Entidade):
    # - Tipo (seleciona de lista) - NF_REFERENCIADA_TIPOS
    tipo = str()

    #  - Nota Fiscal eletronica
    #   - Chave de Acesso
    chave_acesso = str()

    #  - Nota Fiscal
    #   - UF
    uf = str()

    #   - Mes e ano de emissao
    mes_ano_emissao = str()

    #   - CNPJ
    cnpj = str()

    #   - Serie (XXX)
    serie = str()

    #   - Numero
    numero = str()

    #   - Modelo
    modelo = str()


class NotaFiscalProduto(Entidade):
    # - Dados
    #  - Codigo (obrigatorio)
    codigo = str()

    #  - Descricao (obrigatorio)
    descricao = str()

    #  - EAN
    ean = str()

    #  - NCM
    ncm = str()

    #  - EX TIPI
    ex_tipi = str()

    #  - CFOP (obrigatorio)
    cfop = str()

    #  - Genero
    genero = str()

    #  - Unidade Comercial (obrigatorio)
    unidade_comercial = str()

    #  - Quantidade Comercial (obrigatorio)
    quantidade_comercial = Decimal()

    #  - Valor Unitario Comercial (obrigatorio)
    valor_unitario_comercial = Decimal()

    #  - Unidade Tributavel (obrigatorio)
    unidade_tributavel = str()

    #  - Quantidade Tributavel (obrigatorio)
    quantidade_tributavel = Decimal()

    #  - Valor Unitario Tributavel (obrigatorio)
    valor_unitario_tributavel = Decimal()

    #  - EAN Tributavel
    ean_tributavel = str()

    #  - Total Frete
    total_frete = Decimal()

    #  - Total Seguro
    total_seguro = Decimal()

    #  - Desconto
    desconto = Decimal()

    #  - Valor total bruto (obrigatorio)
    valor_total_bruto = Decimal()

    #  - Produto especifico (seleciona de lista) - NF_PRODUTOS_ESPECIFICOS
    produto_especifico = str()

class NotaFiscalDeclaracaoImportacao(Entidade):
    pass

class NotaFiscalDeclaracaoImportacaoAdicao(Entidade):
    pass

class NotaFiscalTransporteVolume(Entidade):
    pass

class NotaFiscalTransporteVolumeLacre(Entidade):
    pass

class NotaFiscalCobrancaDuplicata(Entidade):
    pass

class NotaFiscalObservacaoContribuinte(Entidade):
    pass

class NotaFiscalProcessoReferenciado(Entidade):
    pass

