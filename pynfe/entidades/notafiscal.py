# -*- coding: utf-8 -*-
import random
from decimal import Decimal

from pynfe import get_version

# from pynfe.utils import so_numeros, memoize
from pynfe.utils import so_numeros
from pynfe.utils.flags import CODIGOS_ESTADOS, NF_STATUS

from .base import CampoDeprecated, Entidade


class NotaFiscal(Entidade):
    # campos deprecados
    campos_deprecados = [
        CampoDeprecated(
            "tipo_pagamento",
            novo=None,
            motivo="Por favor utilize os grupos de pagamento pela função adicionar_pagamento.",
            apenas_warning=True,
        ),
    ]

    status = NF_STATUS[0]

    # Código numérico aleatório que compõe a chave de acesso
    codigo_numerico_aleatorio = str()

    # Digito verificador do codigo numerico aleatorio
    dv_codigo_numerico_aleatorio = str()

    # Nota Fisca eletronica
    # - Modelo (formato: NN)
    modelo = int()

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

    # - Processo de emissão da NF-e (obrigatorio - seleciona de lista) - NF_PROCESSOS_EMISSAO
    processo_emissao = 0

    # - Versao do processo de emissão da NF-e
    versao_processo_emissao = get_version()

    # - Tipo impressao DANFE (obrigatorio - seleciona de lista) - NF_TIPOS_IMPRESSAO_DANFE
    tipo_impressao_danfe = int()

    # - Data de saida/entrada
    data_saida_entrada = None

    # - Forma de pagamento  (obrigatorio - seleciona de lista) - NF_FORMAS_PAGAMENTO
    # Removido na NF-e 4.00
    # forma_pagamento = int()

    # - Tipo de pagamento
    """
    Obrigatório o preenchimento do Grupo Informações de Pagamento para NF-e e NFC-e.
    Para as notas com finalidade de Ajuste ou Devolução o campo Forma de Pagamento
    deve ser preenchido com 90=Sem Pagamento.
    01=Dinheiro
    02=Cheque
    03=Cartão de Crédito
    04=Cartão de Débito
    05=Crédito Loja
    10=Vale Alimentação
    11=Vale Refeição
    12=Vale Presente
    13=Vale Combustível
    14=Duplicata Mercantil
    90= Sem pagamento
    99=Outros
    """
    tipo_pagamento = None

    # - Forma de emissao (obrigatorio - seleciona de lista) - NF_FORMAS_EMISSAO
    forma_emissao = str()

    # - Finalidade de emissao (obrigatorio - seleciona de lista) - NF_FINALIDADES_EMISSAO
    finalidade_emissao = int()

    # - Indica se a nota e para consumidor final
    cliente_final = int()

    # - Indica se a compra foi feita presencialmente, telefone, internet, etc
    """
        0=Não se aplica (por exemplo, Nota Fiscal complementar ou deajuste);
        1=Operação presencial;
        2=Operação não presencial, pela Internet;
        3=Operação não presencial, Teleatendimento;
        4=NFC-e em operação com entrega a domicílio;
        5=Operação presencial, fora do estabelecimento;
        9=Operação não presencial, outros.
    """
    indicador_presencial = int()

    # - Indicador de intermediador/marketplace
    """
        0=Operação sem intermediador (em site ou plataforma própria)
        1=Operação em site ou plataforma de terceiros
        (intermediadores/marketplace)</xs:documentation>
    """
    indicador_intermediador = int()

    """ nfce suporta apenas operação interna
        Identificador de local de destino da operação
        1=Operação interna;2=Operação interestadual;3=Operação com exterior.
    """
    indicador_destino = int()
    # - UF - converter para codigos em CODIGOS_ESTADOS
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

    # - Entrega (XXX sera possivel ter entrega e retirada ao mesmo tempo na NF?)
    entrega = None

    # - Retirada
    retirada = None

    # - Local Retirada/Entrega
    #  - Local de retirada diferente do emitente (Sim/Nao)
    local_retirada_diferente_emitente = False

    #  - Local de entrega diferente do destinatario (Sim/Nao)
    local_entrega_diferente_destinatario = False

    # - Autorizados a baixar XML (lista 1 para * / ManyToManyField)
    autorizados_baixar_xml = None

    # - Produtos e Servicos (lista 1 para * / ManyToManyField)
    produtos_e_servicos = None

    # Totais
    # - ICMS
    #  - Base de calculo (somente leitura)
    totais_icms_base_calculo = Decimal()

    #  - Total do ICMS (somente leitura)
    totais_icms_total = Decimal()

    #  - Total do ICMS Desonerado (somente leitura)
    totais_icms_desonerado = Decimal()

    #  - Base de calculo do ICMS ST (somente leitura)
    totais_icms_st_base_calculo = Decimal()

    #  - Total do ICMS ST (somente leitura)
    totais_icms_st_total = Decimal()

    #  - Total dos produtos e servicos (somente leitura)
    totais_icms_total_produtos_e_servicos = Decimal()

    #  - Total do frete (somente leitura)
    totais_icms_total_frete = Decimal()

    #  - Total do seguro (somente leitura)
    totais_icms_total_seguro = Decimal()

    #  - Total do desconto (somente leitura)
    totais_icms_total_desconto = Decimal()

    #  - Total do II (somente leitura)
    totais_icms_total_ii = Decimal()

    #  - Total do IPI (somente leitura)
    totais_icms_total_ipi = Decimal()

    #  - Valor Total do IPI devolvido
    # Deve ser informado quando preenchido o Grupo Tributos Devolvidos na emissão de nota
    # finNFe=4 (devolução) nas operações com não contribuintes do IPI.
    # Corresponde ao total da soma dos campos id:UA04.
    totais_icms_total_ipi_dev = Decimal()

    #  - PIS (somente leitura)
    totais_icms_pis = Decimal()

    #  - COFINS (somente leitura)
    totais_icms_cofins = Decimal()

    #  - Outras despesas acessorias
    totais_icms_outras_despesas_acessorias = Decimal()

    #  - Total da nota
    totais_icms_total_nota = Decimal()

    # - ISSQN
    #  - Base de calculo do ISS
    totais_issqn_base_calculo_iss = Decimal()

    #  - Total do ISS
    totais_issqn_total_iss = Decimal()

    #  - PIS sobre servicos
    totais_issqn_pis = Decimal()

    #  - COFINS sobre servicos
    totais_issqn_cofins = Decimal()

    #  - Total dos servicos sob nao-incidencia ou nao tributados pelo ICMS
    totais_issqn_total = Decimal()

    # - Retencao de Tributos
    #  - Valor retido de PIS
    totais_retencao_valor_retido_pis = Decimal()

    #  - Valor retido de COFINS
    totais_retencao_valor_retido_cofins = Decimal()

    #  - Valor retido de CSLL
    totais_retencao_valor_retido_csll = Decimal()

    #  - Base de calculo do IRRF
    totais_retencao_base_calculo_irrf = Decimal()

    #  - Valor retido do IRRF
    totais_retencao_valor_retido_irrf = Decimal()

    #  - BC da ret. da Prev. Social
    totais_retencao_bc_retencao_previdencia_social = Decimal()

    #  - Retencao da Prev. Social
    totais_retencao_retencao_previdencia_social = Decimal()

    #  - Valor aproximado total de tributos federais, estaduais e municipais.
    totais_tributos_aproximado = Decimal()

    # - Valor Total do FCP (Fundo de Combate à Pobreza)
    totais_fcp = Decimal()

    # - Valor total do ICMS relativo Fundo de Combate à Pobreza (FCP) da UF de destino
    totais_fcp_destino = Decimal()

    # - Valor Total do FCP (Fundo de Combate à Pobreza) retido por substituição tributária
    totais_fcp_st = Decimal()

    # - Valor Total do FCP retido anteriormente por Substituição Tributária
    totais_fcp_st_ret = Decimal()

    # - Valor total do ICMS Interestadual para a UF de destino
    totais_icms_inter_destino = Decimal()

    # - Valor total do ICMS Interestadual para a UF do remetente
    totais_icms_inter_remetente = Decimal()

    # - Valor total do qBCMonoRet
    totais_icms_q_bc_mono_ret = Decimal()

    # - Valor total do vICMSMonoRet
    totais_icms_v_icms_mono_ret = Decimal()

    # - Valor total da quantidade tributada do ICMS monofásico próprio
    totais_icms_q_bc_mono = Decimal()

    # - Valor total do ICMS monofásico próprio
    totais_icms_v_icms_mono = Decimal()

    # - Valor total da quantidade tributada do ICMS monofásico sujeito a retenção
    totais_icms_q_bc_mono_reten = Decimal()

    # - Valor total do ICMS monofásico sujeito a retenção
    totais_icms_v_icms_mono_reten = Decimal()

    # Reforma Tributaria - Totais IVA Dual (Group W03 - IBSCBSTot)
    totais_vbc_ibscbs = Decimal()  # vBCIBSCBS - Total Base de Calculo
    totais_ibs_uf = Decimal()
    totais_ibs_mun = Decimal()
    totais_ibs = Decimal()
    totais_cbs = Decimal()
    totais_is = Decimal()

    # Reforma Tributaria - cMunFGIBS (Group B)
    municipio_fato_gerador_ibs = str()

    # Transporte
    # - Modalidade do Frete (obrigatorio - seleciona de lista) - MODALIDADES_FRETE
    # 0=Contratação do Frete por conta do Remetente (CIF);
    # 1=Contratação do Frete por conta do Destinatário (FOB);
    # 2=Contratação do Frete por conta de Terceiros;
    # 3=Transporte Próprio por conta do Remetente;
    # 4=Transporte Próprio por conta do Destinatário;
    # 9=Sem Ocorrência de Transporte.
    transporte_modalidade_frete = int()

    # - Transportador (seleciona de Transportadoras)
    transporte_transportadora = None

    # - Retencao do ICMS
    #  - Base de calculo
    transporte_retencao_icms_base_calculo = Decimal()

    #  - Aliquota
    transporte_retencao_icms_aliquota = Decimal()

    #  - Valor do servico
    transporte_retencao_icms_valor_servico = Decimal()

    #  - UF
    transporte_retencao_icms_uf = str()

    #  - Municipio
    transporte_retencao_icms_municipio = Decimal()

    #  - CFOP
    transporte_retencao_icms_cfop = str()

    #  - ICMS retido
    transporte_retencao_icms_retido = Decimal()

    # - Veiculo
    #  - Placa
    transporte_veiculo_placa = str()

    #  - RNTC
    transporte_veiculo_rntc = str()

    #  - UF
    transporte_veiculo_uf = str()

    # - Reboque
    #  - Placa
    transporte_reboque_placa = str()

    #  - RNTC
    transporte_reboque_rntc = str()

    #  - UF
    transporte_reboque_uf = str()

    # - Volumes (lista 1 para * / ManyToManyField)
    transporte_volumes = None

    # Cobranca
    # - Fatura
    #  - Numero
    fatura_numero = str()

    #  - Valor original
    fatura_valor_original = Decimal()

    #  - Valor do desconto
    fatura_valor_desconto = Decimal()

    #  - Valor liquido
    fatura_valor_liquido = Decimal()

    # - Duplicatas (lista 1 para * / ManyToManyField)
    duplicatas = None

    # Informacoes Adicionais
    # - Informacoes Adicionais
    #  - Informacoes adicionais de interesse do fisco
    informacoes_adicionais_interesse_fisco = str()

    #  - Informacoes complementares de interesse do contribuinte
    informacoes_complementares_interesse_contribuinte = str()

    # - Observacoes do Contribuinte (lista 1 para * / ManyToManyField)
    observacoes_contribuinte = None

    # - Processo Referenciado (lista 1 para * / ManyToManyField)
    processos_referenciados = None

    # - pagamentos
    pagamentos = list()
    # valor do troco
    valor_troco = Decimal()

    def __init__(self, *args, **kwargs):
        self.autorizados_baixar_xml = []
        self.notas_fiscais_referenciadas = []
        self.produtos_e_servicos = []
        self.transporte_volumes = []
        self.duplicatas = []
        self.observacoes_contribuinte = []
        self.processos_referenciados = []
        self.responsavel_tecnico = []
        self.pagamentos = []

        super(NotaFiscal, self).__init__(*args, **kwargs)

    def __str__(self):
        return " ".join([str(self.modelo), self.serie, self.numero_nf])

    def adicionar_pagamento(self, **kwargs):
        """Adiciona uma instancia de Responsavel Tecnico"""
        obj = NotaFiscalPagamentos(**kwargs)
        self.pagamentos.append(obj)
        return obj

    def adicionar_autorizados_baixar_xml(self, **kwargs):
        obj = AutorizadosBaixarXML(**kwargs)
        self.autorizados_baixar_xml.append(obj)
        return obj

    def adicionar_nota_fiscal_referenciada(self, **kwargs):
        """Adiciona uma instancia de Nota Fisca referenciada"""
        obj = NotaFiscalReferenciada(**kwargs)
        self.notas_fiscais_referenciadas.append(obj)
        return obj

    def adicionar_produto_servico(self, **kwargs):
        """Adiciona uma instancia de Produto"""
        obj = NotaFiscalProduto(**kwargs)
        self.produtos_e_servicos.append(obj)
        self.totais_icms_base_calculo += obj.icms_valor_base_calculo
        self.totais_icms_total += obj.icms_valor
        self.totais_icms_desonerado += obj.icms_desonerado
        self.totais_icms_st_base_calculo += obj.icms_st_valor_base_calculo
        self.totais_icms_st_total += obj.icms_st_valor
        self.totais_icms_total_produtos_e_servicos += obj.valor_total_bruto
        self.totais_icms_total_frete += obj.total_frete
        self.totais_icms_total_seguro += obj.total_seguro
        self.totais_icms_total_desconto += obj.desconto
        self.totais_icms_total_ii += obj.imposto_importacao_valor
        self.totais_icms_total_ipi += obj.ipi_valor_ipi
        self.totais_icms_total_ipi_dev += obj.ipi_valor_ipi_dev
        self.totais_icms_pis += obj.pis_valor
        self.totais_icms_cofins += obj.cofins_valor
        self.totais_icms_outras_despesas_acessorias += obj.outras_despesas_acessorias
        # - Valor Total do FCP (Fundo de Combate à Pobreza)
        self.totais_fcp += obj.fcp_valor
        self.totais_fcp_destino += obj.fcp_destino_valor
        self.totais_fcp_st += obj.fcp_st_valor
        self.totais_fcp_st_ret += obj.fcp_st_ret_valor
        self.totais_icms_inter_destino += obj.icms_inter_destino_valor
        self.totais_icms_inter_remetente += obj.icms_inter_remetente_valor

        # - ICMS monofasico para combustiveis
        self.totais_icms_q_bc_mono += obj.icms_q_bc_mono
        self.totais_icms_v_icms_mono += obj.icms_v_icms_mono
        self.totais_icms_q_bc_mono_reten += obj.icms_q_bc_mono_reten
        self.totais_icms_v_icms_mono_reten += obj.icms_v_icms_mono_reten
        self.totais_icms_q_bc_mono_ret += obj.icms_q_bc_mono_ret
        self.totais_icms_v_icms_mono_ret += obj.icms_v_icms_mono_ret

        # Reforma Tributaria - IVA Dual (NT 2025.002-RTC)
        self.totais_vbc_ibscbs += obj.ibscbs_vbc
        self.totais_ibs_uf += obj.ibscbs_v_ibs_uf
        self.totais_ibs_mun += obj.ibscbs_v_ibs_mun
        self.totais_ibs += obj.ibscbs_v_ibs
        self.totais_cbs += obj.ibscbs_v_cbs
        self.totais_is += obj.is_valor

        # TODO calcular impostos aproximados
        # self.totais_tributos_aproximado += obj.tributos

        # vNF does NOT include IBS/CBS/IS (prohibited in 2025-2026 per NT 2025.002-RTC)
        self.totais_icms_total_nota += (
            obj.valor_total_bruto
            + obj.icms_st_valor
            + obj.fcp_st_valor
            + obj.total_frete
            + obj.total_seguro
            + obj.outras_despesas_acessorias
            + obj.imposto_importacao_valor
            + obj.ipi_valor_ipi
            + obj.ipi_valor_ipi_dev
            - obj.desconto
            - obj.icms_desonerado
        )

        return obj

    def adicionar_transporte_volume(self, **kwargs):
        """Adiciona uma instancia de Volume de Transporte"""
        obj = NotaFiscalTransporteVolume(**kwargs)
        self.transporte_volumes.append(obj)
        return obj

    def adicionar_duplicata(self, **kwargs):
        """Adiciona uma instancia de Duplicata"""
        obj = NotaFiscalCobrancaDuplicata(**kwargs)
        self.duplicatas.append(obj)
        return obj

    def adicionar_observacao_contribuinte(self, **kwargs):
        """Adiciona uma instancia de Observacao do Contribuinte"""
        obj = NotaFiscalObservacaoContribuinte(**kwargs)
        self.observacoes_contribuinte.append(obj)
        return obj

    def adicionar_processo_referenciado(self, **kwargs):
        """Adiciona uma instancia de Processo Referenciado"""
        obj = NotaFiscalProcessoReferenciado(**kwargs)
        self.processos_referenciados.append(obj)
        return obj

    def adicionar_responsavel_tecnico(self, **kwargs):
        """Adiciona uma instancia de Responsavel Tecnico"""
        obj = NotaFiscalResponsavelTecnico(**kwargs)
        self.responsavel_tecnico.append(obj)
        return obj

    def _codigo_numerico_aleatorio(self):
        if not self.codigo_numerico_aleatorio:
            self.codigo_numerico_aleatorio = str(random.randint(0, 99999999)).zfill(8)
        return self.codigo_numerico_aleatorio

    def _dv_codigo_numerico(self, key):
        if not len(key) == 43:
            raise ValueError(
                f"Chave de acesso deve ter 43 caracteres antes de calcular o DV, chave: {key}"
            )

        weights = [2, 3, 4, 5, 6, 7, 8, 9]
        weights_size = len(weights)
        key_numbers = [int(k) for k in key]
        key_numbers.reverse()

        key_sum = 0
        for i, key_number in enumerate(key_numbers):
            # cycle though weights
            i = i % weights_size
            key_sum += key_number * weights[i]

        remainder = key_sum % 11
        if remainder == 0 or remainder == 1:
            self.dv_codigo_numerico_aleatorio = "0"
            return "0"
        self.dv_codigo_numerico_aleatorio = str(11 - remainder)
        return str(self.dv_codigo_numerico_aleatorio)

    @property
    # @memoize
    def identificador_unico(self):
        # Monta 'Id' da tag raiz <infNFe>
        # Ex.: NFe35080599999090910270550010000000011518005123
        key = "%(uf)s%(ano)s%(mes)s%(cnpj)s%(mod)s%(serie)s%(nNF)s%(tpEmis)s%(cNF)s" % {
            "uf": CODIGOS_ESTADOS[self.uf],
            "ano": self.data_emissao.strftime("%y"),
            "mes": self.data_emissao.strftime("%m"),
            "cnpj": so_numeros(self.emitente.cnpj).zfill(14),
            "mod": self.modelo,
            "serie": str(self.serie).zfill(3),
            "nNF": str(self.numero_nf).zfill(9),
            "tpEmis": str(self.forma_emissao),
            "cNF": self._codigo_numerico_aleatorio(),
        }
        return "NFe%(uf)s%(ano)s%(mes)s%(cnpj)s%(mod)s%(serie)s%(nNF)s%(tpEmis)s%(cNF)s%(cDV)s" % {
            "uf": CODIGOS_ESTADOS[self.uf],
            "ano": self.data_emissao.strftime("%y"),
            "mes": self.data_emissao.strftime("%m"),
            "cnpj": so_numeros(self.emitente.cnpj).zfill(14),
            "mod": self.modelo,
            "serie": str(self.serie).zfill(3),
            "nNF": str(self.numero_nf).zfill(9),
            "tpEmis": str(self.forma_emissao),
            "cNF": str(self.codigo_numerico_aleatorio),
            "cDV": self._dv_codigo_numerico(key),
        }


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

    #   - IE
    ie = str()

    #   - Serie (XXX)
    serie = str()

    #   - Numero
    numero = str()

    #   - Modelo
    modelo = str()


