#!/usr/bin/env python
# *-* encoding: utf8 *-*

import unittest

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import (
    NotaFiscal,
    NotaFiscalDeclaracaoImportacaoAdicao,
    NotaFiscalDeclaracaoImportacao
)
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.processamento.serializacao import SerializacaoXML
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.processamento.validacao import Validacao
from pynfe.utils.flags import (
    CODIGO_BRASIL,
    NAMESPACE_NFE,
    NAMESPACE_SIG,
    XSD_FOLDER_NFE,
    XSD_NFE,
    XSD_NFE_PROCESSADA,
)
from decimal import Decimal
import datetime


class SerializacaoNFeTestCase(unittest.TestCase):
    """
    Imprimir o XML completo:
        print(etree.tostring(self.xml_assinado))

    """

    def setUp(self):
        self.certificado = "./tests/certificado.pfx"
        self.senha = bytes('123456', 'utf-8')
        self.uf = 'pr'
        self.homologacao = True

        self.ns = {'ns': NAMESPACE_NFE}
        self.ns_sig = {'ns': NAMESPACE_SIG}

        self.validacao = Validacao()
        self.xsd_procNFe = self.validacao.get_xsd(
            xsd_file=XSD_NFE_PROCESSADA,
            xsd_folder=XSD_FOLDER_NFE
        )
        self.xsd_nfe = self.validacao.get_xsd(
            xsd_file=XSD_NFE,
            xsd_folder=XSD_FOLDER_NFE
        )

    def preenche_emitente(self):
        self.emitente = Emitente(
            razao_social='NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL',
            nome_fantasia='Nome Fantasia da Empresa',
            cnpj='99999999000199',  # cnpj apenas números
            codigo_de_regime_tributario='3',  # 1 para simples nacional ou 3 para normal
            inscricao_estadual='9999999999',  # numero de IE da empresa
            inscricao_municipal='12345',
            cnae_fiscal='9999999',  # cnae apenas números
            endereco_logradouro='Rua da Paz',
            endereco_numero='666',
            endereco_bairro='Sossego',
            endereco_municipio='Paranavaí',
            endereco_uf='PR',
            endereco_cep='87704000',
            endereco_pais=CODIGO_BRASIL
        )
        return self.emitente

    def preenche_destinatario(self):
        self.cliente = Cliente(
            razao_social='JOSE DA SILVA',
            tipo_documento='CPF',  # CPF ou CNPJ
            email='email@email.com',
            numero_documento='12345678900',  # numero do cpf ou cnpj
            indicador_ie=9,  # 9=Não contribuinte
            endereco_logradouro='Rua dos Bobos',
            endereco_numero='Zero',
            endereco_complemento='Ao lado de lugar nenhum',
            endereco_bairro='Aquele Mesmo',
            endereco_municipio='Brasilia',
            endereco_uf='DF',
            endereco_cep='12345123',
            endereco_pais=CODIGO_BRASIL,
            endereco_telefone='11912341234',
        )
        return self.cliente

    def preenche_notafiscal_produto_cst00(self):

        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf='PR',
            natureza_operacao='VENDA',  # venda, compra, transferência, devolução, etc
            forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
            modelo=55,  # 55=NF-e; 65=NFC-e
            serie='1',
            numero_nf='111',  # Número do Documento Fiscal.
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,  # 0=entrada; 1=saida
            municipio='4118402',  # Código IBGE do Município
            tipo_impressao_danfe=1,  # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;  # NOQA
            forma_emissao='1',  # 1=Emissão normal (não em contingência);
            cliente_final=1,  # 0=Normal;1=Consumidor final;
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao='1',  # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.  # NOQA
            processo_emissao='0',  # 0=Emissão de NF-e com aplicativo do contribuinte;
            transporte_modalidade_frete=1,
            informacoes_adicionais_interesse_fisco='Mensagem complementar',
            totais_tributos_aproximado=Decimal('21.06'),
        )

        # Adicionar informações da Declaração de Importação
        declaracao_importacao = []
        di_adicoes = []
        di_adicoes.append(
            NotaFiscalDeclaracaoImportacaoAdicao(
                numero='1',
                sequencia='1',
                codigo_fabricante='1',
                desconto=Decimal('0'),
                numero_drawback='12345678',
            )
        )

        declaracao_importacao.append(
            NotaFiscalDeclaracaoImportacao(
                numero_di_dsi_da='123456789',
                data_registro=data_emissao,
                desembaraco_aduaneiro_local='Santos',
                desembaraco_aduaneiro_uf='SP',
                desembaraco_aduaneiro_data=data_emissao,
                tipo_via_transporte=1,
                valor_afrmm=Decimal('0'),
                tipo_intermediacao=1,
                cnpj_adquirente='00111711999900',
                uf_terceiro='',
                codigo_exportador='1',
                adicoes=di_adicoes,
            )
        )

        self.notafiscal.adicionar_produto_servico(
            codigo='000328',  # id do produto
            descricao='Produto teste',
            ncm='99999999',
            # cest='0100100',  # NT2015/003
            ean='1234567890121',
            cfop='3102',
            unidade_comercial='UN',
            quantidade_comercial=Decimal('12'),  # 12 unidades
            valor_unitario_comercial=Decimal('9.75'),  # preço unitário
            valor_total_bruto=Decimal('117.00'),  # preço total
            unidade_tributavel='UN',
            quantidade_tributavel=Decimal('12'),
            valor_unitario_tributavel=Decimal('9.75'),
            ean_tributavel='SEM GTIN',
            ind_total=1,
            icms_modalidade='00',
            icms_origem=0,
            icms_csosn='',
            pis_modalidade='51',
            cofins_modalidade='51',
            pis_valor_base_calculo=Decimal('117.00'),
            pis_aliquota_percentual=Decimal('0.65'),
            pis_valor=Decimal('0.76'),
            cofins_valor_base_calculo=Decimal('117.00'),
            cofins_aliquota_percentual=Decimal('3.00'),
            cofins_valor=Decimal('3.51'),
            valor_tributos_aprox='21.06',
            numero_pedido='12345',
            numero_item='1',
            nfci='12345678-AAAA-FFFF-1234-000000000000',
            informacoes_adicionais='Informações adicionais',
            ipi_valor_ipi_dev=Decimal('10.00'),
            pdevol=Decimal('1.00'),
            # declaração de importação
            declaracoes_importacao=declaracao_importacao,
            # ipi
            ipi_classe_enquadramento='999',
            ipi_codigo_enquadramento='00',
            ipi_valor_base_calculo=Decimal('117.00'),
            ipi_aliquota=Decimal('10.00'),
            ipi_valor_ipi=Decimal('11.70'),
            # ii
            imposto_importacao_valor_base_calculo=Decimal('117.00'),
            imposto_importacao_valor_despesas_aduaneiras=Decimal('0.00'),
            imposto_importacao_valor=Decimal('0.00'),
            imposto_importacao_valor_iof=Decimal('1.11'),
        )
        
        self.notafiscal.adicionar_pagamento(
            t_pag="03",
            x_pag="Cartao Credito",
            v_pag=118.70,
            ind_pag=0,
            tp_integra="2",
            t_band="99",
        )

    def serializa_nfe(self):
        serializador = SerializacaoXML(_fonte_dados, homologacao=self.homologacao)
        return serializador.exportar()

    def assina_xml(self):
        a1 = AssinaturaA1(self.certificado, self.senha)
        return a1.assinar(self.xml)

    def validacao_com_xsd_do_xml_gerado_sem_processar(self):
        self.validacao.validar_etree(
            xml_doc=self.xml_assinado,
            xsd_file=self.xsd_nfe,
            use_assert=True
        )

    def total_e_produto_cst00_test(self):
        # Produto
        cProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cProd', namespaces=self.ns)[0].text
        cEAN = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEAN', namespaces=self.ns)[0].text
        xProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xProd', namespaces=self.ns)[0].text
        NCM = self.xml_assinado.xpath('//ns:det/ns:prod/ns:NCM', namespaces=self.ns)[0].text
        # CEST = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CEST', namespaces=self.ns)[0].text
        # indEscala = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indEscala', namespaces=self.ns)[0].text  # NOQA
        CEST = None
        indEscala = None
        CFOP = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CFOP', namespaces=self.ns)[0].text
        uCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uCom', namespaces=self.ns)[0].text
        qCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qCom', namespaces=self.ns)[0].text
        vUnCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnCom', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vProd', namespaces=self.ns)[0].text
        cEANTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEANTrib', namespaces=self.ns)[0].text  # NOQA
        uTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uTrib', namespaces=self.ns)[0].text
        qTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qTrib', namespaces=self.ns)[0].text
        vUnTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnTrib', namespaces=self.ns)[0].text
        indTot = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indTot', namespaces=self.ns)[0].text
        xPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xPed', namespaces=self.ns)[0].text
        nItemPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nItemPed', namespaces=self.ns)[0].text  # NOQA
        nFCI = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nFCI', namespaces=self.ns)[0].text

        self.assertEqual(cProd, '000328')
        self.assertEqual(cEAN, '1234567890121')
        self.assertEqual(xProd, 'Produto teste')
        self.assertEqual(NCM, '99999999')
        self.assertEqual(CEST, None)
        self.assertEqual(indEscala, None)
        self.assertEqual(CFOP, '3102')
        self.assertEqual(uCom, 'UN')
        self.assertEqual(qCom, '12')
        self.assertEqual(vUnCom, '9.7500000000')
        self.assertEqual(vProd, '117.00')
        self.assertEqual(cEANTrib, 'SEM GTIN')
        self.assertEqual(uTrib, 'UN')
        self.assertEqual(qTrib, '12')
        self.assertEqual(vUnTrib, '9.7500000000')
        self.assertEqual(indTot, '1')
        self.assertEqual(xPed, '12345')
        self.assertEqual(nItemPed, '1')
        self.assertEqual(nFCI, '12345678-AAAA-FFFF-1234-000000000000')

        # Impostos
        # ICMS
        orig = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:orig', namespaces=self.ns)[0].text  # NOQA
        CST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:CST', namespaces=self.ns)[0].text  # NOQA
        modBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:modBC', namespaces=self.ns)[0].text  # NOQA
        vBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:vBC', namespaces=self.ns)[0].text  # NOQA
        pICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:pICMS', namespaces=self.ns)[0].text  # NOQA
        vICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:vICMS', namespaces=self.ns)[0].text  # NOQA
        # pFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:pFCP', namespaces=self.ns)[0].text  # NOQA
        # vFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:vFCP', namespaces=self.ns)[0].text  # NOQA
        pFCP = None
        vFCP = None

        self.assertEqual(orig, '0')
        self.assertEqual(CST, '00')
        self.assertEqual(modBC, '0')
        self.assertEqual(vBC, '0')
        self.assertEqual(pICMS, '0.00')
        self.assertEqual(vICMS, '0.00')
        # self.assertEqual(pFCP, '0.00')
        # self.assertEqual(vFCP, '0.00')
        self.assertEqual(pFCP, None)
        self.assertEqual(vFCP, None)

        # PIS
        CST_PIS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:PIS/ns:PISOutr/ns:CST', namespaces=self.ns)[0].text  # NOQA
        self.assertEqual(CST_PIS, '51')

        # # COFINS
        CST_COFINS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:COFINS/ns:COFINSOutr/ns:CST', namespaces=self.ns)[0].text  # NOQA
        self.assertEqual(CST_COFINS, '51')

        # Impostos - IPI Devolução
        pDevol = self.xml_assinado.xpath('//ns:det/ns:impostoDevol/ns:pDevol', namespaces=self.ns)[0].text  # NOQA
        vIPIDevol = self.xml_assinado.xpath('//ns:det/ns:impostoDevol/ns:IPI/ns:vIPIDevol', namespaces=self.ns)[0].text  # NOQA
        self.assertEqual(pDevol, '1.00')
        self.assertEqual(vIPIDevol, '10.00')

        # IPI
        ipi_codigo_enquadramento = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:IPI/ns:IPITrib/ns:CST', namespaces=self.ns)[0].text  # NOQA
        ipi_valor_base_calculo = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:IPI/ns:IPITrib/ns:vBC', namespaces=self.ns)[0].text  # NOQA
        ipi_aliquota = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:IPI/ns:IPITrib/ns:pIPI', namespaces=self.ns)[0].text  # NOQA
        ipi_valor = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:IPI/ns:IPITrib/ns:vIPI', namespaces=self.ns)[0].text  # NOQA
        self.assertEqual(ipi_codigo_enquadramento, '00')
        self.assertEqual(ipi_valor_base_calculo, '117.00')
        self.assertEqual(ipi_aliquota, '10.00')
        self.assertEqual(ipi_valor, '11.70')

        # ii
        imposto_importacao_valor_base_calculo = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:II/ns:vBC', namespaces=self.ns)[0].text  # NOQA
        imposto_importacao_valor_despesas_aduaneiras = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:II/ns:vDespAdu', namespaces=self.ns)[0].text  # NOQA
        imposto_importacao_valor = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:II/ns:vII', namespaces=self.ns)[0].text  # NOQA
        imposto_importacao_valor_iof = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:II/ns:vIOF', namespaces=self.ns)[0].text  # NOQA
        self.assertEqual(imposto_importacao_valor_base_calculo, '117.00')
        self.assertEqual(imposto_importacao_valor_despesas_aduaneiras, '0.00')
        self.assertEqual(imposto_importacao_valor, '0.00')
        self.assertEqual(imposto_importacao_valor_iof, '1.11')

        # Declaração de Importação
        numero_di_dsi_da = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:nDI', namespaces=self.ns)[0].text  # NOQA
        data_registro = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:dDI', namespaces=self.ns)[0].text  # NOQA
        desembaraco_aduaneiro_local = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:xLocDesemb', namespaces=self.ns)[0].text  # NOQA
        desembaraco_aduaneiro_uf = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:UFDesemb', namespaces=self.ns)[0].text  # NOQA
        desembaraco_aduaneiro_data = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:dDesemb', namespaces=self.ns)[0].text  # NOQA
        tipo_via_transporte = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:tpViaTransp', namespaces=self.ns)[0].text  # NOQA
        # valor_afrmm = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:vAFRMM', namespaces=self.ns)[0].text  # NOQA
        tipo_intermediacao = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:tpIntermedio', namespaces=self.ns)[0].text  # NOQA
        cnpj_adquirente = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:CNPJ', namespaces=self.ns)[0].text  # NOQA
        # uf_terceiro = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:UFTerceiro', namespaces=self.ns)[0].text  # NOQA
        codigo_exportador = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:cExportador', namespaces=self.ns)[0].text  # NOQA

        adicao_numero = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:adi/ns:nAdicao', namespaces=self.ns)[0].text  # NOQA
        adicao_sequencia = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:adi/ns:nSeqAdic', namespaces=self.ns)[0].text  # NOQA
        adicao_codigo_fabricante = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:adi/ns:cFabricante', namespaces=self.ns)[0].text  # NOQA
        # adicao_desconto = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:adi/ns:vDescDI', namespaces=self.ns)[0].text  # NOQA
        adicao_numero_drawback = self.xml_assinado.xpath('//ns:det/ns:prod/ns:DI/ns:adi/ns:nDraw', namespaces=self.ns)[0].text  # NOQA

        self.assertEqual(numero_di_dsi_da, '123456789')
        self.assertEqual(data_registro, '2021-01-14')
        self.assertEqual(desembaraco_aduaneiro_local, 'Santos')
        self.assertEqual(desembaraco_aduaneiro_uf, 'SP')
        self.assertEqual(desembaraco_aduaneiro_data, '2021-01-14')
        self.assertEqual(tipo_via_transporte, '1')
        # self.assertEqual(valor_afrmm, Decimal('0'))
        self.assertEqual(tipo_intermediacao, '1')
        self.assertEqual(cnpj_adquirente, '00111711999900')
        # self.assertEqual(uf_terceiro, '')
        self.assertEqual(codigo_exportador, '1')

        self.assertEqual(adicao_numero, '1')
        self.assertEqual(adicao_sequencia, '1')
        self.assertEqual(adicao_codigo_fabricante, '1')
        # self.assertEqual(adicao_desconto, '0')
        self.assertEqual(adicao_numero_drawback, '12345678')

        # Informações Adicionais do produto
        infAdProd = self.xml_assinado.xpath('//ns:det/ns:infAdProd', namespaces=self.ns)[0].text
        self.assertEqual(infAdProd, 'Informacoes adicionais')

        # Totalizadores
        vBC = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBC', namespaces=self.ns)[0].text  # NOQA
        vICMS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMS', namespaces=self.ns)[0].text  # NOQA
        vICMSDeson = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMSDeson', namespaces=self.ns)[0].text  # NOQA
        vFCP = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCP', namespaces=self.ns)[0].text  # NOQA
        vBCST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBCST', namespaces=self.ns)[0].text  # NOQA
        vST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vST', namespaces=self.ns)[0].text  # NOQA
        vFCPST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPST', namespaces=self.ns)[0].text  # NOQA
        vFCPSTRet = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPSTRet', namespaces=self.ns)[0].text  # NOQA
        vProd = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vProd', namespaces=self.ns)[0].text  # NOQA
        vFrete = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFrete', namespaces=self.ns)[0].text  # NOQA
        vSeg = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vSeg', namespaces=self.ns)[0].text  # NOQA
        vDesc = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vDesc', namespaces=self.ns)[0].text  # NOQA
        vII = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vII', namespaces=self.ns)[0].text  # NOQA
        vIPI = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPI', namespaces=self.ns)[0].text  # NOQA
        vIPIDevol = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPIDevol', namespaces=self.ns)[0].text  # NOQA
        vPIS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vPIS', namespaces=self.ns)[0].text  # NOQA
        vCOFINS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vCOFINS', namespaces=self.ns)[0].text  # NOQA
        vOutro = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vOutro', namespaces=self.ns)[0].text  # NOQA
        vNF = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vNF', namespaces=self.ns)[0].text  # NOQA
        vTotTrib = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vTotTrib', namespaces=self.ns)[0].text  # NOQA

        self.assertEqual(vBC, '0.00')
        self.assertEqual(vICMS, '0.00')
        self.assertEqual(vICMSDeson, '0.00')
        self.assertEqual(vFCP, '0.00')
        self.assertEqual(vBCST, '0.00')
        self.assertEqual(vST, '0.00')
        self.assertEqual(vFCPST, '0.00')
        self.assertEqual(vFCPSTRet, '0.00')
        self.assertEqual(vProd, '117.00')
        self.assertEqual(vFrete, '0.00')
        self.assertEqual(vSeg, '0.00')
        self.assertEqual(vDesc, '0.00')
        self.assertEqual(vII, '0.00')
        self.assertEqual(vIPI, '11.70')
        self.assertEqual(vIPIDevol, '10.00')
        self.assertEqual(vPIS, '0.76')
        self.assertEqual(vCOFINS, '3.51')
        self.assertEqual(vOutro, '0.00')
        self.assertEqual(vNF, '138.70')
        self.assertEqual(vTotTrib, '21.06')

    def test_notafiscal_produto_cst00(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_cst00()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.total_e_produto_cst00_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()


if __name__ == '__main__':
    unittest.main()
