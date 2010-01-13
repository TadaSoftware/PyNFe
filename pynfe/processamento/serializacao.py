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

class Serializacao(object):
    """Classe abstrata responsavel por fornecer as funcionalidades basicas para
    exportacao e importacao de Notas Fiscais eletronicas para formatos serializados
    de arquivos. Como XML, JSON, binario, etc.
    
    Nao deve ser instanciada diretamente!"""

    _fonte_dados = None

    def __new__(cls, *args, **kwargs):
        if cls == Serializacao:
            raise Exception('Esta classe nao pode ser instanciada diretamente!')
        else:
            return cls(*args, **kwargs)

    def __init__(self, fonte_dados):
        self._fonte_dados = fonte_dados

    def exportar(self, **kwargs):
        """Gera o(s) arquivo(s) de exportacao a partir da Nofa Fiscal eletronica
        ou lista delas."""

        raise Exception('Metodo nao implementado')

    def importar(self, origem):
        """Fabrica que recebe o caminho ou objeto de origem e instancia os objetos
        da PyNFe"""

        raise Exception('Metodo nao implementado')

class SerializacaoXML(Serializacao):
    def exportar(self, **kwargs):
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
        saida.append(self._serializar_clientes(**kwargs))

        # Transportadoras
        saida.append(self._serializar_transportadoras(**kwargs))

        # Produtos
        saida.append(self._serializar_produtos(**kwargs))

        # Lote de Notas Fiscais
        saida.append(self._serializar_notas_fiscais(**kwargs))

        # FIXME
        return '\n'.join(saida)

    def importar(self, origem):
        """Cria as instancias do PyNFe a partir de arquivos XML no formato padrao da
        SEFAZ e Receita Federal."""

        raise Exception('Metodo nao implementado')

    def _obter_emitente_de_notas_fiscais(self, notas_fiscais):
        lista = set([nf.emitente for nf in notas_fiscais if nf.emitente])

        if len(lista) == 0:
            raise NenhumObjetoEncontrado('Nenhum objeto foi encontrado!')
        elif len(lista) > 1:
            raise MuitosObjetosEncontrados('Muitos objetos foram encontrados!')

        return lista[0]

    def _serializar_emitente(self, emitente):
        return ''

    def _serializar_clientes(self, objetos):
        return ''

    def _serializar_transportadoras(self, objetos):
        return ''

    def _serializar_produtos(self, objetos):
        return ''

    def _serializar_notas_fiscais(self, objetos):
        return ''

