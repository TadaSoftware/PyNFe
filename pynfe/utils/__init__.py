# *-* encoding: utf-8 *-*

import os
import codecs
import unicodedata

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

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import flags

# from geraldo.utils import memoize

# @memoize
def so_numeros(texto):
    """Retorna o texto informado mas somente os numeros"""
    return ''.join(filter(lambda c: ord(c) in range(48,58), texto))

# @memoize
def obter_pais_por_codigo(codigo):
    # TODO
    if codigo == '1058':
        return 'Brasil'

CAMINHO_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
CAMINHO_MUNICIPIOS = os.path.join(CAMINHO_DATA, 'MunIBGE')
CARACTERS_ACENTUADOS = {
    ord(u'á'): u'a',
    ord(u'â'): u'a',
    ord(u'à'): u'a',
    ord(u'ã'): u'a',
    ord(u'é'): u'e',
    ord(u'ê'): u'e',
    ord(u'í'): u'i',
    ord(u'ó'): u'o',
    ord(u'õ'): u'o',
    ord(u'ô'): u'o',
    ord(u'ú'): u'u',
    ord(u'ç'): u'c',
}

# @memoize
def normalizar_municipio(municipio):
    if not isinstance(municipio, unicode):  
        municipio = municipio.decode('utf-8')
    
    return municipio.lower().translate(CARACTERS_ACENTUADOS).upper() 

# @memoize
def carregar_arquivo_municipios(uf, reverso=False):
    if isinstance(uf, basestring):
        try:
            uf = int(uf)
        except ValueError:
            uf = flags.CODIGOS_ESTADOS[uf.upper()]

    caminho_arquivo = os.path.join(CAMINHO_MUNICIPIOS, 'MunIBGE-UF%s.txt' % uf)

    # Carrega o conteudo do arquivo
    fp = codecs.open(caminho_arquivo, "r", "utf-8-sig")
    linhas = list(fp.readlines())
    fp.close()
   
    municipios_dict = {}

    for linha in linhas: 
        codigo, municipio = linha.split('\t')
        codigo = codigo.strip()
        municipio = municipio.strip() 

        if not reverso:
            municipios_dict[codigo] = municipio
        else:
            municipios_dict[normalizar_municipio(municipio)] = codigo

    return municipios_dict

# @memoize
def obter_codigo_por_municipio(municipio, uf):
    # TODO: fazer UF ser opcional
    municipios = carregar_arquivo_municipios(uf, True)
    return municipios[normalizar_municipio(municipio)] 

# @memoize
def obter_municipio_por_codigo(codigo, uf, normalizado=False):
    # TODO: fazer UF ser opcional
    municipios = carregar_arquivo_municipios(uf)

    municipio = municipios[codigo]
    if normalizado:
        return normalizar_municipio(municipio)

    return municipio

# @memoize
def obter_municipio_e_codigo(municipio_ou_codigo, uf):
    try:
        cod_municipio = int(municipio_ou_codigo)
    except ValueError:
        cod_municipio = obter_codigo_por_municipio(municipio_ou_codigo, uf)

    municipio = obter_municipio_por_codigo(cod_municipio, uf, normalizado=True)

    return cod_municipio, municipio

# @memoize
def extrair_tag(root):
    return root.tag.split('}')[-1]

def formatar_decimal(dec):
    if dec*100 - int(dec*100):
        return str(dec)
    else:
        return "%.2f" % dec

def safe_str(str_):
    if not isinstance(str_, unicode):
        if isinstance(str_, str):
            str_ = str_.decode('utf8')
        else:
            str_ = unicode(str_)
    return unicodedata.normalize('NFKD', str_).encode('ascii', 'ignore')
