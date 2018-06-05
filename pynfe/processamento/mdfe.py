# -*- coding: utf-8 -*-
# Copyright (C) 2018 - TODAY Luis Felipe Mileo - KMEE INFORMATICA LTDA
# License AGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html

from __future__ import division, print_function, unicode_literals

import time

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
from pynfe.utils import etree, extrai_id_srtxml
from .comunicacao import ComunicacaoSefaz
from .resposta import analisar_retorno

from mdfelib.v3_00 import consStatServMDFe
from mdfelib.v3_00 import consSitMDFe
from mdfelib.v3_00 import consMDFeNaoEnc
from mdfelib.v3_00 import enviMDFe
from mdfelib.v3_00 import consReciMDFe

MDFE_SITUACAO_JA_ENVIADO = ('100', '101', '132')


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
    _edoc_situacao_ja_enviado = MDFE_SITUACAO_JA_ENVIADO
    _edoc_situacao_arquivo_recebido_com_sucesso = '103'
    _edoc_situacao_em_processamento = '105'
    _edoc_situacao_servico_em_operacao = '107'

    consulta_servico_ao_enviar = True
    maximo_tentativas_consulta_recibo = 5

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

    def processar_documento(self, edoc):

        if self.consulta_servico_ao_enviar:
            proc_servico = self.status_servico()
            yield proc_servico
            #
            # Se o serviço não estiver em operação
            #
            if not proc_servico.resposta.cStat == \
               self._edoc_situacao_servico_em_operacao:
                #
                # Interrompe todo o processo
                #
                return
        #
        # Verificar se os documentos já não foram emitados antes
        #
        chave = extrai_id_srtxml(edoc)
        if not chave:
            #
            # Interrompe todo o processo se o documento nao tem chave
            #
            return

        proc_consulta = self.consulta(chave)
        yield proc_consulta

        #
        # Se o documento já constar na SEFAZ (autorizada ou denegada)
        #
        if proc_consulta.resposta.cStat in self._edoc_situacao_ja_enviado:
            #
            # Interrompe todo o processo
            #
            return
        #
        # Documento nao foi enviado, entao vamos envia-lo
        #

        proc_envio = self.autorizacao(edoc)
        yield proc_envio

        #
        # Deu errado?
        #
        if proc_envio.resposta.cStat != \
                self._edoc_situacao_arquivo_recebido_com_sucesso:
            #
            # Interrompe o processo
            #
            return

        #
        # Aguarda o tempo do processamento antes da consulta
        #
        time.sleep(proc_envio.resposta.infRec.tMed * 1.3)

        #
        # Consulta o recibo do lote, para ver o que aconteceu
        #
        proc_recibo = self.consulta_recibo(proc_envio.resposta.infRec.nRec)

        #
        # Tenta receber o resultado do processamento do lote, caso ainda
        # esteja em processamento
        #
        tentativa = 0
        while (proc_recibo.resposta.cStat ==
               self._edoc_situacao_em_processamento and
               tentativa < self.maximo_tentativas_consulta_recibo):
            time.sleep(proc_envio.resposta.infRec.tMed * 1.5)
            tentativa += 1
            proc_recibo = self.consulta_recibo(
                proc_envio.resposta.infRec.nRec
            )
        yield proc_recibo
