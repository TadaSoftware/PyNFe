# -*- coding: utf-8 -*-
try:
    set
except:
    from sets import Set as set

try:
  from lxml import etree
except ImportError:
  try:
    # Python 2.5 - cElementTree
    import xml.etree.cElementTree as etree
  except ImportError:
    try:
      # Python 2.5 - ElementTree
      import xml.etree.ElementTree as etree
    except ImportError:
      try:
        # Instalacao normal do cElementTree
        import cElementTree as etree
      except ImportError:
        try:
          # Instalacao normal do ElementTree
          import elementtree.ElementTree as etree
        except ImportError:
          raise Exception('Falhou ao importar lxml/ElementTree')

from pynfe.entidades import Emitente, Cliente, Produto, Transportadora, NotaFiscal
from pynfe.excecoes import NenhumObjetoEncontrado, MuitosObjetosEncontrados
from pynfe.utils import so_numeros, obter_municipio_por_codigo, obter_pais_por_codigo
from pynfe.utils.flags import CODIGOS_ESTADOS

class Serializacao(object):
    """Classe abstrata responsavel por fornecer as funcionalidades basicas para
    exportacao e importacao de Notas Fiscais eletronicas para formatos serializados
    de arquivos. Como XML, JSON, binario, etc.
    
    Nao deve ser instanciada diretamente!"""

    _fonte_dados = None
    _ambiente = 1
    _nome_aplicacao = 'PyNFe'

    def __new__(cls, *args, **kwargs):
        if cls == Serializacao:
            raise Exception('Esta classe nao pode ser instanciada diretamente!')
        else:
            return super(Serializacao, cls).__new__(cls, *args, **kwargs)

    def __init__(self, fonte_dados, homologacao=False):
        self._fonte_dados = fonte_dados
        self._ambiente = homologacao and 2 or 1

    def exportar(self, destino, **kwargs):
        """Gera o(s) arquivo(s) de exportacao a partir da Nofa Fiscal eletronica
        ou lista delas."""

        raise Exception('Metodo nao implementado')

    def importar(self, origem):
        """Fabrica que recebe o caminho ou objeto de origem e instancia os objetos
        da PyNFe"""

        raise Exception('Metodo nao implementado')

