# -*- coding: utf-8 -*-
from .base import Entidade


class Cliente(Entidade):
    # Dados do Cliente
    # - Nome/Razão Social (obrigatorio)
    razao_social = str()

    # - Email
    email = str()

    # - Tipo de Documento (obrigatorio) - default CNPJ - TIPOS_DOCUMENTO
    tipo_documento = "CNPJ"

    # - Numero do Documento (obrigatorio)
    numero_documento = str()

    # - Indicador da IE do destinatário: 1 – Contribuinte ICMSpagamento à vista;
    # 2 – Contribuinte isento de inscrição; 9 – Não Contribuinte
    indicador_ie = int()

    # - Inscricao Estadual
    inscricao_estadual = str()

    # - Inscricao Municial
    inscricao_municipal = str()

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
    endereco_pais = str()

    # - UF (obrigatorio)
    endereco_uf = str()

    # - Municipio (obrigatorio)
    endereco_municipio = str()

    # - Código do Município (opt)
    endereco_cod_municipio = str()

    # - Telefone
    endereco_telefone = str()

    def __str__(self):
        return " ".join([self.tipo_documento, self.numero_documento])
