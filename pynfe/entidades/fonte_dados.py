# -*- coding: utf-8 -*-
from pynfe.excecoes import NenhumObjetoEncontrado, MuitosObjetosEncontrados


class FonteDados(object):
    """Classe responsável por ser o repositório dos objetos em memória e que
    pode ser extendida para persistir esses objetos. Também tem a função de
    memorizar os objetos redundantes como um só e assim otimizar o desempenho."""

    _objetos = None

    def __init__(self, objetos=None):
        # Inicializa variável que armazena os objetos contidos na Fonte de Dados
        if objetos:
            self._objetos = objetos
        else:
            self._objetos = []

    def carregar_objetos(self, **kwargs):
        """Método responsavel por retornar os objetos que casem com os atributos
        informados no argumento **kwargs (argumentos nomeados).

        Um argumento especial é o '_classe', que representa a classe da entidade
        desejada.

        FIXME: Este algoritimo pode ser melhorado pra fazer pesquisas melhores,
        mas por enquanto vamos nos focar no processo em geral para só depois nos
        preocupar com otimizações e desempenho."""

        # Função de filtro
        def filtrar(obj):
            ret = True

            for k, v in kwargs.items():
                # Filtra pela classe e pelos atributos
                ret = (k == "_classe" and isinstance(obj, v)) or (
                    k != "_classe" and getattr(obj, k, None) == v
                )

                if not ret:
                    break

            return ret

        # Filtra a lista de objetos
        lista = filter(filtrar, self._objetos)

        return lista

    def adicionar_objeto(self, _objeto):
        """Método responsável por adicionar o(s) objeto(s) informado(s) ao
        repositorio de objetos da fonte de dados."""

        from .base import Entidade

        # Adiciona _objeto como objeto
        if isinstance(_objeto, Entidade):
            self._objetos.append(_objeto)

        # Adiciona _objeto como lista
        elif isinstance(_objeto, (list, tuple)):
            self._objetos += _objeto

        else:
            raise Exception("Objeto informado e invalido!")

    def remover_objeto(self, _objeto=None, **kwargs):
        """Método responsavel por remover os objetos que casem com os atributos
        informados no argumento **kwargs (argumentos nomeados).

        Um argumento especial é o '_classe', que representa a classe da entidade
        desejada.

        Outro argumetno especial é o '_objeto', que representa o objeto a ser
        removido. Caso o argumento _objeto seja uma lista de objetos, eles serão
        removidos também."""

        from .base import Entidade

        lista = None

        # Remove objetos
        if not _objeto:
            lista = self.carregar_objetos(**kwargs)

        # Remove _objeto como objeto
        elif isinstance(_objeto, Entidade):
            lista = [_objeto]

        # Remove _objeto como objeto
        elif isinstance(_objeto, (list, tuple)):
            lista = _objeto

        else:
            raise Exception("Objeto informado e invalido!")

        # Efetiva a remoção
        for obj in lista:
            self._objetos.remove(obj)

    def obter_objeto(self, **kwargs):
        """Faz a ponte para o método 'carregar_objetos' mas obriga o retorno de
        apenas um objeto, levantando exceção se nenhum for encontrado ou se forem
        encontrados mais de um."""

        lista = self.carregar_objetos(**kwargs)

        if len(lista) == 0:
            raise NenhumObjetoEncontrado("Nenhum objeto foi encontrado!")
        elif len(lista) > 1:
            raise MuitosObjetosEncontrados("Muitos objetos foram encontrados!")

        return lista[0]

    def obter_lista(self, **kwargs):
        """Método de proxy, que somente repassa a chamada ao metodo 'carregar_objetos'"""
        return self.carregar_objetos(**kwargs)

    def contar_objetos(self, **kwargs):
        """Método que repassa a chamada ao metodo 'carregar_objetos' mas retorna
        somente a quantidade de objetos encontrados."""

        if kwargs:
            return len(self.carregar_objetos(**kwargs))
        else:
            return len(self._objetos)

    def limpar_dados(self):
        self._objetos.clear()


# Instancia da fonte de dados default
_fonte_dados = FonteDados()
