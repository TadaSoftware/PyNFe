# -*- coding: utf-8 -*-

import time
from pynfe.entidades import NotaFiscal
from pynfe.utils import etree, so_numeros, obter_municipio_por_codigo, \
    obter_pais_por_codigo, obter_municipio_e_codigo, formatar_decimal, \
    remover_acentos, obter_uf_por_codigo, obter_codigo_por_municipio
from pynfe.utils.flags import CODIGOS_ESTADOS, VERSAO_PADRAO, NAMESPACE_NFE, VERSAO_QRCODE
from pynfe.utils.webservices import NFCE
import base64
import hashlib


class Serializacao(object):
    """Classe abstrata responsavel por fornecer as funcionalidades basicas para
    exportacao e importacao de Notas Fiscais eletronicas para formatos serializados
    de arquivos. Como XML, JSON, binario, etc.

    Nao deve ser instanciada diretamente!"""

    _fonte_dados = None
    _ambiente = 1           # 1 = Produção, 2 = Homologação
    _contingencia = None    # Justificativa da entrada em contingência (min 20, max 256 caracteres)
    _so_cpf = False         # Destinatário com apenas o cpf do cliente
    _nome_aplicacao = 'PyNFe'

    def __new__(cls, *args, **kwargs):
        if cls == Serializacao:
            raise Exception('Esta classe nao pode ser instanciada diretamente!')
        else:
            return super(Serializacao, cls).__new__(cls)

    def __init__(self, fonte_dados, homologacao=False, contingencia=None, so_cpf=False):
        self._fonte_dados = fonte_dados
        self._ambiente = homologacao and 2 or 1
        self._contingencia = contingencia
        self._so_cpf = so_cpf

    def exportar(self, destino, **kwargs):
        """Gera o(s) arquivo(s) de exportacao a partir da Nofa Fiscal eletronica
        ou lista delas."""
        raise NotImplementedError

    def importar(self, origem):
        """Fabrica que recebe o caminho ou objeto de origem e instancia os objetos
        da PyNFe"""
        raise NotImplementedError


