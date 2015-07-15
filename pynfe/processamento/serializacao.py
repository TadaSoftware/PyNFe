# -*- coding: utf-8 -*-

import time

from pynfe.entidades import NotaFiscal
from pynfe.utils import etree, so_numeros, obter_municipio_por_codigo, \
                        obter_pais_por_codigo, obter_municipio_e_codigo, \
                        formatar_decimal, safe_str, obter_uf_por_codigo, obter_codigo_por_municipio
from pynfe.utils.flags import CODIGOS_ESTADOS, VERSAO_PADRAO

class Serializacao(object):
    """Classe abstrata responsavel por fornecer as funcionalidades basicas para
    exportacao e importacao de Notas Fiscais eletronicas para formatos serializados
    de arquivos. Como XML, JSON, binario, etc.

    Nao deve ser instanciada diretamente!"""

    _fonte_dados = None
    _ambiente = 1   # 1 = Produção, 2 = Homologação
    _nome_aplicacao = 'PyNFe'

    def __new__(cls, *args, **kwargs):
        if cls == Serializacao:
            raise Exception('Esta classe nao pode ser instanciada diretamente!')
        else:
            return super(Serializacao, cls).__new__(cls)

    def __init__(self, fonte_dados, homologacao=False):
        self._fonte_dados = fonte_dados
        self._ambiente = homologacao and 2 or 1

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

    def exportar(self, destino=None, retorna_string=False, **kwargs):
        """Gera o(s) arquivo(s) de Nota Fiscal eletronica no padrao oficial da SEFAZ
        e Receita Federal, para ser(em) enviado(s) para o webservice ou para ser(em)
        armazenado(s) em cache local."""

        # No raiz do XML de saida
        raiz = etree.Element('NFe', xmlns="http://www.portalfiscal.inf.br/nfe")

        # Carrega lista de Notas Fiscais
        notas_fiscais = self._fonte_dados.obter_lista(_classe=NotaFiscal, **kwargs)

        for nf in notas_fiscais:
            raiz.append(self._serializar_nota_fiscal(nf, retorna_string=False))

        if retorna_string:
            return etree.tostring(raiz, pretty_print=True).decode('utf-8')
        else:
            return raiz

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
        etree.SubElement(raiz, 'IE').text = emitente.inscricao_estadual

        # Endereço
        endereco = etree.SubElement(raiz, 'enderEmit')
        etree.SubElement(endereco, 'xLgr').text = emitente.endereco_logradouro
        etree.SubElement(endereco, 'nro').text = emitente.endereco_numero
        etree.SubElement(endereco, 'xCpl').text = emitente.endereco_complemento
        etree.SubElement(endereco, 'xBairro').text = emitente.endereco_bairro
        etree.SubElement(endereco, 'cMun').text = obter_codigo_por_municipio(
            emitente.endereco_municipio, emitente.endereco_uf)
        etree.SubElement(endereco, 'xMun').text = emitente.endereco_municipio
        etree.SubElement(endereco, 'UF').text = emitente.endereco_uf
        etree.SubElement(endereco, 'CEP').text = so_numeros(emitente.endereco_cep)
        etree.SubElement(endereco, 'cPais').text = emitente.endereco_pais
        etree.SubElement(endereco, 'xPais').text = obter_pais_por_codigo(emitente.endereco_pais)
        etree.SubElement(endereco, 'fone').text = emitente.endereco_telefone

        if retorna_string:
            return etree.tostring(raiz, pretty_print=True)
        else:
            return raiz

    def _serializar_cliente(self, cliente, modelo, tag_raiz='dest', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados do cliente (distinatario)
        etree.SubElement(raiz, cliente.tipo_documento).text = so_numeros(cliente.numero_documento)
        etree.SubElement(raiz, 'xNome').text = cliente.razao_social
        # nfc-e nao possui IE mesmo que seja uma empresa
        if modelo == 55:
            etree.SubElement(raiz, 'IE').text = cliente.inscricao_estadual
        # Endereço
        endereco = etree.SubElement(raiz, 'enderDest')
        etree.SubElement(endereco, 'xLgr').text = cliente.endereco_logradouro
        etree.SubElement(endereco, 'nro').text = cliente.endereco_numero
        etree.SubElement(endereco, 'xCpl').text = cliente.endereco_complemento
        etree.SubElement(endereco, 'xBairro').text = cliente.endereco_bairro
        etree.SubElement(endereco, 'cMun').text = obter_codigo_por_municipio(
            cliente.endereco_municipio, cliente.endereco_uf)
        etree.SubElement(endereco, 'xMun').text = cliente.endereco_municipio
        etree.SubElement(endereco, 'UF').text = cliente.endereco_uf
        etree.SubElement(endereco, 'CEP').text = so_numeros(cliente.endereco_cep)
        etree.SubElement(endereco, 'cPais').text = cliente.endereco_pais
        etree.SubElement(endereco, 'xPais').text = obter_pais_por_codigo(cliente.endereco_pais)
        etree.SubElement(endereco, 'fone').text = cliente.endereco_telefone

        if retorna_string:
            return etree.tostring(raiz, pretty_print=True)
        else:
            return raiz

    def _serializar_transportadora(self, transportadora, tag_raiz='transporta', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados da transportadora
        etree.SubElement(raiz, transportadora.tipo_documento).text = so_numeros(transportadora.numero_documento)
        etree.SubElement(raiz, 'xNome').text = transportadora.razao_social
        etree.SubElement(raiz, 'IE').text = transportadora.inscricao_estadual

        # Endereço
        etree.SubElement(raiz, 'xEnder').text = transportadora.endereco_logradouro
        etree.SubElement(raiz, 'cMun').text = transportadora.endereco_municipio
        etree.SubElement(raiz, 'xMun').text = obter_municipio_por_codigo(
                transportadora.endereco_municipio, transportadora.endereco_uf,
                )
        etree.SubElement(raiz, 'UF').text = transportadora.endereco_uf

        if retorna_string:
            return etree.tostring(raiz, pretty_print=True)
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
            return etree.tostring(raiz, pretty_print=True)
        else:
            return raiz

    def _serializar_produto_servico(self, produto_servico, tag_raiz='det', retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Produto
        prod = etree.SubElement(raiz, 'prod')
        etree.SubElement(prod, 'cProd').text = str(produto_servico.codigo)
        etree.SubElement(prod, 'cEAN').text = produto_servico.ean
        etree.SubElement(prod, 'xProd').text = produto_servico.descricao
        etree.SubElement(prod, 'CFOP').text = produto_servico.cfop
        etree.SubElement(prod, 'uCom').text = produto_servico.unidade_comercial
        etree.SubElement(prod, 'qCom').text = str(produto_servico.quantidade_comercial or 0)
        etree.SubElement(prod, 'vUnCom').text = str(produto_servico.valor_unitario_comercial or 0)
        etree.SubElement(prod, 'vProd').text = str(produto_servico.valor_total_bruto or 0)
        etree.SubElement(prod, 'cEANTrib').text = produto_servico.ean_tributavel
        etree.SubElement(prod, 'uTrib').text = produto_servico.unidade_tributavel
        etree.SubElement(prod, 'qTrib').text = str(produto_servico.quantidade_tributavel)
        etree.SubElement(prod, 'vUnTrib').text = str(produto_servico.valor_unitario_tributavel)

        # Imposto
        imposto = etree.SubElement(raiz, 'imposto')

        icms = etree.SubElement(imposto, 'ICMS')
        icms_item = etree.SubElement(icms, 'ICMS'+produto_servico.icms_situacao_tributaria)
        etree.SubElement(icms_item, 'orig').text = str(produto_servico.icms_origem)
        etree.SubElement(icms_item, 'CST').text = produto_servico.icms_situacao_tributaria
        etree.SubElement(icms_item, 'modBC').text = str(produto_servico.icms_modalidade_determinacao_bc)
        etree.SubElement(icms_item, 'vBC').text = str(produto_servico.icms_valor_base_calculo)
        etree.SubElement(icms_item, 'pICMS').text = str(produto_servico.icms_aliquota)
        etree.SubElement(icms_item, 'vICMS').text = str(produto_servico.icms_valor)

        pis = etree.SubElement(imposto, 'PIS')
        pis_item = etree.SubElement(pis, 'PISAliq')
        etree.SubElement(pis_item, 'CST').text = str(produto_servico.pis_situacao_tributaria)
        etree.SubElement(pis_item, 'vBC').text = str(produto_servico.pis_valor_base_calculo)
        etree.SubElement(pis_item, 'pPIS').text = str(produto_servico.pis_aliquota_percentual)
        etree.SubElement(pis_item, 'vPIS').text = str(produto_servico.pis_valor)

        cofins = etree.SubElement(imposto, 'COFINS')
        cofins_item = etree.SubElement(cofins, 'COFINSAliq')
        etree.SubElement(cofins_item, 'CST').text = str(produto_servico.cofins_situacao_tributaria)
        etree.SubElement(cofins_item, 'vBC').text = str(produto_servico.cofins_valor_base_calculo)
        etree.SubElement(cofins_item, 'pCOFINS').text = str(produto_servico.cofins_aliquota_percentual)
        etree.SubElement(cofins_item, 'vCOFINS').text = str(produto_servico.cofins_valor)

        if retorna_string:
            return etree.tostring(raiz, pretty_print=True)
        else:
            return raiz

    def _serializar_nota_fiscal(self, nota_fiscal, tag_raiz='infNFe', retorna_string=True):
        #raiz = etree.Element('NFe', xmlns='http://www.portalfiscal.inf.br/nfe')
        raiz = etree.Element(tag_raiz, versao=self._versao)

        # 'Id' da tag raiz
        # Ex.: NFe35080599999090910270550010000000011518005123
        raiz.attrib['Id'] = nota_fiscal.identificador_unico

        # timezone Brasília -03:00
        tz = time.strftime("%z")
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
        etree.SubElement(ide, 'dhSaiEnt').text = nota_fiscal.data_saida_entrada.strftime('%Y-%m-%dT%H:%M:%S') + tz
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
            etree.SubElement(ide, 'indPres').text = str(1)
            etree.SubElement(ide, 'indFinal').text = str(1)
        else:
            etree.SubElement(ide, 'idDest').text = str(nota_fiscal.indicador_destino)
            etree.SubElement(ide, 'indPres').text = str(nota_fiscal.indicador_presencial)
            etree.SubElement(ide, 'indFinal').text = str(nota_fiscal.cliente_final)
        etree.SubElement(ide, 'cMunFG').text = nota_fiscal.municipio
        etree.SubElement(ide, 'tpImp').text = str(nota_fiscal.tipo_impressao_danfe)
        etree.SubElement(ide, 'tpEmis').text = str(nota_fiscal.forma_emissao)
        etree.SubElement(ide, 'cDV').text = nota_fiscal.dv_codigo_numerico_aleatorio
        etree.SubElement(ide, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(ide, 'finNFe').text = str(nota_fiscal.finalidade_emissao)
        etree.SubElement(ide, 'procEmi').text = str(nota_fiscal.processo_emissao)
        etree.SubElement(ide, 'verProc').text = '%s %s'%(self._nome_aplicacao, nota_fiscal.versao_processo_emissao)
        ### CONTINGENCIA ###
        #etree.SubElement(ide, 'dhCont').text = '' # Data e Hora da entrada em contingência AAAA-MM-DDThh:mm:ssTZD
        #etree.SubElement(ide, 'xJust').text = ''  # Justificativa da entrada em contingência (min 20, max 256 caracteres)

        # Emitente
        raiz.append(self._serializar_emitente(nota_fiscal.emitente, retorna_string=False))

        # Destinatário
        raiz.append(self._serializar_cliente(nota_fiscal.cliente, modelo=nota_fiscal.modelo, retorna_string=False))

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
            det = self._serializar_produto_servico(item, retorna_string=False)
            det.attrib['nItem'] = str(num+1)

            raiz.append(det)

        # Totais
        total = etree.SubElement(raiz, 'total')
        icms_total = etree.SubElement(total, 'ICMSTot')
        etree.SubElement(icms_total, 'vBC').text = str(nota_fiscal.totais_icms_base_calculo)
        etree.SubElement(icms_total, 'vICMS').text = str(nota_fiscal.totais_icms_total)
        etree.SubElement(icms_total, 'vBCST').text = str(nota_fiscal.totais_icms_st_base_calculo)
        etree.SubElement(icms_total, 'vST').text = str(nota_fiscal.totais_icms_st_total)
        etree.SubElement(icms_total, 'vProd').text = str(nota_fiscal.totais_icms_total_produtos_e_servicos)
        etree.SubElement(icms_total, 'vFrete').text = str(nota_fiscal.totais_icms_total_frete)
        etree.SubElement(icms_total, 'vSeg').text = str(nota_fiscal.totais_icms_total_seguro)
        etree.SubElement(icms_total, 'vDesc').text = str(nota_fiscal.totais_icms_total_desconto)
        etree.SubElement(icms_total, 'vOutro').text = str(nota_fiscal.totais_icms_outras_despesas_acessorias)
        etree.SubElement(icms_total, 'vNF').text = str(nota_fiscal.totais_icms_total_nota)


        # Apenas NF-e
        if nota_fiscal.modelo == 55:
            # Tributos
            etree.SubElement(icms_total, 'vIPI').text = str(nota_fiscal.totais_icms_total_ipi)
            etree.SubElement(icms_total, 'vPIS').text = str(nota_fiscal.totais_icms_pis)
            etree.SubElement(icms_total, 'vCOFINS').text = str(nota_fiscal.totais_icms_cofins)
            etree.SubElement(icms_total, 'vII').text = str(nota_fiscal.totais_icms_total_ii)

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
            veiculo = etree.SubElement(transp, 'veicTransp')
            etree.SubElement(veiculo, 'placa').text = nota_fiscal.transporte_veiculo_placa
            etree.SubElement(veiculo, 'UF').text = nota_fiscal.transporte_veiculo_uf
            etree.SubElement(veiculo, 'RNTC').text = nota_fiscal.transporte_veiculo_rntc

            # Reboque
            reboque = etree.SubElement(transp, 'reboque')
            etree.SubElement(reboque, 'placa').text = nota_fiscal.transporte_reboque_placa
            etree.SubElement(reboque, 'UF').text = nota_fiscal.transporte_reboque_uf
            etree.SubElement(reboque, 'RNTC').text = nota_fiscal.transporte_reboque_rntc

            # Volumes
            for volume in nota_fiscal.transporte_volumes:
                vol = etree.SubElement(transp, 'vol')
                etree.SubElement(vol, 'qVol').text = str(volume.quantidade)
                etree.SubElement(vol, 'esp').text = volume.especie
                etree.SubElement(vol, 'marca').text = volume.marca
                etree.SubElement(vol, 'nVol').text = volume.numeracao
                etree.SubElement(vol, 'pesoL').text = str(volume.peso_liquido)
                etree.SubElement(vol, 'pesoB').text = str(volume.peso_bruto)

                # Lacres
                lacres = etree.SubElement(vol, 'lacres')
                for lacre in volume.lacres:
                    etree.SubElement(lacres, 'nLacre').text = lacre.numero_lacre

        # Informações adicionais
        info_ad = etree.SubElement(raiz, 'infAdic')
        etree.SubElement(info_ad, 'infAdFisco').text = nota_fiscal.informacoes_adicionais_interesse_fisco
        etree.SubElement(info_ad, 'infCpl').text = nota_fiscal.informacoes_complementares_interesse_contribuinte

        if retorna_string:
            return etree.tostring(raiz, pretty_print=True)
        else:
            return raiz

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
            id_dest, # idDest
            cod_municipio,
            nota_fiscal.tipo_impressao_danfe,
            nota_fiscal.forma_emissao,
            nota_fiscal.dv_codigo_numerico_aleatorio,
            self._ambiente,
            nota_fiscal.finalidade_emissao,
            nota_fiscal.cliente_final, # indFinal
            nota_fiscal.indicador_presencial, # indPres
            nota_fiscal.processo_emissao,
            '%s %s' % (self._nome_aplicacao,
                                nota_fiscal.versao_processo_emissao),
            '', # dhCont - Data e Hora da entrada em contingência
            '', # xJust - Justificativa da entrada em contingência
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
                return '|'.join(map(safe_str, serial_data))
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
