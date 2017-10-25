# -*- coding: utf-8 -*-

from .base import Entidade
from OpenSSL import crypto
import tempfile
import os


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
        self.arquivos_temp = []

    def separar_arquivo(self, senha, caminho=False):
        """Separa o arquivo de certificado em dois: de chave e de certificado,
        e retorna a string. Se caminho for True grava na pasta temporaria e retorna
        o caminho dos arquivos, senao retorna o objeto. Apos o uso devem ser excluidos com o metodo excluir."""

        # Carrega o arquivo .pfx, erro pode ocorrer se a senha estiver errada ou formato invalido.
        try:
            pkcs12 = crypto.load_pkcs12(open(self.caminho_arquivo, "rb").read(), senha)
        except Exception as e:
            raise Exception('Falha ao carregar certificado digital A1. Verifique local e senha.')

        if caminho:
            cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())
            chave = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())
            # cria arquivos temporarios
            with tempfile.NamedTemporaryFile(delete=False) as arqcert:
                arqcert.write(cert)
            with tempfile.NamedTemporaryFile(delete=False) as arqchave:
                arqchave.write(chave)
            self.arquivos_temp.append(arqchave.name)
            self.arquivos_temp.append(arqcert.name)
            return arqchave.name, arqcert.name
        else:
            # Certificado
            cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate()).decode('utf-8')
            cert = cert.replace('\n', '')
            cert = cert.replace('-----BEGIN CERTIFICATE-----', '')
            cert = cert.replace('-----END CERTIFICATE-----', '')

            # Chave, string decodificada da chave privada
            chave = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())

            return chave, cert

    def excluir(self):
        """Exclui os arquivos temporarios utilizados para o request."""
        try:
            for i in self.arquivos_temp:
                os.remove(i)
            self.arquivos_temp.clear()
        except:
            pass
