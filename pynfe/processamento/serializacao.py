# -*- coding: utf-8 -*-
import base64
import hashlib
import re
import warnings

from datetime import datetime
from decimal import Decimal

import pynfe.utils.xml_writer as xmlw
from pynfe.entidades import Manifesto, NotaFiscal
from pynfe.utils import (
    etree,
    obter_codigo_por_municipio,
    obter_municipio_por_codigo,
    obter_pais_por_codigo,
    so_numeros,
)
from pynfe.utils.flags import (
    CODIGOS_ESTADOS,
    NAMESPACE_MDFE,
    NAMESPACE_NFE,
    NAMESPACE_SIG,
    VERSAO_MDFE,
    VERSAO_PADRAO,
    VERSAO_QRCODE,
)
from pynfe.utils.webservices import MDFE, NFCE


class Serializacao(object):
    """Classe abstrata responsavel por fornecer as funcionalidades basicas para
    exportacao e importacao de Notas Fiscais eletronicas para formatos serializados
    de arquivos. Como XML, JSON, binario, etc.

    Nao deve ser instanciada diretamente!"""

    _fonte_dados = None
    _ambiente = 1  # 1 = Produção, 2 = Homologação
    _contingencia = None  # Justificativa da entrada em contingência (min 20, max 256 caracteres)
    _so_cpf = False  # Destinatário com apenas o cpf do cliente
    _nome_aplicacao = "PyNFe"

    def __new__(cls, *args, **kwargs):
        if cls == Serializacao:
            raise Exception("Esta classe nao pode ser instanciada diretamente!")
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
    """Classe de serialização do arquivo xml"""

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
            raiz = etree.Element("NFe", xmlns=NAMESPACE_NFE)

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

        raise Exception("Metodo nao implementado")

    def _serializar_emitente(self, emitente, tag_raiz="emit", retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados do emitente
        if len(so_numeros(emitente.cnpj)) == 11:
            etree.SubElement(raiz, "CPF").text = so_numeros(emitente.cnpj)
        else:
            etree.SubElement(raiz, "CNPJ").text = so_numeros(emitente.cnpj)
        etree.SubElement(raiz, "xNome").text = emitente.razao_social
        etree.SubElement(raiz, "xFant").text = emitente.nome_fantasia
        # Endereço
        endereco = etree.SubElement(raiz, "enderEmit")
        etree.SubElement(endereco, "xLgr").text = emitente.endereco_logradouro
        etree.SubElement(endereco, "nro").text = emitente.endereco_numero
        if emitente.endereco_complemento:
            etree.SubElement(endereco, "xCpl").text = emitente.endereco_complemento
        etree.SubElement(endereco, "xBairro").text = emitente.endereco_bairro
        etree.SubElement(endereco, "cMun").text = obter_codigo_por_municipio(
            emitente.endereco_municipio, emitente.endereco_uf
        )
        etree.SubElement(endereco, "xMun").text = emitente.endereco_municipio
        etree.SubElement(endereco, "UF").text = emitente.endereco_uf
        etree.SubElement(endereco, "CEP").text = so_numeros(emitente.endereco_cep)
        etree.SubElement(endereco, "cPais").text = emitente.endereco_pais
        etree.SubElement(endereco, "xPais").text = obter_pais_por_codigo(emitente.endereco_pais)
        if emitente.endereco_telefone:
            etree.SubElement(endereco, "fone").text = emitente.endereco_telefone
        etree.SubElement(raiz, "IE").text = emitente.inscricao_estadual
        # Apenas NF-e
        if emitente.inscricao_estadual_subst_tributaria:
            etree.SubElement(raiz, "IEST").text = emitente.inscricao_estadual_subst_tributaria
        # Inscricao Municipal
        if emitente.inscricao_municipal:
            etree.SubElement(raiz, "IM").text = emitente.inscricao_municipal
            # Campo Opcional. Pode ser informado quando a Inscrição Municipal (id:C19)
            if emitente.cnae_fiscal:
                etree.SubElement(raiz, "CNAE").text = emitente.cnae_fiscal
        etree.SubElement(raiz, "CRT").text = emitente.codigo_de_regime_tributario
        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_cliente(self, cliente, modelo, tag_raiz="dest", retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados do cliente (destinatário)
        etree.SubElement(raiz, cliente.tipo_documento).text = so_numeros(cliente.numero_documento)
        if not self._so_cpf:
            if cliente.razao_social:
                etree.SubElement(raiz, "xNome").text = cliente.razao_social
            endereco = etree.SubElement(raiz, "enderDest")
            etree.SubElement(endereco, "xLgr").text = cliente.endereco_logradouro
            etree.SubElement(endereco, "nro").text = cliente.endereco_numero
            if cliente.endereco_complemento:
                etree.SubElement(endereco, "xCpl").text = cliente.endereco_complemento
            etree.SubElement(endereco, "xBairro").text = cliente.endereco_bairro
            etree.SubElement(endereco, "cMun").text = obter_codigo_por_municipio(
                cliente.endereco_municipio, cliente.endereco_uf
            )
            etree.SubElement(endereco, "xMun").text = cliente.endereco_municipio
            etree.SubElement(endereco, "UF").text = cliente.endereco_uf
            if cliente.endereco_cep:
                etree.SubElement(endereco, "CEP").text = so_numeros(cliente.endereco_cep)
            etree.SubElement(endereco, "cPais").text = cliente.endereco_pais
            etree.SubElement(endereco, "xPais").text = obter_pais_por_codigo(cliente.endereco_pais)
            if cliente.endereco_telefone:
                etree.SubElement(endereco, "fone").text = cliente.endereco_telefone
        # Indicador da IE do destinatário:
        # 1 – Contribuinte ICMSpagamento à vista;
        # 2 – Contribuinte isento de inscrição;
        # 9 – Não Contribuinte
        if cliente.indicador_ie == 9:
            # 9 – Não Contribuinte
            etree.SubElement(raiz, "indIEDest").text = "9"
        elif (
            cliente.indicador_ie == 2 or cliente.isento_icms
        ) or cliente.inscricao_estadual.upper() == "ISENTO":
            etree.SubElement(raiz, "indIEDest").text = "2"
        else:
            # Indicador da IE do destinatário: 1 – Contribuinte ICMSpagamento à vista;
            etree.SubElement(raiz, "indIEDest").text = str(cliente.indicador_ie)
            etree.SubElement(raiz, "IE").text = cliente.inscricao_estadual
        # Suframa
        if cliente.inscricao_suframa:
            etree.SubElement(raiz, "ISUF").text = cliente.inscricao_suframa
        # Inscrição Municipal do tomador do serviço
        if cliente.inscricao_municipal:
            etree.SubElement(raiz, "IM").text = cliente.inscricao_municipal
        # E-mail
        if cliente.email:
            etree.SubElement(raiz, "email").text = cliente.email
        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_transportadora(
        self, transportadora, tag_raiz="transporta", retorna_string=True
    ):
        raiz = etree.Element(tag_raiz)

        # Dados da transportadora
        if transportadora.numero_documento:
            etree.SubElement(raiz, transportadora.tipo_documento.upper()).text = so_numeros(
                transportadora.numero_documento
            )
        if transportadora.razao_social:
            etree.SubElement(raiz, "xNome").text = transportadora.razao_social
        if transportadora.inscricao_estadual:
            etree.SubElement(raiz, "IE").text = transportadora.inscricao_estadual

        # Endereço
        if transportadora.endereco_logradouro:
            etree.SubElement(raiz, "xEnder").text = transportadora.endereco_logradouro
        if transportadora.endereco_municipio:
            etree.SubElement(raiz, "xMun").text = transportadora.endereco_municipio
        if transportadora.endereco_uf:
            etree.SubElement(raiz, "UF").text = transportadora.endereco_uf

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_entrega_retirada(
        self, entrega_retirada, tag_raiz="entrega", retorna_string=True
    ):
        raiz = etree.Element(tag_raiz)

        # Dados da entrega/retirada
        etree.SubElement(raiz, entrega_retirada.tipo_documento).text = so_numeros(
            entrega_retirada.numero_documento
        )

        # Endereço
        etree.SubElement(raiz, "xLgr").text = entrega_retirada.endereco_logradouro
        etree.SubElement(raiz, "nro").text = entrega_retirada.endereco_numero
        etree.SubElement(raiz, "xCpl").text = entrega_retirada.endereco_complemento
        etree.SubElement(raiz, "xBairro").text = entrega_retirada.endereco_bairro
        etree.SubElement(raiz, "cMun").text = entrega_retirada.endereco_municipio
        etree.SubElement(raiz, "xMun").text = obter_municipio_por_codigo(
            entrega_retirada.endereco_municipio,
            entrega_retirada.endereco_uf,
        )
        etree.SubElement(raiz, "UF").text = entrega_retirada.endereco_uf

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_autorizados_baixar_xml(
        self, autorizados_baixar_xml, tag_raiz="autXML", retorna_string=True
    ):
        raiz = etree.Element(tag_raiz)

        if len(so_numeros(autorizados_baixar_xml.CPFCNPJ)) == 11:
            etree.SubElement(raiz, "CPF").text = so_numeros(autorizados_baixar_xml.CPFCNPJ)
        else:
            etree.SubElement(raiz, "CNPJ").text = so_numeros(autorizados_baixar_xml.CPFCNPJ)

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _formatarQuantidade(self, quantidade: Decimal) -> str:
        return (
            str(quantidade.quantize(Decimal("1.0000")).normalize())
            if quantidade % 1 != 0
            else str(int(quantidade))
        )

    def _serializar_produto_servico(
        self, produto_servico, modelo, tag_raiz="det", retorna_string=True
    ):
        raiz = etree.Element(tag_raiz)

        # Produto
        prod = etree.SubElement(raiz, "prod")
        etree.SubElement(prod, "cProd").text = str(produto_servico.codigo)
        etree.SubElement(prod, "cEAN").text = produto_servico.ean
        etree.SubElement(prod, "xProd").text = produto_servico.descricao
        etree.SubElement(prod, "NCM").text = produto_servico.ncm
        # Codificação opcional que detalha alguns NCM.
        # Formato: duas letras maiúsculas e 4 algarismos.
        # Se a mercadoria se enquadrar em mais de uma codificação,
        # informar até 8 codificações principais.
        # etree.SubElement(prod, 'NVE').text = ''
        # etree.SubElement(prod, 'CEST').text = produto_service.cest
        if produto_servico.cbenef:
            etree.SubElement(prod, "cBenef").text = produto_servico.cbenef
        etree.SubElement(prod, "CFOP").text = produto_servico.cfop
        etree.SubElement(prod, "uCom").text = produto_servico.unidade_comercial
        etree.SubElement(prod, "qCom").text = self._formatarQuantidade(
            produto_servico.quantidade_comercial or 0
        )
        etree.SubElement(prod, "vUnCom").text = str("{:.10f}").format(
            produto_servico.valor_unitario_comercial or 0
        )
        """
        Código Especificador da Substituição Tributária – CEST,
        que estabelece a sistemática de uniformização
        e identificação das mercadorias e bens passíveis de
        sujeição aos regimes de substituição tributária e de
        antecipação de recolhimento do ICMS.
        """
        # if produto_servico.cest:
        #    etree.SubElement(prod, 'CEST').text = produto_servico.cest
        etree.SubElement(prod, "vProd").text = str("{:.2f}").format(
            produto_servico.valor_total_bruto or 0
        )
        etree.SubElement(prod, "cEANTrib").text = produto_servico.ean_tributavel
        etree.SubElement(prod, "uTrib").text = produto_servico.unidade_tributavel
        etree.SubElement(prod, "qTrib").text = self._formatarQuantidade(
            produto_servico.quantidade_tributavel
        )
        etree.SubElement(prod, "vUnTrib").text = "{:.10f}".format(
            produto_servico.valor_unitario_tributavel or 0
        )

        # frete
        if produto_servico.total_frete:
            etree.SubElement(prod, "vFrete").text = "{:.2f}".format(produto_servico.total_frete)
        # seguro
        if produto_servico.total_seguro:
            etree.SubElement(prod, "vSeg").text = "{:.2f}".format(produto_servico.total_seguro)
        # desconto
        if produto_servico.desconto:
            etree.SubElement(prod, "vDesc").text = "{:.2f}".format(produto_servico.desconto)
        # outras despesas acessórias
        if produto_servico.outras_despesas_acessorias:
            etree.SubElement(prod, "vOutro").text = "{:.2f}".format(
                produto_servico.outras_despesas_acessorias
            )

        """ Indica se valor do Item (vProd) entra no valor total da NF-e (vProd)
            0=Valor do item (vProd) não compõe o valor total da NF-e
            1=Valor do item (vProd) compõe o valor total da NF-e (vProd) (v2.0)
        """
        etree.SubElement(prod, "indTot").text = str(produto_servico.ind_total)

        # DI - Declaração de Importação
        self._serializar_declaracao_importacao(
            produto_servico=produto_servico, tag_raiz=prod, retorna_string=False
        )

        """ Informação de interesse do emissor para controle do B2B.(v2.0) """
        # Número do Pedido de Compra. Tam 1-15
        if produto_servico.numero_pedido:
            etree.SubElement(prod, "xPed").text = str(produto_servico.numero_pedido)
        # Item do Pedido de Compra. Tam 6
        if produto_servico.numero_item:
            etree.SubElement(prod, "nItemPed").text = str(produto_servico.numero_item)
        # nFCI - Número de controle da FCI - Ficha de Conteúdo de Importação.
        if produto_servico.nfci:
            etree.SubElement(prod, "nFCI").text = produto_servico.nfci

        # Combustível
        if produto_servico.cProdANP:
            combustivel = etree.SubElement(prod, "comb")
            etree.SubElement(combustivel, "cProdANP").text = str(produto_servico.cProdANP)
            etree.SubElement(combustivel, "descANP").text = str(produto_servico.descANP)
            if produto_servico.pGLP:
                etree.SubElement(combustivel, "pGLP").text = "{:.4f}".format(
                    produto_servico.pGLP or 0
                )
            if produto_servico.pGNn:
                etree.SubElement(combustivel, "pGNn").text = "{:.4f}".format(
                    produto_servico.pGNn or 0
                )
            if produto_servico.pGNi:
                etree.SubElement(combustivel, "pGNi").text = "{:.4f}".format(
                    produto_servico.pGNi or 0
                )
            if produto_servico.vPart:
                etree.SubElement(combustivel, "vPart").text = "{:.2f}".format(
                    produto_servico.vPart or 0
                )
            if produto_servico.comb_codif:
                etree.SubElement(combustivel, "CODIF").text = produto_servico.comb_codif
            if produto_servico.comb_q_temp:
                etree.SubElement(combustivel, "qTemp").text = produto_servico.comb_q_temp
            etree.SubElement(combustivel, "UFCons").text = str(produto_servico.UFCons)

            # encerrantes
            if produto_servico.comb_n_bico:
                encerrante = etree.SubElement(combustivel, "encerrante")
                etree.SubElement(encerrante, "nBico").text = str(produto_servico.comb_n_bico)
                if produto_servico.comb_n_bomba:
                    etree.SubElement(encerrante, "nBomba").text = str(produto_servico.comb_n_bomba)
                etree.SubElement(encerrante, "nTanque").text = str(produto_servico.comb_n_tanque)
                etree.SubElement(encerrante, "vEncIni").text = "{:.3f}".format(
                    produto_servico.comb_v_enc_ini
                )
                etree.SubElement(encerrante, "vEncFin").text = "{:.3f}".format(
                    produto_servico.comb_v_enc_fin
                )

            if produto_servico.comb_p_bio:
                etree.SubElement(combustivel, "pBio").text = "{:.4f}".format(
                    produto_servico.comb_p_bio or 0
                )

        # Imposto
        imposto = etree.SubElement(raiz, "imposto")

        # Lei da transparencia
        # Tributos aprox por item
        if produto_servico.valor_tributos_aprox:
            etree.SubElement(imposto, "vTotTrib").text = str(produto_servico.valor_tributos_aprox)

        # ICMS
        self._serializar_imposto_icms(
            produto_servico=produto_servico, tag_raiz=imposto, retorna_string=False
        )

        # IPI
        self._serializar_imposto_ipi(
            produto_servico=produto_servico, tag_raiz=imposto, retorna_string=False
        )

        # Imposto de Importação II
        self._serializar_imposto_importacao(
            produto_servico=produto_servico,
            modelo=modelo,
            tag_raiz=imposto,
            retorna_string=False,
        )

        # PIS
        self._serializar_imposto_pis(
            produto_servico=produto_servico,
            modelo=modelo,
            tag_raiz=imposto,
            retorna_string=False,
        )

        # COFINS
        self._serializar_imposto_cofins(
            produto_servico=produto_servico,
            modelo=modelo,
            tag_raiz=imposto,
            retorna_string=False,
        )

        # Reforma Tributaria - IVA Dual
        self._serializar_imposto_ibscbs(
            produto_servico=produto_servico,
            modelo=modelo,
            tag_raiz=imposto,
            retorna_string=False,
        )

        # tag impostoDevol
        if produto_servico.ipi_valor_ipi_dev:
            impostodevol = etree.SubElement(raiz, "impostoDevol")
            etree.SubElement(impostodevol, "pDevol").text = "{:.2f}".format(
                produto_servico.pdevol or 100
            )
            ipidev = etree.SubElement(impostodevol, "IPI")
            etree.SubElement(ipidev, "vIPIDevol").text = "{:.2f}".format(
                produto_servico.ipi_valor_ipi_dev or 0
            )

        # Informações adicionais do produto
        if produto_servico.informacoes_adicionais:
            etree.SubElement(raiz, "infAdProd").text = produto_servico.informacoes_adicionais

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_imposto_icms(self, produto_servico, tag_raiz="imposto", retorna_string=True):
        icms = etree.SubElement(tag_raiz, "ICMS")

        # 00=Tributada integralmente
        if produto_servico.icms_modalidade == "00":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = produto_servico.icms_modalidade
            etree.SubElement(icms_item, "modBC").text = str(
                produto_servico.icms_modalidade_determinacao_bc
            )
            etree.SubElement(icms_item, "vBC").text = str(
                produto_servico.icms_valor_base_calculo
            )  # Valor da BC do ICMS
            etree.SubElement(icms_item, "pICMS").text = "{:.2f}".format(
                produto_servico.icms_aliquota or 0
            )  # Alíquota do imposto
            etree.SubElement(icms_item, "vICMS").text = "{:.2f}".format(
                produto_servico.icms_valor or 0
            )  # Valor do ICMS

            if produto_servico.fcp_valor:
                etree.SubElement(icms_item, "pFCP").text = "{:.2f}".format(
                    produto_servico.fcp_aliquota or 0
                )  # Percentual FCP
                etree.SubElement(icms_item, "vFCP").text = "{:.2f}".format(
                    produto_servico.fcp_valor or 0
                )  # Valor Fundo Combate a Pobreza

        # 02=Tributação monofásica própria sobre combustíveis
        elif produto_servico.icms_modalidade == "02":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = produto_servico.icms_modalidade

            etree.SubElement(icms_item, "qBCMono").text = "{:.4f}".format(
                produto_servico.icms_q_bc_mono or 0
            )
            etree.SubElement(icms_item, "adRemICMS").text = "{:.4f}".format(
                produto_servico.icms_ad_rem_icms or 0
            )
            etree.SubElement(icms_item, "vICMSMono").text = "{:.2f}".format(
                produto_servico.icms_v_icms_mono or 0
            )

        # 10=Tributada e com cobrança do ICMS por substituição tributária
        elif produto_servico.icms_modalidade == "10":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = produto_servico.icms_modalidade
            etree.SubElement(icms_item, "modBC").text = str(
                produto_servico.icms_modalidade_determinacao_bc
            )
            etree.SubElement(icms_item, "vBC").text = str(
                produto_servico.icms_valor_base_calculo
            )  # Valor da BC do ICMS
            etree.SubElement(icms_item, "pICMS").text = "{:.2f}".format(
                produto_servico.icms_aliquota or 0
            )  # Alíquota do imposto
            etree.SubElement(icms_item, "vICMS").text = "{:.2f}".format(
                produto_servico.icms_valor or 0
            )  # Valor do ICMS

            if produto_servico.fcp_valor:
                etree.SubElement(icms_item, "vBCFCP").text = "{:.2f}".format(
                    produto_servico.fcp_base_calculo or 0
                )  # Base de calculo FCP
                etree.SubElement(icms_item, "pFCP").text = "{:.2f}".format(
                    produto_servico.fcp_aliquota or 0
                )  # Percentual FCP
                etree.SubElement(icms_item, "vFCP").text = "{:.2f}".format(
                    produto_servico.fcp_valor or 0
                )  # Valor Fundo Combate a Pobreza

            # Modalidade de determinação da BC do ICMS ST
            # 0=Preço tabelado ou máximo sugerido;
            # 1=Lista Negativa (valor);
            # 2=Lista Positiva (valor);
            # 3=Lista Neutra (valor);4=Margem Valor Agregado (%);5=Pauta (valor);
            etree.SubElement(icms_item, "modBCST").text = str(
                produto_servico.icms_st_modalidade_determinacao_bc
            )
            etree.SubElement(icms_item, "pMVAST").text = "{:.2f}".format(
                produto_servico.icms_st_percentual_adicional or 0
            )  # Percentual da margem de valor Adicionado do ICMS ST
            etree.SubElement(icms_item, "pRedBCST").text = "{:.2f}".format(
                produto_servico.icms_st_percentual_reducao_bc or 0
            )  # APercentual da Redução de BC do ICMS ST
            etree.SubElement(icms_item, "vBCST").text = "{:.2f}".format(
                produto_servico.icms_st_valor_base_calculo or 0
            )
            etree.SubElement(icms_item, "pICMSST").text = "{:.2f}".format(
                produto_servico.icms_st_aliquota or 0
            )
            etree.SubElement(icms_item, "vICMSST").text = "{:.2f}".format(
                produto_servico.icms_st_valor or 0
            )

            if produto_servico.fcp_st_valor:
                etree.SubElement(icms_item, "vBCFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_base_calculo or 0
                )
                etree.SubElement(icms_item, "pFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_aliquota or 0
                )
                etree.SubElement(icms_item, "vFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_valor or 0
                )

        # 15=Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis
        elif produto_servico.icms_modalidade == "15":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = produto_servico.icms_modalidade

            etree.SubElement(icms_item, "qBCMono").text = "{:.4f}".format(
                produto_servico.icms_q_bc_mono or 0
            )
            etree.SubElement(icms_item, "adRemICMS").text = "{:.4f}".format(
                produto_servico.icms_ad_rem_icms or 0
            )
            etree.SubElement(icms_item, "vICMSMono").text = "{:.2f}".format(
                produto_servico.icms_v_icms_mono or 0
            )
            etree.SubElement(icms_item, "qBCMonoReten").text = "{:.4f}".format(
                produto_servico.icms_q_bc_mono_reten or 0
            )
            etree.SubElement(icms_item, "adRemICMSReten").text = "{:.4f}".format(
                produto_servico.icms_ad_rem_icms_reten or 0
            )
            etree.SubElement(icms_item, "vICMSMonoReten").text = "{:.2f}".format(
                produto_servico.icms_v_icms_mono_reten or 0
            )
            if produto_servico.icms_p_red_ad_rem:
                etree.SubElement(icms_item, "pRedAdRem").text = "{:.2f}".format(
                    produto_servico.icms_p_red_ad_rem or 0
                )
                etree.SubElement(icms_item, "motRedAdRem").text = str(
                    produto_servico.icms_mot_red_ad_rem
                )

        # 20=Com redução de base de cálculo
        elif produto_servico.icms_modalidade == "20":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = produto_servico.icms_modalidade
            etree.SubElement(icms_item, "modBC").text = str(
                produto_servico.icms_modalidade_determinacao_bc
            )
            etree.SubElement(icms_item, "pRedBC").text = "{:.2f}".format(
                produto_servico.icms_percentual_reducao_bc or 0
            )  # Percentual da Redução de BC
            etree.SubElement(icms_item, "vBC").text = "{:.2f}".format(
                produto_servico.icms_valor_base_calculo or 0
            )  # Valor da BC do ICMS
            etree.SubElement(icms_item, "pICMS").text = "{:.2f}".format(
                produto_servico.icms_aliquota or 0
            )  # Alíquota do imposto
            etree.SubElement(icms_item, "vICMS").text = "{:.2f}".format(
                produto_servico.icms_valor or 0
            )  # Valor do ICMS

            # Os campos relativos ao Fundo de Combate à Pobreza só devem ser informados
            # se o produto estiver sujeito a incidência do mesmo.
            if produto_servico.fcp_valor:
                etree.SubElement(icms_item, "vBCFCP").text = "{:.2f}".format(
                    produto_servico.fcp_base_calculo or 0
                )  # Base de calculo FCP
                etree.SubElement(icms_item, "pFCP").text = "{:.2f}".format(
                    produto_servico.fcp_aliquota or 0
                )  # Percentual FCP
                etree.SubElement(icms_item, "vFCP").text = "{:.2f}".format(
                    produto_servico.fcp_valor or 0
                )  # Valor Fundo Combate a Pobreza

            if produto_servico.icms_desonerado > 0:
                etree.SubElement(icms_item, "vICMSDeson").text = "{:.2f}".format(
                    produto_servico.icms_desonerado or 0
                )  # Valor do ICMS Desonerado
                etree.SubElement(icms_item, "motDesICMS").text = str(
                    produto_servico.icms_motivo_desoneracao
                )

        # 30=Isenta / não tributada e com cobrança do ICMS por substituição tributária
        elif produto_servico.icms_modalidade == "30":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = produto_servico.icms_modalidade
            etree.SubElement(icms_item, "modBCST").text = str(
                produto_servico.icms_st_modalidade_determinacao_bc
            )
            etree.SubElement(icms_item, "pMVAST").text = "{:.2f}".format(
                produto_servico.icms_st_percentual_adicional or 0
            )  # Percentual da margem de valor Adicionado do ICMS ST
            etree.SubElement(icms_item, "pRedBCST").text = "{:.2f}".format(
                produto_servico.icms_st_percentual_reducao_bc or 0
            )  # APercentual da Redução de BC do ICMS ST
            etree.SubElement(icms_item, "vBCST").text = "{:.2f}".format(
                produto_servico.icms_st_valor_base_calculo or 0
            )
            etree.SubElement(icms_item, "pICMSST").text = "{:.2f}".format(
                produto_servico.icms_st_aliquota or 0
            )
            etree.SubElement(icms_item, "vICMSST").text = "{:.2f}".format(
                produto_servico.icms_st_valor or 0
            )

            if produto_servico.fcp_st_valor:
                etree.SubElement(icms_item, "vBCFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_base_calculo or 0
                )
                etree.SubElement(icms_item, "pFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_aliquota or 0
                )
                etree.SubElement(icms_item, "vFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_valor or 0
                )

            if produto_servico.icms_desonerado > 0:
                etree.SubElement(icms_item, "vICMSDeson").text = "{:.2f}".format(
                    produto_servico.icms_desonerado or 0
                )  # Valor do ICMS Desonerado
                etree.SubElement(icms_item, "motDesICMS").text = str(
                    produto_servico.icms_motivo_desoneracao
                )

        # 40=Isenta / 41=Não tributada / 50=Com suspensão
        elif produto_servico.icms_modalidade in ["40", "41", "50"]:
            icms_item = etree.SubElement(icms, "ICMS40")
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = str(produto_servico.icms_modalidade)

            if produto_servico.icms_desonerado > 0:
                etree.SubElement(icms_item, "vICMSDeson").text = "{:.2f}".format(
                    produto_servico.icms_desonerado or 0
                )  # Valor do ICMS Desonerado
                etree.SubElement(icms_item, "motDesICMS").text = str(
                    produto_servico.icms_motivo_desoneracao
                )

        # 51=Com diferimento
        elif produto_servico.icms_modalidade == "51":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = "51"
            etree.SubElement(icms_item, "modBC").text = str(
                produto_servico.icms_modalidade_determinacao_bc
            )

            if produto_servico.fcp_valor:
                etree.SubElement(icms_item, "vBCFCP").text = "{:.2f}".format(
                    produto_servico.fcp_base_calculo or 0
                )  # Base de calculo FCP
                etree.SubElement(icms_item, "pFCP").text = "{:.2f}".format(
                    produto_servico.fcp_aliquota or 0
                )  # Percentual FCP
                etree.SubElement(icms_item, "vFCP").text = "{:.2f}".format(
                    produto_servico.fcp_valor or 0
                )  # Valor Fundo Combate a Pobreza

        # 53=Tributação monofásica sobre combustíveis com recolhimento diferido
        elif produto_servico.icms_modalidade == "53":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = produto_servico.icms_modalidade

            etree.SubElement(icms_item, "qBCMono").text = "{:.4f}".format(
                produto_servico.icms_q_bc_mono or 0
            )
            etree.SubElement(icms_item, "adRemICMS").text = "{:.4f}".format(
                produto_servico.icms_ad_rem_icms or 0
            )
            etree.SubElement(icms_item, "vICMSMonoOp").text = "{:.2f}".format(
                produto_servico.icms_v_icms_mono_op or 0
            )
            etree.SubElement(icms_item, "pDif").text = "{:.4f}".format(
                produto_servico.icms_p_dif or 0
            )
            etree.SubElement(icms_item, "vICMSMonoDif").text = "{:.4f}".format(
                produto_servico.icms_v_icms_mono_dif or 0
            )
            etree.SubElement(icms_item, "vICMSMono").text = "{:.2f}".format(
                produto_servico.icms_v_icms_mono or 0
            )

        # 60=ICMS cobrado anteriormente por substituição tributária
        elif produto_servico.icms_modalidade in ["ST", "60"]:
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = "60"
            etree.SubElement(icms_item, "vBCSTRet").text = "{:.2f}".format(
                produto_servico.icms_st_ret_base_calculo or 0
            )
            etree.SubElement(icms_item, "pST").text = "{:.2f}".format(
                produto_servico.icms_st_ret_aliquota or 0
            )
            etree.SubElement(icms_item, "vICMSSTRet").text = "{:.2f}".format(
                produto_servico.icms_st_ret_valor or 0
            )

            if produto_servico.fcp_st_ret_valor:
                etree.SubElement(icms_item, "vBCFCPSTRet").text = "{:.2f}".format(
                    produto_servico.fcp_st_ret_base_calculo or 0
                )
                etree.SubElement(icms_item, "pFCPSTRet").text = "{:.2f}".format(
                    produto_servico.fcp_st_ret_aliquota or 0
                )
                etree.SubElement(icms_item, "vFCPSTRet").text = "{:.2f}".format(
                    produto_servico.fcp_st_ret_valor or 0
                )

        # 61=Tributação monofásica sobre combustíveis cobrada anteriormente
        elif produto_servico.icms_modalidade == "61":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = "61"
            etree.SubElement(icms_item, "qBCMonoRet").text = "{:.4f}".format(
                produto_servico.icms_q_bc_mono_ret or 0
            )
            etree.SubElement(icms_item, "adRemICMSRet").text = "{:.4f}".format(
                produto_servico.icms_ad_rem_icms_ret or 0
            )
            etree.SubElement(icms_item, "vICMSMonoRet").text = "{:.2f}".format(
                produto_servico.icms_v_icms_mono_ret or 0
            )

        # 70=Com redução da BC e cobrança do ICMS por substituição tributária
        elif produto_servico.icms_modalidade == "70":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = "70"
            etree.SubElement(icms_item, "modBC").text = str(
                produto_servico.icms_modalidade_determinacao_bc
            )
            etree.SubElement(icms_item, "pRedBC").text = "{:.2f}".format(
                produto_servico.icms_percentual_reducao_bc or 0
            )  # Percentual da Redução de BC
            etree.SubElement(icms_item, "vBC").text = "{:.2f}".format(
                produto_servico.icms_valor_base_calculo or 0
            )  # Valor da BC do ICMS
            etree.SubElement(icms_item, "pICMS").text = "{:.2f}".format(
                produto_servico.icms_aliquota or 0
            )  # Alíquota do imposto
            etree.SubElement(icms_item, "vICMS").text = "{:.2f}".format(
                produto_servico.icms_valor or 0
            )  # Valor do ICMS

            if produto_servico.fcp_valor:
                etree.SubElement(icms_item, "vBCFCP").text = "{:.2f}".format(
                    produto_servico.fcp_base_calculo or 0
                )  # Base de calculo FCP
                etree.SubElement(icms_item, "pFCP").text = "{:.2f}".format(
                    produto_servico.fcp_aliquota or 0
                )  # Percentual FCP
                etree.SubElement(icms_item, "vFCP").text = "{:.2f}".format(
                    produto_servico.fcp_valor or 0
                )  # Valor Fundo Combate a Pobreza

            etree.SubElement(icms_item, "modBCST").text = str(
                produto_servico.icms_st_modalidade_determinacao_bc
            )
            etree.SubElement(icms_item, "pMVAST").text = "{:.2f}".format(
                produto_servico.icms_st_percentual_adicional or 0
            )  # Percentual da margem de valor Adicionado do ICMS ST
            etree.SubElement(icms_item, "pRedBCST").text = "{:.2f}".format(
                produto_servico.icms_st_percentual_reducao_bc or 0
            )  # APercentual da Redução de BC do ICMS ST
            etree.SubElement(icms_item, "vBCST").text = "{:.2f}".format(
                produto_servico.icms_st_valor_base_calculo or 0
            )
            etree.SubElement(icms_item, "pICMSST").text = "{:.2f}".format(
                produto_servico.icms_st_aliquota or 0
            )
            etree.SubElement(icms_item, "vICMSST").text = "{:.2f}".format(
                produto_servico.icms_st_valor or 0
            )

            if produto_servico.fcp_st_valor:
                etree.SubElement(icms_item, "vBCFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_base_calculo or 0
                )
                etree.SubElement(icms_item, "pFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_aliquota or 0
                )
                etree.SubElement(icms_item, "vFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_valor or 0
                )

            if produto_servico.icms_desonerado > 0:
                etree.SubElement(icms_item, "vICMSDeson").text = "{:.2f}".format(
                    produto_servico.icms_desonerado or 0
                )  # Valor do ICMS Desonerado
                etree.SubElement(icms_item, "motDesICMS").text = str(
                    produto_servico.icms_motivo_desoneracao
                )

        # 90=Outras
        elif produto_servico.icms_modalidade == "90":
            icms_item = etree.SubElement(icms, "ICMS" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CST").text = "90"

            if (produto_servico.icms_valor_base_calculo > 0) and (produto_servico.icms_valor > 0):
                etree.SubElement(icms_item, "modBC").text = str(
                    produto_servico.icms_modalidade_determinacao_bc
                )
                etree.SubElement(icms_item, "vBC").text = "{:.2f}".format(
                    produto_servico.icms_valor_base_calculo or 0
                )  # Valor da BC do ICMS
                etree.SubElement(icms_item, "pRedBC").text = "{:.2f}".format(
                    produto_servico.icms_percentual_reducao_bc or 0
                )  # Percentual da Redução de BC
                etree.SubElement(icms_item, "pICMS").text = "{:.2f}".format(
                    produto_servico.icms_aliquota or 0
                )  # Alíquota do imposto
                etree.SubElement(icms_item, "vICMS").text = "{:.2f}".format(
                    produto_servico.icms_valor or 0
                )  # Valor do ICMS

            if produto_servico.fcp_valor:
                etree.SubElement(icms_item, "vBCFCP").text = "{:.2f}".format(
                    produto_servico.fcp_base_calculo or 0
                )  # Base de calculo FCP
                etree.SubElement(icms_item, "pFCP").text = "{:.2f}".format(
                    produto_servico.fcp_aliquota or 0
                )  # Percentual FCP
                etree.SubElement(icms_item, "vFCP").text = "{:.2f}".format(
                    produto_servico.fcp_valor or 0
                )  # Valor Fundo Combate a Pobreza

            if (produto_servico.icms_st_valor_base_calculo > 0) and (
                produto_servico.icms_st_valor > 0
            ):
                etree.SubElement(icms_item, "modBCST").text = str(
                    produto_servico.icms_st_modalidade_determinacao_bc
                )
                etree.SubElement(icms_item, "pMVAST").text = "{:.2f}".format(
                    produto_servico.icms_st_percentual_adicional or 0
                )  # Percentual da margem de valor Adicionado do ICMS ST
                etree.SubElement(icms_item, "pRedBCST").text = "{:.2f}".format(
                    produto_servico.icms_st_percentual_reducao_bc or 0
                )  # APercentual da Redução de BC do ICMS ST
                etree.SubElement(icms_item, "vBCST").text = "{:.2f}".format(
                    produto_servico.icms_st_valor_base_calculo or 0
                )
                etree.SubElement(icms_item, "pICMSST").text = "{:.2f}".format(
                    produto_servico.icms_st_aliquota or 0
                )
                etree.SubElement(icms_item, "vICMSST").text = "{:.2f}".format(
                    produto_servico.icms_st_valor or 0
                )

            if produto_servico.fcp_st_valor:
                etree.SubElement(icms_item, "vBCFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_base_calculo or 0
                )
                etree.SubElement(icms_item, "pFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_aliquota or 0
                )
                etree.SubElement(icms_item, "vFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_valor or 0
                )

            if produto_servico.icms_desonerado > 0:
                etree.SubElement(icms_item, "vICMSDeson").text = "{:.2f}".format(
                    produto_servico.icms_desonerado or 0
                )  # Valor do ICMS Desonerado
                etree.SubElement(icms_item, "motDesICMS").text = str(
                    produto_servico.icms_motivo_desoneracao
                )

        # Grupo do Simples Nacional

        # 101=Tributada pelo Simples Nacional com permissão de crédito
        elif produto_servico.icms_modalidade == "101":
            icms_item = etree.SubElement(icms, "ICMSSN" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CSOSN").text = produto_servico.icms_csosn
            etree.SubElement(icms_item, "pCredSN").text = "{:.2f}".format(
                produto_servico.icms_aliquota
            )  # Alíquota aplicável de cálculo do crédito (Simples Nacional).
            etree.SubElement(icms_item, "vCredICMSSN").text = "{:.2f}".format(
                produto_servico.icms_credito
            )  # Valor crédito do ICMS que pode ser aproveitado nos termos
            # do art. 23 da LC 123 (Simples Nacional)

        # 102=Tributada pelo Simples Nacional sem permissão de crédito
        # 103=Isenção do ICMS no Simples Nacional para faixa de receita bruta
        # 300=Imune
        # 400=Não tributada pelo Simples Nacional
        elif produto_servico.icms_modalidade in ("102", "103", "300", "400"):
            icms_item = etree.SubElement(icms, "ICMSSN102")
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CSOSN").text = produto_servico.icms_csosn

        # 201=Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS
        # 202=Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS
        # 203=Isenção do ICMS no SN para faixa de receita bruta e com cobrança do ICMS
        elif produto_servico.icms_modalidade in ("201", "202", "203"):
            if produto_servico.icms_modalidade == "201":
                icms_item = etree.SubElement(icms, "ICMSSN201")
            elif produto_servico.icms_modalidade in ["202", "203"]:
                icms_item = etree.SubElement(icms, "ICMSSN202")
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CSOSN").text = produto_servico.icms_csosn

            etree.SubElement(icms_item, "modBCST").text = str(
                produto_servico.icms_st_modalidade_determinacao_bc
            )
            etree.SubElement(icms_item, "pMVAST").text = "{:.2f}".format(
                produto_servico.icms_st_percentual_adicional or 0
            )  # Percentual da margem de valor Adicionado do ICMS ST
            etree.SubElement(icms_item, "pRedBCST").text = "{:.2f}".format(
                produto_servico.icms_st_percentual_reducao_bc or 0
            )  # APercentual da Redução de BC do ICMS ST
            etree.SubElement(icms_item, "vBCST").text = "{:.2f}".format(
                produto_servico.icms_st_valor_base_calculo or 0
            )
            etree.SubElement(icms_item, "pICMSST").text = "{:.2f}".format(
                produto_servico.icms_st_aliquota or 0
            )
            etree.SubElement(icms_item, "vICMSST").text = "{:.2f}".format(
                produto_servico.icms_st_valor or 0
            )

            if produto_servico.fcp_st_valor:
                etree.SubElement(icms_item, "vBCFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_base_calculo or 0
                )
                etree.SubElement(icms_item, "pFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_aliquota or 0
                )
                etree.SubElement(icms_item, "vFCPST").text = "{:.2f}".format(
                    produto_servico.fcp_st_valor or 0
                )

            if produto_servico.icms_modalidade == "201":
                etree.SubElement(icms_item, "pCredSN").text = "{:.2f}".format(
                    produto_servico.icms_aliquota
                )  # Alíquota aplicável de cálculo do crédito (Simples Nacional).
                etree.SubElement(icms_item, "vCredICMSSN").text = "{:.2f}".format(
                    produto_servico.icms_credito
                )  # Valor crédito do ICMS que pode ser aproveitado nos termos
                # do art. 23 da LC 123 (Simples Nacional)

        # 500=ICMS cobrado anteriormente por ST (substituído) ou por antecipação
        elif produto_servico.icms_modalidade == "500":
            icms_item = etree.SubElement(icms, "ICMSSN" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CSOSN").text = produto_servico.icms_csosn

        # 900=Outros
        elif produto_servico.icms_modalidade == "900":
            icms_item = etree.SubElement(icms, "ICMSSN" + produto_servico.icms_modalidade)
            etree.SubElement(icms_item, "orig").text = str(produto_servico.icms_origem)
            etree.SubElement(icms_item, "CSOSN").text = produto_servico.icms_csosn

            if (produto_servico.icms_valor_base_calculo > 0) and (produto_servico.icms_valor > 0):
                etree.SubElement(icms_item, "modBC").text = str(
                    produto_servico.icms_modalidade_determinacao_bc
                )
                etree.SubElement(icms_item, "vBC").text = "{:.2f}".format(
                    produto_servico.icms_valor_base_calculo or 0
                )  # Valor da BC do ICMS
                etree.SubElement(icms_item, "pRedBC").text = "{:.2f}".format(
                    produto_servico.icms_percentual_reducao_bc or 0
                )  # Percentual da Redução de BC
                etree.SubElement(icms_item, "pICMS").text = "{:.2f}".format(
                    produto_servico.icms_aliquota or 0
                )  # Alíquota do imposto
                etree.SubElement(icms_item, "vICMS").text = "{:.2f}".format(
                    produto_servico.icms_valor or 0
                )  # Valor do ICMS

            if (produto_servico.icms_st_valor_base_calculo > 0) and (
                produto_servico.icms_st_valor > 0
            ):
                etree.SubElement(icms_item, "modBCST").text = str(
                    produto_servico.icms_st_modalidade_determinacao_bc
                )
                etree.SubElement(icms_item, "pMVAST").text = "{:.2f}".format(
                    produto_servico.icms_st_percentual_adicional or 0
                )  # Percentual da margem de valor Adicionado do ICMS ST
                etree.SubElement(icms_item, "pRedBCST").text = "{:.2f}".format(
                    produto_servico.icms_st_percentual_reducao_bc or 0
                )  # APercentual da Redução de BC do ICMS ST
                etree.SubElement(icms_item, "vBCST").text = "{:.2f}".format(
                    produto_servico.icms_st_valor_base_calculo or 0
                )
                etree.SubElement(icms_item, "pICMSST").text = "{:.2f}".format(
                    produto_servico.icms_st_aliquota or 0
                )
                etree.SubElement(icms_item, "vICMSST").text = "{:.2f}".format(
                    produto_servico.icms_st_valor or 0
                )

                if produto_servico.fcp_st_valor:
                    etree.SubElement(icms_item, "vBCFCPST").text = "{:.2f}".format(
                        produto_servico.fcp_st_base_calculo or 0
                    )
                    etree.SubElement(icms_item, "pFCPST").text = "{:.2f}".format(
                        produto_servico.fcp_st_aliquota or 0
                    )
                    etree.SubElement(icms_item, "vFCPST").text = "{:.2f}".format(
                        produto_servico.fcp_st_valor or 0
                    )

            if produto_servico.icms_aliquota > 0:
                etree.SubElement(icms_item, "pCredSN").text = "{:.2f}".format(
                    produto_servico.icms_aliquota
                )  # Alíquota aplicável de cálculo do crédito (Simples Nacional).
                etree.SubElement(icms_item, "vCredICMSSN").text = "{:.2f}".format(
                    produto_servico.icms_credito
                )  # Valor crédito do ICMS que pode ser aproveitado nos termos
                # do art. 23 da LC 123 (Simples Nacional)

        else:
            raise NotImplementedError

    def _serializar_imposto_ipi(self, produto_servico, tag_raiz="imposto", retorna_string=True):
        ipint_lista = ("01", "02", "03", "04", "05", "51", "52", "53", "54", "55")
        if produto_servico.ipi_codigo_enquadramento in ipint_lista:
            ipi = etree.SubElement(tag_raiz, "IPI")
            # Preenchimento conforme Atos Normativos editados pela Receita Federal (Observação 2)
            etree.SubElement(ipi, "cEnq").text = produto_servico.ipi_classe_enquadramento
            if produto_servico.ipi_classe_enquadramento == "":
                etree.SubElement(ipi, "cEnq").text = "999"

            ipint = etree.SubElement(ipi, "IPINT")
            # 01=Entrada tributada com alíquota zero 02=Entrada isenta 03=Entrada não-tributada
            # 04=Entrada imune 05=Entrada com suspensão 51=Saída tributada com alíquota zero
            # 52=Saída isenta 53=Saída não-tributada 54=Saída imune 55=Saída com suspensão
            etree.SubElement(ipint, "CST").text = produto_servico.ipi_codigo_enquadramento
        else:
            if (
                (produto_servico.ipi_valor_base_calculo > 0)
                and (produto_servico.ipi_aliquota > 0)
                and (produto_servico.ipi_valor_ipi > 0)
            ):
                ipi = etree.SubElement(tag_raiz, "IPI")

                # Preenchimento conforme Atos Normativos editados pela Receita Federal
                # (Observação 2)
                etree.SubElement(ipi, "cEnq").text = produto_servico.ipi_classe_enquadramento
                if produto_servico.ipi_classe_enquadramento == "":
                    etree.SubElement(ipi, "cEnq").text = "999"

                ipi_item = etree.SubElement(ipi, "IPITrib")
                etree.SubElement(ipi_item, "CST").text = produto_servico.ipi_codigo_enquadramento
                etree.SubElement(ipi_item, "vBC").text = "{:.2f}".format(
                    produto_servico.ipi_valor_base_calculo or 0
                )
                etree.SubElement(ipi_item, "pIPI").text = "{:.2f}".format(
                    produto_servico.ipi_aliquota or 0
                )
                etree.SubElement(ipi_item, "vIPI").text = "{:.2f}".format(
                    produto_servico.ipi_valor_ipi or 0
                )

    def _serializar_imposto_pis(
        self, produto_servico, modelo, tag_raiz="imposto", retorna_string=True
    ):
        # Para NFC-e (65), o grupo de tributação do PIS/COFINS são opcionais.
        if (modelo != 55) and (
            (produto_servico.pis_valor_base_calculo == 0)
            and (produto_servico.pis_aliquota_percentual == 0)
            and (produto_servico.pis_valor == 0)
            and (
                produto_servico.pis_modalidade
                not in ("04", "05", "06", "07", "08", "09", "49", "99")
            )
        ):
            return

        pisnt = ("04", "05", "06", "07", "08", "09")
        pis = etree.SubElement(tag_raiz, "PIS")
        if produto_servico.pis_modalidade in pisnt:
            pis_item = etree.SubElement(pis, "PISNT")
            etree.SubElement(pis_item, "CST").text = produto_servico.pis_modalidade
        elif produto_servico.pis_modalidade == "01" or produto_servico.pis_modalidade == "02":
            pis_item = etree.SubElement(pis, "PISAliq")
            etree.SubElement(pis_item, "CST").text = produto_servico.pis_modalidade
            etree.SubElement(pis_item, "vBC").text = "{:.2f}".format(
                produto_servico.pis_valor_base_calculo or 0
            )
            etree.SubElement(pis_item, "pPIS").text = "{:.2f}".format(
                produto_servico.pis_aliquota_percentual or 0
            )
            etree.SubElement(pis_item, "vPIS").text = "{:.2f}".format(
                produto_servico.pis_valor or 0
            )
        elif produto_servico.pis_modalidade == "03":
            pis_item = etree.SubElement(pis, "PISQtde")
            etree.SubElement(pis_item, "CST").text = produto_servico.pis_modalidade
            etree.SubElement(pis_item, "qBCProd").text = "{:.4f}".format(
                produto_servico.quantidade_comercial
            )
            etree.SubElement(pis_item, "vAliqProd").text = "{:.4f}".format(
                produto_servico.pis_aliquota_reais or 0
            )
            etree.SubElement(pis_item, "vPIS").text = "{:.2f}".format(
                produto_servico.pis_valor or 0
            )
        else:
            pis_item = etree.SubElement(pis, "PISOutr")
            etree.SubElement(pis_item, "CST").text = produto_servico.pis_modalidade
            if produto_servico.pis_aliquota_reais > 0:
                etree.SubElement(pis_item, "qBCProd").text = "{:.4f}".format(
                    produto_servico.quantidade_comercial
                )
                etree.SubElement(pis_item, "vAliqProd").text = "{:.4f}".format(
                    produto_servico.pis_aliquota_reais or 0
                )
            else:
                etree.SubElement(pis_item, "vBC").text = "{:.2f}".format(
                    produto_servico.pis_valor_base_calculo or 0
                )
                etree.SubElement(pis_item, "pPIS").text = "{:.2f}".format(
                    produto_servico.pis_aliquota_percentual or 0
                )
            etree.SubElement(pis_item, "vPIS").text = "{:.2f}".format(
                produto_servico.pis_valor or 0
            )

            # PISST
            # pis_item = etree.SubElement(pis, 'PISST')
            # etree.SubElement(pis_item, 'vBC').text = produto_servico.pis_valor_base_calculo
            # etree.SubElement(pis_item, 'pPIS').text = produto_servico.pis_aliquota_percentual
            # etree.SubElement(pis_item, 'qBCProd').text = produto_servico.quantidade_comercial
            # etree.SubElement(pis_item, 'vAliqProd').text = produto_servico
            #   .pis_aliquota_percentual
            # etree.SubElement(pis_item, 'vPIS').text = produto_servico.pis_valor_base_calculo

    def _serializar_imposto_cofins(
        self, produto_servico, modelo, tag_raiz="imposto", retorna_string=True
    ):
        # Para NFC-e (65), o grupo de tributação do PIS/COFINS são opcionais.
        if (modelo != 55) and (
            (produto_servico.cofins_valor_base_calculo == 0)
            and (produto_servico.cofins_aliquota_percentual == 0)
            and (produto_servico.cofins_valor == 0)
            and (
                produto_servico.cofins_modalidade
                not in ("04", "05", "06", "07", "08", "09", "49", "99")
            )
        ):
            return

        cofinsnt = ("04", "05", "06", "07", "08", "09")
        cofins = etree.SubElement(tag_raiz, "COFINS")
        if produto_servico.cofins_modalidade in cofinsnt:
            cofins_item = etree.SubElement(cofins, "COFINSNT")
            etree.SubElement(cofins_item, "CST").text = produto_servico.cofins_modalidade
        elif produto_servico.cofins_modalidade == "01" or produto_servico.cofins_modalidade == "02":
            cofins_item = etree.SubElement(cofins, "COFINSAliq")
            etree.SubElement(cofins_item, "CST").text = produto_servico.cofins_modalidade
            etree.SubElement(cofins_item, "vBC").text = "{:.2f}".format(
                produto_servico.cofins_valor_base_calculo or 0
            )
            etree.SubElement(cofins_item, "pCOFINS").text = "{:.2f}".format(
                produto_servico.cofins_aliquota_percentual or 0
            )
            etree.SubElement(cofins_item, "vCOFINS").text = "{:.2f}".format(
                produto_servico.cofins_valor
            )
        elif produto_servico.cofins_modalidade == "03":
            cofins_item = etree.SubElement(cofins, "COFINSQtde")
            etree.SubElement(cofins_item, "CST").text = produto_servico.cofins_modalidade
            etree.SubElement(cofins_item, "qBCProd").text = "{:.4f}".format(
                produto_servico.quantidade_comercial
            )
            etree.SubElement(cofins_item, "vAliqProd").text = "{:.4f}".format(
                produto_servico.cofins_aliquota_reais
            )
            etree.SubElement(cofins_item, "vCOFINS").text = "{:.2f}".format(
                produto_servico.cofins_valor
            )
        else:
            cofins_item = etree.SubElement(cofins, "COFINSOutr")
            etree.SubElement(cofins_item, "CST").text = produto_servico.cofins_modalidade
            if produto_servico.cofins_aliquota_reais > 0:
                etree.SubElement(cofins_item, "qBCProd").text = "{:.4f}".format(
                    produto_servico.quantidade_comercial
                )
                etree.SubElement(cofins_item, "vAliqProd").text = "{:.4f}".format(
                    produto_servico.cofins_aliquota_reais or 0
                )
            else:
                etree.SubElement(cofins_item, "vBC").text = "{:.2f}".format(
                    produto_servico.cofins_valor_base_calculo or 0
                )
                etree.SubElement(cofins_item, "pCOFINS").text = "{:.2f}".format(
                    produto_servico.cofins_aliquota_percentual or 0
                )
            etree.SubElement(cofins_item, "vCOFINS").text = "{:.2f}".format(
                produto_servico.cofins_valor or 0
            )

            # COFINSST
            # cofins_item = etree.SubElement(cofins, 'COFINSOutr')
            # etree.SubElement(cofins_item, 'vBC').text = produto_servico
            #   .cofins_valor_base_calculo
            # etree.SubElement(cofins_item, 'pCOFINS').text = produto_servico
            #   .cofins_aliquota_percentual
            # etree.SubElement(cofins_item, 'qBCProd').text = produto_servico
            #   .quantidade_comercial
            # etree.SubElement(cofins_item, 'vAliqProd').text = produto_servico
            #   .cofins_aliquota_percentual
            # etree.SubElement(cofins_item, 'vCOFINS').text = produto_servico.cofins_valor

    def _serializar_imposto_importacao(
        self, produto_servico, modelo, tag_raiz="imposto", retorna_string=True
    ):
        if (
            (produto_servico.imposto_importacao_valor_base_calculo > 0)
            or (produto_servico.imposto_importacao_valor_despesas_aduaneiras > 0)
            or (produto_servico.imposto_importacao_valor > 0)
            or (produto_servico.imposto_importacao_valor_iof > 0)
            or (produto_servico.cfop[1] == "3")
        ):
            ii = etree.SubElement(tag_raiz, "II")
            etree.SubElement(ii, "vBC").text = "{:.2f}".format(
                produto_servico.imposto_importacao_valor_base_calculo or 0
            )
            etree.SubElement(ii, "vDespAdu").text = "{:.2f}".format(
                produto_servico.imposto_importacao_valor_despesas_aduaneiras or 0
            )
            etree.SubElement(ii, "vII").text = "{:.2f}".format(
                produto_servico.imposto_importacao_valor
            )
            etree.SubElement(ii, "vIOF").text = "{:.2f}".format(
                produto_servico.imposto_importacao_valor_iof
            )

    # =============================================
    # Reforma Tributaria - IVA Dual (NT 2025.002-RTC)
    # =============================================

    # CSTs that have taxable values (vBC, rates, amounts)
    _IBSCBS_CST_TRIBUTADOS = ("000", "010", "200", "400", "510", "600", "620", "800", "810", "900")

    def _serializar_imposto_ibscbs(
        self, produto_servico, modelo, tag_raiz="imposto", retorna_string=True
    ):
        """Serializa grupo IBSCBS (Group UB) como filho direto de <imposto>.

        Nota: <IS> (Imposto Seletivo) so entra no schema a partir de 2027.
        O metodo _serializar_is() esta pronto mas nao e chamado ate que o
        schema PL 010b inclua o elemento IS dentro de <imposto>.
        """
        has_ibscbs = produto_servico.ibscbs_cst

        if not has_ibscbs:
            return

        self._serializar_ibscbs(produto_servico, tag_raiz)

        # IS: descomentar quando schema suportar (previsto para 2027)
        # if produto_servico.is_cst_selec:
        #     self._serializar_is(produto_servico, tag_raiz)

    def _serializar_ibscbs(self, produto_servico, tag_raiz):
        """Serializa <IBSCBS> com gIBSCBS contendo gIBSUF, gIBSMun e gCBS."""
        ibscbs = etree.SubElement(tag_raiz, "IBSCBS")
        etree.SubElement(ibscbs, "CST").text = produto_servico.ibscbs_cst

        if produto_servico.ibscbs_c_class_trib:
            etree.SubElement(ibscbs, "cClassTrib").text = produto_servico.ibscbs_c_class_trib

        if produto_servico.ibscbs_cst in self._IBSCBS_CST_TRIBUTADOS:
            gibscbs = etree.SubElement(ibscbs, "gIBSCBS")

            etree.SubElement(gibscbs, "vBC").text = "{:.2f}".format(produto_servico.ibscbs_vbc or 0)

            # gIBSUF
            gibsuf = etree.SubElement(gibscbs, "gIBSUF")
            etree.SubElement(gibsuf, "pIBSUF").text = "{:.4f}".format(
                produto_servico.ibscbs_p_ibs_uf or 0
            )
            etree.SubElement(gibsuf, "vIBSUF").text = "{:.2f}".format(
                produto_servico.ibscbs_v_ibs_uf or 0
            )

            # gIBSMun
            gibsmun = etree.SubElement(gibscbs, "gIBSMun")
            etree.SubElement(gibsmun, "pIBSMun").text = "{:.4f}".format(
                produto_servico.ibscbs_p_ibs_mun or 0
            )
            etree.SubElement(gibsmun, "vIBSMun").text = "{:.2f}".format(
                produto_servico.ibscbs_v_ibs_mun or 0
            )

            # vIBS total
            etree.SubElement(gibscbs, "vIBS").text = "{:.2f}".format(
                produto_servico.ibscbs_v_ibs or 0
            )

            # gCBS
            gcbs = etree.SubElement(gibscbs, "gCBS")
            etree.SubElement(gcbs, "pCBS").text = "{:.4f}".format(produto_servico.ibscbs_p_cbs or 0)
            etree.SubElement(gcbs, "vCBS").text = "{:.2f}".format(produto_servico.ibscbs_v_cbs or 0)

    def _serializar_is(self, produto_servico, tag_raiz):
        """Serializa <IS> (Imposto Seletivo) como filho direto de <imposto>.

        Type: TIS (PL 010b DFeTiposBasicos_v1.00.xsd)
        Schema field names: CSTIS, cClassTribIS, vBCIS, pIS, vIS
        """
        is_tag = etree.SubElement(tag_raiz, "IS")
        etree.SubElement(is_tag, "CSTIS").text = produto_servico.is_cst_selec

        if produto_servico.is_c_class_trib:
            etree.SubElement(is_tag, "cClassTribIS").text = produto_servico.is_c_class_trib

        if produto_servico.is_cst_selec in ("01", "02"):
            etree.SubElement(is_tag, "vBCIS").text = "{:.2f}".format(produto_servico.is_vbc or 0)
            etree.SubElement(is_tag, "pIS").text = "{:.4f}".format(produto_servico.is_aliquota or 0)
            etree.SubElement(is_tag, "vIS").text = "{:.2f}".format(produto_servico.is_valor or 0)

    def _serializar_declaracao_importacao(
        self, produto_servico, tag_raiz="prod", retorna_string=True
    ):
        # DI de 0-100
        if (
            produto_servico.declaracoes_importacao
            and len(produto_servico.declaracoes_importacao) > 0
        ):
            for item_di in produto_servico.declaracoes_importacao:
                di = etree.SubElement(tag_raiz, "DI")
                # Número do Documento de Importação (DI, DSI, DIRE, ...)
                etree.SubElement(di, "nDI").text = str(item_di.numero_di_dsi_da)
                # Data de Registro do documento
                etree.SubElement(di, "dDI").text = item_di.data_registro.strftime("%Y-%m-%d")
                # Local de desembaraço
                etree.SubElement(di, "xLocDesemb").text = str(item_di.desembaraco_aduaneiro_local)
                # UF onde ocorreu o Desembaraço Aduaneiro
                etree.SubElement(di, "UFDesemb").text = str(item_di.desembaraco_aduaneiro_uf)
                # Data do Desembaraço Aduaneiro
                etree.SubElement(di, "dDesemb").text = item_di.desembaraco_aduaneiro_data.strftime(
                    "%Y-%m-%d"
                )
                # Via de transporte internacional informada na Declaração de Importação (DI)
                etree.SubElement(di, "tpViaTransp").text = str(item_di.tipo_via_transporte)
                # Valor da AFRMM - Adicional ao Frete para Renovação da Marinha Mercante
                if item_di.valor_afrmm:
                    etree.SubElement(di, "vAFRMM").text = "{:.2f}".format(item_di.valor_afrmm or 0)
                # tpIntermedio
                etree.SubElement(di, "tpIntermedio").text = str(item_di.tipo_intermediacao)
                # CNPJ
                if item_di.cnpj_adquirente:
                    etree.SubElement(di, "CNPJ").text = so_numeros(item_di.cnpj_adquirente)
                # UFTerceiro
                if item_di.uf_terceiro:
                    etree.SubElement(di, "UFTerceiro").text = item_di.uf_terceiro
                # cExportador
                etree.SubElement(di, "cExportador").text = str(item_di.codigo_exportador)

                # Adições 1-100
                for adicao in item_di.adicoes:
                    adi = etree.SubElement(di, "adi")
                    etree.SubElement(adi, "nAdicao").text = str(adicao.numero)
                    etree.SubElement(adi, "nSeqAdic").text = str(adicao.sequencia)
                    etree.SubElement(adi, "cFabricante").text = str(adicao.codigo_fabricante)
                    if adicao.desconto:
                        etree.SubElement(adi, "vDescDI").text = "{:.2f}".format(
                            adicao.desconto or 0
                        )
                    # Número do ato concessório de Drawback
                    if adicao.numero_drawback:
                        etree.SubElement(adi, "nDraw").text = str(adicao.numero_drawback)

    def _serializar_responsavel_tecnico(
        self, responsavel_tecnico, tag_raiz="infRespTec", retorna_string=True
    ):
        raiz = etree.Element(tag_raiz)
        etree.SubElement(raiz, "CNPJ").text = responsavel_tecnico.cnpj
        etree.SubElement(raiz, "xContato").text = responsavel_tecnico.contato
        etree.SubElement(raiz, "email").text = responsavel_tecnico.email
        etree.SubElement(raiz, "fone").text = responsavel_tecnico.fone

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_pagamentos_antigo_deprecado(
        self, tipo_pagamento, finalidade_emissao, totais_icms_total_nota
    ):
        pag = etree.Element("pag")
        detpag = etree.SubElement(pag, "detPag")
        if str(finalidade_emissao) == "3" or str(finalidade_emissao) == "4":
            etree.SubElement(detpag, "tPag").text = "90"
            etree.SubElement(detpag, "vPag").text = "{:.2f}".format(0)
        else:
            etree.SubElement(detpag, "tPag").text = str(tipo_pagamento).zfill(2)
            etree.SubElement(detpag, "vPag").text = "{:.2f}".format(totais_icms_total_nota)
            if tipo_pagamento == 3 or tipo_pagamento == 4:
                cartao = etree.SubElement(detpag, "card")
                """ Tipo de Integração do processo de pagamento com
                    o sistema de automação da empresa:
                    1=Pagamento integrado com o sistema de automação da empresa
                    2= Pagamento não integrado com o sistema de automação da empresa
                """
                etree.SubElement(cartao, "tpIntegra").text = "2"
                # etree.SubElement(cartao, 'CNPJ').text = ''
                # # Informar o CNPJ da Credenciadora de cartão de crédito / débito
                # etree.SubElement(cartao, 'tBand').text = ''
                # # 01=Visa 02=Mastercard 03=American Express 04=Sorocred
                # 05=Diners Club 06=Elo 07=Hipercard 08=Aura 09=Caba 99=Outros
                # etree.SubElement(cartao, 'cAut').text = ''
                # # Identifica o número da autorização da transação da operação
                # com cartão de crédito e/ou débito
            # troco
            # etree.SubElement(pag, 'vTroco').text = str('')
        return pag

    def _serializar_pagamentos(
        self, pagamentos: list(), finalidade_emissao="", valor_troco=0.00, retorna_string=True
    ):
        pag = etree.Element("pag")
        if finalidade_emissao in [3, 4]:
            detpag = etree.SubElement(pag, "detPag")
            etree.SubElement(detpag, "tPag").text = "90"
            etree.SubElement(detpag, "vPag").text = "{:.2f}".format(0)
        else:
            for item in pagamentos:
                det = etree.Element("detPag")
                xmlw.write_txt(det, "indPag", item.ind_pag, False)
                xmlw.write_txt(det, "tPag", item.t_pag, True)
                xmlw.write_txt(det, "xPag", item.x_pag, False)
                xmlw.write_float(det, "vPag", item.v_pag, True, 2, 2)
                if item.tp_integra:
                    card = etree.SubElement(det, "card")
                    xmlw.write_txt(card, "tpIntegra", item.tp_integra, True)
                    xmlw.write_txt(card, "CNPJ", item.cnpj, False)
                    xmlw.write_txt(card, "tBand", item.t_band, False)
                    xmlw.write_txt(card, "cAut", item.c_aut, False)
                pag.append(det)

        # troco
        xmlw.write_float(pag, "vTroco", valor_troco, False, 2, 2)

        if retorna_string:
            return etree.tostring(pag, encoding="unicode", pretty_print=False)
        else:
            return pag

    def _serializar_nota_fiscal(self, nota_fiscal, tag_raiz="infNFe", retorna_string=True):
        raiz = etree.Element(tag_raiz, versao=self._versao)

        # 'Id' da tag raiz
        # Ex.: NFe35080599999090910270550010000000011518005123
        raiz.attrib["Id"] = nota_fiscal.identificador_unico

        tz = nota_fiscal.data_emissao.strftime("%z")
        if not tz:
            tz = datetime.now().astimezone().strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])

        # Dados da Nota Fiscal
        ide = etree.SubElement(raiz, "ide")
        etree.SubElement(ide, "cUF").text = CODIGOS_ESTADOS[nota_fiscal.uf]
        etree.SubElement(ide, "cNF").text = nota_fiscal.codigo_numerico_aleatorio
        etree.SubElement(ide, "natOp").text = nota_fiscal.natureza_operacao
        etree.SubElement(ide, "mod").text = str(nota_fiscal.modelo)
        etree.SubElement(ide, "serie").text = nota_fiscal.serie
        etree.SubElement(ide, "nNF").text = str(nota_fiscal.numero_nf)
        etree.SubElement(ide, "dhEmi").text = (
            nota_fiscal.data_emissao.strftime("%Y-%m-%dT%H:%M:%S") + tz
        )
        # Apenas NF-e
        if nota_fiscal.modelo == 55:
            if nota_fiscal.data_saida_entrada:
                etree.SubElement(ide, "dhSaiEnt").text = (
                    nota_fiscal.data_saida_entrada.strftime("%Y-%m-%dT%H:%M:%S") + tz
                )
            """ dhCont Data e Hora da entrada em contingência E B01 D 0-1
                Formato AAAA-MM-DDThh:mm:ssTZD (UTC - Universal Coordinated Time)
            """
        etree.SubElement(ide, "tpNF").text = str(nota_fiscal.tipo_documento)  # 0=entrada 1=saida
        """ nfce suporta apenas operação interna
            Identificador de local de destino da operação
            1=Operação interna;2=Operação interestadual;3=Operação com exterior.
        """
        if nota_fiscal.modelo == 65:
            etree.SubElement(ide, "idDest").text = str(1)
        else:
            etree.SubElement(ide, "idDest").text = str(nota_fiscal.indicador_destino)
        etree.SubElement(ide, "cMunFG").text = nota_fiscal.municipio
        if nota_fiscal.municipio_fato_gerador_ibs:
            etree.SubElement(ide, "cMunFGIBS").text = nota_fiscal.municipio_fato_gerador_ibs
        etree.SubElement(ide, "tpImp").text = str(nota_fiscal.tipo_impressao_danfe)
        """ # CONTINGENCIA #
            1=Emissão normal (não em contingência);
            2=Contingência FS-IA, com impressão do DANFE em formulário de segurança;
            3=Contingência SCAN (Sistema de Contingência do Ambiente Nacional);
            4=Contingência DPEC (Declaração Prévia da Emissão em Contingência);
            5=Contingência FS-DA, com impressão do DANFE em formulário de segurança;
            6=Contingência SVC-AN (SEFAZ Virtual de Contingência do AN);
            7=Contingência SVC-RS (SEFAZ Virtual de Contingência do RS);
            9=Contingência off-line da NFC-e
            (as demais opções de contingência são válidas também para a NFC-e).
            Para a NFC-e somente estão disponíveis e são válidas as opções de contingência 5 e 9.
        """
        if self._contingencia is not None:
            if nota_fiscal.forma_emissao == "1":
                nota_fiscal.forma_emissao = "9"
        etree.SubElement(ide, "tpEmis").text = str(nota_fiscal.forma_emissao)
        etree.SubElement(ide, "cDV").text = nota_fiscal.dv_codigo_numerico_aleatorio
        etree.SubElement(ide, "tpAmb").text = str(self._ambiente)
        etree.SubElement(ide, "finNFe").text = str(nota_fiscal.finalidade_emissao)
        if nota_fiscal.modelo == 65:
            etree.SubElement(ide, "indFinal").text = str(1)
            etree.SubElement(ide, "indPres").text = str(1)
        else:
            etree.SubElement(ide, "indFinal").text = str(nota_fiscal.cliente_final)
            etree.SubElement(ide, "indPres").text = str(nota_fiscal.indicador_presencial)
        # Rejeição 435: NF-e não pode ter o indicativo do intermediador quando for modelo 55
        #               e informando o indicativo de presença (indPres) igual a 0, 1 ou 5.
        if (nota_fiscal.modelo in [55, 65]) and (nota_fiscal.indicador_presencial not in [0, 1, 5]):
            etree.SubElement(ide, "indIntermed").text = str(nota_fiscal.indicador_intermediador)
        etree.SubElement(ide, "procEmi").text = str(nota_fiscal.processo_emissao)
        etree.SubElement(ide, "verProc").text = "%s %s" % (
            self._nome_aplicacao,
            nota_fiscal.versao_processo_emissao,
        )

        # NF-e referenciada (utilizado em casos de devolução/garantia)
        # Apenas NF-e
        if nota_fiscal.modelo == 55:
            if nota_fiscal.notas_fiscais_referenciadas:
                for refNFe in nota_fiscal.notas_fiscais_referenciadas:
                    nfref = etree.SubElement(ide, "NFref")
                    if refNFe.tipo == "Conhecimento de frete":
                        if refNFe.chave_acesso and len(refNFe.chave_acesso) == 44:
                            etree.SubElement(nfref, "refCTe").text = refNFe.chave_acesso

                    elif refNFe.tipo == "Nota Fiscal":
                        refNF = etree.SubElement(nfref, "refNF")
                        etree.SubElement(refNF, "cUF").text = str(refNFe.uf)
                        etree.SubElement(refNF, "AAMM").text = str(refNFe.mes_ano_emissao)
                        etree.SubElement(refNF, "CNPJ").text = so_numeros(refNFe.cnpj)
                        etree.SubElement(refNF, "mod").text = str(refNFe.modelo)  # 1 ou 2
                        etree.SubElement(refNF, "serie").text = str(refNFe.serie)
                        etree.SubElement(refNF, "nNF").text = str(refNFe.numero)

                    elif refNFe.tipo == "Nota Fiscal produtor":
                        refNFP = etree.SubElement(nfref, "refNFP")
                        etree.SubElement(refNFP, "cUF").text = str(refNFe.uf)
                        etree.SubElement(refNFP, "AAMM").text = str(refNFe.mes_ano_emissao)
                        if len(so_numeros(refNFe.cnpj)) == 11:
                            etree.SubElement(refNFP, "CPF").text = so_numeros(refNFe.cnpj)
                        else:
                            etree.SubElement(refNFP, "CNPJ").text = so_numeros(refNFe.cnpj)
                        etree.SubElement(refNFP, "IE").text = so_numeros(refNFe.ie)
                        etree.SubElement(refNFP, "mod").text = "04"
                        etree.SubElement(refNFP, "serie").text = str(refNFe.serie)
                        etree.SubElement(refNFP, "nNF").text = str(refNFe.numero)

                    else:
                        # tipo == 'Nota Fiscal eletronica'
                        if refNFe.chave_acesso and len(refNFe.chave_acesso) == 44:
                            etree.SubElement(nfref, "refNFe").text = refNFe.chave_acesso

        # CONTINGENCIA
        if self._contingencia is not None:
            etree.SubElement(ide, "dhCont").text = (
                nota_fiscal.data_emissao.strftime("%Y-%m-%dT%H:%M:%S") + tz
            )  # Data e Hora da entrada em contingência AAAA-MM-DDThh:mm:ssTZD
            etree.SubElement(
                ide, "xJust"
            ).text = (
                self._contingencia
            )  # Justificativa da entrada em contingência (min 20, max 256 caracteres)

        # Emitente
        raiz.append(self._serializar_emitente(nota_fiscal.emitente, retorna_string=False))

        # Destinatário
        try:
            raiz.append(
                self._serializar_cliente(
                    nota_fiscal.cliente, modelo=nota_fiscal.modelo, retorna_string=False
                )
            )
        except AttributeError as e:
            # NFC-e pode ser gerada sem destinatário
            if nota_fiscal.modelo == 65:
                pass
            else:
                raise e
        # Retirada
        if nota_fiscal.retirada:
            raiz.append(
                self._serializar_entrega_retirada(
                    nota_fiscal.retirada,
                    retorna_string=False,
                    tag_raiz="retirada",
                )
            )

        # Entrega
        if nota_fiscal.entrega:
            raiz.append(
                self._serializar_entrega_retirada(
                    nota_fiscal.entrega,
                    retorna_string=False,
                    tag_raiz="entrega",
                )
            )

        # Autorizados a baixar o XML
        for num, item in enumerate(nota_fiscal.autorizados_baixar_xml):
            raiz.append(self._serializar_autorizados_baixar_xml(item, retorna_string=False))

        # Itens
        for num, item in enumerate(nota_fiscal.produtos_e_servicos):
            det = self._serializar_produto_servico(
                item, modelo=nota_fiscal.modelo, retorna_string=False
            )
            det.attrib["nItem"] = str(num + 1)

            raiz.append(det)

        # Totais
        total = etree.SubElement(raiz, "total")
        icms_total = etree.SubElement(total, "ICMSTot")
        etree.SubElement(icms_total, "vBC").text = "{:.2f}".format(
            nota_fiscal.totais_icms_base_calculo
        )
        etree.SubElement(icms_total, "vICMS").text = "{:.2f}".format(nota_fiscal.totais_icms_total)
        etree.SubElement(icms_total, "vICMSDeson").text = "{:.2f}".format(
            nota_fiscal.totais_icms_desonerado
        )  # Valor Total do ICMS desonerado
        if nota_fiscal.totais_fcp_destino:
            etree.SubElement(icms_total, "vFCPUFDest").text = "{:.2f}".format(
                nota_fiscal.totais_fcp_destino
            )
        if nota_fiscal.totais_icms_inter_destino:
            etree.SubElement(icms_total, "vICMSUFDest").text = "{:.2f}".format(
                nota_fiscal.totais_icms_inter_destino
            )
        if nota_fiscal.totais_icms_inter_remetente:
            etree.SubElement(icms_total, "vICMSUFRemet").text = "{:.2f}".format(
                nota_fiscal.totais_icms_remetente
            )
        etree.SubElement(icms_total, "vFCP").text = "{:.2f}".format(nota_fiscal.totais_fcp)
        etree.SubElement(icms_total, "vBCST").text = "{:.2f}".format(
            nota_fiscal.totais_icms_st_base_calculo
        )
        etree.SubElement(icms_total, "vST").text = "{:.2f}".format(nota_fiscal.totais_icms_st_total)
        etree.SubElement(icms_total, "vFCPST").text = "{:.2f}".format(nota_fiscal.totais_fcp_st)
        etree.SubElement(icms_total, "vFCPSTRet").text = "{:.2f}".format(
            nota_fiscal.totais_fcp_st_ret
        )

        # ICMS monofasico
        if nota_fiscal.totais_icms_q_bc_mono:
            etree.SubElement(icms_total, "qBCMono").text = "{:.2f}".format(
                nota_fiscal.totais_icms_q_bc_mono
            )
        if nota_fiscal.totais_icms_v_icms_mono:
            etree.SubElement(icms_total, "vICMSMono").text = "{:.2f}".format(
                nota_fiscal.totais_icms_v_icms_mono
            )
        if nota_fiscal.totais_icms_q_bc_mono_reten:
            etree.SubElement(icms_total, "qBCMonoReten").text = "{:.2f}".format(
                nota_fiscal.totais_icms_q_bc_mono_reten
            )
        if nota_fiscal.totais_icms_v_icms_mono_reten:
            etree.SubElement(icms_total, "vICMSMonoReten").text = "{:.2f}".format(
                nota_fiscal.totais_icms_v_icms_mono_reten
            )
        if nota_fiscal.totais_icms_q_bc_mono_ret:
            etree.SubElement(icms_total, "qBCMonoRet").text = "{:.2f}".format(
                nota_fiscal.totais_icms_q_bc_mono_ret
            )
        if nota_fiscal.totais_icms_v_icms_mono_ret:
            etree.SubElement(icms_total, "vICMSMonoRet").text = "{:.2f}".format(
                nota_fiscal.totais_icms_v_icms_mono_ret
            )

        etree.SubElement(icms_total, "vProd").text = "{:.2f}".format(
            nota_fiscal.totais_icms_total_produtos_e_servicos
        )
        etree.SubElement(icms_total, "vFrete").text = "{:.2f}".format(
            nota_fiscal.totais_icms_total_frete
        )
        etree.SubElement(icms_total, "vSeg").text = "{:.2f}".format(
            nota_fiscal.totais_icms_total_seguro
        )
        etree.SubElement(icms_total, "vDesc").text = "{:.2f}".format(
            nota_fiscal.totais_icms_total_desconto
        )

        # Tributos
        etree.SubElement(icms_total, "vII").text = "{:.2f}".format(nota_fiscal.totais_icms_total_ii)
        etree.SubElement(icms_total, "vIPI").text = "{:.2f}".format(
            nota_fiscal.totais_icms_total_ipi
        )
        etree.SubElement(icms_total, "vIPIDevol").text = "{:.2f}".format(
            nota_fiscal.totais_icms_total_ipi_dev
        )
        etree.SubElement(icms_total, "vPIS").text = "{:.2f}".format(nota_fiscal.totais_icms_pis)
        etree.SubElement(icms_total, "vCOFINS").text = "{:.2f}".format(
            nota_fiscal.totais_icms_cofins
        )

        etree.SubElement(icms_total, "vOutro").text = "{:.2f}".format(
            nota_fiscal.totais_icms_outras_despesas_acessorias
        )
        etree.SubElement(icms_total, "vNF").text = "{:.2f}".format(
            nota_fiscal.totais_icms_total_nota
        )
        if nota_fiscal.totais_tributos_aproximado:
            etree.SubElement(icms_total, "vTotTrib").text = "{:.2f}".format(
                nota_fiscal.totais_tributos_aproximado
            )

        # Reforma Tributaria - Totais IVA Dual (Group W03 - IBSCBSTot)
        # Type: TIBSCBSMonoTot (PL 010b DFeTiposBasicos_v1.00.xsd)
        has_reforma = (
            nota_fiscal.totais_vbc_ibscbs or nota_fiscal.totais_ibs or nota_fiscal.totais_cbs
        )
        if has_reforma:
            ibscbs_tot = etree.SubElement(total, "IBSCBSTot")
            etree.SubElement(ibscbs_tot, "vBCIBSCBS").text = "{:.2f}".format(
                nota_fiscal.totais_vbc_ibscbs
            )

            # gIBS (optional — emit if any IBS value exists)
            if nota_fiscal.totais_ibs_uf or nota_fiscal.totais_ibs_mun or nota_fiscal.totais_ibs:
                g_ibs = etree.SubElement(ibscbs_tot, "gIBS")

                g_ibs_uf = etree.SubElement(g_ibs, "gIBSUF")
                etree.SubElement(g_ibs_uf, "vDif").text = "0.00"
                etree.SubElement(g_ibs_uf, "vDevTrib").text = "0.00"
                etree.SubElement(g_ibs_uf, "vIBSUF").text = "{:.2f}".format(
                    nota_fiscal.totais_ibs_uf
                )

                g_ibs_mun = etree.SubElement(g_ibs, "gIBSMun")
                etree.SubElement(g_ibs_mun, "vDif").text = "0.00"
                etree.SubElement(g_ibs_mun, "vDevTrib").text = "0.00"
                etree.SubElement(g_ibs_mun, "vIBSMun").text = "{:.2f}".format(
                    nota_fiscal.totais_ibs_mun
                )

                etree.SubElement(g_ibs, "vIBS").text = "{:.2f}".format(nota_fiscal.totais_ibs)
                etree.SubElement(g_ibs, "vCredPres").text = "0.00"
                etree.SubElement(g_ibs, "vCredPresCondSus").text = "0.00"

            # gCBS (optional — emit if any CBS value exists)
            if nota_fiscal.totais_cbs:
                g_cbs = etree.SubElement(ibscbs_tot, "gCBS")
                etree.SubElement(g_cbs, "vDif").text = "0.00"
                etree.SubElement(g_cbs, "vDevTrib").text = "0.00"
                etree.SubElement(g_cbs, "vCBS").text = "{:.2f}".format(nota_fiscal.totais_cbs)
                etree.SubElement(g_cbs, "vCredPres").text = "0.00"
                etree.SubElement(g_cbs, "vCredPresCondSus").text = "0.00"

            # gMono: not implemented yet (monofasia totals)
            # gEstornoCred: not implemented yet (estorno de credito totals)

        # Transporte
        transp = etree.SubElement(raiz, "transp")
        etree.SubElement(transp, "modFrete").text = str(nota_fiscal.transporte_modalidade_frete)

        # Apenas NF-e
        if nota_fiscal.modelo == 55:
            # Transportadora
            if nota_fiscal.transporte_transportadora:
                transp.append(
                    self._serializar_transportadora(
                        nota_fiscal.transporte_transportadora,
                        retorna_string=False,
                    )
                )

            # Veículo
            if nota_fiscal.transporte_veiculo_placa and nota_fiscal.transporte_veiculo_uf:
                veiculo = etree.SubElement(transp, "veicTransp")
                etree.SubElement(
                    veiculo, "placa"
                ).text = nota_fiscal.transporte_veiculo_placa  # Obrigatório EX: XXX9999
                etree.SubElement(veiculo, "UF").text = nota_fiscal.transporte_veiculo_uf
                # Registro Nacional de Transportador de Carga (ANTT)
                if nota_fiscal.transporte_veiculo_rntc:
                    etree.SubElement(veiculo, "RNTC").text = nota_fiscal.transporte_veiculo_rntc

            # Reboque
            if nota_fiscal.transporte_reboque_placa and nota_fiscal.transporte_reboque_uf:
                reboque = etree.SubElement(transp, "reboque")
                etree.SubElement(reboque, "placa").text = nota_fiscal.transporte_reboque_placa
                etree.SubElement(reboque, "UF").text = nota_fiscal.transporte_reboque_uf
                # Registro Nacional de Transportador de Carga (ANTT)
                if nota_fiscal.transporte_reboque_rntc:
                    etree.SubElement(reboque, "RNTC").text = nota_fiscal.transporte_reboque_rntc

            # Volumes
            if nota_fiscal.transporte_volumes:
                for volume in nota_fiscal.transporte_volumes:
                    vol = etree.SubElement(transp, "vol")
                    if volume.quantidade:
                        etree.SubElement(vol, "qVol").text = str(volume.quantidade)
                        etree.SubElement(vol, "esp").text = volume.especie
                        if volume.marca:
                            etree.SubElement(vol, "marca").text = volume.marca
                        if volume.numeracao:
                            etree.SubElement(vol, "nVol").text = volume.numeracao
                        etree.SubElement(vol, "pesoL").text = str(volume.peso_liquido)
                        etree.SubElement(vol, "pesoB").text = str(volume.peso_bruto)

                        # Lacres
                        if volume.lacres:
                            lacres = etree.SubElement(vol, "lacres")
                            for lacre in volume.lacres:
                                etree.SubElement(lacres, "nLacre").text = lacre.numero_lacre

        # Cobrança
        if (nota_fiscal.fatura_numero) or (
            nota_fiscal.duplicatas and len(nota_fiscal.duplicatas) > 0
        ):
            cobr = etree.SubElement(raiz, "cobr")

            # Fatura 0-1
            if nota_fiscal.fatura_numero:
                fat = etree.SubElement(cobr, "fat")
                etree.SubElement(fat, "nFat").text = nota_fiscal.fatura_numero
                etree.SubElement(fat, "vOrig").text = "{:.2f}".format(
                    nota_fiscal.fatura_valor_original
                )
                etree.SubElement(fat, "vDesc").text = "{:.2f}".format(
                    nota_fiscal.fatura_valor_desconto
                )
                etree.SubElement(fat, "vLiq").text = "{:.2f}".format(
                    nota_fiscal.fatura_valor_liquido
                )

            # Duplicata 0-N
            if nota_fiscal.duplicatas and len(nota_fiscal.duplicatas) > 0:
                for num, item in enumerate(nota_fiscal.duplicatas):
                    dup = etree.SubElement(cobr, "dup")
                    etree.SubElement(dup, "nDup").text = item.numero
                    etree.SubElement(dup, "dVenc").text = item.data_vencimento.strftime("%Y-%m-%d")
                    etree.SubElement(dup, "vDup").text = "{:.2f}".format(item.valor)

        # Pagamento
        """ Obrigatório o preenchimento do Grupo Informações de Pagamento para NF-e e NFC-e.
        Para as notas com finalidade de Ajuste ou Devolução
        o campo Forma de Pagamento deve ser preenchido com 90=Sem Pagamento. """
        if nota_fiscal.tipo_pagamento is not None:
            warnings.warn(
                "O campo 'tipo_pagamento' está obsoleto e será removido em versões futuras. "
                "Utilize o campo 'pagamentos' em seu lugar.",
                DeprecationWarning,
            )
            raiz.append(
                self._serializar_pagamentos_antigo_deprecado(
                    tipo_pagamento=nota_fiscal.tipo_pagamento,
                    finalidade_emissao=nota_fiscal.finalidade_emissao,
                    totais_icms_total_nota=nota_fiscal.totais_icms_total_nota,
                )
            )
        else:
            raiz.append(
                self._serializar_pagamentos(
                    pagamentos=nota_fiscal.pagamentos,
                    finalidade_emissao=nota_fiscal.finalidade_emissao,
                    valor_troco=nota_fiscal.valor_troco,
                    retorna_string=False,
                )
            )

        # Informações adicionais
        if (
            nota_fiscal.informacoes_adicionais_interesse_fisco
            or nota_fiscal.informacoes_complementares_interesse_contribuinte
        ):
            info_ad = etree.SubElement(raiz, "infAdic")
            if nota_fiscal.informacoes_adicionais_interesse_fisco:
                etree.SubElement(
                    info_ad, "infAdFisco"
                ).text = nota_fiscal.informacoes_adicionais_interesse_fisco
            if nota_fiscal.informacoes_complementares_interesse_contribuinte:
                etree.SubElement(
                    info_ad, "infCpl"
                ).text = nota_fiscal.informacoes_complementares_interesse_contribuinte

        # Responsavel Tecnico NT2018/003
        if nota_fiscal.responsavel_tecnico:
            raiz.append(
                self._serializar_responsavel_tecnico(
                    nota_fiscal.responsavel_tecnico[0], retorna_string=False
                )
            )

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def serializar_evento(self, evento, tag_raiz="evento", retorna_string=False):
        tz = datetime.now().astimezone().strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])
        raiz = etree.Element(tag_raiz, versao="1.00", xmlns=NAMESPACE_NFE)
        e = etree.SubElement(raiz, "infEvento", Id=evento.identificador)
        etree.SubElement(e, "cOrgao").text = CODIGOS_ESTADOS[evento.uf.upper()]
        etree.SubElement(e, "tpAmb").text = str(self._ambiente)
        if len(so_numeros(evento.cnpj)) == 11:
            etree.SubElement(e, "CPF").text = evento.cnpj
        else:
            etree.SubElement(e, "CNPJ").text = evento.cnpj
        etree.SubElement(e, "chNFe").text = evento.chave
        etree.SubElement(e, "dhEvento").text = (
            evento.data_emissao.strftime("%Y-%m-%dT%H:%M:%S") + tz
        )
        etree.SubElement(e, "tpEvento").text = evento.tp_evento
        etree.SubElement(e, "nSeqEvento").text = str(evento.n_seq_evento)
        etree.SubElement(e, "verEvento").text = "1.00"
        det = etree.SubElement(e, "detEvento", versao="1.00")
        etree.SubElement(det, "descEvento").text = evento.descricao
        if evento.descricao == "Cancelamento":
            etree.SubElement(det, "nProt").text = evento.protocolo
            etree.SubElement(det, "xJust").text = evento.justificativa
        elif evento.descricao == "Carta de Correcao":
            etree.SubElement(det, "xCorrecao").text = evento.correcao
            etree.SubElement(det, "xCondUso").text = evento.cond_uso
        elif evento.descricao == "Operacao nao Realizada":
            etree.SubElement(det, "xJust").text = evento.justificativa

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def serializar_evento_mdfe(self, evento, tag_raiz="eventoMDFe", retorna_string=False):
        tz = datetime.now().astimezone().strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])
        raiz = etree.Element(tag_raiz, versao=VERSAO_MDFE, xmlns=NAMESPACE_MDFE)
        e = etree.SubElement(raiz, "infEvento", Id=evento.identificador)
        etree.SubElement(e, "cOrgao").text = CODIGOS_ESTADOS[evento.uf.upper()]
        etree.SubElement(e, "tpAmb").text = str(self._ambiente)
        if len(so_numeros(evento.cnpj)) == 11:
            etree.SubElement(e, "CPF").text = evento.cnpj
        else:
            etree.SubElement(e, "CNPJ").text = evento.cnpj
        etree.SubElement(e, "chMDFe").text = evento.chave
        etree.SubElement(e, "dhEvento").text = (
            evento.data_emissao.strftime("%Y-%m-%dT%H:%M:%S") + tz
        )
        etree.SubElement(e, "tpEvento").text = evento.tp_evento
        etree.SubElement(e, "nSeqEvento").text = str(evento.n_seq_evento)
        det = etree.SubElement(e, "detEvento", versaoEvento=VERSAO_MDFE)
        if evento.descricao == "Cancelamento":
            cancelamento = etree.SubElement(det, "evCancMDFe")
            etree.SubElement(cancelamento, "descEvento").text = evento.descricao
            etree.SubElement(cancelamento, "nProt").text = evento.protocolo
            etree.SubElement(cancelamento, "xJust").text = evento.justificativa
        if evento.descricao == "Encerramento":
            encerramento = etree.SubElement(det, "evEncMDFe")
            etree.SubElement(encerramento, "descEvento").text = evento.descricao
            etree.SubElement(encerramento, "nProt").text = evento.protocolo
            etree.SubElement(encerramento, "dtEnc").text = evento.dtenc.strftime("%Y-%m-%d")
            etree.SubElement(encerramento, "cUF").text = str(evento.cuf)
            etree.SubElement(encerramento, "cMun").text = str(evento.cmun)
        elif evento.descricao == "Inclusão Condutor":
            inclusao = etree.SubElement(det, "evIncCondutorMDFe")
            etree.SubElement(inclusao, "descEvento").text = evento.descricao
            condutor = etree.SubElement(inclusao, "condutor")
            etree.SubElement(condutor, "xNome").text = evento.nome_motorista
            etree.SubElement(condutor, "CPF").text = evento.cpf_motorista
        elif evento.descricao == "Inclusao DF-e":
            inclusao = etree.SubElement(det, "evIncDFeMDFe")
            etree.SubElement(inclusao, "descEvento").text = evento.descricao
            etree.SubElement(inclusao, "nProt").text = evento.protocolo
            etree.SubElement(inclusao, "cMunCarrega").text = str(evento.cmun_carrega)
            etree.SubElement(inclusao, "xMunCarrega").text = evento.xmun_carrega
            infDoc = etree.SubElement(inclusao, "infDoc")
            etree.SubElement(infDoc, "cMunDescarga").text = str(evento.cmun_descarga)
            etree.SubElement(infDoc, "xMunDescarga").text = evento.xmun_descarga
            etree.SubElement(infDoc, "chNFe").text = evento.chave_nfe
        elif evento.descricao == "Pagamento Operacao MDF-e":
            pagamento = etree.SubElement(det, "evPagtoOperMDFe")
            etree.SubElement(pagamento, "descEvento").text = evento.descricao
            etree.SubElement(pagamento, "nProt").text = evento.protocolo

            # Viagens
            infViagens = etree.SubElement(pagamento, "infViagens")
            etree.SubElement(infViagens, "qtdViagens").text = evento.qtd_viagens.zfill(5)
            etree.SubElement(infViagens, "nroViagem").text = evento.nro_viagens.zfill(5)

            # Informações do pagamento
            infPag = etree.SubElement(pagamento, "infPag")
            etree.SubElement(infPag, "xNome").text = evento.nome_contratante
            if len(evento.cpfcnpj_contratante) == 11:
                etree.SubElement(infPag, "CPF").text = evento.cpfcnpj_contratante
            else:
                etree.SubElement(infPag, "CNPJ").text = evento.cpfcnpj_contratante

            # Componentes de Pagamento do Frete
            Comp = etree.SubElement(infPag, "Comp")
            etree.SubElement(Comp, "tpComp").text = evento.tpComp.zfill(2)
            etree.SubElement(Comp, "vComp").text = "{:.2f}".format(evento.vComp)

            # Continuação das Informações do pagamento
            etree.SubElement(infPag, "vContrato").text = "{:.2f}".format(evento.vContrato)
            etree.SubElement(infPag, "indPag").text = evento.indPag

            # Se indPag == 1 (0=A vista e 1=A prazo)
            if evento.indPag != "":
                if int(evento.indPag) == 1:
                    infPrazo = etree.SubElement(infPag, "infPrazo")
                    etree.SubElement(infPrazo, "nParcela").text = evento.nParcela.zfill(3)
                    etree.SubElement(infPrazo, "dVenc").text = evento.dVenc.strftime("%Y-%m-%d")
                    etree.SubElement(infPrazo, "vParcela").text = "{:.2f}".format(evento.vParcela)

            # Informações bancárias
            infBanc = etree.SubElement(infPag, "infBanc")
            if evento.CNPJIPEF != "":
                etree.SubElement(infBanc, "CNPJIPEF").text = evento.CNPJIPEF.zfill(14)
            else:
                etree.SubElement(infBanc, "codBanco").text = evento.codBanco
                etree.SubElement(infBanc, "codAgencia").text = evento.codAgencia

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz


