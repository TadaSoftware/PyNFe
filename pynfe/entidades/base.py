# -*- coding: utf-8 -*-

class Entidade(object):
    _fonte_dados = None

    def __init__(self, **kwargs):
        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)

        # Adiciona o objeto à fonte de dados informada
        if self._fonte_dados:
            self._fonte_dados.adicionar_objeto(self)

class Lote(object):
    pass

