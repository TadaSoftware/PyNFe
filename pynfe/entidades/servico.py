"""
    @author: Junior Tada, Leonardo Tada
"""

from .base import Entidade
from decimal import Decimal

class Servico(Entidade):

    valor_servico = Decimal()
    iss_retido = Decimal()
    """ http://www1.receita.fazenda.gov.br/sistemas/nfse/tabelas-de-codigos.htm 
        Lista com códigos dos serviços
    """
    item_lista = str()
    discriminacao = str()
    exigibilidade = int()
    codigo_municipio = str()

    def __str__(self):
        return self.discriminacao