# -*- coding: utf-8 -*-

from .base import Entidade
from OpenSSL import crypto


class Certificado(Entidade):
    """Classe abstrata responsavel por definir o modelo padrao para as demais
    classes de certificados digitais.
    
    Caso va implementar um novo formato de certificado, crie uma classe que
    herde desta."""

    def __new__(cls, *args, **kwargs):
        if cls == Certificado:
            raise Exception('Esta classe nao pode ser instanciada diretamente!')
        else:
            return super(Certificado, cls).__new__(cls)


class CertificadoA1(Certificado):
    """Implementa a entidade do certificado eCNPJ A1, suportado pelo OpenSSL,
    e amplamente utilizado."""

    caminho_arquivo = None

    def __init__(self, caminho_arquivo=None):
        self.caminho_arquivo = caminho_arquivo
    
    def separar_arquivo(self, senha):
        """Separa o arquivo de certificado em dois: de chave e de certificado,
        e retorna a string."""
        
        # Carrega o arquivo .pfx, erro pode ocorrer se a senha estiver errada ou formato invalido.
        pkcs12 = crypto.load_pkcs12(open(self.caminho_arquivo, "rb").read(), senha)
        
        # Certificado
        cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate()).decode('utf-8')
        cert = cert.replace('\n', '')
        cert = cert.replace('-----BEGIN CERTIFICATE-----', '')
        cert = cert.replace('-----END CERTIFICATE-----', '')
        
        # Chave, string decodificada da chave privada
        chave = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())
        
        return chave, cert

