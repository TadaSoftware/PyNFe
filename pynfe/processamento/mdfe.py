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


    def _post_soap(self, classe, ws_metodo, raiz_xml, str_xml=False):
        url, webservice, metodo = self._get_url_webservice_metodo(
            ws_metodo
        )
        if not str_xml:
            xml = self._construir_xml_soap(
                webservice,
                self._construir_etree_ds(raiz_xml)
            )
        else:
            etree_ds = self._construir_etree_ds(raiz_xml)
            etree_ds.append(etree.fromstring(str_xml))
            xml = self._construir_xml_soap(webservice, etree_ds)

        retorno = self._post(
            url, xml, soap_webservice_method=webservice + b'/' + metodo
        )
        return analisar_retorno(ws_metodo, retorno, classe)

    def status_servico(self):
        raiz = consStatServMDFe.TConsStatServ(
            versao=self._versao,
            tpAmb=str(self._ambiente),
            xServ='STATUS',
        )
        raiz.original_tagname_ = 'consStatServMDFe'
        return self._post_soap(
            classe=consStatServMDFe,
            ws_metodo=WS_MDFE_STATUS_SERVICO,
            raiz_xml=raiz
        )

    def consulta(self, chave):
        raiz = consSitMDFe.TConsSitMDFe(
            versao=self._versao,
            tpAmb=str(self._ambiente),
            xServ='CONSULTAR',
            chMDFe=chave,
        )
        raiz.original_tagname_ = 'consSitMDFe'
        return self._post_soap(
            classe=consSitMDFe,
            ws_metodo=WS_MDFE_CONSULTA,
            raiz_xml=raiz
        )

    def consulta_nao_encerrados(self, cnpj):
        raiz = consMDFeNaoEnc.TConsMDFeNaoEnc(
            versao=self._versao,
            tpAmb=str(self._ambiente),
            xServ='CONSULTAR NÃO ENCERRADOS',
            CNPJ=cnpj,
        )
        raiz.original_tagname_ = 'consMDFeNaoEnc'

        return self._post_soap(
            classe=consMDFeNaoEnc,
            ws_metodo=WS_MDFE_CONSULTA_NAO_ENCERRADOS,
            raiz_xml=raiz
        )

    def autorizacao(self, str_documento_assinado, id_lote='1'):
        raiz = enviMDFe.TEnviMDFe(
            versao=self._versao,
            idLote=id_lote
        )
        raiz.original_tagname_ = 'enviMDFe'
        return self._post_soap(
            classe=enviMDFe,
            ws_metodo=WS_MDFE_RECEPCAO,
            raiz_xml=raiz,
            str_xml=str_documento_assinado,
        )

    def consulta_recibo(self, numero):
        raiz = consReciMDFe.TConsReciMDFe(
            versao=self._versao,
            tpAmb=str(self._ambiente),
            nRec=numero,
        )
        raiz.original_tagname_ = 'consReciMDFe'
        return self._post_soap(
            classe=consReciMDFe,
            ws_metodo=WS_MDFE_RET_RECEPCAO,
            raiz_xml=raiz,
        )
