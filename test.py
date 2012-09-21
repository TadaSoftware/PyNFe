#!/usr/bin/env python

from pynfe.entidades.emitente import Emitente
from pynfe.utils.flags import CODIGO_BRASIL


emitente = Emitente(
    razao_social='Spring Publicacoes Ltda',
    cnpj='08234482000156',
    codigo_de_regime_tributario='3',
    inscricao_estadual='149431130117',
    endereco_logradouro='RUA FERREIRA DE ARAUJO',
    endereco_numero='202',
    endereco_complemento='9o andar - cj 91/92',
    endereco_bairro='PINHEIROS',
    endereco_municipio='SAO PAULO',
    endereco_uf='SP',
    endereco_cep='05428000', 
    endereco_pais=CODIGO_BRASIL,
)

import pprint
pprint.pprint(emitente.__dict__)
