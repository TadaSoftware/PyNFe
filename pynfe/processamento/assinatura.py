# -*- coding: utf-8 -*-
import signxml
from typing import Union

from pynfe.entidades import CertificadoA1
from pynfe.utils import CustomXMLSigner, etree, remover_acentos


class Assinatura(object):
    """Classe abstrata responsavel por definir os metodos e logica das classes
    de assinatura digital."""

    certificado = None
    senha = None

    def __init__(self, certificado, senha, autorizador=None):
        self.certificado = certificado
        self.senha = senha
        self.autorizador = autorizador

    def assinar(self, xml):
        """Efetua a assinatura da nota"""
        pass


class AssinaturaA1(Assinatura):
    def __init__(self, certificado, senha):
        self.key, self.cert = CertificadoA1(certificado).separar_arquivo(senha)

    def assinar(self, xml: etree._Element, retorna_string=False) -> Union[str, etree._Element]:
        # busca tag que tem id(reference_uri), logo nao importa se tem namespace
        reference = xml.find(".//*[@Id]").attrib["Id"]

        # retira acentos
        xml_str = remover_acentos(etree.tostring(xml, encoding="unicode", pretty_print=False))
        xml = etree.fromstring(xml_str)

        signer = CustomXMLSigner(
            method=signxml.methods.enveloped,
            signature_algorithm="rsa-sha1",
            digest_algorithm="sha1",
            c14n_algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
        )
        signer.excise_empty_xmlns_declarations = True

        ns = {None: signer.namespaces["ds"]}
        signer.namespaces = ns

        ref_uri = ("#%s" % reference) if reference else None
        signed_root = signer.sign(xml, key=self.key, cert=self.cert, reference_uri=ref_uri)

        # Reparse to ensure namespaces are correctly associated with elements
        # This is required for lxml 6.x compatibility when using default namespace (None prefix)
        signed_xml_str = etree.tostring(signed_root, encoding="unicode", pretty_print=False)
        signed_root = etree.fromstring(signed_xml_str)

        if retorna_string:
            return signed_xml_str
        else:
            return signed_root