class SerializacaoXML(Serializacao):
    def exportar(self, destino, **kwargs):
        """Gera o(s) arquivo(s) de Nofa Fiscal eletronica no padrao oficial da SEFAZ
        e Receita Federal, para ser(em) enviado(s) para o webservice ou para ser(em)
        armazenado(s) em cache local."""

        # Carrega lista de Notas Fiscais
        notas_fiscais = self._fonte_dados.obter_lista(_classe=NotaFiscal, **kwargs)

        saida = []

        # Dados do emitente
        saida.append(self._serializar_emitente(self._obter_emitente_de_notas_fiscais(notas_fiscais)))

        # Certificado Digital? XXX

        # Clientes
        #saida.append(self._serializar_clientes(**kwargs))

        # Transportadoras
        #saida.append(self._serializar_transportadoras(**kwargs))

        # Produtos
        #saida.append(self._serializar_produtos(**kwargs))

        # Lote de Notas Fiscais
        #saida.append(self._serializar_notas_fiscais(**kwargs))

    def importar(self, origem):
        """Cria as instancias do PyNFe a partir de arquivos XML no formato padrao da
        SEFAZ e Receita Federal."""

        raise Exception('Metodo nao implementado')

    def _obter_emitente_de_notas_fiscais(self, notas_fiscais):
        lista = list(set([nf.emitente for nf in notas_fiscais if nf.emitente]))

        if len(lista) == 0:
            raise NenhumObjetoEncontrado('Nenhum objeto foi encontrado!')
        elif len(lista) > 1:
            raise MuitosObjetosEncontrados('Muitos objetos foram encontrados!')

        return lista[0]

    def _serializar_emitente(self, emitente, tag_raiz='emit', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados do emitente
        etree.SubElement(raiz, 'CNPJ').text = so_numeros(emitente.cnpj)
        etree.SubElement(raiz, 'xNome').text = emitente.razao_social
        etree.SubElement(raiz, 'xFant').text = emitente.nome_fantasia
        etree.SubElement(raiz, 'IE').text = emitente.inscricao_estadual

        # Endereço
        endereco = etree.SubElement(raiz, 'enderEmit')
        etree.SubElement(endereco, 'xLgr').text = emitente.endereco_logradouro
        etree.SubElement(endereco, 'nro').text = emitente.endereco_numero
        etree.SubElement(endereco, 'xCpl').text = emitente.endereco_complemento
        etree.SubElement(endereco, 'xBairro').text = emitente.endereco_bairro
        etree.SubElement(endereco, 'cMun').text = emitente.endereco_municipio
        etree.SubElement(endereco, 'xMun').text = obter_municipio_por_codigo(
                emitente.endereco_municipio, emitente.endereco_uf,
                )
        etree.SubElement(endereco, 'UF').text = emitente.endereco_uf
        etree.SubElement(endereco, 'CEP').text = so_numeros(emitente.endereco_cep)
        etree.SubElement(endereco, 'cPais').text = emitente.endereco_pais
        etree.SubElement(endereco, 'xPais').text = obter_pais_por_codigo(emitente.endereco_pais)
        etree.SubElement(endereco, 'fone').text = emitente.endereco_telefone

        if retorna_string:
            return etree.tostring(raiz, pretty_print=True)
        else:
            return raiz

    def _serializar_cliente(self, cliente, tag_raiz='dest', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados do cliente
        etree.SubElement(raiz, cliente.tipo_documento).text = so_numeros(cliente.numero_documento)
        etree.SubElement(raiz, 'xNome').text = cliente.razao_social
        etree.SubElement(raiz, 'IE').text = cliente.inscricao_estadual

        # Endereço
        endereco = etree.SubElement(raiz, 'enderDest')
        etree.SubElement(endereco, 'xLgr').text = cliente.endereco_logradouro
        etree.SubElement(endereco, 'nro').text = cliente.endereco_numero
        etree.SubElement(endereco, 'xCpl').text = cliente.endereco_complemento
        etree.SubElement(endereco, 'xBairro').text = cliente.endereco_bairro
        etree.SubElement(endereco, 'cMun').text = cliente.endereco_municipio
        etree.SubElement(endereco, 'xMun').text = obter_municipio_por_codigo(
                cliente.endereco_municipio, cliente.endereco_uf,
                )
        etree.SubElement(endereco, 'UF').text = cliente.endereco_uf
        etree.SubElement(endereco, 'CEP').text = so_numeros(cliente.endereco_cep)
        etree.SubElement(endereco, 'cPais').text = cliente.endereco_pais
        etree.SubElement(endereco, 'xPais').text = obter_pais_por_codigo(cliente.endereco_pais)
        etree.SubElement(endereco, 'fone').text = cliente.endereco_telefone

        if retorna_string:
            return etree.tostring(raiz, pretty_print=True)
        else:
            return raiz

    def _serializar_transportadora(self, transportadora, tag_raiz='transporta', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados da transportadora
        etree.SubElement(raiz, transportadora.tipo_documento).text = so_numeros(transportadora.numero_documento)
        etree.SubElement(raiz, 'xNome').text = transportadora.razao_social
        etree.SubElement(raiz, 'IE').text = transportadora.inscricao_estadual

        # Endereço
        etree.SubElement(raiz, 'xEnder').text = transportadora.endereco_logradouro
        etree.SubElement(raiz, 'cMun').text = transportadora.endereco_municipio
        etree.SubElement(raiz, 'xMun').text = obter_municipio_por_codigo(
                transportadora.endereco_municipio, transportadora.endereco_uf,
                )
        etree.SubElement(raiz, 'UF').text = transportadora.endereco_uf

        if retorna_string:
            return etree.tostring(raiz, pretty_print=True)
        else:
            return raiz

    def _serializar_produto(self, produto, tag_raiz='prod', retorna_string=True):
        # Provavelmente nao vai ser feito desta forma, e sim como serializacao do produto
        # na NF (NotaFiscalProduto)
        return ''

    def _serializar_notas_fiscal(self, nota_fiscal, tag_raiz='infNFe', retorna_string=True):
        raiz = etree.Element(tag_raiz, versao="2.00")

        # Dados da Nota Fiscal
        ide = etree.SubElement(raiz, 'ide')
        etree.SubElement(ide, 'cUF').text = CODIGOS_ESTADOS[nota_fiscal.uf]
        etree.SubElement(ide, 'cNF').text = nota_fiscal.codigo_numerico_aleatorio
        etree.SubElement(ide, 'natOp').text = nota_fiscal.natureza_operacao
        etree.SubElement(ide, 'indPag').text = str(nota_fiscal.forma_pagamento)
        etree.SubElement(ide, 'mod').text = str(nota_fiscal.modelo)
        etree.SubElement(ide, 'serie').text = nota_fiscal.serie
        etree.SubElement(ide, 'nNF').text = nota_fiscal.numero_nf
        etree.SubElement(ide, 'dEmi').text = nota_fiscal.data_emissao.strftime('%Y-%m-%d')
        etree.SubElement(ide, 'dSaiEnt').text = nota_fiscal.data_saida_entrada.strftime('%Y-%m-%d')
        etree.SubElement(ide, 'tpNF').text = str(nota_fiscal.tipo_documento)
        etree.SubElement(ide, 'cMunFG').text = nota_fiscal.municipio
        etree.SubElement(ide, 'tpImp').text = str(nota_fiscal.tipo_impressao_danfe)
        etree.SubElement(ide, 'tpEmis').text = str(nota_fiscal.forma_emissao)
        etree.SubElement(ide, 'cDV').text = nota_fiscal.dv_codigo_numerico_aleatorio
        etree.SubElement(ide, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(ide, 'finNFe').text = str(nota_fiscal.finalidade_emissao)
        etree.SubElement(ide, 'procEmi').text = str(nota_fiscal.processo_emissao)
        etree.SubElement(ide, 'verProc').text = '%s %s'%(self._nome_aplicacao,
                nota_fiscal.versao_processo_emissao)

        # Emitente
        raiz.append(self._serializar_emitente(nota_fiscal.emitente, retorna_string=False))

        # Destinatário
        raiz.append(self._serializar_cliente(nota_fiscal.cliente, retorna_string=False))

        # Transporte
        transp = etree.SubElement(raiz, 'transp')
        transp.append(self._serializar_transportadora(nota_fiscal.transporte_transportadora, retorna_string=False))

        # 'Id' da tag raiz
        # Ex.: NFe35080599999090910270550010000000011518005123
        raiz.attrib['Id'] = nota_fiscal.identificador_unico

        if retorna_string:
            return etree.tostring(raiz, pretty_print=True)
        else:
            return raiz