class SerializacaoQrcode(object):
    """Classe que gera e serializa o qrcode de NFC-e no xml"""

    def gerar_qrcode(self, token, csc, xml, return_qr=False, online=True):
        """Classe para gerar url do qrcode da NFC-e"""
        # Procura atributos no xml
        ns = {"ns": NAMESPACE_NFE}
        sig = {"sig": NAMESPACE_SIG}
        # Tag Raiz NFe Ex: <NFe>
        nfe = xml
        chave = nfe[0].attrib["Id"].replace("NFe", "")
        data = nfe.xpath("ns:infNFe/ns:ide/ns:dhEmi/text()", namespaces=ns)[0].encode()
        tpamb = nfe.xpath("ns:infNFe/ns:ide/ns:tpAmb/text()", namespaces=ns)[0]
        cuf = nfe.xpath("ns:infNFe/ns:ide/ns:cUF/text()", namespaces=ns)[0]
        uf = [key for key, value in CODIGOS_ESTADOS.items() if value == cuf][0].upper()

        # tenta encontrar a tag cpf
        try:
            cpf = nfe.xpath("ns:infNFe/ns:dest/ns:CPF/text()", namespaces=ns)[0]
        except IndexError:
            # em caso de erro tenta procurar a tag cnpj
            try:
                cpf = nfe.xpath("ns:infNFe/ns:dest/ns:CNPJ/text()", namespaces=ns)[0]
            except IndexError:
                cpf = None  # noqa: F841
        total = nfe.xpath("ns:infNFe/ns:total/ns:ICMSTot/ns:vNF/text()", namespaces=ns)[0]
        # icms = nfe.xpath('ns:infNFe/ns:total/ns:ICMSTot/ns:vICMS/text()', namespaces=ns)[0]
        digest = nfe.xpath(
            "sig:Signature/sig:SignedInfo/sig:Reference/sig:DigestValue/text()",
            namespaces=sig,
        )[0].encode()

        lista_dia = re.findall(r"-\d{2}", str(data))
        dia = str(lista_dia[1])
        dia = dia[1:]
        replacements = {"0": ""}
        token = re.sub("([0])", lambda m: replacements[m.group()], token)

        # VERSAO_QRCODE =2
        if online:
            # versão online
            url = "{}|{}|{}|{}".format(chave, VERSAO_QRCODE, tpamb, token)
        else:
            # versão offline
            digest = digest.hex()

            url = "{}|{}|{}|{}|{}|{}|{}".format(
                chave, VERSAO_QRCODE, tpamb, dia, total, digest, token
            )

        url_complementar = url + csc
        url_hash = hashlib.sha1(url_complementar.encode()).digest()
        url_hash = base64.b16encode(url_hash).decode()

        url = "p={}|{}".format(url, url_hash)

        # url_chave -Texto com a URL de consulta por chave de acesso a ser impressa no DANFE NFC-e.
        # Informar a URL da “Consulta por chave de acesso da NFC-e”.
        # A mesma URL que deve estar informada no DANFE NFC-e para consulta por chave de acesso
        lista_uf_padrao = ["PR", "CE", "RS", "RJ", "RO", "DF"]
        if uf in lista_uf_padrao:
            qrcode = NFCE[uf]["QR"] + url
            url_chave = NFCE[uf]["URL"]
        elif uf == "SP":
            if tpamb == "1":
                qrcode = NFCE[uf]["HTTPS"] + "www." + NFCE[uf]["QR"] + url
                url_chave = NFCE[uf]["HTTPS"] + "www." + NFCE[uf]["URL"]
            else:
                qrcode = NFCE[uf]["HTTPS"] + "www.homologacao." + NFCE[uf]["QR"] + url
                url_chave = NFCE[uf]["HTTPS"] + "www.homologacao." + NFCE[uf]["URL"]
        # BA tem comportamento distindo para qrcode e url
        elif uf == "BA":
            if tpamb == "1":
                qrcode = NFCE[uf]["HTTPS"] + NFCE[uf]["QR"] + url
            else:
                qrcode = NFCE[uf]["HOMOLOGACAO"] + NFCE[uf]["QR"] + url
            url_chave = url_chave = NFCE[uf]["URL"]
        # MG tem comportamento distintos para qrcode e url
        elif uf == "MG":
            qrcode = NFCE[uf]["QR"] + url
            if tpamb == "1":
                url_chave = NFCE[uf]["HTTPS"] + NFCE[uf]["URL"]
            else:
                url_chave = NFCE[uf]["HOMOLOGACAO"] + NFCE[uf]["URL"]
        # AM tem comportamento distintos para qrcode e url
        elif uf == "AM":
            if tpamb == "1":
                qrcode = NFCE[uf]["HTTPS"] + NFCE[uf]["QR"] + url
                url_chave = NFCE[uf]["HTTPS"] + NFCE[uf]["URL"]
            else:
                qrcode = NFCE[uf]["HTTPS"] + NFCE[uf]["QR_HOMOLOGACAO"] + url
                url_chave = NFCE[uf]["HTTPS"] + NFCE[uf]["URL"]
        # AC, RR, PA, SE
        else:
            if tpamb == "1":
                qrcode = NFCE[uf]["HTTPS"] + NFCE[uf]["QR"] + url
                url_chave = NFCE[uf]["HTTPS"] + NFCE[uf]["URL"]
            else:
                qrcode = NFCE[uf]["HOMOLOGACAO"] + NFCE[uf]["QR"] + url
                url_chave = NFCE[uf]["HOMOLOGACAO"] + NFCE[uf]["URL"]
        # adicionta tag infNFeSupl com qrcode
        info = etree.Element("infNFeSupl")
        etree.SubElement(info, "qrCode").text = etree.CDATA(qrcode.strip())
        etree.SubElement(info, "urlChave").text = url_chave

        nfe.insert(1, info)

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
        if self.autorizador.lower() == "betha":
            from pynfe.processamento.autorizador_nfse import SerializacaoBetha

            return SerializacaoBetha().gerar(nfse)
        else:
            raise Exception("Este método só esta implementado no autorizador Betha.")

    def gerar_lote(self, nfse):
        if self.autorizador.lower() == "ginfes":
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes

            return SerializacaoGinfes().serializar_lote_assincrono(nfse)
        else:
            raise Exception("Este método só esta implementado no autorizador ginfes.")

    def consultar_nfse(self, emitente, numero=None, inicio=None, fim=None):
        if self.autorizador.lower() == "ginfes":
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes

            return SerializacaoGinfes().consultar_nfse(emitente, numero, inicio, fim)
        else:
            raise Exception("Este método só esta implementado no autorizador ginfes.")

    def consultar_lote(self, emitente, numero):
        if self.autorizador.lower() == "ginfes":
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes

            return SerializacaoGinfes().consultar_lote(emitente, numero)
        else:
            raise Exception("Este método só esta implementado no autorizador ginfes.")

    def consultar_rps(self, emitente, numero, serie, tipo):
        if self.autorizador.lower() == "ginfes":
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes

            return SerializacaoGinfes().consultar_rps(emitente, numero, serie, tipo)
        else:
            raise Exception("Este método só esta implementado no autorizador ginfes.")

    def consultar_situacao_lote(self, emitente, numero):
        if self.autorizador.lower() == "ginfes":
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes

            return SerializacaoGinfes().consultar_situacao_lote(emitente, numero)
        else:
            raise Exception("Este método só esta implementado no autorizador ginfes.")

    def cancelar(self, nfse):
        if self.autorizador.lower() == "ginfes":
            from pynfe.processamento.autorizador_nfse import SerializacaoGinfes

            # versao 3
            # return SerializacaoGinfes().cancelar(nfse)
            # versao 2
            return SerializacaoGinfes().cancelar_v2(nfse)
        elif self.autorizador.lower() == "betha":
            from pynfe.processamento.autorizador_nfse import SerializacaoBetha

            return SerializacaoBetha().cancelar(nfse)
        else:
            raise Exception("Autorizador não suportado para cancelamento!")


