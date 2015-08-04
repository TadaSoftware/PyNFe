# -*- coding: utf-8 -*-

from pynfe.utils import etree
import subprocess


class Assinatura(object):
    """Classe abstrata responsavel por definir os metodos e logica das classes
    de assinatura digital."""

    certificado = None
    senha = None

    def __init__(self, certificado, senha):
        self.certificado = certificado
        self.senha = senha

    def assinar(self, xml):
        """Efetua a assinatura da nota"""
        pass

class AssinaturaA1(Assinatura):
    """Classe responsavel por efetuar a assinatura do certificado
    digital no XML informado."""

    def assinar(self, xml, retorna_string=False):
        try:
            # No raiz do XML de saida
            tag = 'infNFe'; # tag que será assinada
            raiz = etree.Element('Signature', xmlns='http://www.w3.org/2000/09/xmldsig#')
            siginfo = etree.SubElement(raiz, 'SignedInfo')
            etree.SubElement(siginfo, 'CanonicalizationMethod', Algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315')
            etree.SubElement(siginfo, 'SignatureMethod', Algorithm='http://www.w3.org/2000/09/xmldsig#rsa-sha1')
            if xml.findall('infNFe')[0].attrib['Id']:
                ref = etree.SubElement(siginfo, 'Reference', URI='#'+xml.findall('infNFe')[0].attrib['Id'])
            elif xml.findall('infEvento')[0].attrib['Id']:
                tag = 'infEvento'
                ref = etree.SubElement(siginfo, 'Reference', URI='#'+xml.findall('infEvento')[0].attrib['Id'])
            trans = etree.SubElement(ref, 'Transforms')
            etree.SubElement(trans, 'Transform', Algorithm='http://www.w3.org/2000/09/xmldsig#enveloped-signature')
            etree.SubElement(trans, 'Transform', Algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315')
            etree.SubElement(ref, 'DigestMethod', Algorithm='http://www.w3.org/2000/09/xmldsig#sha1')
            etree.SubElement(ref, 'DigestValue')
            etree.SubElement(raiz, 'SignatureValue')
            keyinfo = etree.SubElement(raiz, 'KeyInfo')
            etree.SubElement(keyinfo, 'X509Data')

            xml.append(raiz)

            with open('testes.xml', 'w') as arquivo:
                arquivo.write(etree.tostring(xml, encoding="unicode", pretty_print=False))
            
            subprocess.call(['xmlsec1', '--sign', '--pkcs12', self.certificado, '--pwd', self.senha, '--crypto', 'openssl', '--output', 'funfa.xml', '--id-attr:Id', tag, 'testes.xml'])
            xml = etree.parse('funfa.xml').getroot()

            if retorna_string:
                return etree.tostring(xml, encoding="unicode", pretty_print=False)
            else:
                return xml
        except Exception as e:
            raise e
        