class NotaFiscalProduto(Entidade):
    # Campos depreciados
    campos_deprecados = [
        CampoDeprecated("fcp_percentual", "fcp_aliquota", "Consistencia de nomes"),
        CampoDeprecated("fcp_st_percentual", "fcp_st_aliquota", "Consistencia de nomes"),
    ]
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

    # Número de controle da FCI (nFCI) - Ficha de Conteúdo de Importação.
    nfci = str()

    #  - Unidade Comercial (obrigatorio)
    unidade_comercial = str()

    #  - Quantidade Comercial (obrigatorio)
    quantidade_comercial = Decimal()

    #  - Valor Unitario Comercial (obrigatorio)
    valor_unitario_comercial = Decimal()

    #  - Unidade Tributavel (obrigatorio)
    unidade_tributavel = str()

    # - cBenef
    cbenef = str()

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

    # - Outras despesas acessórias
    outras_despesas_acessorias = Decimal()

    # - Indica se valor do Item (vProd) entra no valor total da NF-e
    compoe_valor_total = 1

    #  - Valor total bruto (obrigatorio)
    valor_total_bruto = Decimal()

    # - Número do Pedido de Compra
    numero_pedido = str()

    # - Item do Pedido de Compra
    numero_item = str()

    #  - Produto especifico (seleciona de lista) - NF_PRODUTOS_ESPECIFICOS
    produto_especifico = str()

    # Grupo de informações de Combustível
    # Código de produto da ANP
    cProdANP = str()

    # Descrição do produto conforme ANP
    descANP = str()

    # Percentual de Gás derivado do Petróleo
    pGLP = Decimal()

    # Percentual de gás natural nacional
    pGNn = Decimal()

    # Percentual do gás natural importado
    pGNi = Decimal()

    # Valor de Partida (apenas para GLP)
    vPart = Decimal()

    # Sigla da UF de consumo – (OBS: Deve ser a Sigla e não o Código da UF)
    UFCons = str()

    # Código de autorização / registro do CODI
    comb_codif = str()

    # Quantidade de combustível faturada à temperatura ambiente.
    comb_q_temp = str()

    # - Grupo de informações dos encerrantes
    # Número de identificação do bico utilizado no abastecimento
    comb_n_bico = int()

    # Número de identificação da bomba ao qual o bico está interligado
    comb_n_bomba = int()

    # Número de identificação do tanque ao qual o bico está interligado
    comb_n_tanque = int()

    # Valor do Encerrante no início do abastecimento
    comb_v_enc_ini = Decimal()

    # Valor do Encerrante no final do abastecimento
    comb_v_enc_fin = Decimal()

    # Percentual do índice de mistura do Biodiesel (B100) no Óleo Diesel B
    comb_p_bio = Decimal()

    # - Tributos
    #  - ICMS
    #   - Situacao tributaria (obrigatorio - seleciona de lista) - ICMS_TIPOS_TRIBUTACAO
    icms_modalidade = str()

    #   - Origem (obrigatorio - seleciona de lista) - ICMS_ORIGENS
    icms_origem = int()

    #   - ICMS
    #    - Modalidade de determinacao da BC ICMS (seleciona de lista) - ICMS_MODALIDADES
    icms_modalidade_determinacao_bc = int()

    #    - Percentual reducao da BC ICMS
    icms_percentual_reducao_bc = Decimal()

    #    - Valor da base de calculo ICMS
    icms_valor_base_calculo = Decimal()

    #    - Aliquota ICMS
    icms_aliquota = Decimal()

    #    - Valor do ICMS
    icms_valor = Decimal()

    #    - ICMS Desonerado
    icms_desonerado = Decimal()

    #    - Motivo da desoneração do ICMS (seleciona de lista) - ICMS_MOTIVO_DESONERACAO
    icms_motivo_desoneracao = int()

    #   - ICMS ST
    #    - Modalidade de determinacao da BC ICMS ST - ICMS_ST_MODALIDADES
    icms_st_modalidade_determinacao_bc = int()

    #    - Percentual da margem de valor Adicionado do ICMS ST
    icms_st_percentual_adicional = Decimal()
    #    - Percentual reducao da BC ICMS ST
    icms_st_percentual_reducao_bc = Decimal()

    #    - Valor da base de calculo ICMS ST
    icms_st_valor_base_calculo = Decimal()

    #    - Aliquota ICMS ST
    icms_st_aliquota = Decimal()

    #    - Valor do ICMS ST
    icms_st_valor = Decimal()

    #    - Fundo de Combate a Pobreza
    fcp_base_calculo = Decimal()
    fcp_aliquota = Decimal()
    fcp_valor = Decimal()

    # FCP ST
    fcp_st_base_calculo = Decimal()
    fcp_st_aliquota = Decimal()
    fcp_st_valor = Decimal()
    fcp_destino_valor = Decimal()

    # FCP ST Retido
    fcp_st_ret_base_calculo = Decimal()
    fcp_st_ret_aliquota = Decimal()
    fcp_st_ret_valor = Decimal()

    icms_inter_destino_valor = Decimal()
    icms_inter_remetente_valor = Decimal()

    #   - ICMS ST Retido
    #    - Valor da base de calculo
    icms_st_ret_base_calculo = Decimal()

    #    - Aliquota
    icms_st_ret_aliquota = Decimal()

    #    - Valor
    icms_st_ret_valor = Decimal()

    # - ICMS monofásico
    icms_ad_rem_icms = Decimal()
    icms_v_icms_mono = Decimal()
    icms_q_bc_mono = Decimal()
    icms_ad_rem_icms_reten = Decimal()
    icms_v_icms_mono_reten = Decimal()
    icms_q_bc_mono_reten = Decimal()
    icms_p_red_ad_rem = Decimal()
    icms_mot_red_ad_rem = int()
    icms_v_icms_mono_op = Decimal()
    icms_v_icms_mono_dif = Decimal()
    icms_ad_rem_icms_ret = Decimal()
    icms_v_icms_mono_ret = Decimal()
    icms_q_bc_mono_ret = Decimal()
    icms_p_dif = Decimal()

    #  - IPI
    #   - Situacao tributaria (seleciona de lista) - IPI_TIPOS_TRIBUTACAO
    ipi_situacao_tributaria = str()

    #   - Classe de enquadramento
    #    - A informacao para classe de enquadramento do IPI para Cigarros e Bebidas,
    #      quando aplicavel, deve ser informada utilizando a codificacao prevista nos
    #      Atos Normativos editados pela Receita Federal
    ipi_classe_enquadramento = str()

    #   - Codigo do enquadramento
    ipi_codigo_enquadramento = str()

    #   - CNPJ do Produtor
    ipi_cnpj_produtor = str()

    #   - Codigo do selo de controle
    #    - A informacao do codigo de selo, quando aplicavel, deve ser informada
    #      utilizando a codificacao prevista nos Atos Normativos editados pela Receita
    #      Federal
    ipi_codigo_selo_controle = str()

    #   - Quantidade do selo de controle
    ipi_quantidade_selo_controle = Decimal()

    #   - Tipo de calculo (seleciona de lista) - IPI_TIPOS_CALCULO
    ipi_tipo_calculo = str()

    #    - Percentual
    #     - Valor da base de calculo
    ipi_valor_base_calculo = Decimal()

    #     - Aliquota
    ipi_aliquota = Decimal()

    #    - Em valor
    #     - Quantidade total unidade padrao
    ipi_quantidade_total_unidade_padrao = Decimal()

    #     - Valor por unidade
    ipi_valor_unidade = Decimal()

    #   - Valor do IPI
    ipi_valor_ipi = Decimal()

    # - Percentual Devolucao Produto
    pdevol = Decimal()

    #   - Valor do IPI Devolvido
    ipi_valor_ipi_dev = Decimal()

    #  - PIS
    #   - PIS
    #    - Situacao tributaria (obrigatorio - seleciona de lista) - PIS_TIPOS_TRIBUTACAO
    pis_situacao_tributaria = str()

    #    - Tipo de calculo (seleciona de lista) - PIS_TIPOS_CALCULO
    pis_tipo_calculo = str()

    #     - Percentual
    #      - Valor da base de calculo
    pis_valor_base_calculo = Decimal()

    #      - Aliquota (percentual)
    pis_aliquota_percentual = Decimal()

    #     - Em valor
    #      - Aliquota (em reais)
    pis_aliquota_reais = Decimal()

    #      - Quantidade vendida
    pis_quantidade_vendida = Decimal()

    #    - Valor do PIS
    pis_valor = Decimal()

    #   - PIS ST
    #    - Tipo de calculo (seleciona de lista) - PIS_TIPOS_CALCULO
    pis_st_tipo_calculo = str()

    #     - Percentual
    #      - Valor da base de calculo
    pis_st_valor_base_calculo = Decimal()

    #      - Aliquota (percentual)
    pis_st_aliquota_percentual = Decimal()

    #     - Em valor
    #      - Aliquota (em reais)
    pis_st_aliquota_reais = Decimal()

    #      - Quantidade vendida
    pis_st_quantidade_vendida = Decimal()

    #    - Valor do PIS ST
    pis_st_valor = Decimal()

    #  - COFINS
    #   - COFINS
    #    - Situacao tributaria (obrigatorio - seleciona de lista) - COFINS_TIPOS_TRIBUTACAO
    cofins_situacao_tributaria = str()

    #    - Tipo de calculo (seleciona de lista) - COFINS_TIPOS_CALCULO
    cofins_tipo_calculo = str()

    #     - Percentual
    #      - Valor da base de calculo
    cofins_valor_base_calculo = Decimal()

    #      - Aliquota (percentual)
    cofins_aliquota_percentual = Decimal()

    #     - Em Valor
    #      - Aliquota (em reais)
    cofins_aliquota_reais = Decimal()

    #      - Quantidade vendida
    cofins_quantidade_vendida = Decimal()

    #    - Valor do COFINS
    cofins_valor = Decimal()

    #   - COFINS ST
    #    - Tipo de calculo (seleciona de lista) - COFINS_TIPOS_CALCULO
    cofins_st_tipo_calculo = str()

    #     - Percentual
    #      - Valor da base de calculo
    cofins_st_valor_base_calculo = Decimal()

    #      - Aliquota (percentual)
    cofins_st_aliquota_percentual = Decimal()

    #     - Em Valor
    #      - Aliquota (em reais)
    cofins_st_aliquota_reais = Decimal()

    #      - Quantidade vendida
    cofins_st_quantidade_vendida = Decimal()

    #    - Valor do COFINS ST
    cofins_st_valor = Decimal()

    #   - ISSQN
    #   - Valor da base de calculo
    issqn_valor_base_calculo = Decimal()

    #   - Aliquota
    issqn_aliquota = Decimal()

    #   - Lista de servico (seleciona de lista)
    #   - Aceita somente valores maiores que 100,
    #   disponiveis no arquivo data/ISSQN/Lista-Servicos.txt
    issqn_lista_servico = str()

    #   - UF
    issqn_uf = str()

    #   - Municipio de ocorrencia
    issqn_municipio = str()

    #   - Valor do ISSQN
    issqn_valor = Decimal()

    #  - Imposto de Importacao
    #   - Valor base de calculo
    imposto_importacao_valor_base_calculo = Decimal()

    #   - Valor despesas aduaneiras
    imposto_importacao_valor_despesas_aduaneiras = Decimal()

    #   - Valor do IOF
    imposto_importacao_valor_iof = Decimal()

    #   - Valor imposto de importacao
    imposto_importacao_valor = Decimal()

    # =============================================
    # Reforma Tributaria - IVA Dual (NT 2025.002-RTC)
    # =============================================

    # IBSCBS group (Group UB)
    ibscbs_cst = str()  # CST 3-digit (e.g. "000", "222")
    ibscbs_c_class_trib = str()  # cClassTrib 6-digit classification code
    ibscbs_vbc = Decimal()  # vBC - shared base de calculo for IBS + CBS

    # gIBSUF - IBS estadual (UF)
    ibscbs_p_ibs_uf = Decimal()  # pIBSUF
    ibscbs_v_ibs_uf = Decimal()  # vIBSUF

    # gIBSMun - IBS municipal
    ibscbs_p_ibs_mun = Decimal()  # pIBSMun
    ibscbs_v_ibs_mun = Decimal()  # vIBSMun

    # vIBS total (UF + Mun)
    ibscbs_v_ibs = Decimal()

    # gCBS - CBS federal
    ibscbs_p_cbs = Decimal()  # pCBS
    ibscbs_v_cbs = Decimal()  # vCBS

    # IS (Imposto Seletivo) - Group UB-IS
    is_cst_selec = str()  # CSTSelec (2-digit)
    is_c_class_trib = str()  # cClassTribIS 6-digit
    is_vbc = Decimal()  # vBC
    is_aliquota = Decimal()  # pIS
    is_valor = Decimal()  # vIS

    # - Informacoes Adicionais
    #  - Texto livre de informacoes adicionais
    informacoes_adicionais = str()

    # - Declaracao de Importacao (lista 1 para * / ManyToManyField)
    declaracoes_importacao = None

    def __init__(self, *args, **kwargs):
        self.declaracoes_importacao = []

        super(NotaFiscalProduto, self).__init__(*args, **kwargs)

    def adicionar_declaracao_importacao(self, **kwargs):
        """Adiciona uma instancia de Declaracao de Importacao"""
        self.declaracoes_importacao.append(NotaFiscalDeclaracaoImportacao(**kwargs))


