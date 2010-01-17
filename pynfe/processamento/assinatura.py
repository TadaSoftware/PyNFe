# -*- coding: utf-8 -*-

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
  from lxml import etree
except ImportError:
  try:
    # Python 2.5 - cElementTree
    import xml.etree.cElementTree as etree
  except ImportError:
    try:
      # Python 2.5 - ElementTree
      import xml.etree.ElementTree as etree
    except ImportError:
      try:
        # Instalacao normal do cElementTree
        import cElementTree as etree
      except ImportError:
        try:
          # Instalacao normal do ElementTree
          import elementtree.ElementTree as etree
        except ImportError:
          raise Exception('Falhou ao importar lxml/ElementTree')

import xmlsec, libxml2 # FIXME: verificar ambiguidade de dependencias: lxml e libxml2

from geraldo.utils import memoize

NAMESPACE_NFE = u'http://www.portalfiscal.inf.br/nfe'
NAMESPACE_SIG = u'http://www.w3.org/2000/09/xmldsig#'

class Assinatura(object):
    """Classe abstrata responsavel por definir os metodos e logica das classes
    de assinatura digital."""

    certificado = None
    senha = None

    def __init__(self, certificado, senha):
        self.certificado = certificado
        self.senha = senha

    def assinar_arquivo(self, caminho_arquivo):
        """Efetua a assinatura dos arquivos XML informados"""
        pass

    def assinar_xml(self, xml):
        """Efetua a assinatura numa string contendo XML valido."""
        pass

    def assinar_etree(self, raiz):
        u"""Efetua a assinatura numa instancia da biblioteca lxml.etree.
        
        Este metodo de assinatura será utilizado internamente pelos demais,
        sendo que eles convertem para uma instancia lxml.etree para somente
        depois efetivar a assinatura.
        
        TODO: Verificar o funcionamento da PyXMLSec antes de efetivar isso."""
        pass

    def assinar_objetos(self, objetos):
        """Efetua a assinatura em instancias do PyNFe"""
        pass

    def verificar_arquivo(self, caminho_arquivo):
        pass

    def verificar_xml(self, xml):
        pass

    def verificar_etree(self, raiz):
        pass

    def verificar_objetos(self, objetos):
        pass


@memoize
def extrair_tag(root):
    return root.tag.split('}')[-1]

class AssinaturaA1(Assinatura):
    """Classe abstrata responsavel por efetuar a assinatura do certificado
    digital no XML informado."""
    
    def assinar_arquivo(self, caminho_arquivo):
        # Carrega o XML do arquivo
        raiz = etree.parse(caminho_arquivo)
        return self.assinar_etree(raiz)

    def assinar_xml(self, xml):
        raiz = etree.parse(StringIO(xml))
        return self.assinar_etree(raiz)

    def assinar_etree(self, raiz):
        # Extrai a tag do elemento raiz
        tipo = extrair_tag(raiz.getroot())

        # doctype compatível com o tipo da tag raiz
        if tipo == u'NFe':
            doctype = u'<!DOCTYPE NFe [<!ATTLIST infNFe Id ID #IMPLIED>]>'
        elif tipo == u'inutNFe':
            doctype = u'<!DOCTYPE inutNFe [<!ATTLIST infInut Id ID #IMPLIED>]>'
        elif tipo == u'cancNFe':
            doctype = u'<!DOCTYPE cancNFe [<!ATTLIST infCanc Id ID #IMPLIED>]>'
        elif tipo == u'DPEC':
            doctype = u'<!DOCTYPE DPEC [<!ATTLIST infDPEC Id ID #IMPLIED>]>'

        # Tag de assinatura
        if raiz.getroot().find('Signature') is None:
            signature = etree.Element(
                    'Signature',
                    URI=raiz.getroot().getchildren()[0].attrib['Id'],
                    xmlns=NAMESPACE_SIG,
                    )
            signature.text = ''
            raiz.getroot().insert(0, signature)

        # Acrescenta a tag de doctype (como o lxml nao suporta alteracao do doctype,
        # converte para string para faze-lo)
        xml = etree.tostring(raiz, xml_declaration=True, encoding='utf-8')
        pos = xml.find('>') + 1
        xml = xml[:pos] + doctype + xml[pos:]
        raiz = etree.parse(StringIO(xml))

        # Ativa funções criptográficas
        self._ativa_funcoes_criptograficas()

        # Colocamos o texto no avaliador XML
        #doc_xml = libxml2.parseMemory(xml, len(xml))
    
        # Cria o contexto para manipulação do XML via sintaxe XPATH
        #ctxt = doc_xml.xpathNewContext()
        #ctxt.xpathRegisterNs(u'sig', NAMESPACE_SIG)
    
        # Separa o nó da assinatura
        #noh_assinatura = ctxt.xpathEval(u'//*/sig:Signature')[0]
    
        # Buscamos a chave no arquivo do certificado
        chave = xmlsec.cryptoAppKeyLoad(
                filename=str(self.certificado.caminho_arquivo),
                format=xmlsec.KeyDataFormatPkcs12,
                pwd=str(self.senha),
                pwdCallback=None,
                pwdCallbackCtx=None,
                )
    
        # Cria a variável de chamada (callable) da função de assinatura
        assinador = xmlsec.DSigCtx()
    
        # Atribui a chave ao assinador
        assinador.signKey = chave

        # Desativa funções criptográficas
        self._desativa_funcoes_criptograficas()

        #print etree.tostring(raiz, pretty_print=True, xml_declaration=True, encoding='utf-8')

    def _ativa_funcoes_criptograficas(self):
        # Ativa as funções de análise de arquivos XML FIXME
        libxml2.initParser()
        libxml2.substituteEntitiesDefault(1)
        
        # Ativa as funções da API de criptografia
        xmlsec.init()
        xmlsec.cryptoAppInit(None)
        xmlsec.cryptoInit()
    
    def _desativa_funcoes_criptograficas(self):
        ''' Desativa as funções criptográficas e de análise XML
        As funções devem ser chamadas aproximadamente na ordem inversa da ativação
        '''
        
        # Shutdown xmlsec-crypto library
        xmlsec.cryptoShutdown()
        
        # Shutdown crypto library
        xmlsec.cryptoAppShutdown()
        
        # Shutdown xmlsec library
        xmlsec.shutdown()
        
        # Shutdown LibXML2 FIXME
        libxml2.cleanupParser()

