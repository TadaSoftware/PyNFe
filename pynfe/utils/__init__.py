# *-* encoding: utf-8 *-*

import codecs
import os
from unicodedata import normalize
from signxml import XMLSigner
from typing import Literal
from decimal import Decimal

try:
    from lxml import etree  # noqa: F401
except ImportError:
    raise Exception("Falhou ao importar lxml/ElementTree")

try:
    from . import flags
except ImportError:
    raise Exception("Falhou ao importar flags")


# @memoize
def so_numeros(texto) -> str:
    """
    Retorna o texto informado mas somente os numeros

    :param texto: String ou Inteiro a ser analisada
    :return: String somente com números
    """
    return "".join(filter(str.isdigit, str(texto)))


# @memoize
def obter_pais_por_codigo(codigo):
    if codigo == "1058" or codigo == "" or codigo is None:
        return "Brasil"

    pais = carregar_arquivo_pais(codigo=codigo)
    pais = pais.get(codigo)
    if not pais:
        raise ValueError
    return pais


CAMINHO_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
CAMINHO_MUNICIPIOS = os.path.join(CAMINHO_DATA, "MunIBGE")
CARACTERS_ACENTUADOS = {
    ord("á"): "a",
    ord("â"): "a",
    ord("à"): "a",
    ord("ã"): "a",
    ord("é"): "e",
    ord("ê"): "e",
    ord("í"): "i",
    ord("ó"): "o",
    ord("õ"): "o",
    ord("ô"): "o",
    ord("ú"): "u",
    ord("ç"): "c",
    ord("'"): "",
}


# @memoize
def normalizar_municipio(municipio):
    if not isinstance(municipio, str):
        municipio = municipio.decode("utf-8")

    return municipio.lower().translate(CARACTERS_ACENTUADOS).upper()


# @memoize
def carregar_arquivo_municipios(uf, reverso=False):
    if isinstance(uf, str):
        try:
            uf = int(uf)
        except ValueError:
            uf = flags.CODIGOS_ESTADOS[uf.upper()]

    caminho_arquivo = os.path.join(CAMINHO_MUNICIPIOS, "MunIBGE-UF%s.txt" % uf)

    # Carrega o conteudo do arquivo
    fp = codecs.open(caminho_arquivo, "r", "utf-8-sig")
    linhas = list(fp.readlines())
    fp.close()

    municipios_dict = {}

    for linha in linhas:
        codigo, municipio = linha.split("\t")
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
    municipio_normalizado = normalizar_municipio(municipio)
    if municipio_normalizado not in municipios:
        raise ValueError("Município inválido %s" % municipio)
    return municipios[municipio_normalizado]


# @memoize
def obter_municipio_por_codigo(codigo, uf, normalizado=False):
    # TODO: fazer UF ser opcional
    municipios = carregar_arquivo_municipios(uf)
    municipio = municipios.get(codigo)
    if municipio is None:
        raise ValueError
    if normalizado:
        return normalizar_municipio(municipio)
    return municipio


# @memoize
def obter_municipio_e_codigo(dados, uf):
    """Retorna código e município
    municipio_ou_codigo - espera receber um dicionário no formato:
        {codigo: 121212, municipio: u'municipio'}
    """

    cod = dados.get("codigo", "")
    mun = normalizar_municipio(dados.get("municipio", ""))
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
    return root.tag.split("}")[-1]


def formatar_decimal(dec):
    if dec * 100 - int(dec * 100):
        return str(dec)
    else:
        return "%.2f" % dec


def obter_uf_por_codigo(codigo_uf):
    if isinstance(codigo_uf, str) and codigo_uf.isalpha():
        return codigo_uf

    estados = {v: k for k, v in flags.CODIGOS_ESTADOS.items()}
    return estados[codigo_uf]


def remover_acentos(txt):
    return normalize("NFKD", txt).encode("ASCII", "ignore").decode("ASCII")


def carregar_arquivo_pais(codigo):
    caminho_arquivo = os.path.join(CAMINHO_MUNICIPIOS, "PaisIBGE.txt")

    with open(caminho_arquivo, "r", encoding="utf-8-sig") as arquivo:
        linhas = arquivo.readlines()

    return {
        linha.split("\t", maxsplit=1)[0].strip(): linha.split("\t", maxsplit=1)[1].strip()
        for linha in linhas
    }


class CustomXMLSigner(XMLSigner):
    def __init__(self, method, signature_algorithm, digest_algorithm, c14n_algorithm):
        super().__init__(method, signature_algorithm, digest_algorithm, c14n_algorithm)

    def check_deprecated_methods(self):
        pass


def is_empty(value):
    """
    Verifica se um valor está vazio.

    Parameters:
    - value: O valor a ser verificado.

    Returns:
    - True se o valor estiver vazio, False caso contrário.
    """
    if value is None:
        return True
    elif isinstance(value, (int, float, Decimal)) and value == Decimal(0):
        # Verifica se o valor numérico é igual a zero.
        return True
    elif isinstance(value, str) and not value.strip():
        # Verifica se a string está vazia ou contém apenas espaços em branco.
        return True
    elif isinstance(value, (list, tuple, dict)) and not value:
        # Verifica se a lista, tupla ou dicionário está vazio.
        return True
    else:
        return False


def truncar_valor(float_number: float, decimal_places: int, suprimir_zeros: bool = False):
    multiplier = 10**decimal_places
    result = str(int(float_number * multiplier) / multiplier)
    if suprimir_zeros:
        result = result.rstrip("0").rstrip(".")
    return result


def arredondar_valor(value: float, decimal_places: int, suprimir_zeros: bool = False):
    f = f"%.{decimal_places}f"
    result = f % value
    if suprimir_zeros:
        result = result.rstrip("0").rstrip(".")
    return result


def ajustar_valor(
    value: float,
    decimal_places: int = 2,
    min_decimal_places: int = 2,
    tipo: Literal["ROUND", "TRUNC"] = "ROUND",
    decimal_separator: str = ".",
):
    value = 0 if value is None else value

    formated_value: str = "0"
    supress_zeros = min_decimal_places < decimal_places

    if tipo == "ROUND":
        formated_value = arredondar_valor(value, decimal_places, supress_zeros)
    else:
        formated_value = truncar_valor(value, decimal_places, supress_zeros)

    pi, sep, dec = list(formated_value.partition("."))

    # preenche com zeros a direita até a quantidade minima
    if min_decimal_places:
        dec = dec.ljust(min_decimal_places, "0")
    # se não tem decimais não haverá separator
    sep = decimal_separator if dec else ""

    return f"{pi}{sep}{dec}".replace(".", decimal_separator)
