#!/usr/bin/env python
# *-* encoding: utf8 *-*


from decimal import Decimal

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscal
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.processamento.comunicacao import ComunicacaoSefaz
from pynfe.processamento.serializacao import SerializacaoXML
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.utils.flags import CODIGO_BRASIL
import datetime

emitente = Emitente(
    razao_social='Spring Publicacoes Ltda',
    nome_fantasia='Spring Publicacoes',
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
nota_fiscal = NotaFiscal(
   emitente=emitente,
   cliente=cliente,
   uf='PR',
   # NAO INFORMAR SISTEMA PREENCHE SOZINHO codigo_numerico_aleatorio=None,
   natureza_operacao='VENDA', # venda, compra, transferência, devolução, importação, consignação, remessa (para fins de demonstração, de industrialização ou outra)
   forma_pagamento='0', # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
   modelo=55, # 55=NF-e; 65=NFC-e
   serie='1',
   numero_nf='100', # Número do Documento Fiscal. ?? numero orçamento ??
   data_emissao=datetime.datetime.now(),
   data_saida_entrada=datetime.datetime.now(),
   #hora_saida_entrada=datetime.time(03,12,00),
   tipo_documento=1, # 0=entrada; 1=saida
   municipio='4118402', # buscar no banco
   #municipio='3550308',
   tipo_impressao_danfe=1, # nfce 4 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal, Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
   forma_emissao='1', # 1=Emissão normal (não em contingência); (NAO EMITIR EM CONTINGENCIA)
   cliente_final=1, # 0=Normal;1=Consumidor final;
   indicador_destino=1,
   indicador_presencial=1,
   finalidade_emissao='1', # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
   processo_emissao='0', #0=Emissão de NF-e com aplicativo do contribuinte;
   transporte_modalidade_frete=1,
   informacoes_adicionais_interesse_fisco='NF-e emitida de acordo com os termos do Convenio ICMS 24/2011. Assinatura Numero 8061746',
   totais_tributos_aproximado=0,
)
nota_fiscal.adicionar_produto_servico(codigo='000328', # id do produto (000328 era o id no antigo sistemas de assinatura)
    descricao='Armacao para oculos', # nao utilizar caracteres especiais
    ncm='90031100', # categoria international do prod (sempre esse para assinaturas)
    cfop='5102',
    #ean='123',
    unidade_comercial='UN',
    quantidade_comercial=Decimal('12'), # 12 unidades (12 revistas)
    valor_unitario_comercial=Decimal('9.75'),
    valor_total_bruto=Decimal('117.00'),
    unidade_tributavel='UN',
    quantidade_tributavel=Decimal('12'),
    valor_unitario_tributavel=Decimal('9.75'),
    ind_total=1,
    numero_pedido='12345', # id da ordem
    numero_do_item='12345328', # id do item (pode ser o id do produto concatenado com o do pedido)
    icms_modalidade='102',
    icms_origem=0,
    icms_csosn='400',
    pis_modalidade='07',
    cofins_modalidade='07',
    # pis_tipo_calculo='01',
    # pis_valor_base_calculo=Decimal('117.00'),
    # pis_aliquota_percentual=Decimal('0.65'),
    # pis_valor=Decimal('0.76'),
    # cofins_situacao_tributaria='01',
    # cofins_valor_base_calculo=Decimal('117.00'),
    # cofins_aliquota_percentual=Decimal('3.00'),
    # cofins_valor=Decimal('3.51')
    )

serializador = SerializacaoXML(_fonte_dados, homologacao=True)
xml = serializador.exportar(retorna_string=True)

certificado = "/home/user/certificado.pfx"
senha = 'senha'
uf = 'pr'
homologacao = True

# assinatura
a1 = AssinaturaA1(certificado, senha)
xml = a1.assinar(xml)

con = ComunicacaoSefaz(uf, certificado, senha, homologacao)
envio = con.autorizacao(modelo='nfe', nota_fiscal=xml)

print (envio.text)