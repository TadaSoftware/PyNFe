# -*- coding: utf-8 -*-

class Entidade(object):
    _fonte_dados = None

    def __init__(self, **kwargs):
        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)

        # Adiciona o objeto à fonte de dados informada
        if not self._fonte_dados:
            from .fonte_dados import _fonte_dados
            self._fonte_dados = _fonte_dados

        self._fonte_dados.adicionar_objeto(self)

    def __repr__(self):
        return '<%s %s>'%(self.__class__.__name__, str(self))

class Lote(object):
    pass

