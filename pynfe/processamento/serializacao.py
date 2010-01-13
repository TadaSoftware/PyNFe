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

class Serializacao(object):
    """Classe abstrata responsavel por fornecer as funcionalidades basicas para
    exportacao e importacao de Notas Fiscais eletronicas para formatos serializados
    de arquivos. Como XML, JSON, binario, etc.
    
    Nao deve ser instanciada diretamente!"""

    lista_de_nfs = None

    def __new__(cls, *args, **kwargs):
        if cls == Serializacao:
            raise Exception('Esta classe nao pode ser instanciada diretamente!')
        else:
            return cls(*args, **kwargs)

    def __init__(self, nf_ou_lista):
        self.lista_de_nfs = isinstance(nf_ou_lista, list) and nf_ou_lista or [nf_ou_lista]

    def exportar(self, destino):
        """Gera o(s) arquivo(s) de exportacao a partir da Nofa Fiscal eletronica
        ou lista delas."""

        raise Exception('Metodo nao implementado')

    def importar(self, origem):
        """Fabrica que recebe o caminho ou objeto de origem e instancia os objetos
        da PyNFe"""

        raise Exception('Metodo nao implementado')

class SerializacaoXML(Serializacao):
    def exportar(self, objetos, destino):
        """Gera o(s) arquivo(s) de Nofa Fiscal eletronica no padrao oficial da SEFAZ
        e Receita Federal, para ser(em) enviado(s) para o webservice ou para ser(em)
        armazenado(s) em cache local."""

        saida = []

        # Dados do emitente
        saida.append(self._serializar_emitente(objetos))

        # Certificado Digital? XXX

        # Clientes
        saida.append(self._serializar_clientes(objetos))

        # Transportadoras
        saida.append(self._serializar_transportadoras(objetos))

        # Produtos
        saida.append(self._serializar_produtos(objetos))

        # Lote de Notas Fiscais
        saida.append(self._serializar_notas_fiscais(objetos))

        # FIXME
        return '\n'.join(saida)

    def importar(self, objetos, origem):
        """Cria as instancias do PyNFe a partir de arquivos XML no formato padrao da
        SEFAZ e Receita Federal."""

        raise Exception('Metodo nao implementado')

    def _serializar_emitente(self, objetos):
        return ''

    def _serializar_clientes(self, objetos):
        return ''

    def _serializar_transportadoras(self, objetos):
        return ''

    def _serializar_produtos(self, objetos):
        return ''

    def _serializar_notas_fiscais(self, objetos):
        return ''

