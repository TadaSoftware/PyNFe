#!/usr/bin/env python
# *-* encoding: utf8 *-*


from decimal import Decimal

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscal, NotaFiscalProduto
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.processamento.serializacao import SerializacaoPipes, SerializacaoXML
from pynfe.processamento.validacao import Validacao
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.utils.flags import CODIGO_BRASIL
import datetime

#serializador = SerializacaoPipes(_fonte_dados, homologacao=True)
#serializador = SerializacaoXML(_fonte_dados, homologacao=True)

emitente = Emitente(
    razao_social='Spring Publicacoes Ltda',
    nome_fantasia='Falcao Ferragens',
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

#print serializador._serializar_emitente(emitente)

cliente = Cliente(
    razao_social='MARIANA CARVALHO SILVA',
    tipo_documento='CPF', #CPF ou CNPJ
    email='email@email.com',
    numero_documento='12345678900', # numero do cpf ou cnpj
    inscricao_estadual='ISENTO',
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
#print serializador._serializar_cliente(cliente)

nota_fiscal = NotaFiscal(
   emitente=emitente,
   cliente=cliente,
   uf='PR',
   codigo_numerico_aleatorio='66998237',
   natureza_operacao='VENDA ASSINATURAS',
   forma_pagamento='1',
   modelo=55,
   serie='1',
   numero_nf='1',
   data_emissao=datetime.datetime.now(),
   data_saida_entrada=datetime.datetime.now(),
   #hora_saida_entrada=datetime.time(03,12,00),
   tipo_documento=1,
   municipio='4118402',
   tipo_impressao_danfe=1, # nfce 4
   forma_emissao='1',
   #dv_codigo_numerico_aleatorio=, ?
   finalidade_emissao='1',
   processo_emissao='3',
   transporte_modalidade_frete=0,
   informacoes_adicionais_interesse_fisco='NF-e emitida de acordo com os termos do Convenio ICMS 24/2011. Assinatura Numero 8061746'
)
nota_fiscal.adicionar_produto_servico(codigo='000328', # id do produto (000328 era o id no antigo sistemas de assinatura)
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
    icms_origem=0,
    icms_modalidade_determinacao_bc=41,
    pis_tipo_calculo='01',
    pis_valor_base_calculo=Decimal('117.00'),
    pis_aliquota_percentual=Decimal('0.65'),
    pis_valor=Decimal('0.76'),
    cofins_situacao_tributaria='01',
    cofins_valor_base_calculo=Decimal('117.00'),
    cofins_aliquota_percentual=Decimal('3.00'),
    cofins_valor=Decimal('3.51'))

serializador = SerializacaoXML(_fonte_dados, homologacao=True)
xml = serializador.exportar(retorna_string=True).decode('utf-8')
certificado = "certificado_A1.pfx"
senha = 'sua_senha'
# assinatura
a1 = AssinaturaA1(certificado, senha)
xml = a1.assinar_nfe(xml)
# escreve
with open('teste.xml', 'wb') as arquivo:
    arquivo.write(xml)