class NotaFiscalDeclaracaoImportacao(Entidade):
    #  - Numero DI/DSI/DA
    numero_di_dsi_da = str()

    #  - Data de registro
    data_registro = None

    #  - Desembaraco aduaneiro
    #   - UF
    desembaraco_aduaneiro_uf = str()

    #   - Local
    desembaraco_aduaneiro_local = str()

    #   - Data
    desembaraco_aduaneiro_data = str()

    #   - Via de transporte internacional informada na Declaração de Importação (DI)
    tipo_via_transporte = str()

    #   - Valor da AFRMM - Adicional ao Frete para Renovação da Marinha Mercante
    valor_afrmm = Decimal()

    #   - Forma de importação quanto a intermediação
    tipo_intermediacao = str()

    #   - CNPJ do adquirente ou do encomendante
    cnpj_adquirente = str()

    #   - UFTerceiro - Sigla da UF do adquirente ou do encomendante
    uf_terceiro = str()

    #  - Codigo exportador
    codigo_exportador = str()

    #  - Adicoes (lista 1 para * / ManyToManyField)
    adicoes = None

    def __init__(self, *args, **kwargs):
        self.declaracoes_importacao = []

        super(NotaFiscalDeclaracaoImportacao, self).__init__(*args, **kwargs)

    def adicionar_adicao(self, **kwargs):
        """Adiciona uma instancia de Adicao de Declaracao de Importacao"""
        self.adicoes.append(NotaFiscalDeclaracaoImportacaoAdicao(**kwargs))


