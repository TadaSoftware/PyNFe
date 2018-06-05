# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from pynfe.utils import etree
from pynfe.utils.flags import (
    NAMESPACE_XSI,
    NAMESPACE_BETHA,
)
from pynfe.utils.webservices import NFSE
from pynfe.entidades.certificado import CertificadoA1
from .comunicacao import Comunicacao


class ComunicacaoNfse(Comunicacao):
    """ Classe de comunicação que segue o padrão definido para as SEFAZ dos Municípios. """

    _versao = ''
    _namespace = ''

    def __init__(self, certificado, certificado_senha, autorizador, homologacao=False):
        self.certificado = certificado
        self.certificado_senha = certificado_senha
        self._ambiente = 2 if homologacao else 1
        self.autorizador = autorizador.upper()
        if self.autorizador == 'GINFES':
            self._namespace = 'http://www.ginfes.com.br/cabecalho_v03.xsd'
            self._versao = '3'
        elif self.autorizador == 'BETHA':
            self._namespace = NAMESPACE_BETHA
            self._versao = '2.02'
        else:
            raise Exception('Autorizador não encontrado!')

    def autorizacao(self, nota):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'BETHA':
            # xml
            xml = etree.tostring(nota, encoding='unicode', pretty_print=False)
            # comunica via wsdl
            return self._post(url, xml, 'gerar')
        else:
            raise Exception('Este método só esta implementado no autorizador betha.')

    def enviar_lote(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'GINFES':
            # xml
            xml = '<?xml version="1.0" encoding="UTF-8"?>' + xml
            # comunica via wsdl
            return self._post_https(url, xml, 'enviar_lote')
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def consultar(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'GINFES':
            # xml
            xml = '<?xml version="1.0" encoding="UTF-8"?>' + xml
            # comunica via wsdl
            return self._post_https(url, xml, 'consulta')
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def consultar_rps(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'BETHA':
            # comunica via wsdl
            return self._post(url, xml, 'consultaRps')
        elif self.autorizador == 'GINFES':
            return self._post_https(url, xml, 'consultaRps')
        # TODO outros autorizadres
        else:
            raise Exception('Autorizador não encontrado!')

    def consultar_faixa(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'BETHA':
            # comunica via wsdl
            return self._post(url, xml, 'consultaFaixa')
        else:
            raise Exception('Este método só esta implementado no autorizador betha.')

    def consultar_lote(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'GINFES':
            # xml
            xml = '<?xml version="1.0" encoding="UTF-8"?>' + xml
            # comunica via wsdl
            return self._post_https(url, xml, 'consulta_lote')
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def consultar_situacao_lote(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'GINFES':
            # comunica via wsdl
            return self._post_https(url, xml, 'consulta_situacao_lote')
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def cancelar(self, xml):
        # url do serviço
        url = self._get_url()
        # Betha
        if self.autorizador == 'BETHA':
            # comunica via wsdl
            return self._post(url, xml, 'cancelar')
        # Ginfes
        elif self.autorizador == 'GINFES':
            # comunica via wsdl com certificado
            return self._post_https(url, xml, 'cancelar')
        # TODO outros autorizadres
        else:
            raise Exception('Autorizador não encontrado!')

    def _cabecalho(self, retorna_string=True):
        """ Monta o XML do cabeçalho da requisição wsdl
            Namespaces padrão homologação (Ginfes) """

        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
        # cabecalho = '<ns2:cabecalho versao="3" xmlns:ns2="http://www.ginfes.com.br/cabecalho_v03.xsd"
        # xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><versaoDados>3</versaoDados></ns2:cabecalho>'
        # cabecalho
        raiz = etree.Element('{%s}cabecalho'%self._namespace, nsmap={'ns2':self._namespace, 'xsi':NAMESPACE_XSI}, versao=self._versao)
        etree.SubElement(raiz, 'versaoDados').text = self._versao

        if retorna_string:
            cabecalho = etree.tostring(raiz, encoding='unicode', pretty_print=False).replace('\n','')
            cabecalho = xml_declaration + cabecalho
            return cabecalho
        else:
            return raiz

    def _cabecalho2(self, retorna_string=True):
        """ Monta o XML do cabeçalho da requisição wsdl
            Namespaces que funcionaram em produção (Ginfes)"""

        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'

        # cabecalho
        raiz = etree.Element('cabecalho', xmlns=self._namespace, versao=self._versao)
        etree.SubElement(raiz, 'versaoDados').text = self._versao

        if retorna_string:
            cabecalho = etree.tostring(raiz, encoding='unicode', pretty_print=False).replace('\n', '')
            cabecalho = xml_declaration + cabecalho
            return cabecalho
        else:
            return raiz

    def _cabecalho_ginfes(self):
        """ Retorna o XML do cabeçalho gerado pelo xsd"""
        from pynfe.processamento.autorizador_nfse import SerializacaoGinfes
        return SerializacaoGinfes().cabecalho()

    def _get_url(self):
        """ Retorna a url para comunicação com o webservice """
        if self._ambiente == 1:
            ambiente = 'HTTPS'
        else:
            ambiente = 'HOMOLOGACAO'
        if self.autorizador in NFSE:
            self.url = NFSE[self.autorizador][ambiente]
        else:
            raise Exception('Autorizador nao encontrado!')
        return self.url

    def _post(self, url, xml, metodo):
        """ Comunicação wsdl (http) sem certificado digital """
        # cabecalho
        cabecalho = self._cabecalho()
        # comunicacao wsdl
        try:
            from suds.client import Client
            cliente = Client(url)
            # gerar nfse
            if metodo == 'gerar':
                return cliente.service.GerarNfse(cabecalho, xml)
            elif metodo == 'consultaRps':
                return cliente.service.ConsultarNfsePorRps(cabecalho, xml)
            elif metodo == 'consultaFaixa':
                return cliente.service.ConsultarNfseFaixa(cabecalho, xml)
            elif metodo == 'cancelar':
                return cliente.service.CancelarNfse(cabecalho, xml)
            # TODO outros metodos
            else:
                raise Exception('Método não implementado no autorizador.')
        except Exception as e:
            raise e

    def _post_https(self, url, xml, metodo):
        """ Comunicação wsdl (https) utilizando certificado do usuário """
        # cabecalho
        cabecalho = self._cabecalho()
        # comunicacao wsdl
        try:
            from suds.client import Client
            from pynfe.utils.https_nfse import HttpAuthenticated

            certificadoA1 = CertificadoA1(self.certificado)
            chave, cert = certificadoA1.separar_arquivo(self.certificado_senha, caminho=True)

            cliente = Client(url, transport = HttpAuthenticated(key=chave, cert=cert, endereco=url))

            # gerar nfse
            if metodo == 'gerar':
                return cliente.service.GerarNfse(cabecalho, xml)
            elif metodo == 'enviar_lote':
                return cliente.service.RecepcionarLoteRpsV3(cabecalho, xml)
            elif metodo == 'consulta':
                return cliente.service.ConsultarNfseV3(cabecalho, xml)
            elif metodo == 'consulta_lote':
                return cliente.service.ConsultarLoteRpsV3(cabecalho, xml)
            elif metodo == 'consulta_situacao_lote':
                return cliente.service.ConsultarSituacaoLoteRpsV3(cabecalho, xml)
            elif metodo == 'consultaRps':
                return cliente.service.ConsultarNfsePorRpsV3(cabecalho, xml)
            elif metodo == 'consultaFaixa':
                return cliente.service.ConsultarNfseFaixa(cabecalho, xml)
            elif metodo == 'cancelar':
                # versão 2
                return cliente.service.CancelarNfse(xml)
                # versão 3
                # return cliente.service.CancelarNfseV3(cabecalho, xml)
            # TODO outros metodos
            else:
                raise Exception('Método não implementado no autorizador.')
        except Exception as e:
            raise e
