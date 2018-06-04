# *-* encoding: utf-8 *-*

import os
import codecs
from unicodedata import normalize
import re

try:
    from lxml import etree
except ImportError:
    raise Exception('Falhou ao importar lxml/ElementTree')

from io import StringIO

try:
    from . import flags
except ImportError:
    raise Exception('Falhou ao importar flags')


# @memoize
def so_numeros(texto):
    """Retorna o texto informado mas somente os numeros"""
    return ''.join(filter(lambda c: ord(c) in range(48, 58), texto))


# @memoize
def obter_pais_por_codigo(codigo):
    # TODO
    if codigo == '1058':
        return 'Brasil'

CAMINHO_DATA = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'data')
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
    if not isinstance(municipio, str):
        municipio = municipio.decode('utf-8')

    return municipio.lower().translate(CARACTERS_ACENTUADOS).upper()


# @memoize
def carregar_arquivo_municipios(uf, reverso=False):
    if isinstance(uf, str):
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
    municipio = municipios.get(unicode(codigo))
    if municipio is None:
        raise ValueError
    if normalizado:
        return normalizar_municipio(municipio)
    return municipio


# @memoize
def obter_municipio_e_codigo(dados, uf):
    '''Retorna código e município
    municipio_ou_codigo - espera receber um dicionário no formato:
        {codigo: 121212, municipio: u'municipio'}
    '''

    cod = dados.get('codigo', '')
    mun = normalizar_municipio(dados.get('municipio', ''))
    try:
        cod = int(cod)
    except ValueError:
        cod = obter_codigo_por_municipio(mun, uf)
    # TODO: se ainda com este teste apresentar erros de nessa seção
    # desenvolver um retorno que informe ao cliente quais nfes estão com erro
    # e não explodir esse a geração das outras nfes
    municipio = obter_municipio_por_codigo(cod, uf, normalizado=True)
    return cod, municipio

# @memoize
def extrair_tag(root):
    return root.tag.split('}')[-1]


def formatar_decimal(dec):
    if dec * 100 - int(dec * 100):
        return str(dec)
    else:
        return "%.2f" % dec


def obter_uf_por_codigo(codigo_uf):
    if isinstance(codigo_uf, basestring) and codigo_uf.isalpha():
        return codigo_uf

    estados = {v: k for k, v in flags.CODIGOS_ESTADOS.items()}
    return estados[unicode(codigo_uf)]


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')


def extrai_id_srtxml(edoc):
    result = ''
    match = re.search('Id=[^0-9]+(\d+)"', edoc)
    if match:
        result = match.group(1)
    return result
