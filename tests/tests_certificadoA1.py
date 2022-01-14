#!/usr/bin/env python
# *-* encoding: utf8 *-*

import unittest

from pynfe.entidades.certificado import CertificadoA1


class CertificadoTestCase(unittest.TestCase):

    def setUp(self):
        self.certificado = "./tests/certificado.pfx"
        self.senha = '123456'

    def test_assinatura_com_caminho(self):
        self.a1 = CertificadoA1(self.certificado)
        cert = self.a1.separar_arquivo(senha=self.senha, caminho=self.certificado)

        self.assertTrue(cert[0].startswith('/tmp/'))
        self.assertTrue(cert[1].startswith('/tmp/'))

        self.a1.excluir()

    def test_exception_certificado_filenotfounderror(self):
        self.certificado = "./tests/arquivo_erro.pfx"
        self.senha = '123456'

        with self.assertRaises(Exception) as context:
            self.a1 = CertificadoA1(self.certificado)
            self.a1.separar_arquivo(senha=self.senha, caminho=self.certificado)
        self.assertEqual(str(context.exception), "Falha ao abrir arquivo do certificado digital A1. Verifique local e permissoes do arquivo.")

    def test_exception_certificado_senha_errada(self):
        self.certificado = "./tests/certificado.pfx"
        self.senha = '654321'

        with self.assertRaises(Exception) as context:
            self.a1 = CertificadoA1(self.certificado)
            self.a1.separar_arquivo(senha=self.senha, caminho=self.certificado)
        self.assertEqual(str(context.exception), "Falha ao carregar certificado digital A1. Verifique a senha do certificado.")

    def test_assinatura_sem_caminho(self):
        self.a1 = CertificadoA1(self.certificado)
        cert = self.a1.separar_arquivo(senha=self.senha)

        texto_inicial_esperado = '-----BEGIN PRIVATE KEY-----'
        texto_inicial_gerado = cert[0].decode('utf-8')

        self.assertTrue(texto_inicial_gerado.startswith(texto_inicial_esperado))

        self.a1.excluir()

    def test_verificar_se_arquivos_temporarios_existem(self):
        self.a1 = CertificadoA1(self.certificado)
        self.a1.separar_arquivo(senha=self.senha, caminho=self.certificado)
        self.assertTrue(len(self.a1.arquivos_temp) > 0)

        self.a1.excluir()

    def test_excluir_arquivos_temporarios(self):
        self.a1 = CertificadoA1(self.certificado)
        self.a1.separar_arquivo(senha=self.senha, caminho=self.certificado)
        self.a1.excluir()

        self.assertTrue(len(self.a1.arquivos_temp) == 0)


if __name__ == '__main__':
    unittest.main()
