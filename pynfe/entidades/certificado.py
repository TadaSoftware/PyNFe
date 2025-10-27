# -*- coding: utf-8 -*-

import os
import tempfile

from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
    pkcs12,
)

from .base import Entidade


class Certificado(Entidade):
    """Classe abstrata responsavel por definir o modelo padrao para as demais
    classes de certificados digitais.

    Caso va implementar um novo formato de certificado, crie uma classe que
    herde desta."""

    def __new__(cls, *args, **kwargs):
        if cls == Certificado:
            raise Exception("Esta classe nao pode ser instanciada diretamente!")
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
        """Separa o arquivo de certificado em dois: de chave e de certificado e retorna a string.
        Se caminho for True grava na pasta temporaria e retorna o caminho dos arquivos,
        senao retorna o objeto. Apos o uso devem ser excluidos com o metodo excluir.
        """

        try:
            with open(self.caminho_arquivo, "rb") as cert_arquivo:
                cert_conteudo = cert_arquivo.read()
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                "Falha ao abrir arquivo do certificado digital A1. Verifique o local do arquivo."
            ) from exc
        except PermissionError as exc:
            raise PermissionError(
                "Falha ao abrir arquivo do certificado digital A1. Verifique as permissoes do arquivo."
            ) from exc
        except Exception as exc:
            raise Exception(
                "Falha ao abrir arquivo do certificado digital A1. Causa desconhecida."
            ) from exc

        if not isinstance(senha, bytes):
            senha = str.encode(senha)

        # Carrega o arquivo .pfx, erro pode ocorrer se a senha estiver errada ou formato invalido.
        try:
            (
                chave,
                cert,
            ) = pkcs12.load_key_and_certificates(cert_conteudo, senha)[:2]
        except Exception as e:
            if "invalid password" in str(e).lower():
                raise Exception(
                    "Falha ao carregar certificado digital A1. Verifique a senha do certificado."
                ) from e
            else:
                raise Exception(
                    "Falha ao carregar certificado digital A1. Causa desconhecida."
                ) from e

        if caminho:
            # cria arquivos temporarios
            with tempfile.NamedTemporaryFile(delete=False) as arqcert:
                arqcert.write(cert.public_bytes(Encoding.PEM))
            with tempfile.NamedTemporaryFile(delete=False) as arqchave:
                arqchave.write(
                    chave.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
                )
            self.arquivos_temp.append(arqchave.name)
            self.arquivos_temp.append(arqcert.name)
            return arqchave.name, arqcert.name
        else:
            # Certificado
            cert = cert.public_bytes(Encoding.PEM).decode("utf-8")
            # Chave, string decodificada da chave privada
            chave = chave.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())

            return chave, cert

    def excluir(self):
        """Exclui os arquivos temporarios utilizados para o request."""
        try:
            for i in self.arquivos_temp:
                os.remove(i)
            self.arquivos_temp.clear()
        except Exception:
            pass
