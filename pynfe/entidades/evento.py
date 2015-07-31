# -*- coding: utf-8 -*-

"""
    @author: Junior Tada, Leonardo Tada
"""

from .base import Entidade

class Evento(Entidade):
    pass

class EventoCancelarNota(Evento):
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
    # - Código do evento = 110111
    tp_evento = '110111'
    # - Sequencial do evento para o mesmo tipo de evento. Para maioria dos eventos nSeqEvento=1, nos casos em quepossa existir mais de um evento, como é o caso da Carta de Correção, o autor do evento deve numerar de forma sequencial.
    n_seq_evento = '1'
    # # - Versão do detalhe do evento (grupo detEvento – HP17), informação utilizada para a SEFAZ validar o grupo detEvento.
    # ver_evento = str()
    # # - Informações do Pedido de Cancelamento
    # det_evento = str()
    # # - Versão do Pedido de Cancelamento, deve ser informado com a mesma informação da tag verEvento (HP16)
    # versao = str()
    # - descEvento
    descricao = 'Cancelamento'
    # - Informar o número do Protocolo de Autorização da NF-e a ser Cancelada. (vide item 5.8).
    protocolo = str()
    # - Informar a justificativa do cancelamento (min 15 max 255 caracteres)
    justificativa = str()

    @property
    def identificador(self):
        """ 
            Gera o valor para o campo id 
            A regra de formação do Id é: “ID” + tpEvento + chave da NF-e + nSeqEvento
        """
        self.id = "ID%(tp_evento)s%(um)s%(chave)s%(n_seq_evento)s"%{
                'tp_evento': self.tp_evento,
                'um': '1',
                'chave': self.chave,
                'n_seq_evento': self.n_seq_evento,
        }
        return self.id