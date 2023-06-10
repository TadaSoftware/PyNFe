from .base import Entidade
from pynfe.utils.flags import CODIGO_BRASIL


class Emitente(Entidade):
    # Dados do Emitente
    # - Nome/Razao Social (obrigatorio)
    razao_social = str()

    # - Nome Fantasia
    nome_fantasia = str()

    # - CNPJ (obrigatorio)
    cnpj = str()

    # - Inscricao Estadual (obrigatorio)
    inscricao_estadual = str()

    # - CNAE Fiscal
    cnae_fiscal = str()

    # - Inscricao Municipal
    inscricao_municipal = str()

    # - Inscricao Estadual (Subst. Tributario)
    inscricao_estadual_subst_tributaria = str()

    # - Codigo de Regime Tributario (obrigatorio)
    codigo_de_regime_tributario = str()

    # Endereco
    # - Logradouro (obrigatorio)
    endereco_logradouro = str()

    # - Numero (obrigatorio)
    endereco_numero = str()

    # - Complemento
    endereco_complemento = str()

    # - Bairro (obrigatorio)
    endereco_bairro = str()

    # - CEP
    endereco_cep = str()

    # - Pais (aceita somente Brasil)
    endereco_pais = CODIGO_BRASIL

    # - UF (obrigatorio)
    endereco_uf = str()

    # - Municipio (obrigatorio)
    endereco_municipio = str()

    # - Codigo Municipio (opt)
    endereco_cod_municipio = str()

    # - Telefone
    endereco_telefone = str()

    # Logotipo
    logotipo = None

    def __str__(self):
        return self.cnpj
