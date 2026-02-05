#!/usr/bin/env python
# *-* encoding: utf8 *-*

import tempfile
import unittest

from pynfe.entidades.certificado import CertificadoA1


class CertificadoTestCase(unittest.TestCase):
    def setUp(self):
        self.certificado_correto = "./tests/certificado.pfx"
        self.certificado_incorreto = "./tests/arquivo_erro.pfx"
        self.senha_correto = bytes("123456", encoding="utf-8")
        self.senha_incorreto = bytes("654321", encoding="utf-8")

    def test_assinatura_com_caminho(self):
        self.a1 = CertificadoA1(self.certificado_correto)
        cert = self.a1.separar_arquivo(senha=self.senha_correto, caminho=self.certificado_correto)

        temp_dir = tempfile.gettempdir()
        self.assertTrue(cert[0].startswith(temp_dir))
        self.assertTrue(cert[1].startswith(temp_dir))

        self.a1.excluir()

    def test_exception_certificado_filenotfounderror(self):
        with self.assertRaises(FileNotFoundError) as context:
            self.a1 = CertificadoA1(self.certificado_incorreto)
            self.a1.separar_arquivo(senha=self.senha_incorreto, caminho=self.certificado_incorreto)
        self.assertEqual(
            str(context.exception),
            ("Falha ao abrir arquivo do certificado digital A1. Verifique o local do arquivo."),
        )

    def test_exception_certificado_senha_errada(self):
        with self.assertRaises(Exception) as context:
            self.a1 = CertificadoA1(self.certificado_correto)
            self.a1.separar_arquivo(senha=self.senha_incorreto, caminho=self.certificado_correto)
        self.assertEqual(
            str(context.exception),
            ("Falha ao carregar certificado digital A1. Verifique a senha do certificado."),
        )

    def test_assinatura_sem_caminho(self):
        self.a1 = CertificadoA1(self.certificado_correto)
        cert = self.a1.separar_arquivo(senha=self.senha_correto, caminho=None)

        texto_inicial_esperado = "-----BEGIN PRIVATE KEY-----"
        texto_inicial_gerado = cert[0].decode("utf-8")

        self.assertTrue(texto_inicial_gerado.startswith(texto_inicial_esperado))

        self.a1.excluir()

    def test_verificar_se_arquivos_temporarios_existem(self):
        self.a1 = CertificadoA1(self.certificado_correto)
        self.a1.separar_arquivo(senha=self.senha_correto, caminho=self.certificado_correto)
        self.assertTrue(len(self.a1.arquivos_temp) > 0)

        self.a1.excluir()

    def test_excluir_arquivos_temporarios(self):
        self.a1 = CertificadoA1(self.certificado_correto)
        self.a1.separar_arquivo(senha=self.senha_correto, caminho=self.certificado_correto)
        self.a1.excluir()

        self.assertTrue(len(self.a1.arquivos_temp) == 0)


if __name__ == "__main__":
    unittest.main()
