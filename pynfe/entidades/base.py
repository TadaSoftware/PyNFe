# -*- coding: utf-8 -*-

class Entidade(object):
    def __init__(self, **kwargs):
        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs:
            setattr(self, k, v)

class Lote(object):
    pass

