# -*- coding: utf-8 -*-

class Assinatura(object):
    """Classe abstrata responsavel por definir os metodos e logica das classes
    de assinatura digital."""

    def __init__(self, certificado):
        self.certificado = certificado

    def assinar_arquivos(self, caminho_raiz):
        """Efetua a assinatura dos arquivos XML informados"""
        pass

    def assinar_xml(self, xml):
        """Efetua a assinatura numa string contendo XML valido."""
        pass

    def assinar_etree(self, raiz):
        u"""Efetua a assinatura numa instancia da biblioteca lxml.etree.
        
        Este metodo de assinatura será utilizado internamente pelos demais,
        sendo que eles convertem para uma instancia lxml.etree para somente
        depois efetivar a assinatura.
        
        TODO: Verificar o funcionamento da PyXMLSec antes de efetivar isso."""
        pass

    def assinar_objetos(self, objetos):
        """Efetua a assinatura em instancias do PyNFe"""
        pass

class AssinaturaA1(Assinatura):
    """Classe abstrata responsavel por efetuar a assinatura do certificado
    digital no XML informado."""
    
    pass
