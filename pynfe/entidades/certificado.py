# -*- coding; utf-8 -*-
from base import Entidade

class Certificado(Entidade):
    u"""Classe abstrata responsavel por definir o modelo padrao para as demais
    classes de certificados digitais.
    
    Caso va implementar um novo formato de certificado, crie uma classe que
    herde desta."""

    def __new__(cls, *args, **kwargs):
        if cls == Certificado:
            raise Exception('Esta classe nao pode ser instanciada diretamente!')
        else:
            return super(Certificado, cls).__new__(cls, *args, **kwargs)

class CertificadoA1(Certificado):
    """Implementa a entidade do certificado eCNPJ A1, suportado pelo OpenSSL,
    e amplamente utilizado."""

    caminho_arquivo = None
    conteudo_x509 = None

    def __init__(self, caminho_arquivo=None, conteudo_x509=None):
        self.caminho_arquivo = caminho_arquivo or self.caminho_arquivo
        self.conteudo_x509 = conteudo_x509 or self.conteudo_x509