class NotaFiscalDeclaracaoImportacaoAdicao(Entidade):
    #   - Numero
    numero = str()

    #   - Desconto
    desconto = Decimal()

    #   - Codigo fabricante
    codigo_fabricante = str()

    #   - Número do ato concessório de Drawback
    numero_drawback = str()


class NotaFiscalTransporteVolume(Entidade):
    #  - Quantidade
    quantidade = Decimal()

    #  - Especie
    especie = str()

    #  - Marca
    marca = str()

    #  - Numeracao
    numeracao = str()

    #  - Peso Liquido (kg)
    peso_liquido = Decimal()

    #  - Peso Bruto (kg)
    peso_bruto = Decimal()

    #  - Lacres (lista 1 para * / ManyToManyField)
    lacres = None

    def __init__(self, *args, **kwargs):
        self.lacres = []

        super(NotaFiscalTransporteVolume, self).__init__(*args, **kwargs)

    def adicionar_lacre(self, **kwargs):
        """Adiciona uma instancia de Lacre de Volume de Transporte"""
        self.lacres.append(NotaFiscalTransporteVolumeLacre(**kwargs))


class NotaFiscalTransporteVolumeLacre(Entidade):
    #   - Numero de lacres
    numero_lacre = str()


class NotaFiscalCobrancaDuplicata(Entidade):
    #  - Numero
    numero = str()

    #  - Data de vencimento
    data_vencimento = None

    #  - Valor
    valor = Decimal()


