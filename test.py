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
    razao_social='MARIANA CARVALHO SILVA',
    tipo_documento='CPF', #CPF ou CNPJ
    email='email@email.com',
    numero_documento='12345678900',
    endereco_logradouro='Rua dos Bobos',
    endereco_numero='Zero',
    endereco_complemento='Ao lado de lugar nenhum',
    endereco_bairro='Aquele Mesmo',
    endereco_municipio='Brasilia',
    endereco_uf='DF',
    endereco_cep='12345123',
    endereco_pais=CODIGO_BRASIL,
    endereco_telefone='11912341234',
)

nota_fiscal = NotaFiscal(
    emitente=emitente,
    cliente=cliente,
)

import pprint
pprint.pprint(emitente.__dict__)
pprint.pprint(cliente.__dict__)
