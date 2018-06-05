# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import re
import requests
from pynfe.utils import etree, StringIO
from pynfe.utils.flags import (
    NAMESPACE_XSD,
    NAMESPACE_XSI,
    NAMESPACE_SOAP,
    CODIGOS_ESTADOS,
)
from pynfe.entidades.certificado import CertificadoA1
from .assinatura import AssinaturaA1


class Comunicacao(object):
    """
    Classe abstrata responsavel por definir os metodos e logica das classes
    de comunicação com os webservices.
    """

    _ambiente = 1   # 1 = Produção, 2 = Homologação
    uf = None
    certificado = None
    certificado_senha = None
    url = None
    _versao = False
    _assinatura = AssinaturaA1
    _namespace = False
    _header = False
    _envio_mensagem = False
    _namespace_metodo = False
    _accept = False
    _soap_action = False
    _ws_url = False
    _namespace_soap = NAMESPACE_SOAP
    _namespace_xsi = NAMESPACE_XSI
    _namespace_xsd = NAMESPACE_XSD
    _soap_version = 'soap'

    def __init__(self, uf, certificado, certificado_senha, homologacao=False):
        self.uf = uf
        self.certificado = certificado
        self.certificado_senha = certificado_senha
        self._ambiente = 2 if homologacao else 1

    def _construir_xml_soap(self, metodo, dados):
        """Mota o XML para o envio via SOAP"""

        raiz = etree.Element(
            '{%s}Envelope' % self._namespace_soap,
            nsmap={
                'xsi': self._namespace_xsi,
                'xsd': self._namespace_xsd,
                self._soap_version: self._namespace_soap,
            })

        if self._header:
            cabecalho = self._cabecalho_soap(metodo)
            c = etree.SubElement(raiz, '{%s}Header' % self._namespace_soap)
            c.append(cabecalho)

        body = etree.SubElement(raiz, '{%s}Body' % self._namespace_soap)

        a = etree.SubElement(
            body,
            self._envio_mensagem,
            xmlns=self._namespace_metodo+metodo
        )
        a.append(dados)
        return raiz

    def _construir_etree_ds(self, ds):
        output = StringIO()
        ds.export(
            output,
            0,
            pretty_print=False,
            namespacedef_='xmlns="' + self._namespace + '"'
        )
        contents = output.getvalue()
        output.close()
        return etree.fromstring(contents)

    def _post_header(self, soap_webservice_method=False):
        """Retorna um dicionário com os atributos para o cabeçalho da requisição HTTP"""
        header = {
            b'content-type': b'text/xml; charset=utf-8;',
        }

        # PE é a únca UF que exige SOAPAction no header
        if soap_webservice_method:
            header[b'SOAPAction'] = \
                (self._namespace_metodo + soap_webservice_method).encode('utf-8')

        if self._accept:
            header[b'Accept'] = b'application/soap+xml; charset=utf-8;'

        return header

    def _post(self, url, xml, soap_webservice_method=False):
        certificado_a1 = CertificadoA1(self.certificado)
        chave, cert = certificado_a1.separar_arquivo(self.certificado_senha, caminho=True)
        chave_cert = (cert, chave)
        # Abre a conexão HTTPS
        try:
            xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'

            # limpa xml com caracteres bugados para infNFeSupl em NFC-e
            xml = re.sub(
                '<qrCode>(.*?)</qrCode>',
                lambda x: x.group(0).replace('&lt;', '<').replace('&gt;', '>').replace('amp;', ''),
                etree.tostring(xml, encoding='unicode').replace('\n', '')
            )
            xml = xml_declaration + xml
            # Faz o request com o servidor
            result = requests.post(
                url.encode('utf-8'),
                xml.encode('utf-8'),
                headers=self._post_header(soap_webservice_method),
                cert=chave_cert,
                verify=False
            )
            result.encoding = 'utf-8'
            return result
        except requests.exceptions.RequestException as e:
            raise e
        finally:
            certificado_a1.excluir()
