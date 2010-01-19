# -*- coding: utf-8 -*-

from httplib import HTTPSConnection, HTTPResponse

from pynfe.utils import etree, StringIO
from pynfe.utils.flags import NAMESPACE_NFE, NAMESPACE_SOAP, VERSAO_PADRAO

class Comunicacao(object):
    u"""Classe abstrata responsavel por definir os metodos e logica das classes
    de comunicação com os webservices da NF-e."""

    servidor = None
    certificado = None
    certificado_senha = None

    def __init__(self, servidor, certificado, certificado_senha):
        self.servidor = servidor
        self.certificado = certificado
        self.certificado_senha = certificado_senha

class ComunicacaoSefaz(Comunicacao):
    u"""Classe de comunicação que segue o padrão definido para as SEFAZ dos Estados."""

    _versao = VERSAO_PADRAO
    
    def transmitir(self, nota_fiscal):
        pass

    def cancelar(self, nota_fiscal):
        pass

    def situacao_nfe(self, nota_fiscal):
        pass

    def status_servico(self):
        post = '/nfeweb/services/nfestatusservico.asmx'

        # Monta XML do corpo da requisição # FIXME
        raiz = etree.Element('teste')
        dados = etree.tostring(raiz)

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap(
                metodo='CadConsultaCadastro',
                tag_metodo='consultaCadastro',
                cabecalho=self._cabecalho_soap(),
                dados=dados,
                )

        # Chama método que efetua a requisição POST no servidor SOAP
        retorno = self._post(post, xml, self._post_header())

        # Transforma o retorno em etree
        try:
            retorno = etree.parse(StringIO(retorno))
            return retorno
        except TypeError:
            pass

    def consultar_cadastro(self, instancia):
        #post = '/nfeweb/services/cadconsultacadastro.asmx'
        post = '/nfeweb/services/nfeconsulta.asmx'

    def inutilizar_faixa_numeracao(self, faixa):
        pass

    def _cabecalho_soap(self):
        u"""Monta o XML do cabeçalho da requisição SOAP"""

        raiz = etree.Element('cabecMsg', xmlns=NAMESPACE_NFE, versao="1.02")
        etree.SubElement(raiz, 'versaoDados').text = self._versao

        return etree.tostring(raiz, encoding='utf-8', xml_declaration=True)

    def _construir_xml_soap(self, metodo, tag_metodo, cabecalho, dados):
        u"""Mota o XML para o envio via SOAP"""

        raiz = etree.Element('{%s}Envelope'%NAMESPACE_SOAP, nsmap={'soap': NAMESPACE_SOAP})

        body = etree.SubElement(raiz, '{%s}Body'%NAMESPACE_SOAP)
        met = etree.SubElement(
                body, tag_metodo, xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/%s"%metodo,
                )

        etree.SubElement(met, 'nfeCabecMsg').text = cabecalho
        etree.SubElement(met, 'nfeDadosMsg').text = dados

        return etree.tostring(raiz, encoding='utf-8', xml_declaration=True)

    def _post_header(self):
        u"""Retorna um dicionário com os atributos para o cabeçalho da requisição HTTP"""
        return {
            u'content-type': u'application/soap+xml; charset=utf-8',
            u'Accept': u'application/soap+xml; charset=utf-8',
            }

    def _post(self, post, xml, header):
        # Separa arquivos de certificado para chave e certificado (sozinho)
        caminho_chave, caminho_cert = self.certificado.separar_arquivo(senha=self.certificado_senha)

        # Abre a conexão HTTPS
        con = HTTPSConnection(self.servidor, key_file=caminho_chave, cert_file=caminho_cert)

        try:
            #con.set_debuglevel(100)
    
            con.request(u'POST', post, xml, header)

            resp = con.getresponse()
        
            # Tudo certo!
            if resp.status == 200:
                return resp.read()
        finally:
            con.close()

