# -*- coding: utf-8 -*-
# Copyright (C) 2018 - TODAY Luis Felipe Mileo - KMEE INFORMATICA LTDA
# License AGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html

import re
from pynfe.utils import etree


def analisar_retorno(retorno, classe_resposta):

    retorno.raise_for_status()

    match = re.search('<soap:Body>(.*?)</soap:Body>', retorno.text)

    if match:
        resultado = etree.tostring(etree.fromstring(match.group(1))[0])
        classe_resposta.Validate_simpletypes_ = False
        retorno = classe_resposta.parseString(resultado.encode('utf-8'))

    return retorno
