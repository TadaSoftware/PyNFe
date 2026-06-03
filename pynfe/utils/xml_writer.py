from lxml import etree
from decimal import Decimal
from . import ajustar_valor, is_empty
from typing import Literal, Any

__MIN_LEN_ERROR = 'Tamanho do campo {} é menor que o mímino permitido "{}"'
__MAX_LEN_ERROR = 'Tamanho do campo {} é maior que o mímino permitido "{}"'


def write_txt(root: etree.ElementTree, tag_name, value: str, required: bool, min_len=0, max_len=0):
    """
    :param root: XML root
    :param tag_name: Nome da TAG a ser escrita (str)
    :param value: Valor a ser escrito na TAG (str)
    :param min_len: comprimento minimo
    :param max-len: comprimento maximo
    :param required: Se `True` e esta vazio, escreve a TAG vazia, do contrario não precisa gerar a TAG
    """
    tag_value = str(value).strip()

    # retorna sem gerar nada se a TAG não é obrigatoria
    if is_empty(tag_value) and not required:
        return

    if len(tag_value) < min_len:
        raise Exception(__MIN_LEN_ERROR.format(len(tag_value), min_len))
    if max_len > 0 and len(tag_value) > max_len:
        raise Exception(__MAX_LEN_ERROR.format(len(tag_value), max_len))

    etree.SubElement(root, tag_name).text = tag_value


def write_float(
    root: etree.ElementTree,
    tag_name: str,
    value: Decimal,
    required: bool,
    decimal_places=2,
    min_decimals=0,
    iat: Literal["ROUND", "TRUNC"] = "ROUND",
):
    """
    :param root: XML root
    :param tag_name: Nome da TAG a ser escrita (str)
    :param value: Valor a ser escrito na TAG (str)
    :param decimal_places: casas decimais
    :param min_decimals: numero minimo de casas decimais
    :param required: Se `True` e esta vazio, escreve a TAG vazia, do contrario não precisa gerar a TAG (considera 0 como vazio)
    :param iat: indice de arredondamento/truncamento (default: ROUND)
    """

    # retorna sem gerar nada se a TAG não é obrigatoria
    if is_empty(Decimal(value or "0")):
        if not required:
            return
        raise Exception(f"{tag_name} - Valor requerido e não informado")

    tag_value = ajustar_valor(
        value=value.__float__(),
        decimal_places=decimal_places,
        min_decimal_places=min_decimals,
        tipo=iat,
    )

    etree.SubElement(root, tag_name).text = tag_value


def write_int(root: etree.ElementTree, tag_name: str, value: int, required: bool):
    """
    :param root: XML root
    :param tag_name: Nome da TAG a ser escrita (str)
    :param value: Valor a ser escrito na TAG (str)
    :param required: Se `True` e esta vazio, escreve a TAG vazia, do contrario não precisa gerar a TAG (considera 0 como vazio)
    :param zero_is_empty: se `True` e o valor for zero será tratado como vazio
    """

    # retorna sem gerar nada se a TAG não é obrigatoria
    if is_empty(value):
        if not required:
            return
        raise Exception(f"{tag_name} - Valor requerido e não informado")

    etree.SubElement(root, tag_name).text = int(value)


def write_tag(root: etree.ElementTree, tag_name: str, value: Any, required: bool):
    # retorna sem gerar nada se a TAG não é obrigatoria
    if is_empty(value):
        if not required:
            return
        raise Exception(f"{tag_name} - Valor requerido e não informado")

    etree.SubElement(root, tag_name).text = str(value)
