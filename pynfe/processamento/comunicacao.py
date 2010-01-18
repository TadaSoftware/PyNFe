# -*- coding: utf-8 -*-

class Comunicacao(object):
    u"""Classe abstrata responsavel por definir os metodos e logica das classes
    de comunicação com os webservices da NF-e."""

    servidor = None
    porta = None

    def __init__(self, servidor, porta):
        self.servidor = servidor
        self.porta = porta

class ComunicacaoSefaz(Comunicacao):
    u"""Classe de comunicação que segue o padrão definido para as SEFAZ dos Estados."""

    def transmitir(self, nota_fiscal):
        pass

    def cancelar(self, nota_fiscal):
        pass

    def situacao_nfe(self, nota_fiscal):
        pass

    def status_servico(self):
        pass

    def consultar_cadastro(self, instancia):
        pass

    def inutilizar_faixa_numeracao(self, faixa):
        pass

