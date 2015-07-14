# -*- coding: utf-8 -*-

from pynfe.utils.flags import NAMESPACE_NFE, NAMESPACE_SIG

class Assinatura(object):
    """Classe abstrata responsavel por definir os metodos e logica das classes
    de assinatura digital."""

    certificado = None
    senha = None

    def __init__(self, certificado, senha):
        self.certificado = certificado
        self.senha = senha

    def assinar_nfe(self, xml):
        """Efetua a assinatura da nfe"""
        pass

class AssinaturaA1(Assinatura):
    """Classe abstrata responsavel por efetuar a assinatura do certificado
    digital no XML informado."""

    def assinar_nfe(self, xml):
        #from lxml import etree
        import signxml
        from signxml import xmldsig

        cert = open("cert.pem").read()
        key = open("key.pem", "rb").read()

        root = etree.parse(xml).getroot()
        signer = xmldsig(root, digest_algorithm="sha1")
        signer.sign(method=signxml.methods.enveloped, key=key, cert=cert,
                    algorithm="rsa-sha1", c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315',
                    reference_uri='#NFe41150715380524000122651010000000271333611649')
        #verified_data = signer.verify(require_x509=True, ca_pem_file="cert.pem")
        e = etree.tostring(signer.data)
        open("testesig.xml", "wb").write(e)