class NotaFiscalObservacaoContribuinte(Entidade):
    #  - Nome do campo
    nome_campo = str()

    #  - Observacao
    observacao = str()


class NotaFiscalProcessoReferenciado(Entidade):
    #  - Identificador do processo
    identificador_processo = str()

    #  - Origem (seleciona de lista) - ORIGENS_PROCESSO
    #   - SEFAZ
    #   - Justica federal
    #   - Justica estadual
    #   - Secex/RFB
    #   - Outros
    origem = str()


class NotaFiscalEntregaRetirada(Entidade):
    # - Tipo de Documento (obrigatorio) - default CNPJ
    tipo_documento = "CNPJ"

    # - Numero do Documento (obrigatorio)
    numero_documento = str()

    # - Endereco
    #  - Logradouro (obrigatorio)
    endereco_logradouro = str()

    #  - Numero (obrigatorio)
    endereco_numero = str()

    #  - Complemento
    endereco_complemento = str()

    #  - Bairro (obrigatorio)
    endereco_bairro = str()

    #  - CEP
    endereco_cep = str()

    #  - Pais (seleciona de lista)
    endereco_pais = str()

    #  - UF (obrigatorio)
    endereco_uf = str()

    #  - Municipio (obrigatorio)
    endereco_municipio = str()

    # - Código Município (opt)
    endereco_cod_municipio = str()

    #  - Telefone
    endereco_telefone = str()


