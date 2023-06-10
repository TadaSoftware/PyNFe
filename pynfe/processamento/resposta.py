# -*- coding: utf-8 -*-
import re
from pynfe.utils import etree


class RetornoSoap(object):
    def __init__(self, webservice, retorno, resposta):
        self.webservice = webservice
        self.resposta = resposta
        self.retorno = retorno


def analisar_retorno(webservice, retorno, classe_resposta):
    # retorno.raise_for_status()
    # print(retorno.text)

    match = re.search("<soap:Body>(.*?)</soap:Body>", retorno.text)

    if match:
        resultado = etree.tostring(etree.fromstring(match.group(1))[0])
        # classe_resposta.Validate_simpletypes_ = False
        # resposta = classe_resposta.parseString(resultado)
        resposta = resultado
        # resposta = retorno.text

    return RetornoSoap(webservice, retorno, resposta)
