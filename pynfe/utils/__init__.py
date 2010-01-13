import os

import flags

from geraldo.utils import memoize

@memoize
def so_numeros(texto):
    """Retorna o texto informado mas somente os numeros"""
    return ''.join(filter(lambda c: ord(c) in range(48,58), texto))

@memoize
def obter_pais_por_codigo(codigo):
    # TODO
    if codigo == '1058':
        return 'Brasil'

ARQUIVOS_ESTADOS = {
    'RO': 'MunIBGE-UF11.txt',
    'AC': 'MunIBGE-UF12.txt',
    'AM': 'MunIBGE-UF13.txt',
    'RR': 'MunIBGE-UF14.txt',
    'PA': 'MunIBGE-UF15.txt',
    'AP': 'MunIBGE-UF16.txt',
    'TO': 'MunIBGE-UF17.txt',
    'MA': 'MunIBGE-UF21.txt',
    'PI': 'MunIBGE-UF22.txt',
    'CE': 'MunIBGE-UF23.txt',
    'RN': 'MunIBGE-UF24.txt',
    'PB': 'MunIBGE-UF25.txt',
    'PE': 'MunIBGE-UF26.txt',
    'AL': 'MunIBGE-UF27.txt',
    'SE': 'MunIBGE-UF28.txt',
    'BA': 'MunIBGE-UF29.txt',
    'MG': 'MunIBGE-UF31.txt',
    'ES': 'MunIBGE-UF32.txt',
    'RJ': 'MunIBGE-UF33.txt',
    'SP': 'MunIBGE-UF35.txt',
    'PR': 'MunIBGE-UF41.txt',
    'SC': 'MunIBGE-UF42.txt',
    'RS': 'MunIBGE-UF43.txt',
    'MS': 'MunIBGE-UF50.txt',
    'MT': 'MunIBGE-UF51.txt',
    'GO': 'MunIBGE-UF52.txt',
    'DF': 'MunIBGE-UF53.txt',
}

CAMINHO_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
CAMINHO_MUNICIPIOS = os.path.join(CAMINHO_DATA, 'MunIBGE')

@memoize
def carregar_arquivo_municipios(uf):
    caminho_arquivo = os.path.join(CAMINHO_MUNICIPIOS, ARQUIVOS_ESTADOS[uf.upper()])

    fp = file(caminho_arquivo)
    linhas = list(fp.readlines())
    fp.close()

    return dict([(linha[:7], linha[7:].strip()) for linha in linhas])

@memoize
def obter_municipio_por_codigo(codigo, uf):
    # TODO: fazer UF ser opcional
    municipios = carregar_arquivo_municipios(uf)

    return municipios[codigo]
    
