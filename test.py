#!/usr/bin/env python
# *-* encoding: utf8 *-*

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscal
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.processamento.serializacao import SerializacaoPipes
from pynfe.utils.flags import CODIGO_BRASIL

serializador = SerializacaoPipes(_fonte_dados, homologacao=True)

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

print serializador._serializar_emitente(emitente)

cliente = Cliente(
    razao_social='MARIANA DE CARVALHO CASCELLI',
    tipo_documento='CPF', #CPF ou CNPJ
    email='ianafonteboa@hotmail.com',
    numero_documento='04247008161',
    endereco_logradouro='Q SHIS QI 23 CONJUNTO 1',
    endereco_numero='SN',
    endereco_complemento='CASA 05',
    endereco_bairro='SETOR DE HABITACOES INDIVIDUAI',
    endereco_municipio='Brasilia',
    endereco_uf='DF',
    endereco_cep='71660150',
    endereco_pais=CODIGO_BRASIL,
    endereco_telefone='6132029975',
)

nota_fiscal = NotaFiscal(
    emitente=emitente,
    cliente=cliente,
)

import pprint
pprint.pprint(emitente.__dict__)
pprint.pprint(cliente.__dict__)
