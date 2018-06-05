# -*- coding: utf-8 -*-
# Copyright (C) 2018 - TODAY Luis Felipe Mileo - KMEE INFORMATICA LTDA
# License AGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html

from __future__ import division, print_function, unicode_literals

import re
from pynfe.utils import etree


class RetornoSoap(object):

    def __init__(self, webservice, retorno, resposta):
        self.webservice = webservice
        self.resposta = resposta
        self.retorno = retorno
        self.processo = False

    def analisar_processo(self, documento, entidade):

        if documento == 'MDFe' and self.resposta.protMDFe:
            self.processo = entidade(
                versao=self.resposta.versao,
                protMDFe=self.resposta.protMDFe,
            )
        if documento == 'MDFe' and self.resposta.procEventoMDFe:
            print('procEventoMDFe')
            # self.processo = entidade(
            #     versao=self.resposta.versao,
            #     protMDFe=self.resposta.protMDFe,
            # )
        return self


def analisar_retorno(webservice, retorno, classe_resposta):

    retorno.raise_for_status()

    match = re.search('<soap:Body>(.*?)</soap:Body>', retorno.text)

    if match:
        resultado = etree.tostring(etree.fromstring(match.group(1))[0])
        classe_resposta.Validate_simpletypes_ = False
        resposta = classe_resposta.parseString(resultado.encode('utf-8'))

        return RetornoSoap(webservice, retorno, resposta)