class NotaFiscalServico(Entidade):
    # id do rps
    identificador = str()
    # tag competencia
    data_emissao = None
    # Serviço executado pelo prestador
    servico = None
    # Emitente da NFS-e
    emitente = None
    # Cliente para quem a NFS-e será emitida
    cliente = None
    # Optante Simples Nacional
    simples = int()  # 1-Sim; 2-Não
    # Incentivo Fiscal
    incentivo = int()  # 1-Sim; 2-Não
    # Serie
    serie = str()
    # Tipo
    tipo = str()
    # Natureza de operação
    natureza_operacao = int()
    # Regime especial de tributação
    regime_especial = int()

    def __init__(self, *args, **kwargs):
        super(NotaFiscalServico, self).__init__(*args, **kwargs)

    def __str__(self):
        return " ".join([str(self.identificador)])


class NotaFiscalResponsavelTecnico(Entidade):
    # NT 2018/003
    cnpj = str()
    contato = str()
    email = str()
    fone = str()
    csrt = str()


class AutorizadosBaixarXML(Entidade):
    CPFCNPJ = str()


class NotaFiscalPagamentos(Entidade):
    # forma de pagamento flag: FORMAS_PAGAMENTO
    t_pag = str()
    # descrição da forma de pagametno
    x_pag = str()
    # valor
    v_pag = Decimal()
    # tipo de integracao: '', '1' integrado, '2' - não integrado
    tp_integra = str()
    # CNPJ da Credenciadora de cartão de crédito e/ou débito
    cnpj = str()
    # Bandeira da operadora de cartão de crédito e/ou débito flag: BANDEIRA_CARTAO
    t_band = int()
    # Número de autorização da operação cartão de crédito e/ou débito
    c_aut = str()
    # Indicador da Forma de Pagamento: 0=à Vista, 1=à Prazo
    ind_pag = int()