class SerializacaoXML(Serializacao):
    _versao = VERSAO_PADRAO

    def exportar(self, destino=None, retorna_string=False, limpar=True, **kwargs):
        """Gera o(s) arquivo(s) de Nota Fiscal eletronica no padrao oficial da SEFAZ
        e Receita Federal, para ser(em) enviado(s) para o webservice ou para ser(em)
        armazenado(s) em cache local.
        @param destino -
        @param retorna_string - Retorna uma string para debug.
        @param limpar - Limpa a fonte de dados para não gerar xml com dados duplicados.
        """
        try:
            # No raiz do XML de saida
            raiz = etree.Element('NFe', xmlns=NAMESPACE_NFE)

            # Carrega lista de Notas Fiscais
            notas_fiscais = self._fonte_dados.obter_lista(_classe=NotaFiscal, **kwargs)

            for nf in notas_fiscais:
                raiz.append(self._serializar_nota_fiscal(nf, retorna_string=False))

            if retorna_string:
                return etree.tostring(raiz, encoding="unicode", pretty_print=False)
            else:
                return raiz
        except Exception as e:
            raise e
        finally:
            if limpar:
                self._fonte_dados.limpar_dados()

    def importar(self, origem):
        """Cria as instancias do PyNFe a partir de arquivos XML no formato padrao da
        SEFAZ e Receita Federal."""

        raise Exception('Metodo nao implementado')

    def _serializar_emitente(self, emitente, tag_raiz='emit', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados do emitente
        etree.SubElement(raiz, 'CNPJ').text = so_numeros(emitente.cnpj)
        etree.SubElement(raiz, 'xNome').text = emitente.razao_social
        etree.SubElement(raiz, 'xFant').text = emitente.nome_fantasia
        # Endereço
        endereco = etree.SubElement(raiz, 'enderEmit')
        etree.SubElement(endereco, 'xLgr').text = emitente.endereco_logradouro
        etree.SubElement(endereco, 'nro').text = emitente.endereco_numero
        if emitente.endereco_complemento:
            etree.SubElement(endereco, 'xCpl').text = emitente.endereco_complemento
        etree.SubElement(endereco, 'xBairro').text = emitente.endereco_bairro
        etree.SubElement(endereco, 'cMun').text = obter_codigo_por_municipio(
            emitente.endereco_municipio, emitente.endereco_uf)
        etree.SubElement(endereco, 'xMun').text = emitente.endereco_municipio
        etree.SubElement(endereco, 'UF').text = emitente.endereco_uf
        etree.SubElement(endereco, 'CEP').text = so_numeros(emitente.endereco_cep)
        etree.SubElement(endereco, 'cPais').text = emitente.endereco_pais
        etree.SubElement(endereco, 'xPais').text = obter_pais_por_codigo(emitente.endereco_pais)
        if emitente.endereco_telefone:
            etree.SubElement(endereco, 'fone').text = emitente.endereco_telefone
        etree.SubElement(raiz, 'IE').text = emitente.inscricao_estadual
        # Apenas NF-e
        if emitente.inscricao_estadual_subst_tributaria:
            etree.SubElement(raiz, 'IEST').text = emitente.inscricao_estadual_subst_tributaria
        # Inscricao Municipal
        if emitente.inscricao_municipal:
            etree.SubElement(raiz, 'IM').text = emitente.inscricao_municipal
            # Campo Opcional. Pode ser informado quando a Inscrição Municipal (id:C19) for informada.
            if emitente.cnae_fiscal:
                etree.SubElement(raiz, 'CNAE').text = emitente.cnae_fiscal
        etree.SubElement(raiz, 'CRT').text = emitente.codigo_de_regime_tributario
        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_cliente(self, cliente, modelo, tag_raiz='dest', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados do cliente (distinatario)
        etree.SubElement(raiz, cliente.tipo_documento).text = so_numeros(cliente.numero_documento)
        if not self._so_cpf:
            if cliente.razao_social:
                etree.SubElement(raiz, 'xNome').text = cliente.razao_social
            endereco = etree.SubElement(raiz, 'enderDest')
            etree.SubElement(endereco, 'xLgr').text = cliente.endereco_logradouro
            etree.SubElement(endereco, 'nro').text = cliente.endereco_numero
            if cliente.endereco_complemento:
                etree.SubElement(endereco, 'xCpl').text = cliente.endereco_complemento
            etree.SubElement(endereco, 'xBairro').text = cliente.endereco_bairro
            etree.SubElement(endereco, 'cMun').text = obter_codigo_por_municipio(
                cliente.endereco_municipio, cliente.endereco_uf)
            etree.SubElement(endereco, 'xMun').text = cliente.endereco_municipio
            etree.SubElement(endereco, 'UF').text = cliente.endereco_uf
            etree.SubElement(endereco, 'CEP').text = so_numeros(cliente.endereco_cep)
            etree.SubElement(endereco, 'cPais').text = cliente.endereco_pais
            etree.SubElement(endereco, 'xPais').text = obter_pais_por_codigo(cliente.endereco_pais)
            if cliente.endereco_telefone:
                etree.SubElement(endereco, 'fone').text = cliente.endereco_telefone
        #Indicador da IE do destinatário: 1 – Contribuinte ICMSpagamento à vista; 2 – Contribuinte isento de inscrição; 9 – Não Contribuinte
        if cliente.indicador_ie == 9:
            # 9 – Não Contribuinte
            etree.SubElement(raiz, 'indIEDest').text = '9'
        elif (cliente.indicador_ie == 2 or cliente.isento_icms) or cliente.inscricao_estadual.upper() == 'ISENTO':
            etree.SubElement(raiz, 'indIEDest').text = '2'
        else:
            # Indicador da IE do destinatário: 1 – Contribuinte ICMSpagamento à vista;
            etree.SubElement(raiz, 'indIEDest').text = str(cliente.indicador_ie)
            etree.SubElement(raiz, 'IE').text = cliente.inscricao_estadual
        # Suframa
        if cliente.inscricao_suframa:
            etree.SubElement(raiz, 'ISUF').text = cliente.inscricao_suframa
        # Inscrição Municipal do tomador do serviço
        if cliente.inscricao_municipal:
            etree.SubElement(raiz, 'IM').text = cliente.inscricao_municipal
        # E-mail
        if cliente.email:
            etree.SubElement(raiz, 'email').text = cliente.email
        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_transportadora(self, transportadora, tag_raiz='transporta', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados da transportadora
        etree.SubElement(raiz, transportadora.tipo_documento.upper()).text = so_numeros(transportadora.numero_documento)
        etree.SubElement(raiz, 'xNome').text = transportadora.razao_social
        etree.SubElement(raiz, 'IE').text = transportadora.inscricao_estadual
        # Endereço
        etree.SubElement(raiz, 'xEnder').text = transportadora.endereco_logradouro
        etree.SubElement(raiz, 'xMun').text = transportadora.endereco_municipio
        etree.SubElement(raiz, 'UF').text = transportadora.endereco_uf

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_entrega_retirada(self, entrega_retirada, tag_raiz='entrega', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados da entrega/retirada
        etree.SubElement(raiz, entrega_retirada.tipo_documento).text = so_numeros(entrega_retirada.numero_documento)

        # Endereço
        etree.SubElement(raiz, 'xLgr').text = entrega_retirada.endereco_logradouro
        etree.SubElement(raiz, 'nro').text = entrega_retirada.endereco_numero
        etree.SubElement(raiz, 'xCpl').text = entrega_retirada.endereco_complemento
        etree.SubElement(raiz, 'xBairro').text = entrega_retirada.endereco_bairro
        etree.SubElement(raiz, 'cMun').text = entrega_retirada.endereco_municipio
        etree.SubElement(raiz, 'xMun').text = obter_municipio_por_codigo(
                entrega_retirada.endereco_municipio, entrega_retirada.endereco_uf,
                )
        etree.SubElement(raiz, 'UF').text = entrega_retirada.endereco_uf

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_produto_servico(self, produto_servico, modelo, tag_raiz='det', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Produto
        prod = etree.SubElement(raiz, 'prod')
        etree.SubElement(prod, 'cProd').text = str(produto_servico.codigo)
        etree.SubElement(prod, 'cEAN').text = produto_servico.ean
        etree.SubElement(prod, 'xProd').text = produto_servico.descricao
        etree.SubElement(prod, 'NCM').text = produto_servico.ncm
        # Codificação opcional que detalha alguns NCM. Formato: duas letras maiúsculas e 4 algarismos.
        # Se a mercadoria se enquadrar em mais de uma codificação, informar até 8 codificações principais.
        #etree.SubElement(prod, 'NVE').text = ''
        etree.SubElement(prod, 'CFOP').text = produto_servico.cfop
        etree.SubElement(prod, 'uCom').text = produto_servico.unidade_comercial
        etree.SubElement(prod, 'qCom').text = str(produto_servico.quantidade_comercial or 0)
        etree.SubElement(prod, 'vUnCom').text = str('{:.2f}').format(produto_servico.valor_unitario_comercial or 0)
        """ Código Especificador da Substituição Tributária – CEST, que estabelece a sistemática de uniformização e identificação das mercadorias e bens passíveis de
        sujeição aos regimes de substituição tributária e de antecipação de recolhimento do ICMS. """
        #if produto_servico.cest:
        #    etree.SubElement(prod, 'CEST').text = produto_servico.cest
        etree.SubElement(prod, 'vProd').text = str('{:.2f}').format(produto_servico.valor_total_bruto or 0)
        etree.SubElement(prod, 'cEANTrib').text = produto_servico.ean_tributavel
        etree.SubElement(prod, 'uTrib').text = produto_servico.unidade_tributavel
        etree.SubElement(prod, 'qTrib').text = str(produto_servico.quantidade_tributavel)
        etree.SubElement(prod, 'vUnTrib').text = '{:.4f}'.format(produto_servico.valor_unitario_tributavel or 0)
        """ Indica se valor do Item (vProd) entra no valor total da NF-e (vProd)
            0=Valor do item (vProd) não compõe o valor total da NF-e
            1=Valor do item (vProd) compõe o valor total da NF-e (vProd) (v2.0)
        """
        etree.SubElement(prod, 'indTot').text = str(produto_servico.ind_total)

        # Imposto
        imposto = etree.SubElement(raiz, 'imposto')

        # Lei da transparencia
        # Tributos aprox por item
        if produto_servico.valor_tributos_aprox:
            etree.SubElement(imposto, 'vTotTrib').text = produto_servico.valor_tributos_aprox

        ### ICMS
        icms = etree.SubElement(imposto, 'ICMS')
        icms_csosn = ('102', '103', '300', '400')
        if produto_servico.icms_modalidade in icms_csosn:
            icms_item = etree.SubElement(icms, 'ICMSSN'+produto_servico.icms_modalidade)
            etree.SubElement(icms_item, 'orig').text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, 'CSOSN').text = produto_servico.icms_csosn
        elif produto_servico.icms_modalidade == '101':
            icms_item = etree.SubElement(icms, 'ICMSSN'+produto_servico.icms_modalidade)
            etree.SubElement(icms_item, 'orig').text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, 'CSOSN').text = produto_servico.icms_csosn
            etree.SubElement(icms_item, 'pCredSN').text = str(produto_servico.icms_aliquota)       # Alíquota aplicável de cálculo do crédito (Simples Nacional).
            etree.SubElement(icms_item, 'vCredICMSSN').text = str(produto_servico.icms_credito)    # Valor crédito do ICMS que pode ser aproveitado nos termos do art. 23 da LC 123 (Simples Nacional)
        elif produto_servico.icms_modalidade == 'ST':
            icms_item = etree.SubElement(icms, 'ICMS'+produto_servico.icms_modalidade)
            etree.SubElement(icms_item, 'orig').text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, 'CST').text = '41'          # Nao tributado
            etree.SubElement(icms_item, 'vBCSTRet').text = ''       # Informar o valor da BC do ICMS ST retido na UF remetente
            etree.SubElement(icms_item, 'vICMSSTRet').text = ''     # Informar o valor do ICMS ST retido na UF remetente
            etree.SubElement(icms_item, 'vBCSTDest').text = ''      # Informar o valor da BC do ICMS ST da UF destino
            etree.SubElement(icms_item, 'vICMSSTDest').text = ''    # Informar o valor do ICMS ST da UF destino
        else:
            # FIXME
            ### OUTROS TIPOS DE ICMS
            etree.SubElement(icms_item, 'modBC').text = str(produto_servico.icms_modalidade_determinacao_bc)
            etree.SubElement(icms_item, 'vBC').text = str(produto_servico.icms_valor_base_calculo)
            etree.SubElement(icms_item, 'pICMS').text = str(produto_servico.icms_aliquota)
            etree.SubElement(icms_item, 'vICMS').text = str(produto_servico.icms_valor)

        # apenas nfe
        pisnt = ('04','05','06','07','08','09')
        if modelo == 55:
            ## PIS
            pis = etree.SubElement(imposto, 'PIS')
            if produto_servico.pis_modalidade in pisnt:
                pis_item = etree.SubElement(pis, 'PISNT')
                etree.SubElement(pis_item, 'CST').text = produto_servico.pis_modalidade
            elif produto_servico.pis_modalidade == '01' or produto_servico.pis_modalidade == '02':
                pis_item = etree.SubElement(pis, 'PISAliq')
                etree.SubElement(pis_item, 'CST').text = produto_servico.pis_modalidade
                etree.SubElement(pis_item, 'vBC').text = produto_servico.pis_valor_base_calculo
                etree.SubElement(pis_item, 'pPIS').text = produto_servico.pis_aliquota_percentual
                etree.SubElement(pis_item, 'vPIS').text = produto_servico.pis_valor
            elif produto_servico.pis_modalidade == '03':
                pis_item = etree.SubElement(pis, 'PISQtde')
                etree.SubElement(pis_item, 'CST').text = produto_servico.pis_modalidade
                etree.SubElement(pis_item, 'qBCProd').text = produto_servico.quantidade_comercial
                etree.SubElement(pis_item, 'vAliqProd').text = produto_servico.pis_aliquota_percentual
                etree.SubElement(pis_item, 'vPIS').text = produto_servico.pis_valor_base_calculo
            else:
                pis_item = etree.SubElement(pis, 'PISOutr')
                etree.SubElement(pis_item, 'CST').text = produto_servico.pis_modalidade
                etree.SubElement(pis_item, 'vBC').text = produto_servico.pis_valor_base_calculo
                etree.SubElement(pis_item, 'pPIS').text = produto_servico.pis_aliquota_percentual
                if produto_servico.pis_modalidade is not '99':
                    etree.SubElement(pis_item, 'qBCProd').text = produto_servico.quantidade_comercial
                    etree.SubElement(pis_item, 'vAliqProd').text = produto_servico.pis_aliquota_percentual
                etree.SubElement(pis_item, 'vPIS').text = produto_servico.pis_valor_base_calculo

                ## PISST
                # pis_item = etree.SubElement(pis, 'PISST')
                # etree.SubElement(pis_item, 'vBC').text = produto_servico.pis_valor_base_calculo
                # etree.SubElement(pis_item, 'pPIS').text = produto_servico.pis_aliquota_percentual
                # etree.SubElement(pis_item, 'qBCProd').text = produto_servico.quantidade_comercial
                # etree.SubElement(pis_item, 'vAliqProd').text = produto_servico.pis_aliquota_percentual
                # etree.SubElement(pis_item, 'vPIS').text = produto_servico.pis_valor_base_calculo

            cofinsnt = ('04','05','06','07','08','09')
            ## COFINS
            cofins = etree.SubElement(imposto, 'COFINS')
            if produto_servico.cofins_modalidade in cofinsnt:
                cofins_item = etree.SubElement(cofins, 'COFINSNT')
                etree.SubElement(cofins_item, 'CST').text = produto_servico.cofins_modalidade
            elif produto_servico.cofins_modalidade == '01' or produto_servico.cofins_modalidade == '02':
                cofins_item = etree.SubElement(cofins, 'COFINSAliq')
                etree.SubElement(cofins_item, 'CST').text = produto_servico.cofins_modalidade
                etree.SubElement(cofins_item, 'vBC').text = produto_servico.cofins_valor_base_calculo
                etree.SubElement(cofins_item, 'pCOFINS').text = produto_servico.cofins_aliquota_percentual
                etree.SubElement(cofins_item, 'vCOFINS').text = produto_servico.cofins_valor
            elif produto_servico.cofins_modalidade == '03':
                cofins_item = etree.SubElement(cofins, 'COFINSQtde')
                etree.SubElement(cofins_item, 'CST').text = produto_servico.cofins_modalidade
                etree.SubElement(cofins_item, 'qBCProd').text = produto_servico.quantidade_comercial
                etree.SubElement(cofins_item, 'vAliqProd').text = produto_servico.cofins_aliquota_percentual
                etree.SubElement(cofins_item, 'vCOFINS').text = produto_servico.cofins_valor
            else:
                cofins_item = etree.SubElement(cofins, 'COFINSOutr')
                etree.SubElement(cofins_item, 'CST').text = produto_servico.cofins_modalidade
                etree.SubElement(cofins_item, 'vBC').text = produto_servico.cofins_valor_base_calculo
                etree.SubElement(cofins_item, 'pCOFINS').text = produto_servico.cofins_aliquota_percentual
                if produto_servico.cofins_modalidade is not '99':
                    etree.SubElement(cofins_item, 'vAliqProd').text = produto_servico.cofins_aliquota_percentual
                etree.SubElement(cofins_item, 'vCOFINS').text = produto_servico.cofins_valor

                ## COFINSST
                # cofins_item = etree.SubElement(cofins, 'COFINSOutr')
                # etree.SubElement(cofins_item, 'vBC').text = produto_servico.cofins_valor_base_calculo
                # etree.SubElement(cofins_item, 'pCOFINS').text = produto_servico.cofins_aliquota_percentual
                # etree.SubElement(cofins_item, 'qBCProd').text = produto_servico.quantidade_comercial
                # etree.SubElement(cofins_item, 'vAliqProd').text = produto_servico.cofins_aliquota_percentual
                # etree.SubElement(cofins_item, 'vCOFINS').text = produto_servico.cofins_valor

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_nota_fiscal(self, nota_fiscal, tag_raiz='infNFe', retorna_string=True):
        #raiz = etree.Element('NFe', xmlns='http://www.portalfiscal.inf.br/nfe')
        raiz = etree.Element(tag_raiz, versao=self._versao)

        # 'Id' da tag raiz
        # Ex.: NFe35080599999090910270550010000000011518005123
        raiz.attrib['Id'] = nota_fiscal.identificador_unico

        # timezone Brasília -03:00
        # bug no python < 3.5 no windows
        # http://bugs.python.org/issue20010
        # TODO utilizar assim quando python superior a 3.5
        # tz = time.strftime("%z")
        from datetime import datetime
        from dateutil import tz
        tz = datetime.now(tz.tzlocal()).strftime('%z')
        tz = "{}:{}".format(tz[:-2], tz[-2:])

        # Dados da Nota Fiscal
        ide = etree.SubElement(raiz, 'ide')
        etree.SubElement(ide, 'cUF').text = CODIGOS_ESTADOS[nota_fiscal.uf]
        etree.SubElement(ide, 'cNF').text = nota_fiscal.codigo_numerico_aleatorio
        etree.SubElement(ide, 'natOp').text = nota_fiscal.natureza_operacao
        etree.SubElement(ide, 'indPag').text = str(nota_fiscal.forma_pagamento)
        etree.SubElement(ide, 'mod').text = str(nota_fiscal.modelo)
        etree.SubElement(ide, 'serie').text = nota_fiscal.serie
        etree.SubElement(ide, 'nNF').text = str(nota_fiscal.numero_nf)
        etree.SubElement(ide, 'dhEmi').text = nota_fiscal.data_emissao.strftime('%Y-%m-%dT%H:%M:%S') + tz
        #etree.SubElement(ide, 'dhSaiEnt').text = nota_fiscal.data_saida_entrada.strftime('%Y-%m-%dT%H:%M:%S') + tz
        """dhCont Data e Hora da entrada em contingência E B01 D 0-1 Formato AAAA-MM-DDThh:mm:ssTZD (UTC - Universal
            Coordinated Time)
            Exemplo: no formato UTC para os campos de Data-Hora, "TZD" pode ser -02:00 (Fernando de Noronha), -03:00 (Brasília) ou -04:00 (Manaus), no
            horário de verão serão -01:00, -02:00 e -03:00. Exemplo: "2010-08-19T13:00:15-03:00".
        """
        etree.SubElement(ide, 'tpNF').text = str(nota_fiscal.tipo_documento)  # 0=entrada 1=saida
        """ nfce suporta apenas operação interna
            Identificador de local de destino da operação 1=Operação interna;2=Operação interestadual;3=Operação com exterior.
        """
        if nota_fiscal.modelo == 65:
            etree.SubElement(ide, 'idDest').text = str(1)
        else:
            etree.SubElement(ide, 'idDest').text = str(nota_fiscal.indicador_destino)
        etree.SubElement(ide, 'cMunFG').text = nota_fiscal.municipio
        etree.SubElement(ide, 'tpImp').text = str(nota_fiscal.tipo_impressao_danfe)
        """ ### CONTINGENCIA ###
            1=Emissão normal (não em contingência);
            2=Contingência FS-IA, com impressão do DANFE em formulário de segurança;
            3=Contingência SCAN (Sistema de Contingência do Ambiente Nacional);
            4=Contingência DPEC (Declaração Prévia da Emissão em Contingência);
            5=Contingência FS-DA, com impressão do DANFE em formulário de segurança;
            6=Contingência SVC-AN (SEFAZ Virtual de Contingência do AN);
            7=Contingência SVC-RS (SEFAZ Virtual de Contingência do RS);
            9=Contingência off-line da NFC-e (as demais opções de contingência são válidas também para a NFC-e).
            Para a NFC-e somente estão disponíveis e são válidas as opções de contingência 5 e 9.
        """
        if self._contingencia != None:
            if nota_fiscal.forma_emissao == '1':
                nota_fiscal.forma_emissao = '9'
        etree.SubElement(ide, 'tpEmis').text = str(nota_fiscal.forma_emissao)
        etree.SubElement(ide, 'cDV').text = nota_fiscal.dv_codigo_numerico_aleatorio
        etree.SubElement(ide, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(ide, 'finNFe').text = str(nota_fiscal.finalidade_emissao)
        if nota_fiscal.modelo == 65:
            etree.SubElement(ide, 'indFinal').text = str(1)
            etree.SubElement(ide, 'indPres').text = str(1)
        else:
            etree.SubElement(ide, 'indFinal').text = str(nota_fiscal.cliente_final)
            etree.SubElement(ide, 'indPres').text = str(nota_fiscal.indicador_presencial)
        etree.SubElement(ide, 'procEmi').text = str(nota_fiscal.processo_emissao)
        etree.SubElement(ide, 'verProc').text = '%s %s'%(self._nome_aplicacao, nota_fiscal.versao_processo_emissao)
        ### CONTINGENCIA ###
        if self._contingencia != None:
            etree.SubElement(ide, 'dhCont').text = nota_fiscal.data_emissao.strftime('%Y-%m-%dT%H:%M:%S') + tz # Data e Hora da entrada em contingência AAAA-MM-DDThh:mm:ssTZD
            etree.SubElement(ide, 'xJust').text = nota_fiscal.self._contingencia  # Justificativa da entrada em contingência (min 20, max 256 caracteres)

        # Emitente
        raiz.append(self._serializar_emitente(nota_fiscal.emitente, retorna_string=False))

        # Destinatário
        try:
            raiz.append(self._serializar_cliente(nota_fiscal.cliente, modelo=nota_fiscal.modelo, retorna_string=False))
        except AttributeError as e:
            # NFC-e pode ser gerada sem destinatário
            if nota_fiscal.modelo == 65:
                pass
            else:
                raise e
        # Retirada
        if nota_fiscal.retirada:
            raiz.append(self._serializar_entrega_retirada(
                nota_fiscal.retirada,
                retorna_string=False,
                tag_raiz='retirada',
                ))

        # Entrega
        if nota_fiscal.entrega:
            raiz.append(self._serializar_entrega_retirada(
                nota_fiscal.entrega,
                retorna_string=False,
                tag_raiz='entrega',
                ))

        # Itens
        for num, item in enumerate(nota_fiscal.produtos_e_servicos):
            det = self._serializar_produto_servico(item, modelo=nota_fiscal.modelo, retorna_string=False)
            det.attrib['nItem'] = str(num+1)

            raiz.append(det)

        # Totais
        total = etree.SubElement(raiz, 'total')
        icms_total = etree.SubElement(total, 'ICMSTot')
        #etree.SubElement(icms_total, 'vBC').text = str(nota_fiscal.totais_icms_base_calculo)
        etree.SubElement(icms_total, 'vBC').text = '{:.2f}'.format(nota_fiscal.totais_icms_base_calculo)
        etree.SubElement(icms_total, 'vICMS').text = '{:.2f}'.format(nota_fiscal.totais_icms_total)
        etree.SubElement(icms_total, 'vICMSDeson').text = '{:.2f}'.format(nota_fiscal.totais_icms_desonerado)  # Valor Total do ICMS desonerado
        etree.SubElement(icms_total, 'vBCST').text = '{:.2f}'.format(nota_fiscal.totais_icms_st_base_calculo)
        etree.SubElement(icms_total, 'vST').text = '{:.2f}'.format(nota_fiscal.totais_icms_st_total)
        etree.SubElement(icms_total, 'vProd').text = str(nota_fiscal.totais_icms_total_produtos_e_servicos)
        etree.SubElement(icms_total, 'vFrete').text = '{:.2f}'.format(nota_fiscal.totais_icms_total_frete)
        etree.SubElement(icms_total, 'vSeg').text = '{:.2f}'.format(nota_fiscal.totais_icms_total_seguro)
        etree.SubElement(icms_total, 'vDesc').text = '{:.2f}'.format(nota_fiscal.totais_icms_total_desconto)

        # Tributos
        etree.SubElement(icms_total, 'vII').text = '{:.2f}'.format(nota_fiscal.totais_icms_total_ii)
        etree.SubElement(icms_total, 'vIPI').text = '{:.2f}'.format(nota_fiscal.totais_icms_total_ipi)
        etree.SubElement(icms_total, 'vPIS').text = '{:.2f}'.format(nota_fiscal.totais_icms_pis)
        etree.SubElement(icms_total, 'vCOFINS').text = '{:.2f}'.format(nota_fiscal.totais_icms_cofins)

        etree.SubElement(icms_total, 'vOutro').text = '{:.2f}'.format(nota_fiscal.totais_icms_outras_despesas_acessorias)
        etree.SubElement(icms_total, 'vNF').text = str(nota_fiscal.totais_icms_total_nota)
        if nota_fiscal.totais_tributos_aproximado:
            etree.SubElement(icms_total, 'vTotTrib').text = '{:.2f}'.format(nota_fiscal.totais_tributos_aproximado)

        # Apenas NF-e
        if nota_fiscal.modelo == 55:

            # Transporte
            transp = etree.SubElement(raiz, 'transp')
            etree.SubElement(transp, 'modFrete').text = str(nota_fiscal.transporte_modalidade_frete)

            # Transportadora
            if nota_fiscal.transporte_transportadora:
                transp.append(self._serializar_transportadora(
                    nota_fiscal.transporte_transportadora,
                    retorna_string=False,
                    ))

            # Veículo
            if nota_fiscal.transporte_veiculo_placa and nota_fiscal.transporte_veiculo_uf:
                veiculo = etree.SubElement(transp, 'veicTransp')
                etree.SubElement(veiculo, 'placa').text = nota_fiscal.transporte_veiculo_placa # Obrigatório EX: XXX9999
                etree.SubElement(veiculo, 'UF').text = nota_fiscal.transporte_veiculo_uf
                # Registro Nacional de Transportador de Carga (ANTT)
                if nota_fiscal.transporte_veiculo_rntc:
                    etree.SubElement(veiculo, 'RNTC').text = nota_fiscal.transporte_veiculo_rntc

            # Reboque
            if nota_fiscal.transporte_reboque_placa and nota_fiscal.transporte_reboque_uf:
                reboque = etree.SubElement(transp, 'reboque')
                etree.SubElement(reboque, 'placa').text = nota_fiscal.transporte_reboque_placa
                etree.SubElement(reboque, 'UF').text = nota_fiscal.transporte_reboque_uf
                # Registro Nacional de Transportador de Carga (ANTT)
                if nota_fiscal.transporte_reboque_rntc:
                    etree.SubElement(reboque, 'RNTC').text = nota_fiscal.transporte_reboque_rntc

            # Volumes
            if nota_fiscal.transporte_volumes:
                for volume in nota_fiscal.transporte_volumes:
                    vol = etree.SubElement(transp, 'vol')
                    etree.SubElement(vol, 'qVol').text = str(volume.quantidade)
                    etree.SubElement(vol, 'esp').text = volume.especie
                    etree.SubElement(vol, 'marca').text = volume.marca
                    etree.SubElement(vol, 'nVol').text = volume.numeracao
                    etree.SubElement(vol, 'pesoL').text = str(volume.peso_liquido)
                    etree.SubElement(vol, 'pesoB').text = str(volume.peso_bruto)

                    # Lacres
                    if volume.lacres:
                        lacres = etree.SubElement(vol, 'lacres')
                        for lacre in volume.lacres:
                            etree.SubElement(lacres, 'nLacre').text = lacre.numero_lacre

        # Somente NFC-e
        """ Grupo obrigatório para a NFC-e, a critério da UF. Não informar para a NF-e (modelo 55). """
        if nota_fiscal.modelo == 65:
            # Transporte
            transp = etree.SubElement(raiz, 'transp')
            etree.SubElement(transp, 'modFrete').text = str(9)
            # Pagamento
            pag = etree.SubElement(raiz, 'pag')
            etree.SubElement(pag, 'tPag').text = str(nota_fiscal.tipo_pagamento).zfill(2) # 01=Dinheiro 02=Cheque 03=Cartão de Crédito 04=Cartão de Débito 05=Crédito Loja 10=Vale Alimentação 11=Vale Refeição 12=Vale Presente 13=Vale Combustível 99=Outros
            etree.SubElement(pag, 'vPag').text = '{:.2f}'.format(nota_fiscal.totais_icms_total_nota)
            # Cartão NT2015.002
            cartao = etree.SubElement(pag, 'card')
            """ Tipo de Integração do processo de pagamento com o sistema de automação da empresa:
                1=Pagamento integrado com o sistema de automação da empresa (Ex.: equipamento TEF, Comércio Eletrônico);
                2= Pagamento não integrado com o sistema de automação da empresa (Ex.: equipamento POS);
            """
            etree.SubElement(cartao, 'tpIntegra').text = '2'
            #etree.SubElement(cartao, 'CNPJ').text = '' # Informar o CNPJ da Credenciadora de cartão de crédito / débito
            #etree.SubElement(cartao, 'tBand').text = '' # 01=Visa 02=Mastercard 03=American Express 04=Sorocred 99=Outros
            #etree.SubElement(cartao, 'cAut').text = '' # Identifica o número da autorização da transação da operação com cartão de crédito e/ou débito

        # Informações adicionais
        if nota_fiscal.informacoes_adicionais_interesse_fisco or nota_fiscal.informacoes_complementares_interesse_contribuinte:
            info_ad = etree.SubElement(raiz, 'infAdic')
            if nota_fiscal.informacoes_adicionais_interesse_fisco:
                etree.SubElement(info_ad, 'infAdFisco').text = nota_fiscal.informacoes_adicionais_interesse_fisco
            if nota_fiscal.informacoes_complementares_interesse_contribuinte:
                etree.SubElement(info_ad, 'infCpl').text = nota_fiscal.informacoes_complementares_interesse_contribuinte

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_evento(self, evento, tag_raiz='evento', retorna_string=False):

        # timezone Brasília -03:00
        tz = time.strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])
        #import ipdb
        #ipdb.set_trace()
        raiz = etree.Element(tag_raiz, versao='1.00', xmlns=NAMESPACE_NFE)
        e = etree.SubElement(raiz, 'infEvento', Id=evento.identificador)
        etree.SubElement(e, 'cOrgao').text = CODIGOS_ESTADOS[evento.uf.upper()]
        etree.SubElement(e, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(e, 'CNPJ').text = evento.cnpj # Empresas somente terão CNPJ
        #etree.SubElement(e, 'CPF').text = ''
        etree.SubElement(e, 'chNFe').text = evento.chave
        etree.SubElement(e, 'dhEvento').text = evento.data_emissao.strftime('%Y-%m-%dT%H:%M:%S') + tz
        etree.SubElement(e, 'tpEvento').text = evento.tp_evento
        etree.SubElement(e, 'nSeqEvento').text = str(evento.n_seq_evento)
        etree.SubElement(e, 'verEvento').text = '1.00'
        det = etree.SubElement(e, 'detEvento', versao='1.00')
        etree.SubElement(det, 'descEvento').text = evento.descricao
        etree.SubElement(det, 'nProt').text = evento.protocolo
        etree.SubElement(det, 'xJust').text = evento.justificativa

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz


class SerializacaoQrcode(object):
    """ Classe que gera e serializa o qrcode de NFC-e no xml """
    def gerar_qrcode(self, token, csc, xml, return_qr=False):
        """ Classe para gerar url do qrcode da NFC-e """
        # Procura atributos no xml
        ns = {'ns':'http://www.portalfiscal.inf.br/nfe'}
        sig = {'sig':'http://www.w3.org/2000/09/xmldsig#'}
        # Tag Raiz NFe Ex: <NFe>
        nfe = xml
        chave = nfe[0].attrib['Id'].replace('NFe','')
        data = nfe.xpath('ns:infNFe/ns:ide/ns:dhEmi/text()', namespaces=ns)[0].encode()
        tpamb = nfe.xpath('ns:infNFe/ns:ide/ns:tpAmb/text()', namespaces=ns)[0]
        cuf = nfe.xpath('ns:infNFe/ns:ide/ns:cUF/text()', namespaces=ns)[0]
        uf = [key for key, value in CODIGOS_ESTADOS.items() if value == cuf][0]

        # tenta encontrar a tag cpf
        try:
            cpf = nfe.xpath('ns:infNFe/ns:dest/ns:CPF/text()', namespaces=ns)[0]
        except IndexError:
            # em caso de erro tenta procurar a tag cnpj
            try:
                cpf = nfe.xpath('ns:infNFe/ns:dest/ns:CNPJ/text()', namespaces=ns)[0]
            except IndexError:
                cpf = None
        total = nfe.xpath('ns:infNFe/ns:total/ns:ICMSTot/ns:vNF/text()', namespaces=ns)[0]
        icms = nfe.xpath('ns:infNFe/ns:total/ns:ICMSTot/ns:vICMS/text()', namespaces=ns)[0]
        digest = nfe.xpath('sig:Signature/sig:SignedInfo/sig:Reference/sig:DigestValue/text()', namespaces=sig)[0].encode()

        data = base64.b16encode(data).decode()
        digest = base64.b16encode(digest).decode()

        if cpf is None:
            url = 'chNFe={}&nVersao={}&tpAmb={}&dhEmi={}&vNF={}&vICMS={}&digVal={}&cIdToken={}'.format(
                   chave, VERSAO_QRCODE, tpamb, data.lower(), total, icms, digest.lower(), token)
        else:
            url = 'chNFe={}&nVersao={}&tpAmb={}&cDest={}&dhEmi={}&vNF={}&vICMS={}&digVal={}&cIdToken={}'.format(
                   chave, VERSAO_QRCODE, tpamb, cpf, data.lower(), total, icms, digest.lower(), token)

        url_hash = hashlib.sha1(url.encode()+csc.encode()).digest()
        url_hash = base64.b16encode(url_hash).decode()

        url = url + '&cHashQRCode=' + url_hash.upper()

        if uf.upper() == 'PR':
            qrcode = NFCE[uf.upper()]['QR'] + url
        else:
            if tpamb == '1':
                qrcode = NFCE[uf.upper()]['HTTPS'] + NFCE[uf.upper()]['QR'] + url
            else:
                qrcode = NFCE[uf.upper()]['HOMOLOGACAO'] + NFCE[uf.upper()]['QR'] + url

        # adicionta tag infNFeSupl com qrcode
        info = etree.Element('infNFeSupl')
        etree.SubElement(info, 'qrCode').text = '<![CDATA['+ qrcode.strip() + ']]>'
        nfe.insert(1, info)
        # correção da tag qrCode, retira caracteres pois e CDATA
        tnfe = etree.tostring(nfe, encoding='unicode')
        etree.tostring(nfe.find(".//qrCode"), encoding='unicode') \
            .replace('\n','').replace('&lt;','<').replace('&gt;','>').replace('amp;','')
        nfe = etree.fromstring(tnfe)
        # retorna nfe com o qrcode incluido NT2015/002 e qrcode
        if return_qr:
            return nfe, qrcode.strip()
        # retorna apenas nfe com o qrcode incluido NT2015/002
        else:
            return nfe


class SerializacaoNfse(object):
    def __init__(self, autorizador):
        "Recebe uma string com o nome do autorizador."
        self.autorizador = autorizador

    def gerar(self, nfse):
        if self.autorizador.lower() == 'betha':
            from pynfe.processamento.autorizador_nfse import SerializacaoBetha
            return SerializacaoBetha().gerar(nfse)
        else:
            raise Exception('Este método só esta implementado no autorizador Betha.')

    def gerar_lote(self, nfse):
        if self.autorizador.lower() == 'ginfes':
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes
            return SerializacaoGinfes().serializar_lote_assincrono(nfse)
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def consultar_nfse(self, emitente, numero=None, inicio=None, fim=None):
        if self.autorizador.lower() == 'ginfes':
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes
            return SerializacaoGinfes().consultar_nfse(emitente, numero, inicio, fim)
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def consultar_lote(self, emitente, numero):
        if self.autorizador.lower() == 'ginfes':
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes
            return SerializacaoGinfes().consultar_lote(emitente, numero)
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def consultar_rps(self, emitente, numero, serie, tipo):
        if self.autorizador.lower() == 'ginfes':
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes
            return SerializacaoGinfes().consultar_rps(emitente, numero, serie, tipo)
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def consultar_situacao_lote(self, emitente, numero):
        if self.autorizador.lower() == 'ginfes':
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes
            return SerializacaoGinfes().consultar_situacao_lote(emitente, numero)
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def cancelar(self, nfse):
        if self.autorizador.lower() == 'ginfes':
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes
            ## versao 3
            #return SerializacaoGinfes().cancelar(nfse)
            ## versao 2
            return SerializacaoGinfes().cancelar_v2(nfse)
        elif self.autorizador.lower() == 'betha':
            from pynfe.processamento.autorizador_nfse import SerializacaoBetha
            return SerializacaoBetha().cancelar(nfse)
        else:
            raise Exception('Autorizador não suportado para cancelamento!')


class SerializacaoPipes(Serializacao):
    """Serialização utilizada pela SEFAZ-SP para a importação de notas."""

    def exportar(self, destino, **kwargs):
        pass

    def _serializar_emitente(self, emitente, retorna_string=True):

        cod_municipio, municipio = obter_municipio_e_codigo(
            dict(codigo=emitente.endereco_cod_municipio,
                 municipio=emitente.endereco_municipio),
            emitente.endereco_uf
        )

        serial_emitente_list = [
            '\nC',
            emitente.razao_social,
            emitente.nome_fantasia,
            emitente.inscricao_estadual,
            emitente.inscricao_estadual_subst_tributaria,
            emitente.inscricao_municipal,
            emitente.cnae_fiscal,
            emitente.codigo_de_regime_tributario,
            '\nC02',
            emitente.cnpj,
            '\nC05',
            emitente.endereco_logradouro,
            emitente.endereco_numero,
            emitente.endereco_complemento,
            emitente.endereco_bairro,
            cod_municipio,
            municipio,
            obter_uf_por_codigo(emitente.endereco_uf),
            emitente.endereco_cep.replace('-',''),
            emitente.endereco_pais,
            obter_pais_por_codigo(emitente.endereco_pais),
            emitente.endereco_telefone,
        ]

        if retorna_string:
            return '|'.join(map(str,serial_emitente_list))
        return serial_emitente_list

    def _serializar_cliente(self, cliente, retorna_string=True):

        cod_municipio, municipio = obter_municipio_e_codigo(
            dict(codigo=cliente.endereco_cod_municipio,
                 municipio=cliente.endereco_municipio),
            cliente.endereco_uf
        )

        serial_data = [
            '\nE',
            cliente.razao_social,
            '2', # indIEDest
            cliente.inscricao_estadual,
            cliente.inscricao_suframa,
            '', # IM
            cliente.email,
            '\nE02' if cliente.tipo_documento == 'CNPJ' else '\nE03',
            cliente.numero_documento,
            '\nE05',
            cliente.endereco_logradouro,
            cliente.endereco_numero,
            cliente.endereco_complemento,
            cliente.endereco_bairro,
            cod_municipio,
            municipio,
            obter_uf_por_codigo(cliente.endereco_uf),
            cliente.endereco_cep.replace('-',''),
            cliente.endereco_pais,
            obter_pais_por_codigo(cliente.endereco_pais),
            cliente.endereco_telefone
        ]

        if retorna_string:
            return '|'.join(map(str,serial_data))
        return serial_data

    def _serializar_produto_servico(self, produto_servico, retorna_string=True):
        serial_data = [
            '\nI',
            produto_servico.codigo,
            produto_servico.ean,
            produto_servico.descricao,
            produto_servico.ncm,
            produto_servico.ex_tipi,
            produto_servico.cfop,
            produto_servico.unidade_comercial,
            formatar_decimal(produto_servico.quantidade_comercial),
            formatar_decimal(produto_servico.valor_unitario_comercial),
            formatar_decimal(produto_servico.valor_total_bruto),
            produto_servico.ean_tributavel,
            produto_servico.unidade_tributavel,
            formatar_decimal(produto_servico.quantidade_tributavel),
            formatar_decimal(produto_servico.valor_unitario_tributavel),
            formatar_decimal(produto_servico.total_frete) if produto_servico.total_frete else '',
            formatar_decimal(produto_servico.total_seguro) if produto_servico.total_seguro else '',
            formatar_decimal(produto_servico.desconto) if produto_servico.desconto else '',
            formatar_decimal(produto_servico.outras_despesas_acessorias) if produto_servico.outras_despesas_acessorias else '',
            produto_servico.compoe_valor_total,
            produto_servico.numero_pedido,
            produto_servico.numero_do_item,
            '', # nFCI
            '\nM', #IMPOSTOS
            '\nN', #ICMS
            '\nN06',
            produto_servico.icms_origem,
            produto_servico.icms_modalidade_determinacao_bc,
            produto_servico.icms_valor if produto_servico.icms_valor else '',
            produto_servico.icms_motivo_desoneracao if produto_servico.icms_valor else '',
            '\nQ', #PIS
            '\nQ02',
            produto_servico.pis_tipo_calculo,
            formatar_decimal(produto_servico.pis_valor_base_calculo),
            formatar_decimal(produto_servico.pis_aliquota_percentual),
            formatar_decimal(produto_servico.pis_valor),
            '\nS', #COFINS
            '\nS02',
            produto_servico.cofins_situacao_tributaria,
            formatar_decimal(produto_servico.cofins_valor_base_calculo),
            formatar_decimal(produto_servico.cofins_aliquota_percentual),
            formatar_decimal(produto_servico.cofins_valor)
        ]

        if retorna_string:
            return '|'.join(map(str, serial_data))
        return serial_data

    def _serializar_nota_fiscal(self, nota_fiscal, retorna_string=True):

        cod_municipio, municipio = obter_municipio_e_codigo(
            dict(codigo='',
                 municipio=nota_fiscal.municipio),
            nota_fiscal.uf
        )

        if nota_fiscal.emitente.endereco_uf == nota_fiscal.cliente.endereco_uf:
            id_dest = '1'
        else:
            id_dest = '2'

        tz = time.strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])

        serial_data = [
            'A',
            '3.10',
            nota_fiscal.identificador_unico,
            '\nB',
            CODIGOS_ESTADOS.get(nota_fiscal.uf, nota_fiscal.uf),
            nota_fiscal.codigo_numerico_aleatorio,
            nota_fiscal.natureza_operacao,
            nota_fiscal.forma_pagamento,
            nota_fiscal.modelo,
            nota_fiscal.serie,
            nota_fiscal.numero_nf,
            nota_fiscal.data_emissao.strftime('%Y-%m-%dT%H:%M:%S') + tz,
            nota_fiscal.data_saida_entrada.strftime('%Y-%m-%dT%H:%M:%S') + tz,
            nota_fiscal.tipo_documento,
            id_dest,  # idDest
            cod_municipio,
            nota_fiscal.tipo_impressao_danfe,
            nota_fiscal.forma_emissao,
            nota_fiscal.dv_codigo_numerico_aleatorio,
            self._ambiente,
            nota_fiscal.finalidade_emissao,
            nota_fiscal.cliente_final,  # indFinal
            nota_fiscal.indicador_presencial,  # indPres
            nota_fiscal.processo_emissao,
            '%s %s' % (self._nome_aplicacao,
                       nota_fiscal.versao_processo_emissao),
            '',  # dhCont - Data e Hora da entrada em contingência
            '',  # xJust - Justificativa da entrada em contingência
        ]

        serial_data += self._serializar_emitente(nota_fiscal.emitente,
                                                 retorna_string=False)
        serial_data += self._serializar_cliente(nota_fiscal.cliente,
                                                retorna_string=False)

        # Produtos e serviços
        produtos_servicos = enumerate(nota_fiscal.produtos_e_servicos, start=1)
        for num, produto_servico in produtos_servicos:
            num_produto = [
                '\nH',
                num, # Número do produto na lista
                ''
                '' # End Pipe
            ]
            serial_data += num_produto
            serial_data += self._serializar_produto_servico(produto_servico,
                                                        retorna_string=False)

        serial_data += [
            '\nW', #Valores totais NFe,
            '\nW02',
            formatar_decimal(nota_fiscal.totais_icms_base_calculo),
            formatar_decimal(nota_fiscal.totais_icms_total),
            '', # ICMSDeson
            formatar_decimal(nota_fiscal.totais_icms_st_base_calculo),
            formatar_decimal(nota_fiscal.totais_icms_st_total),
            formatar_decimal(nota_fiscal.totais_icms_total_produtos_e_servicos),
            formatar_decimal(nota_fiscal.totais_icms_total_frete),
            formatar_decimal(nota_fiscal.totais_icms_total_seguro),
            formatar_decimal(nota_fiscal.totais_icms_total_desconto),
            formatar_decimal(nota_fiscal.totais_icms_total_ii),
            formatar_decimal(nota_fiscal.totais_icms_total_ipi),
            formatar_decimal(nota_fiscal.totais_icms_pis),
            formatar_decimal(nota_fiscal.totais_icms_cofins),
            formatar_decimal(nota_fiscal.totais_icms_outras_despesas_acessorias),
            formatar_decimal(nota_fiscal.totais_icms_total_nota),
            '', # vTotTrib
            '\nX',
            nota_fiscal.transporte_modalidade_frete,
            '\nZ',
            nota_fiscal.informacoes_adicionais_interesse_fisco,
            nota_fiscal.informacoes_complementares_interesse_contribuinte,
            '' # End Pipe
        ]

        if retorna_string:
            try:
                return '|'.join(map(remover_acentos, serial_data))
            except TypeError as err:
                enum_args = '\n'.join(
                    map(
                        lambda x: str(x[0]) + ' ' + str(x[1]),
                        enumerate(serial_data)
                    )
                )
                message = err.message + '\n' + enum_args
                raise TypeError(message)

        return serial_data
