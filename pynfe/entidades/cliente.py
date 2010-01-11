# -*- coding: utf-8 -*-
from base import Entidade

TIPOS_DOCUMENTO = (
    'CNPJ',
    'CPF',
)

class Cliente(Entidade):
    # Dados do Cliente
    # - Nome/Razão Social (obrigatorio)
    razao_social = str()

    # - Tipo de Documento (obrigatorio) - default CNPJ - TIPOS_DOCUMENTO
    tipo_documento = 'CNPJ'

    # - Numero do Documento (obrigatorio)
    numero_documento = str()

    # - Inscricao Estadual
    inscricao_estadual = str()

    # - Inscricao SUFRAMA
    inscricao_suframa = str()

    # - Isento do ICMS (Sim/Nao)
    isento_icms = False

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

    # - Pais (seleciona de lista)
    endereco_pais = 'BRASIL'

    # - UF (obrigatorio)
    endereco_uf = str()

    # - Municipio (obrigatorio)
    endereco_municipio = str()

    # - Telefone
    endereco_telefone = str()

