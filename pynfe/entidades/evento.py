# -*- coding: utf-8 -*-

"""
    @author: Junior Tada, Leonardo Tada
"""

from .base import Entidade

class Evento(Entidade):
    # - Identificador da TAG a ser assinada, a regra de formação do Id é: “ID” + tpEvento + chave da NF-e + nSeqEvento
    id = str()
    # - Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE, utilizar 91 para identificar o Ambiente Nacional.
    orgao = str()
    # - CNPJ (obrigatorio)
    cnpj = str()
    # - Chave de Acesso da NF-e vinculada ao Evento
    chave = str()
    # - Data e hora do evento no formato AAAA-MM-DDThh:mm:ssTZD
    data_emissao = None
    # - uf de onde a nota foi enviada
    uf = str()
    # - Código do evento = Cancelamento(110111), Carta de Correcao(110110)
    tp_evento = str()
    # - Sequencial do evento para o mesmo tipo de evento. 
    """ Para maioria dos eventos nSeqEvento=1, nos casos em que possa existir mais de um evento, 
    como é o caso da Carta de Correção, o autor do evento deve numerar de forma sequencial."""
    n_seq_evento = 1
    # - descEvento
    descricao = str()

    @property
    def identificador(self):
        """ 
            Gera o valor para o campo id 
            A regra de formação do Id é: “ID” + tpEvento + chave da NF-e + nSeqEvento
        """
        self.id = "ID%(tp_evento)s%(chave)s%(n_seq_evento)s"%{
                'tp_evento': self.tp_evento,
                'chave': self.chave,
                'n_seq_evento': str(self.n_seq_evento).zfill(2),
        }
        return self.id


class EventoCancelarNota(Evento):

    def __init__(self, *args, **kwargs):
        super(EventoCancelarNota, self).__init__(*args, **kwargs)
        # - Código do evento = 110111
        self.tp_evento = '110111'
        # - "Cancelamento"
        self.descricao = 'Cancelamento'

    # - Informar o número do Protocolo de Autorização da NF-e a ser Cancelada. (vide item 5.8).
    protocolo = str()
    # - Informar a justificativa do cancelamento (min 15 max 255 caracteres)
    justificativa = str()


class EventoCartaCorrecao(Evento):

    def __init__(self, *args, **kwargs):
        super(EventoCartaCorrecao, self).__init__(*args, **kwargs)
        # - Código do evento = 110110
        self.tp_evento = '110110'
        # - “Carta de Correção” ou “Carta de Correcao” 
        self.descricao = 'Carta de Correcao'

    """ - xCondUso - Condições de uso da Carta de Correção, informar a literal : 
    A Carta de Correcao e disciplinada pelo paragrafo 1o-A do art. 7o do Convenio S/N, de 15 de dezembro de 1970 
    e pode ser utilizada para regularizacao de erro ocorrido na emissao de documento fiscal, 
    desde que o erro nao esteja relacionado com: 
    I - as variaveis que determinam o valor do imposto tais como: base de calculo, aliquota, diferenca de preco, quantidade, valor da operacao ou da prestacao; 
    II - a correcao de dados cadastrais que implique mudanca do remetente ou do destinatario; 
    III - a data de emissao ou de saida."""
    cond_uso = 'A Carta de Correcao e disciplinada pelo paragrafo 1o-A do art. 7o do Convenio S/N, de 15 de dezembro de 1970 e pode ser utilizada para regularizacao de erro ocorrido na emissao de documento fiscal, desde que o erro nao esteja relacionado com: I - as variaveis que determinam o valor do imposto tais como: base de calculo, aliquota, diferenca de preco, quantidade, valor da operacao ou da prestacao; II - a correcao de dados cadastrais que implique mudanca do remetente ou do destinatario; III - a data de emissao ou de saida.'
    # - xCorrecao - Correção a ser considerada, texto livre. A correção mais recente substitui as anteriores. min 15 max 1000
    correcao = str()
