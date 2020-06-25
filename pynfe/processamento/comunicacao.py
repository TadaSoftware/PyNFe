# -*- coding: utf-8 -*-
import ssl
import datetime

from pynfe.utils import etree, so_numeros
from pynfe.utils.flags import (
    NAMESPACE_NFE,
    NAMESPACE_XSD,
    NAMESPACE_XSI,
    VERSAO_PADRAO,
    NAMESPACE_SOAP,
    CODIGOS_ESTADOS,
    NAMESPACE_BETHA,
    NAMESPACE_METODO
)
from pynfe.utils.webservices import NFE, NFCE, NFSE
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