class SerializacaoQrcodeMDFe(object):
    """Classe que gera e serializa o qrcode do MDF-e no xml"""

    def gerar_qrcode(self, xml, return_qr=False):
        # Procura atributos no xml
        ns = {"ns": NAMESPACE_MDFE}

        # Tag Raiz MDFe Ex: <MDFe>
        mdfe = xml
        chave = mdfe[0].attrib["Id"].replace("MDFe", "")
        tpamb = mdfe.xpath("ns:infMDFe/ns:ide/ns:tpAmb/text()", namespaces=ns)[0]

        url_padrao = MDFE["SVRS"]["QRCODE"]
        qrcode = f"{url_padrao}?chMDFe={chave}&tpAmb={tpamb}"

        # adiciona tag infMDFeSupl com qrcode
        infMDFeSupl = etree.Element("infMDFeSupl")
        etree.SubElement(infMDFeSupl, "qrCodMDFe").text = etree.CDATA(qrcode.strip())
        mdfe.insert(1, infMDFeSupl)

        if return_qr:
            return mdfe, qrcode.strip()
        else:
            return mdfe


class SerializacaoMDFe(Serializacao):
    """Classe de serialização do arquivo xml"""

    _versao = VERSAO_MDFE

    def exportar(self, destino=None, retorna_string=False, limpar=True, **kwargs):
        """Gera o(s) arquivo(s) do Manifesto de Documento Fiscais Eletrônicos no padrao oficial
        da SEFAZ e Receita Federal, para ser(em) enviado(s) para o webservice ou para ser(em)
        armazenado(s) em cache local.
        @param destino -
        @param retorna_string - Retorna uma string para debug.
        @param limpar - Limpa a fonte de dados para não gerar xml com dados duplicados.
        """
        try:
            # No raiz do XML de saida
            raiz = etree.Element("MDFe", xmlns=NAMESPACE_MDFE)

            # Carrega lista de Manifestos
            manifestos = self._fonte_dados.obter_lista(_classe=Manifesto, **kwargs)

            for mdfe in manifestos:
                raiz.append(self._serializar_manifesto(mdfe, retorna_string=False))

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

        raise Exception("Metodo nao implementado")

    def _serializar_emitente(self, emitente, tag_raiz="emit", retorna_string=True):
        raiz = etree.Element(tag_raiz)

        # Dados do emitente
        if len(so_numeros(emitente.cpfcnpj)) == 11:
            etree.SubElement(raiz, "CPF").text = so_numeros(emitente.cpfcnpj)
        else:
            etree.SubElement(raiz, "CNPJ").text = so_numeros(emitente.cpfcnpj)
        etree.SubElement(raiz, "IE").text = emitente.inscricao_estadual
        etree.SubElement(raiz, "xNome").text = emitente.razao_social
        if emitente.nome_fantasia:
            etree.SubElement(raiz, "xFant").text = emitente.nome_fantasia
        # Endereço
        endereco = etree.SubElement(raiz, "enderEmit")
        etree.SubElement(endereco, "xLgr").text = emitente.endereco_logradouro
        etree.SubElement(endereco, "nro").text = emitente.endereco_numero
        if emitente.endereco_complemento:
            etree.SubElement(endereco, "xCpl").text = emitente.endereco_complemento
        etree.SubElement(endereco, "xBairro").text = emitente.endereco_bairro
        etree.SubElement(endereco, "cMun").text = obter_codigo_por_municipio(
            emitente.endereco_municipio, emitente.endereco_uf
        )
        etree.SubElement(endereco, "xMun").text = emitente.endereco_municipio
        etree.SubElement(endereco, "CEP").text = so_numeros(emitente.endereco_cep)
        etree.SubElement(endereco, "UF").text = emitente.endereco_uf
        if emitente.endereco_telefone:
            etree.SubElement(endereco, "fone").text = emitente.endereco_telefone
        if emitente.endereco_email:
            etree.SubElement(endereco, "email").text = emitente.endereco_email
        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_municipio_carrega(
        self, municipio_carrega, tag_raiz="infMunCarrega", retorna_string=True
    ):
        raiz = etree.Element(tag_raiz)
        etree.SubElement(raiz, "cMunCarrega").text = str(municipio_carrega.cMunCarrega)
        etree.SubElement(raiz, "xMunCarrega").text = str(municipio_carrega.xMunCarrega)

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_percurso(self, percurso, tag_raiz="infPercurso", retorna_string=True):
        raiz = etree.Element(tag_raiz)
        etree.SubElement(raiz, "UFPer").text = percurso.UFPer

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_modal_rodoviario(
        self, modal_rodoviario, tag_raiz="infModal", retorna_string=True
    ):
        """
        <infModal versaoModal="3.00">
            rodo
                infANTT
                    infCIOT
                    valePed
                    infContratante
                    infPag
                veicTracao
                    prop
                    condutor
                veicReboque
                    prop
        """
        raiz = etree.Element(tag_raiz, versaoModal=self._versao)
        rodo = etree.SubElement(raiz, "rodo")

        infANTT = etree.SubElement(rodo, "infANTT")
        if modal_rodoviario.rntrc:
            etree.SubElement(infANTT, "RNTRC").text = modal_rodoviario.rntrc.zfill(8)

        # CIOT
        if modal_rodoviario.ciot is not None:
            for num, item in enumerate(modal_rodoviario.ciot):
                infCIOT = etree.SubElement(infANTT, "infCIOT")
                etree.SubElement(infCIOT, "CIOT").text = item.numero_ciot
                if len(item.cpfcnpj) == 11:
                    etree.SubElement(infCIOT, "CPF").text = item.cpfcnpj
                elif len(item.cpfcnpj) == 14:
                    etree.SubElement(infCIOT, "CNPJ").text = item.cpfcnpj

        # Vale Pedágio
        if modal_rodoviario.pedagio is not None:
            valePed = etree.SubElement(infANTT, "valePed")
            for num, item in enumerate(modal_rodoviario.pedagio):
                disp = etree.SubElement(valePed, "disp")
                etree.SubElement(disp, "CNPJForn").text = item.cnpj_fornecedor
                if len(item.cpfcnpj_pagador) == 11:
                    etree.SubElement(disp, "CPFPg").text = item.cpfcnpj_pagador
                elif len(item.cpfcnpj_pagador) == 14:
                    etree.SubElement(disp, "CNPJPg").text = item.cpfcnpj_pagador
                etree.SubElement(disp, "nCompra").text = item.numero_compra
                etree.SubElement(disp, "vValePed").text = "{:.2f}".format(
                    item.valor_pedagio or 0
                )  # Valor do ICMS

        # Contratantes
        if modal_rodoviario.contratante is not None:
            for num, item in enumerate(modal_rodoviario.contratante):
                infContratante = etree.SubElement(infANTT, "infContratante")
                etree.SubElement(infContratante, "xNome").text = item.nome
                if len(item.cpfcnpj) == 11:
                    etree.SubElement(infContratante, "CPF").text = item.cpfcnpj
                elif len(item.cpfcnpj) == 14:
                    etree.SubElement(infContratante, "CNPJ").text = item.cpfcnpj

                # Contrato
                if item.NroContrato:
                    infContrato = etree.SubElement(infContratante, "infContrato")
                    etree.SubElement(infContrato, "NroContrato").text = item.NroContrato
                    etree.SubElement(infContrato, "vContratoGlobal").text = "{:.2f}".format(
                        item.vContratoGlobal or 0
                    )

        # Veículo Tração
        if len(modal_rodoviario.veiculo_tracao) != 1:
            raise "Permitido somente um único veículo Tração"

        for num, item in enumerate(modal_rodoviario.veiculo_tracao):
            veicTracao = etree.SubElement(rodo, "veicTracao")
            if item.cInt:
                etree.SubElement(veicTracao, "cInt").text = item.cInt
            etree.SubElement(veicTracao, "placa").text = item.placa
            if item.RENAVAM:
                etree.SubElement(veicTracao, "RENAVAM").text = item.RENAVAM
            etree.SubElement(veicTracao, "tara").text = "{:.0f}".format(item.tara or 0)
            etree.SubElement(veicTracao, "capKG").text = "{:.0f}".format(item.capKG or 0)
            etree.SubElement(veicTracao, "capM3").text = "{:.0f}".format(item.capM3 or 0)

            # Propritario do veículo Tração
            if item.proprietario:
                prop = etree.SubElement(veicTracao, "prop")

                if len(item.proprietario.cpfcnpj) == 11:
                    etree.SubElement(prop, "CPF").text = item.proprietario.cpfcnpj
                elif len(item.proprietario.cpfcnpj) == 14:
                    etree.SubElement(prop, "CNPJ").text = item.proprietario.cpfcnpj

                if item.proprietario.rntrc:
                    etree.SubElement(prop, "RNTRC").text = item.proprietario.rntrc.zfill(8)
                etree.SubElement(prop, "xNome").text = item.proprietario.nome
                if item.proprietario.inscricao_estudual is not None:
                    etree.SubElement(prop, "IE").text = item.proprietario.inscricao_estudual
                etree.SubElement(prop, "UF").text = item.proprietario.uf
                # tpProp: 0=TACAgregado; 1=TACIndependente; 2=Outros
                etree.SubElement(prop, "tpProp").text = item.proprietario.tipo

            # condutor 1-n
            if item.condutor is not None:
                for num, item_condutor in enumerate(item.condutor):
                    condutor = etree.SubElement(veicTracao, "condutor")
                    etree.SubElement(condutor, "xNome").text = item_condutor.nome_motorista
                    etree.SubElement(condutor, "CPF").text = item_condutor.cpf_motorista
            # fim-condutor

            etree.SubElement(veicTracao, "tpRod").text = item.tpRod
            etree.SubElement(veicTracao, "tpCar").text = item.tpCar
            etree.SubElement(veicTracao, "UF").text = item.UF
            # fim-veicTracao

        # Veículos reboque 1-n
        if modal_rodoviario.veiculo_reboque is not None:
            for num, item_reboque in enumerate(modal_rodoviario.veiculo_reboque):
                veicReboque = etree.SubElement(rodo, "veicReboque")
                if item_reboque.cInt:
                    etree.SubElement(veicReboque, "cInt").text = item_reboque.cInt
                etree.SubElement(veicReboque, "placa").text = item_reboque.placa
                if item_reboque.RENAVAM:
                    etree.SubElement(veicReboque, "RENAVAM").text = item_reboque.RENAVAM
                etree.SubElement(veicReboque, "tara").text = "{:.0f}".format(item_reboque.tara or 0)
                etree.SubElement(veicReboque, "capKG").text = "{:.0f}".format(
                    item_reboque.capKG or 0
                )
                etree.SubElement(veicReboque, "capM3").text = "{:.0f}".format(
                    item_reboque.capM3 or 0
                )

                # Propritario do veículo Reboque
                if item_reboque.proprietario:
                    prop = etree.SubElement(veicReboque, "prop")

                    if len(item_reboque.proprietario.cpfcnpj) == 11:
                        etree.SubElement(prop, "CPF").text = item_reboque.proprietario.cpfcnpj
                    elif len(item_reboque.proprietario.cpfcnpj) == 14:
                        etree.SubElement(prop, "CNPJ").text = item_reboque.proprietario.cpfcnpj

                    if item_reboque.proprietario.rntrc:
                        etree.SubElement(
                            prop, "RNTRC"
                        ).text = item_reboque.proprietario.rntrc.zfill(8)
                    etree.SubElement(prop, "xNome").text = item_reboque.proprietario.nome
                    if item_reboque.proprietario.inscricao_estudual is not None:
                        etree.SubElement(
                            prop, "IE"
                        ).text = item_reboque.proprietario.inscricao_estudual
                    etree.SubElement(prop, "UF").text = item_reboque.proprietario.uf
                    # tpProp: 0=TACAgregado; 1=TACIndependente; 2=Outros
                    etree.SubElement(prop, "tpProp").text = item_reboque.proprietario.tipo

                etree.SubElement(veicReboque, "tpCar").text = item_reboque.tpCar
                etree.SubElement(veicReboque, "UF").text = item_reboque.UF
        # fim-veicReboque

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_documentos(self, documentos, tag_raiz="infDoc", retorna_string=True):
        raiz = etree.Element(tag_raiz)

        if len(documentos) <= 0:
            raise "MDFe deve ter uma NFe ou uma CTe vinculadas"

        for num, item in enumerate(documentos):
            infMunDescarga = etree.SubElement(raiz, "infMunDescarga")
            etree.SubElement(infMunDescarga, "cMunDescarga").text = item.cMunDescarga
            etree.SubElement(infMunDescarga, "xMunDescarga").text = item.xMunDescarga

            if len(item.documentos_nfe) > 0:
                for num, item_doc in enumerate(item.documentos_nfe):
                    infNFe = etree.SubElement(infMunDescarga, "infNFe")
                    etree.SubElement(infNFe, "chNFe").text = item_doc.chave_acesso_nfe

            elif len(documentos.documentos_cte) > 0:
                for num, item_doc in enumerate(item.documentos_cte):
                    infCTe = etree.SubElement(infMunDescarga, "infCTe")
                    etree.SubElement(infCTe, "chCTe").text = item_doc.chave_acesso_cte

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_seguradora(self, seguradora, tag_raiz="seg", retorna_string=True):
        raiz = etree.Element(tag_raiz)

        infResp = etree.SubElement(raiz, "infResp")
        etree.SubElement(infResp, "respSeg").text = seguradora.responsavel_seguro
        etree.SubElement(infResp, "CNPJ").text = seguradora.cnpj_responsavel

        infSeg = etree.SubElement(raiz, "infSeg")
        etree.SubElement(infSeg, "xSeg").text = seguradora.nome_seguradora
        etree.SubElement(infSeg, "CNPJ").text = seguradora.cnpj_seguradora

        etree.SubElement(raiz, "nApol").text = seguradora.numero_apolice

        if len(seguradora.averbacoes) > 0:
            for num, item in enumerate(seguradora.averbacoes):
                etree.SubElement(raiz, "nAver").text = item.numero

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_produto(self, produto, tag_raiz="prodPred", retorna_string=True):
        raiz = etree.Element(tag_raiz)
        etree.SubElement(raiz, "tpCarga").text = produto.tipo_carga
        etree.SubElement(raiz, "xProd").text = produto.nome_produto
        etree.SubElement(raiz, "cEAN").text = produto.cean
        etree.SubElement(raiz, "NCM").text = produto.ncm

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_totais(self, totais, tag_raiz="tot", retorna_string=True):
        raiz = etree.Element(tag_raiz)

        if totais.qCTe > 0:
            etree.SubElement(raiz, "qCTe").text = str(totais.qCTe)
        elif totais.qNFe > 0:
            etree.SubElement(raiz, "qNFe").text = str(totais.qNFe)

        etree.SubElement(raiz, "vCarga").text = str("{:.2f}").format(totais.vCarga or 0)
        if totais.cUnid == "KG":
            etree.SubElement(raiz, "cUnid").text = "01"
        elif totais.cUnid == "TON":
            etree.SubElement(raiz, "cUnid").text = "02"
        else:
            raise "cUnid deve ser KG ou TON"
        etree.SubElement(raiz, "qCarga").text = str("{:.4f}").format(totais.qCarga or 0)

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_lacres(self, lacres, tag_raiz="lacres", retorna_string=True):
        raiz = etree.Element(tag_raiz)
        etree.SubElement(raiz, "nLacre").text = str(lacres.nLacre)

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_responsavel_tecnico(
        self, responsavel_tecnico, tag_raiz="infRespTec", retorna_string=True
    ):
        raiz = etree.Element(tag_raiz)
        etree.SubElement(raiz, "CNPJ").text = responsavel_tecnico.cnpj
        etree.SubElement(raiz, "xContato").text = responsavel_tecnico.contato
        etree.SubElement(raiz, "email").text = responsavel_tecnico.email
        etree.SubElement(raiz, "fone").text = responsavel_tecnico.fone

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_manifesto(self, manifesto, tag_raiz="infMDFe", retorna_string=True):
        raiz = etree.Element(tag_raiz, versao=self._versao)

        # 'Id' da tag raiz
        # Ex.: MDFe35080599999090910270550010000000011518005123
        raiz.attrib["Id"] = manifesto.identificador_unico

        tz = manifesto.data_emissao.strftime("%z")
        if not tz:
            tz = datetime.now().astimezone().strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])

        # Dados do Manifesto
        ide = etree.SubElement(raiz, "ide")
        etree.SubElement(ide, "cUF").text = CODIGOS_ESTADOS[manifesto.uf]
        etree.SubElement(ide, "tpAmb").text = str(self._ambiente)
        etree.SubElement(ide, "tpEmit").text = str(manifesto.tipo_emitente)

        # 0=nenhum; 1=etc; 2=tac; 3=ctc
        if manifesto.tipo_transportador != 0:
            etree.SubElement(ide, "tpTransp").text = str(manifesto.tipo_transportador)

        etree.SubElement(ide, "mod").text = str(manifesto.modelo)
        etree.SubElement(ide, "serie").text = manifesto.serie
        etree.SubElement(ide, "nMDF").text = str(manifesto.numero_mdfe)
        etree.SubElement(ide, "cMDF").text = manifesto.codigo_numerico_aleatorio
        etree.SubElement(ide, "cDV").text = manifesto.dv_codigo_numerico_aleatorio
        etree.SubElement(ide, "modal").text = str(manifesto.modal)
        etree.SubElement(ide, "dhEmi").text = (
            manifesto.data_emissao.strftime("%Y-%m-%dT%H:%M:%S") + tz
        )
        etree.SubElement(ide, "tpEmis").text = str(manifesto.forma_emissao)
        etree.SubElement(ide, "procEmi").text = str(manifesto.processo_emissao)
        etree.SubElement(
            ide, "verProc"
        ).text = f"{self._nome_aplicacao} {manifesto.versao_processo_emissao}"
        etree.SubElement(ide, "UFIni").text = manifesto.UFIni
        etree.SubElement(ide, "UFFim").text = manifesto.UFFim

        # Municipios de Carregamento
        for num, item in enumerate(manifesto.infMunCarrega):
            ide.append(self._serializar_municipio_carrega(item, retorna_string=False))

        # UFs Percurso
        for num, item in enumerate(manifesto.infPercurso):
            ide.append(self._serializar_percurso(item, retorna_string=False))

        if manifesto.dhIniViagem is not None:
            etree.SubElement(ide, "dhIniViagem").text = (
                manifesto.dhIniViagem.strftime("%Y-%m-%dT%H:%M:%S") + tz
            )
        # - fim ide

        # Emitente
        raiz.append(self._serializar_emitente(manifesto.emitente, retorna_string=False))

        # infModal rodo
        raiz.append(
            self._serializar_modal_rodoviario(manifesto.modal_rodoviario, retorna_string=False)
        )

        # infDoc infCTe ou infNFe
        raiz.append(self._serializar_documentos(manifesto.documentos, retorna_string=False))

        # seg
        if len(manifesto.seguradora) > 0:
            for num, item in enumerate(manifesto.seguradora):
                raiz.append(self._serializar_seguradora(item, retorna_string=False))

        # prodPred
        if len(manifesto.produto) > 0:
            raiz.append(self._serializar_produto(manifesto.produto[0], retorna_string=False))

        # totais
        raiz.append(self._serializar_totais(manifesto.totais, retorna_string=False))

        # lacres
        if len(manifesto.lacres) > 0:
            for num, item in enumerate(manifesto.lacres):
                raiz.append(self._serializar_lacres(item, retorna_string=False))

        # Informações adicionais
        if (
            manifesto.informacoes_adicionais_interesse_fisco
            or manifesto.informacoes_complementares_interesse_contribuinte
        ):
            info_ad = etree.SubElement(raiz, "infAdic")
            if manifesto.informacoes_adicionais_interesse_fisco:
                etree.SubElement(
                    info_ad, "infAdFisco"
                ).text = manifesto.informacoes_adicionais_interesse_fisco
            if manifesto.informacoes_complementares_interesse_contribuinte:
                etree.SubElement(
                    info_ad, "infCpl"
                ).text = manifesto.informacoes_complementares_interesse_contribuinte

        # Responsavel Tecnico NT2018/003
        if manifesto.responsavel_tecnico:
            raiz.append(
                self._serializar_responsavel_tecnico(
                    manifesto.responsavel_tecnico[0], retorna_string=False
                )
            )

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz
