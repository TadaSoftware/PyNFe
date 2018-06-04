# -*- coding: utf-8 -*-
# Copyright (C) 2018 - TODAY Luis Felipe Mileo - KMEE INFORMATICA LTDA
# License AGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html

from __future__ import division, print_function, unicode_literals


from pynfe.utils.flags import (
    NAMESPACE_MDFE,
    MODELO_MDFE,
    NAMESPACE_MDFE_METODO,
    NAMESPACE_SOAP,
    NAMESPACE_XSI,
    NAMESPACE_XSD,
)
from pynfe.utils.webservices import (
    MDFE_WS_URL,
    MDFE_WS_METODO,
    WS_MDFE_CONSULTA,
    WS_MDFE_STATUS_SERVICO,
    WS_MDFE_CONSULTA_NAO_ENCERRADOS,
    WS_MDFE_RECEPCAO,
    WS_MDFE_RET_RECEPCAO,
    WS_MDFE_RECEPCAO_EVENTO,
)
from pynfe.utils import etree
from .comunicacao import ComunicacaoSefaz
from .resposta import analisar_retorno

from mdfelib.v3_00 import consStatServMDFe
from mdfelib.v3_00 import consSitMDFe
from mdfelib.v3_00 import consMDFeNaoEnc
from mdfelib.v3_00 import enviMDFe
from mdfelib.v3_00 import consReciMDFe


class ComunicacaoMDFE(ComunicacaoSefaz):

    _modelo = MODELO_MDFE
    _namespace = NAMESPACE_MDFE
    _versao = '3.00'
    _ws_url = MDFE_WS_URL
    _ws_metodo = MDFE_WS_METODO
    _header = 'mdfeCabecMsg'
    _envio_mensagem = 'mdfeDadosMsg'
    _retorno_mensagem = 'mdfeRecepcaoResult'
    _namespace_metodo = NAMESPACE_MDFE_METODO

    _accept = True
    _soap_action = False
    _namespace_soap = NAMESPACE_SOAP
    _namespace_xsi = NAMESPACE_XSI
    _namespace_xsd = NAMESPACE_XSD
    _soap_version = 'soap12'

    def status_servico(self):
        url, webservice, metodo = self._get_url_webservice_metodo(
            WS_MDFE_STATUS_SERVICO
        )

        raiz = consStatServMDFe.TConsStatServ(
            versao=self._versao,
            tpAmb=str(self._ambiente),
            xServ='STATUS',
        )
        raiz.original_tagname_ = 'consStatServMDFe'

        xml = self._construir_xml_soap(
            webservice,
            self._construir_etree_ds(raiz)
        )

        retorno = self._post(
            url, xml, soap_webservice_method=webservice + b'/' + metodo
        )
        return analisar_retorno(retorno, consStatServMDFe)

    def consulta(self, chave):
        url, webservice, metodo = self._get_url_webservice_metodo(
            WS_MDFE_CONSULTA
        )
        raiz = consSitMDFe.TConsSitMDFe(
            versao=self._versao,
            tpAmb=str(self._ambiente),
            xServ='CONSULTAR',
            chMDFe=chave,
        )
        raiz.original_tagname_ = 'consSitMDFe'
        xml = self._construir_xml_soap(
            webservice,
            self._construir_etree_ds(raiz)
        )
        retorno = self._post(
            url, xml, soap_webservice_method=webservice + b'/' + metodo
        )
        return analisar_retorno(retorno, consSitMDFe)

    def consulta_nao_encerrados(self, cnpj):
        url, webservice, metodo = self._get_url_webservice_metodo(
            WS_MDFE_CONSULTA_NAO_ENCERRADOS
        )
        raiz = consMDFeNaoEnc.TConsMDFeNaoEnc(
            versao=self._versao,
            tpAmb=str(self._ambiente),
            xServ='CONSULTAR NÃO ENCERRADOS',
            CNPJ=cnpj,
        )
        raiz.original_tagname_ = 'consMDFeNaoEnc'
        xml = self._construir_xml_soap(
            webservice,
            self._construir_etree_ds(raiz)
        )
        retorno = self._post(
            url, xml, soap_webservice_method=webservice + b'/' + metodo
        )
        return analisar_retorno(retorno, consMDFeNaoEnc)

    def autorizacao(self, str_documento_assinado, id_lote='1'):
        url, webservice, metodo = self._get_url_webservice_metodo(
            WS_MDFE_RECEPCAO
        )

        raiz = enviMDFe.TEnviMDFe(versao=self._versao, idLote=id_lote)
        raiz.original_tagname_ = 'enviMDFe'

        etree_ds = self._construir_etree_ds(raiz)
        etree_ds.append(etree.fromstring(str_documento_assinado))

        xml = self._construir_xml_soap(webservice, etree_ds)

        retorno = self._post(
            url, xml, soap_webservice_method=webservice + b'/' + metodo
        )
        return analisar_retorno(retorno, enviMDFe)

    def consulta_recibo(self, numero):
        url, webservice, metodo = self._get_url_webservice_metodo(
            WS_MDFE_RET_RECEPCAO
        )

        raiz = consReciMDFe.TConsReciMDFe(
            versao=self._versao,
            tpAmb=str(self._ambiente),
            nRec=numero,
        )
        raiz.original_tagname_ = 'consReciMDFe'
        xml = self._construir_xml_soap(
            webservice,
            self._construir_etree_ds(raiz)
        )
        retorno = self._post(
            url, xml, soap_webservice_method=webservice + b'/' + metodo
        )
        return analisar_retorno(retorno, consReciMDFe)

