# -*- coding: utf-8 -*-

import warnings
from dataclasses import dataclass
from typing import List


@dataclass
class CampoDeprecated(object):
    anterior: str
    novo: str
    motivo: str
    apenas_warning: bool = False


class Entidade(object):
    _fonte_dados = None
    campos_deprecados: List[CampoDeprecated] = []

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

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, str(self))

    def __setattr__(self, name, value):
        if hasattr(self, name):
            # Verifica se o atributo é um campo deprecado
            campo_deprecado = next(
                (campo for campo in self.campos_deprecados if campo.anterior == name),
                None,
            )

            if campo_deprecado:
                if campo_deprecado.novo:
                    warnings.warn(
                        f"O campo {campo_deprecado.anterior} foi deprecado e será removido em versões futuras. "
                        f"Utilize {campo_deprecado.novo} no lugar. Motivo: {campo_deprecado.motivo}",
                        DeprecationWarning,
                    )
                    setattr(self, campo_deprecado.novo, value)
                    return
                if campo_deprecado.apenas_warning:
                    warnings.warn(
                        f"O campo {campo_deprecado.anterior} foi deprecado e será removido em versões futuras. "
                        f"Motivo: {campo_deprecado.motivo}",
                        DeprecationWarning,
                    )
                else:
                    raise AttributeError(
                        f"O campo {campo_deprecado.anterior} foi deprecado e removido."
                        f"Motivo: {campo_deprecado.motivo}"
                    )
        super(Entidade, self).__setattr__(name, value)


class Lote(object):
    pass
