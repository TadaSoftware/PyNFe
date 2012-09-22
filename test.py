#!/usr/bin/env python
# *-* encoding: utf8 *-*

from decimal import Decimal

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscal, NotaFiscalProduto
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.processamento.serializacao import SerializacaoPipes
from pynfe.utils.flags import CODIGO_BRASIL

serializador = SerializacaoPipes(_fonte_dados, homologacao=True)

emitente = Emitente(
    razao_social='Spring Publicacoes Ltda',
    cnpj='08234482000156',
    codigo_de_regime_tributario='3', # 1 para simples nacional ou 3 para normal
    inscricao_estadual='149431130117', # numero de IE da empresa
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
    numero_documento='12345678900', # numero do cpf ou cnpj
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
print serializador._serializar_cliente(cliente)

produto = NotaFiscalProduto(
    codigo='000328', # id do produto (000328 era o id no antigo sistemas de assinatura)
    descricao='Assinatura Rolling Stone',
    ncm='49029000', # categoria international do prod (sempre esse para assinaturas)
    cfop='6922', 
    unidade_comercial='UN',
    quantidade_comercial=Decimal('12'), # 12 unidades (12 revistas) 
    valor_unitario_comercial=Decimal('9.75'),
    valor_total_bruto=Decimal('117.00'),
    unidade_tributavel='UN',
    quantidade_tributavel=Decimal('12'),
    valor_unitario_tributavel=Decimal('9.75'),
    numero_pedido='12345', # id da ordem
    numero_do_item='12345328', # id do item (pode ser o id do produto concatenado com o do pedido)
)
print serializador._serializar_produto_servico(produto)

#nota_fiscal = NotaFiscal(
#    emitente=emitente,
#    cliente=cliente,
#)
