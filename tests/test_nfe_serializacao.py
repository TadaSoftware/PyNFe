#!/usr/bin/env python
# *-* encoding: utf8 *-*

import unittest

from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscal
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
            codigo_de_regime_tributario='1',  # 1 para simples nacional ou 3 para normal
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
            tipo_pagamento=1,
            modelo=55,  # 55=NF-e; 65=NFC-e
            serie='1',
            numero_nf='111',  # Número do Documento Fiscal.
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,  # 0=entrada; 1=saida
            municipio='4118402',  # Código IBGE do Município
            tipo_impressao_danfe=1,  # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
            forma_emissao='1',  # 1=Emissão normal (não em contingência);
            cliente_final=1,  # 0=Normal;1=Consumidor final;
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao='1',  # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
            processo_emissao='0',  # 0=Emissão de NF-e com aplicativo do contribuinte;
            transporte_modalidade_frete=1,
            informacoes_adicionais_interesse_fisco='Mensagem complementar',
            totais_tributos_aproximado=Decimal('21.06'),
        )

        self.notafiscal.adicionar_produto_servico(
            codigo='000328',  # id do produto
            descricao='Produto teste',
            ncm='99999999',
            # cest='0100100',  # NT2015/003
            ean='1234567890121',
            cfop='5102',
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
            icms_csosn='400',
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
        )
        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900001'
        )
        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900002'
        )

        self.notafiscal.adicionar_responsavel_tecnico(
            cnpj='99999999000199',
            contato='Teste PyNFe',
            email='pynfe@pynfe.io',
            fone='11912341234'
        )

    def preenche_notafiscal_produto_cst40(self):

        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf='PR',
            natureza_operacao='VENDA',  # venda, compra, transferência, devolução, etc
            forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
            tipo_pagamento=1,
            modelo=55,  # 55=NF-e; 65=NFC-e
            serie='1',
            numero_nf='111',  # Número do Documento Fiscal.
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,  # 0=entrada; 1=saida
            municipio='4118402',  # Código IBGE do Município
            tipo_impressao_danfe=1,  # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
            forma_emissao='1',  # 1=Emissão normal (não em contingência);
            cliente_final=1,  # 0=Normal;1=Consumidor final;
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao='1',  # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
            processo_emissao='0',  # 0=Emissão de NF-e com aplicativo do contribuinte;
            transporte_modalidade_frete=1,
            informacoes_adicionais_interesse_fisco='Mensagem complementar',
            totais_tributos_aproximado=Decimal('21.06'),
        )

        self.notafiscal.adicionar_produto_servico(
            codigo='000328',  # id do produto
            descricao='Produto teste',
            ncm='99999999',
            # cest='0100100',  # NT2015/003
            ean='1234567890121',
            cfop='5102',
            unidade_comercial='UN',
            quantidade_comercial=Decimal('12'),  # 12 unidades
            valor_unitario_comercial=Decimal('9.75'),  # preço unitário
            valor_total_bruto=Decimal('117.00'),  # preço total
            unidade_tributavel='UN',
            quantidade_tributavel=Decimal('12'),
            valor_unitario_tributavel=Decimal('9.75'),
            ean_tributavel='SEM GTIN',
            ind_total=1,
            icms_modalidade='40',
            icms_origem=0,
            icms_csosn='400',
            pis_modalidade='07',
            cofins_modalidade='07',
            valor_tributos_aprox='21.06',
            numero_pedido='12345',
            numero_item='1',
            nfci='12345678-AAAA-FFFF-1234-000000000000',
            informacoes_adicionais='Informações adicionais',
            icms_desonerado=Decimal('10.00'),
            icms_motivo_desoneracao='90'
        )

        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900001'
        )
        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900002'
        )

        self.notafiscal.adicionar_responsavel_tecnico(
            cnpj='99999999000199',
            contato='Teste PyNFe',
            email='pynfe@pynfe.io',
            fone='11912341234'
        )

    def preenche_notafiscal_produto_cst41(self):

        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf='PR',
            natureza_operacao='VENDA',  # venda, compra, transferência, devolução, etc
            forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
            tipo_pagamento=1,
            modelo=55,  # 55=NF-e; 65=NFC-e
            serie='1',
            numero_nf='111',  # Número do Documento Fiscal.
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,  # 0=entrada; 1=saida
            municipio='4118402',  # Código IBGE do Município
            tipo_impressao_danfe=1,  # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
            forma_emissao='1',  # 1=Emissão normal (não em contingência);
            cliente_final=1,  # 0=Normal;1=Consumidor final;
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao='1',  # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
            processo_emissao='0',  # 0=Emissão de NF-e com aplicativo do contribuinte;
            transporte_modalidade_frete=1,
            informacoes_adicionais_interesse_fisco='Mensagem complementar',
            totais_tributos_aproximado=Decimal('21.06'),
        )

        self.notafiscal.adicionar_produto_servico(
            codigo='000328',  # id do produto
            descricao='Produto teste',
            ncm='99999999',
            # cest='0100100',  # NT2015/003
            ean='1234567890121',
            cfop='5102',
            unidade_comercial='UN',
            quantidade_comercial=Decimal('12'),  # 12 unidades
            valor_unitario_comercial=Decimal('9.75'),  # preço unitário
            valor_total_bruto=Decimal('117.00'),  # preço total
            unidade_tributavel='UN',
            quantidade_tributavel=Decimal('12'),
            valor_unitario_tributavel=Decimal('9.75'),
            ean_tributavel='SEM GTIN',
            ind_total=1,
            icms_modalidade='41',
            icms_origem=0,
            icms_csosn='400',
            pis_modalidade='07',
            cofins_modalidade='07',
            valor_tributos_aprox='21.06',
            numero_pedido='12345',
            numero_item='1',
            nfci='12345678-AAAA-FFFF-1234-000000000000',
            informacoes_adicionais='Informações adicionais',
            icms_desonerado=Decimal('10.00'),
            icms_motivo_desoneracao='90'
        )

        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900001'
        )
        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900002'
        )

        self.notafiscal.adicionar_responsavel_tecnico(
            cnpj='99999999000199',
            contato='Teste PyNFe',
            email='pynfe@pynfe.io',
            fone='11912341234'
        )

    def preenche_notafiscal_produto_cst50(self):

        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf='PR',
            natureza_operacao='VENDA',  # venda, compra, transferência, devolução, etc
            forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
            tipo_pagamento=1,
            modelo=55,  # 55=NF-e; 65=NFC-e
            serie='1',
            numero_nf='111',  # Número do Documento Fiscal.
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,  # 0=entrada; 1=saida
            municipio='4118402',  # Código IBGE do Município
            tipo_impressao_danfe=1,  # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
            forma_emissao='1',  # 1=Emissão normal (não em contingência);
            cliente_final=1,  # 0=Normal;1=Consumidor final;
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao='1',  # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
            processo_emissao='0',  # 0=Emissão de NF-e com aplicativo do contribuinte;
            transporte_modalidade_frete=1,
            informacoes_adicionais_interesse_fisco='Mensagem complementar',
            totais_tributos_aproximado=Decimal('21.06'),
        )

        self.notafiscal.adicionar_produto_servico(
            codigo='000328',  # id do produto
            descricao='Produto teste',
            ncm='99999999',
            # cest='0100100',  # NT2015/003
            ean='1234567890121',
            cfop='5102',
            unidade_comercial='UN',
            quantidade_comercial=Decimal('12'),  # 12 unidades
            valor_unitario_comercial=Decimal('9.75'),  # preço unitário
            valor_total_bruto=Decimal('117.00'),  # preço total
            unidade_tributavel='UN',
            quantidade_tributavel=Decimal('12'),
            valor_unitario_tributavel=Decimal('9.75'),
            ean_tributavel='SEM GTIN',
            ind_total=1,
            icms_modalidade='50',
            icms_origem=0,
            icms_csosn='400',
            pis_modalidade='07',
            cofins_modalidade='07',
            valor_tributos_aprox='21.06',
            numero_pedido='12345',
            numero_item='1',
            nfci='12345678-AAAA-FFFF-1234-000000000000',
            informacoes_adicionais='Informações adicionais',
            icms_desonerado=Decimal('10.00'),
            icms_motivo_desoneracao='90'
        )

        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900001'
        )
        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900002'
        )

        self.notafiscal.adicionar_responsavel_tecnico(
            cnpj='99999999000199',
            contato='Teste PyNFe',
            email='pynfe@pynfe.io',
            fone='11912341234'
        )

    def preenche_notafiscal_produto_cst51(self):

        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf='PR',
            natureza_operacao='VENDA',  # venda, compra, transferência, devolução, etc
            forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
            tipo_pagamento=1,
            modelo=55,  # 55=NF-e; 65=NFC-e
            serie='1',
            numero_nf='111',  # Número do Documento Fiscal.
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,  # 0=entrada; 1=saida
            municipio='4118402',  # Código IBGE do Município
            tipo_impressao_danfe=1,  # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
            forma_emissao='1',  # 1=Emissão normal (não em contingência);
            cliente_final=1,  # 0=Normal;1=Consumidor final;
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao='1',  # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
            processo_emissao='0',  # 0=Emissão de NF-e com aplicativo do contribuinte;
            transporte_modalidade_frete=1,
            informacoes_adicionais_interesse_fisco='Mensagem complementar',
            totais_tributos_aproximado=Decimal('21.06'),
        )

        self.notafiscal.adicionar_produto_servico(
            codigo='000328',  # id do produto
            descricao='Produto teste',
            ncm='99999999',
            # cest='0100100',  # NT2015/003
            ean='1234567890121',
            cfop='5102',
            unidade_comercial='UN',
            quantidade_comercial=Decimal('12'),  # 12 unidades
            valor_unitario_comercial=Decimal('9.75'),  # preço unitário
            valor_total_bruto=Decimal('117.00'),  # preço total
            unidade_tributavel='UN',
            quantidade_tributavel=Decimal('12'),
            valor_unitario_tributavel=Decimal('9.75'),
            ean_tributavel='SEM GTIN',
            ind_total=1,
            icms_modalidade='51',
            icms_origem=0,
            icms_csosn='400',
            pis_modalidade='07',
            cofins_modalidade='07',
            valor_tributos_aprox='21.06',
            numero_pedido='12345',
            numero_item='1',
            nfci='12345678-AAAA-FFFF-1234-000000000000',
            informacoes_adicionais='Informações adicionais',
        )

        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900001'
        )
        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900002'
        )

        self.notafiscal.adicionar_responsavel_tecnico(
            cnpj='99999999000199',
            contato='Teste PyNFe',
            email='pynfe@pynfe.io',
            fone='11912341234'
        )

    def preenche_notafiscal_produto_cst60(self):

        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf='PR',
            natureza_operacao='VENDA',  # venda, compra, transferência, devolução, etc
            forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
            tipo_pagamento=1,
            modelo=55,  # 55=NF-e; 65=NFC-e
            serie='1',
            numero_nf='111',  # Número do Documento Fiscal.
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,  # 0=entrada; 1=saida
            municipio='4118402',  # Código IBGE do Município
            tipo_impressao_danfe=1,  # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
            forma_emissao='1',  # 1=Emissão normal (não em contingência);
            cliente_final=1,  # 0=Normal;1=Consumidor final;
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao='1',  # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
            processo_emissao='0',  # 0=Emissão de NF-e com aplicativo do contribuinte;
            transporte_modalidade_frete=1,
            informacoes_adicionais_interesse_fisco='Mensagem complementar',
            totais_tributos_aproximado=Decimal('21.06'),
        )

        self.notafiscal.adicionar_produto_servico(
            codigo='000328',  # id do produto
            descricao='Produto teste',
            ncm='99999999',
            # cest='0100100',  # NT2015/003
            ean='1234567890121',
            cfop='5102',
            unidade_comercial='UN',
            quantidade_comercial=Decimal('12'),  # 12 unidades
            valor_unitario_comercial=Decimal('9.75'),  # preço unitário
            valor_total_bruto=Decimal('117.00'),  # preço total
            unidade_tributavel='UN',
            quantidade_tributavel=Decimal('12'),
            valor_unitario_tributavel=Decimal('9.75'),
            ean_tributavel='SEM GTIN',
            ind_total=1,
            icms_modalidade='60',
            icms_origem=0,
            icms_csosn='400',
            pis_modalidade='07',
            cofins_modalidade='07',
            valor_tributos_aprox='21.06',
            numero_pedido='12345',
            numero_item='1',
            nfci='12345678-AAAA-FFFF-1234-000000000000',
            informacoes_adicionais='Informações adicionais',
        )

        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900001'
        )
        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900002'
        )

        self.notafiscal.adicionar_responsavel_tecnico(
            cnpj='99999999000199',
            contato='Teste PyNFe',
            email='pynfe@pynfe.io',
            fone='11912341234'
        )

    def preenche_notafiscal_produto_cst70(self):

        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf='PR',
            natureza_operacao='VENDA',  # venda, compra, transferência, devolução, etc
            forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
            tipo_pagamento=1,
            modelo=55,  # 55=NF-e; 65=NFC-e
            serie='1',
            numero_nf='111',  # Número do Documento Fiscal.
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,  # 0=entrada; 1=saida
            municipio='4118402',  # Código IBGE do Município
            tipo_impressao_danfe=1,  # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
            forma_emissao='1',  # 1=Emissão normal (não em contingência);
            cliente_final=1,  # 0=Normal;1=Consumidor final;
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao='1',  # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
            processo_emissao='0',  # 0=Emissão de NF-e com aplicativo do contribuinte;
            transporte_modalidade_frete=1,
            informacoes_adicionais_interesse_fisco='Mensagem complementar',
            totais_tributos_aproximado=Decimal('21.06'),
        )

        self.notafiscal.adicionar_produto_servico(
            codigo='000328',  # id do produto
            descricao='Produto teste',
            ncm='99999999',
            # cest='0100100',  # NT2015/003
            ean='1234567890121',
            cfop='5102',
            unidade_comercial='UN',
            quantidade_comercial=Decimal('12'),  # 12 unidades
            valor_unitario_comercial=Decimal('9.75'),  # preço unitário
            valor_total_bruto=Decimal('117.00'),  # preço total
            unidade_tributavel='UN',
            quantidade_tributavel=Decimal('12'),
            valor_unitario_tributavel=Decimal('9.75'),
            ean_tributavel='SEM GTIN',
            ind_total=1,
            icms_modalidade='70',
            icms_origem=0,
            icms_csosn='400',
            pis_modalidade='07',
            cofins_modalidade='07',
            valor_tributos_aprox='21.06',
            numero_pedido='12345',
            numero_item='1',
            nfci='12345678-AAAA-FFFF-1234-000000000000',
            informacoes_adicionais='Informações adicionais',
            icms_modalidade_determinacao_bc=0,
            icms_valor_base_calculo=Decimal('18.67'),
            icms_percentual_reducao_bc=Decimal('10.00'),
            icms_aliquota=Decimal('18.00'),
            icms_valor=Decimal('3.36'),
            fcp_base_calculo=Decimal('3.36'),
            fcp_percentual=Decimal('2.00'),
            fcp_valor=Decimal('0.06'),
            icms_st_modalidade_determinacao_bc=4,
            icms_st_percentual_adicional=Decimal('0.00'),
            icms_st_percentual_reducao_bc=Decimal('10.00'),
            icms_st_valor_base_calculo=Decimal('26.68'),
            icms_st_aliquota=Decimal('18.00'),
            icms_st_valor=Decimal('1.44'),
            fcp_st_base_calculo=Decimal('1.44'),
            fcp_st_percentual=Decimal('2.00'),
            fcp_st_valor=Decimal('0.02'),
        )

        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900001'
        )
        self.notafiscal.adicionar_nota_fiscal_referenciada(
            chave_acesso='12345678901234567890123456789012345678900002'
        )

        self.notafiscal.adicionar_responsavel_tecnico(
            cnpj='99999999000199',
            contato='Teste PyNFe',
            email='pynfe@pynfe.io',
            fone='11912341234'
        )

    def preenche_notafiscal_produto_cst90(self):

        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_saida_entrada = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        self.notafiscal = NotaFiscal(
            emitente=self.emitente,
            cliente=self.cliente,
            uf='PR',
            natureza_operacao='VENDA',  # venda, compra, transferência, devolução, etc
            forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
            tipo_pagamento=1,
            modelo=55,  # 55=NF-e; 65=NFC-e
            serie='1',
            numero_nf='111',  # Número do Documento Fiscal.
            data_emissao=data_emissao,
            data_saida_entrada=data_saida_entrada,
            tipo_documento=1,  # 0=entrada; 1=saida
            municipio='4118402',  # Código IBGE do Município
            tipo_impressao_danfe=1,  # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
            forma_emissao='1',  # 1=Emissão normal (não em contingência);
            cliente_final=1,  # 0=Normal;1=Consumidor final;
            indicador_destino=1,
            indicador_presencial=1,
            finalidade_emissao='1',  # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
            processo_emissao='0',  # 0=Emissão de NF-e com aplicativo do contribuinte;
            transporte_modalidade_frete=1,
            informacoes_adicionais_interesse_fisco='Mensagem complementar',
            totais_tributos_aproximado=Decimal('21.06'),
        )

        self.notafiscal.adicionar_produto_servico(
            codigo='000328',  # id do produto
            descricao='Produto teste',
            ncm='99999999',
            # cest='0100100',  # NT2015/003
            ean='1234567890121',
            cfop='5102',
            unidade_comercial='UN',
            quantidade_comercial=Decimal('12'),  # 12 unidades
            valor_unitario_comercial=Decimal('9.75'),  # preço unitário
            valor_total_bruto=Decimal('117.00'),  # preço total
            unidade_tributavel='UN',
            quantidade_tributavel=Decimal('12'),
            valor_unitario_tributavel=Decimal('9.75'),
            ean_tributavel='SEM GTIN',
            ind_total=1,
            icms_modalidade='90',
            icms_origem=0,
            icms_csosn='400',
            pis_modalidade='07',
            cofins_modalidade='07',
            valor_tributos_aprox='21.06',
            numero_pedido='12345',
            numero_item='1',
            nfci='12345678-AAAA-FFFF-1234-000000000000',
            informacoes_adicionais='Informações adicionais',
            icms_modalidade_determinacao_bc=0,
            icms_valor_base_calculo=Decimal('117.00'),
            icms_percentual_reducao_bc=Decimal('0.00'),
            icms_aliquota=Decimal('10.00'),
            icms_valor=Decimal('11.70'),
        )

        self.notafiscal.adicionar_nota_fiscal_referenciada(
            tipo='Nota Fiscal produtor',
            chave_acesso='',
            uf='51',
            mes_ano_emissao='2205',
            cnpj='99999999000199',
            ie='132001280',
            modelo='04',
            serie='1',
            numero='999999998'
        )

        self.notafiscal.adicionar_nota_fiscal_referenciada(
            tipo='Nota Fiscal produtor',
            chave_acesso='',
            uf='51',
            mes_ano_emissao='2205',
            cnpj='99999999000199',
            ie='132001280',
            modelo='04',
            serie='1',
            numero='999999999'
        )

        self.notafiscal.adicionar_responsavel_tecnico(
            cnpj='99999999000199',
            contato='Teste PyNFe',
            email='pynfe@pynfe.io',
            fone='11912341234'
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

    def grupo_ide_test(self):
        uf = self.xml_assinado.xpath('//ns:ide/ns:cUF', namespaces=self.ns)[0].text
        natureza_operacao = self.xml_assinado.xpath('//ns:ide/ns:natOp', namespaces=self.ns)[0].text
        modelo = self.xml_assinado.xpath('//ns:ide/ns:mod', namespaces=self.ns)[0].text
        serie = self.xml_assinado.xpath('//ns:ide/ns:serie', namespaces=self.ns)[0].text
        numero_nf = self.xml_assinado.xpath('//ns:ide/ns:nNF', namespaces=self.ns)[0].text
        data_emissao = self.xml_assinado.xpath('//ns:ide/ns:dhEmi', namespaces=self.ns)[0].text
        data_saida_entrada = self.xml_assinado.xpath('//ns:ide/ns:dhSaiEnt', namespaces=self.ns)[0].text
        tipo_documento = self.xml_assinado.xpath('//ns:ide/ns:tpNF', namespaces=self.ns)[0].text
        indicador_destino = self.xml_assinado.xpath('//ns:ide/ns:idDest', namespaces=self.ns)[0].text
        municipio = self.xml_assinado.xpath('//ns:ide/ns:cMunFG', namespaces=self.ns)[0].text
        tipo_impressao_danfe = self.xml_assinado.xpath('//ns:ide/ns:tpImp', namespaces=self.ns)[0].text
        forma_emissao = self.xml_assinado.xpath('//ns:ide/ns:tpEmis', namespaces=self.ns)[0].text
        tipo_ambiente = self.xml_assinado.xpath('//ns:ide/ns:tpAmb', namespaces=self.ns)[0].text
        finalidade_emissao = self.xml_assinado.xpath('//ns:ide/ns:finNFe', namespaces=self.ns)[0].text
        cliente_final = self.xml_assinado.xpath('//ns:ide/ns:indFinal', namespaces=self.ns)[0].text
        indicador_presencial = self.xml_assinado.xpath('//ns:ide/ns:indPres', namespaces=self.ns)[0].text
        processo_emissao = self.xml_assinado.xpath('//ns:ide/ns:procEmi', namespaces=self.ns)[0].text

        self.assertEqual(uf, '41')
        self.assertEqual(natureza_operacao, 'VENDA')
        self.assertEqual(modelo, '55')
        self.assertEqual(serie, '1')
        self.assertEqual(numero_nf, '111')
        self.assertEqual(data_emissao, '2021-01-14T12:00:00+00:00')
        self.assertEqual(data_saida_entrada, '2021-01-14T13:10:20+00:00')
        self.assertEqual(tipo_documento, '1')
        self.assertEqual(indicador_destino, '1')
        self.assertEqual(municipio, '4118402')
        self.assertEqual(tipo_impressao_danfe, '1')
        self.assertEqual(forma_emissao, '1')
        self.assertEqual(tipo_ambiente, '2')
        self.assertEqual(finalidade_emissao, '1')
        self.assertEqual(cliente_final, '1')
        self.assertEqual(indicador_presencial, '1')
        self.assertEqual(processo_emissao, '0')

    def dados_emitente_test(self):
        razao_social = self.xml_assinado.xpath('//ns:emit/ns:xNome', namespaces=self.ns)[0].text
        nome_fantasia = self.xml_assinado.xpath('//ns:emit/ns:xFant', namespaces=self.ns)[0].text
        cnpj = self.xml_assinado.xpath('//ns:emit/ns:CNPJ', namespaces=self.ns)[0].text
        codigo_de_regime_tributario = self.xml_assinado.xpath('//ns:emit/ns:CRT', namespaces=self.ns)[0].text
        inscricao_estadual = self.xml_assinado.xpath('//ns:emit/ns:IE', namespaces=self.ns)[0].text
        inscricao_municipal = self.xml_assinado.xpath('//ns:emit/ns:IM', namespaces=self.ns)[0].text
        cnae_fiscal = self.xml_assinado.xpath('//ns:emit/ns:CNAE', namespaces=self.ns)[0].text
        endereco_logradouro = self.xml_assinado.xpath('//ns:emit/ns:enderEmit/ns:xLgr', namespaces=self.ns)[0].text
        endereco_numero = self.xml_assinado.xpath('//ns:emit/ns:enderEmit/ns:nro', namespaces=self.ns)[0].text
        endereco_bairro = self.xml_assinado.xpath('//ns:emit/ns:enderEmit/ns:xBairro', namespaces=self.ns)[0].text
        endereco_municipio = self.xml_assinado.xpath('//ns:emit/ns:enderEmit/ns:xMun', namespaces=self.ns)[0].text
        endereco_uf = self.xml_assinado.xpath('//ns:emit/ns:enderEmit/ns:UF', namespaces=self.ns)[0].text
        endereco_cep = self.xml_assinado.xpath('//ns:emit/ns:enderEmit/ns:CEP', namespaces=self.ns)[0].text
        endereco_pais = self.xml_assinado.xpath('//ns:emit/ns:enderEmit/ns:xPais', namespaces=self.ns)[0].text

        self.assertEqual(razao_social, 'NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL')
        self.assertEqual(nome_fantasia, 'Nome Fantasia da Empresa')
        self.assertEqual(cnpj, '99999999000199')
        self.assertEqual(codigo_de_regime_tributario, '1')
        self.assertEqual(inscricao_estadual, '9999999999')
        self.assertEqual(inscricao_municipal, '12345')
        self.assertEqual(cnae_fiscal, '9999999')
        self.assertEqual(endereco_logradouro, 'Rua da Paz')
        self.assertEqual(endereco_numero, '666')
        self.assertEqual(endereco_bairro, 'Sossego')
        self.assertEqual(endereco_municipio, 'Paranavai')
        self.assertEqual(endereco_uf, 'PR')
        self.assertEqual(endereco_cep, '87704000')
        self.assertEqual(endereco_pais, 'Brasil')

    def dados_destinatario_test(self):
        razao_social = self.xml_assinado.xpath('//ns:dest/ns:xNome', namespaces=self.ns)[0].text
        email = self.xml_assinado.xpath('//ns:dest/ns:email', namespaces=self.ns)[0].text
        numero_documento = self.xml_assinado.xpath('//ns:dest/ns:CPF', namespaces=self.ns)[0].text
        indicador_ie = self.xml_assinado.xpath('//ns:dest/ns:indIEDest', namespaces=self.ns)[0].text
        endereco_logradouro = self.xml_assinado.xpath('//ns:dest/ns:enderDest/ns:xLgr', namespaces=self.ns)[0].text
        endereco_numero = self.xml_assinado.xpath('//ns:dest/ns:enderDest/ns:nro', namespaces=self.ns)[0].text
        endereco_complemento = self.xml_assinado.xpath('//ns:dest/ns:enderDest/ns:xCpl', namespaces=self.ns)[0].text
        endereco_bairro = self.xml_assinado.xpath('//ns:dest/ns:enderDest/ns:xBairro', namespaces=self.ns)[0].text
        endereco_municipio = self.xml_assinado.xpath('//ns:dest/ns:enderDest/ns:xMun', namespaces=self.ns)[0].text
        endereco_uf = self.xml_assinado.xpath('//ns:dest/ns:enderDest/ns:UF', namespaces=self.ns)[0].text
        endereco_cep = self.xml_assinado.xpath('//ns:dest/ns:enderDest/ns:CEP', namespaces=self.ns)[0].text
        endereco_pais = self.xml_assinado.xpath('//ns:dest/ns:enderDest/ns:xPais', namespaces=self.ns)[0].text
        endereco_telefone = self.xml_assinado.xpath('//ns:dest/ns:enderDest/ns:fone', namespaces=self.ns)[0].text

        self.assertEqual(razao_social, 'JOSE DA SILVA')
        self.assertEqual(email, 'email@email.com')
        self.assertEqual(numero_documento, '12345678900')
        self.assertEqual(indicador_ie, '9')
        self.assertEqual(endereco_logradouro, 'Rua dos Bobos')
        self.assertEqual(endereco_numero, 'Zero')
        self.assertEqual(endereco_complemento, 'Ao lado de lugar nenhum')
        self.assertEqual(endereco_bairro, 'Aquele Mesmo')
        self.assertEqual(endereco_municipio, 'Brasilia')
        self.assertEqual(endereco_uf, 'DF')
        self.assertEqual(endereco_cep, '12345123')
        self.assertEqual(endereco_pais, 'Brasil')
        self.assertEqual(endereco_telefone, '11912341234')

    def total_e_produto_cst00_test(self):
        # Produto
        cProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cProd', namespaces=self.ns)[0].text
        cEAN = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEAN', namespaces=self.ns)[0].text
        xProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xProd', namespaces=self.ns)[0].text
        NCM = self.xml_assinado.xpath('//ns:det/ns:prod/ns:NCM', namespaces=self.ns)[0].text
        # CEST = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CEST', namespaces=self.ns)[0].text
        # indEscala = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indEscala', namespaces=self.ns)[0].text
        CEST = None
        indEscala = None
        CFOP = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CFOP', namespaces=self.ns)[0].text
        uCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uCom', namespaces=self.ns)[0].text
        qCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qCom', namespaces=self.ns)[0].text
        vUnCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnCom', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vProd', namespaces=self.ns)[0].text
        cEANTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEANTrib', namespaces=self.ns)[0].text
        uTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uTrib', namespaces=self.ns)[0].text
        qTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qTrib', namespaces=self.ns)[0].text
        vUnTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnTrib', namespaces=self.ns)[0].text
        indTot = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indTot', namespaces=self.ns)[0].text
        xPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xPed', namespaces=self.ns)[0].text
        nItemPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nItemPed', namespaces=self.ns)[0].text
        nFCI = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nFCI', namespaces=self.ns)[0].text

        self.assertEqual(cProd, '000328')
        self.assertEqual(cEAN, '1234567890121')
        self.assertEqual(xProd, 'Produto teste')
        self.assertEqual(NCM, '99999999')
        self.assertEqual(CEST, None)
        self.assertEqual(indEscala, None)
        self.assertEqual(CFOP, '5102')
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
        orig = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:orig', namespaces=self.ns)[0].text
        CST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:CST', namespaces=self.ns)[0].text
        modBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:modBC', namespaces=self.ns)[0].text
        vBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:vBC', namespaces=self.ns)[0].text
        pICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:pICMS', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:vICMS', namespaces=self.ns)[0].text
        # pFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:pFCP', namespaces=self.ns)[0].text
        # vFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:vFCP', namespaces=self.ns)[0].text
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
        CST_PIS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:PIS/ns:PISOutr/ns:CST', namespaces=self.ns)[0].text
        self.assertEqual(CST_PIS, '51')

        # # COFINS
        CST_COFINS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:COFINS/ns:COFINSOutr/ns:CST', namespaces=self.ns)[0].text
        self.assertEqual(CST_COFINS, '51')

        # Impostos - IPI Devolução
        pDevol = self.xml_assinado.xpath('//ns:det/ns:impostoDevol/ns:pDevol', namespaces=self.ns)[0].text
        vIPIDevol = self.xml_assinado.xpath('//ns:det/ns:impostoDevol/ns:IPI/ns:vIPIDevol', namespaces=self.ns)[0].text
        self.assertEqual(pDevol, '1.00')
        self.assertEqual(vIPIDevol, '10.00')
        
        # Informações Adicionais do produto
        infAdProd = self.xml_assinado.xpath('//ns:det/ns:infAdProd', namespaces=self.ns)[0].text
        self.assertEqual(infAdProd, 'Informacoes adicionais')

        # Totalizadores
        vBC = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBC', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMS', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMSDeson', namespaces=self.ns)[0].text
        vFCP = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCP', namespaces=self.ns)[0].text
        vBCST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBCST', namespaces=self.ns)[0].text
        vST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vST', namespaces=self.ns)[0].text
        vFCPST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPST', namespaces=self.ns)[0].text
        vFCPSTRet = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPSTRet', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vProd', namespaces=self.ns)[0].text
        vFrete = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFrete', namespaces=self.ns)[0].text
        vSeg = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vSeg', namespaces=self.ns)[0].text
        vDesc = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vDesc', namespaces=self.ns)[0].text
        vII = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vII', namespaces=self.ns)[0].text
        vIPI = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPI', namespaces=self.ns)[0].text
        vIPIDevol = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPIDevol', namespaces=self.ns)[0].text
        vPIS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vPIS', namespaces=self.ns)[0].text
        vCOFINS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vCOFINS', namespaces=self.ns)[0].text
        vOutro = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vOutro', namespaces=self.ns)[0].text
        vNF = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vNF', namespaces=self.ns)[0].text
        vTotTrib = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vTotTrib', namespaces=self.ns)[0].text

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
        self.assertEqual(vIPI, '0.00')
        self.assertEqual(vIPIDevol, '10.00')
        self.assertEqual(vPIS, '0.76')
        self.assertEqual(vCOFINS, '3.51')
        self.assertEqual(vOutro, '0.00')
        self.assertEqual(vNF, '127.00')
        self.assertEqual(vTotTrib, '21.06')

    def total_e_produto_cst40_test(self):
        # Produto
        cProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cProd', namespaces=self.ns)[0].text
        cEAN = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEAN', namespaces=self.ns)[0].text
        xProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xProd', namespaces=self.ns)[0].text
        NCM = self.xml_assinado.xpath('//ns:det/ns:prod/ns:NCM', namespaces=self.ns)[0].text
        # CEST = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CEST', namespaces=self.ns)[0].text
        # indEscala = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indEscala', namespaces=self.ns)[0].text
        CEST = None
        indEscala = None
        CFOP = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CFOP', namespaces=self.ns)[0].text
        uCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uCom', namespaces=self.ns)[0].text
        qCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qCom', namespaces=self.ns)[0].text
        vUnCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnCom', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vProd', namespaces=self.ns)[0].text
        cEANTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEANTrib', namespaces=self.ns)[0].text
        uTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uTrib', namespaces=self.ns)[0].text
        qTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qTrib', namespaces=self.ns)[0].text
        vUnTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnTrib', namespaces=self.ns)[0].text
        indTot = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indTot', namespaces=self.ns)[0].text
        xPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xPed', namespaces=self.ns)[0].text
        nItemPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nItemPed', namespaces=self.ns)[0].text
        nFCI = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nFCI', namespaces=self.ns)[0].text

        self.assertEqual(cProd, '000328')
        self.assertEqual(cEAN, '1234567890121')
        self.assertEqual(xProd, 'Produto teste')
        self.assertEqual(NCM, '99999999')
        self.assertEqual(CEST, None)
        self.assertEqual(indEscala, None)
        self.assertEqual(CFOP, '5102')
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
        orig = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:orig', namespaces=self.ns)[0].text
        CST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:CST', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:vICMSDeson', namespaces=self.ns)[0].text
        motDesICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:motDesICMS', namespaces=self.ns)[0].text

        self.assertEqual(orig, '0')
        self.assertEqual(CST, '40')
        self.assertEqual(vICMSDeson, '10.00')
        self.assertEqual(motDesICMS, '90')

        # Informações Adicionais do produto
        infAdProd = self.xml_assinado.xpath('//ns:det/ns:infAdProd', namespaces=self.ns)[0].text
        self.assertEqual(infAdProd, 'Informacoes adicionais')

        # Totalizadores
        vBC = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBC', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMS', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMSDeson', namespaces=self.ns)[0].text
        vFCP = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCP', namespaces=self.ns)[0].text
        vBCST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBCST', namespaces=self.ns)[0].text
        vST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vST', namespaces=self.ns)[0].text
        vFCPST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPST', namespaces=self.ns)[0].text
        vFCPSTRet = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPSTRet', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vProd', namespaces=self.ns)[0].text
        vFrete = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFrete', namespaces=self.ns)[0].text
        vSeg = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vSeg', namespaces=self.ns)[0].text
        vDesc = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vDesc', namespaces=self.ns)[0].text
        vII = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vII', namespaces=self.ns)[0].text
        vIPI = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPI', namespaces=self.ns)[0].text
        vIPIDevol = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPIDevol', namespaces=self.ns)[0].text
        vPIS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vPIS', namespaces=self.ns)[0].text
        vCOFINS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vCOFINS', namespaces=self.ns)[0].text
        vOutro = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vOutro', namespaces=self.ns)[0].text
        vNF = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vNF', namespaces=self.ns)[0].text
        vTotTrib = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vTotTrib', namespaces=self.ns)[0].text

        self.assertEqual(vBC, '0.00')
        self.assertEqual(vICMS, '0.00')
        self.assertEqual(vICMSDeson, '10.00')
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
        self.assertEqual(vIPI, '0.00')
        self.assertEqual(vIPIDevol, '0.00')
        self.assertEqual(vPIS, '0.00')
        self.assertEqual(vCOFINS, '0.00')
        self.assertEqual(vOutro, '0.00')
        self.assertEqual(vNF, '107.00')
        self.assertEqual(vTotTrib, '21.06')

    def total_e_produto_cst41_test(self):
        # Produto
        cProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cProd', namespaces=self.ns)[0].text
        cEAN = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEAN', namespaces=self.ns)[0].text
        xProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xProd', namespaces=self.ns)[0].text
        NCM = self.xml_assinado.xpath('//ns:det/ns:prod/ns:NCM', namespaces=self.ns)[0].text
        # CEST = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CEST', namespaces=self.ns)[0].text
        # indEscala = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indEscala', namespaces=self.ns)[0].text
        CEST = None
        indEscala = None
        CFOP = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CFOP', namespaces=self.ns)[0].text
        uCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uCom', namespaces=self.ns)[0].text
        qCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qCom', namespaces=self.ns)[0].text
        vUnCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnCom', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vProd', namespaces=self.ns)[0].text
        cEANTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEANTrib', namespaces=self.ns)[0].text
        uTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uTrib', namespaces=self.ns)[0].text
        qTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qTrib', namespaces=self.ns)[0].text
        vUnTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnTrib', namespaces=self.ns)[0].text
        indTot = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indTot', namespaces=self.ns)[0].text
        xPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xPed', namespaces=self.ns)[0].text
        nItemPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nItemPed', namespaces=self.ns)[0].text
        nFCI = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nFCI', namespaces=self.ns)[0].text

        self.assertEqual(cProd, '000328')
        self.assertEqual(cEAN, '1234567890121')
        self.assertEqual(xProd, 'Produto teste')
        self.assertEqual(NCM, '99999999')
        self.assertEqual(CEST, None)
        self.assertEqual(indEscala, None)
        self.assertEqual(CFOP, '5102')
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
        orig = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:orig', namespaces=self.ns)[0].text
        CST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:CST', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:vICMSDeson', namespaces=self.ns)[0].text
        motDesICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:motDesICMS', namespaces=self.ns)[0].text

        self.assertEqual(orig, '0')
        self.assertEqual(CST, '41')
        self.assertEqual(vICMSDeson, '10.00')
        self.assertEqual(motDesICMS, '90')

        # Informações Adicionais do produto
        infAdProd = self.xml_assinado.xpath('//ns:det/ns:infAdProd', namespaces=self.ns)[0].text
        self.assertEqual(infAdProd, 'Informacoes adicionais')

        # Totalizadores
        vBC = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBC', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMS', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMSDeson', namespaces=self.ns)[0].text
        vFCP = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCP', namespaces=self.ns)[0].text
        vBCST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBCST', namespaces=self.ns)[0].text
        vST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vST', namespaces=self.ns)[0].text
        vFCPST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPST', namespaces=self.ns)[0].text
        vFCPSTRet = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPSTRet', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vProd', namespaces=self.ns)[0].text
        vFrete = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFrete', namespaces=self.ns)[0].text
        vSeg = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vSeg', namespaces=self.ns)[0].text
        vDesc = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vDesc', namespaces=self.ns)[0].text
        vII = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vII', namespaces=self.ns)[0].text
        vIPI = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPI', namespaces=self.ns)[0].text
        vIPIDevol = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPIDevol', namespaces=self.ns)[0].text
        vPIS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vPIS', namespaces=self.ns)[0].text
        vCOFINS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vCOFINS', namespaces=self.ns)[0].text
        vOutro = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vOutro', namespaces=self.ns)[0].text
        vNF = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vNF', namespaces=self.ns)[0].text
        vTotTrib = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vTotTrib', namespaces=self.ns)[0].text

        self.assertEqual(vBC, '0.00')
        self.assertEqual(vICMS, '0.00')
        self.assertEqual(vICMSDeson, '10.00')
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
        self.assertEqual(vIPI, '0.00')
        self.assertEqual(vIPIDevol, '0.00')
        self.assertEqual(vPIS, '0.00')
        self.assertEqual(vCOFINS, '0.00')
        self.assertEqual(vOutro, '0.00')
        self.assertEqual(vNF, '107.00')
        self.assertEqual(vTotTrib, '21.06')

    def total_e_produto_cst50_test(self):
        # Produto
        cProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cProd', namespaces=self.ns)[0].text
        cEAN = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEAN', namespaces=self.ns)[0].text
        xProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xProd', namespaces=self.ns)[0].text
        NCM = self.xml_assinado.xpath('//ns:det/ns:prod/ns:NCM', namespaces=self.ns)[0].text
        # CEST = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CEST', namespaces=self.ns)[0].text
        # indEscala = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indEscala', namespaces=self.ns)[0].text
        CEST = None
        indEscala = None
        CFOP = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CFOP', namespaces=self.ns)[0].text
        uCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uCom', namespaces=self.ns)[0].text
        qCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qCom', namespaces=self.ns)[0].text
        vUnCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnCom', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vProd', namespaces=self.ns)[0].text
        cEANTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEANTrib', namespaces=self.ns)[0].text
        uTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uTrib', namespaces=self.ns)[0].text
        qTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qTrib', namespaces=self.ns)[0].text
        vUnTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnTrib', namespaces=self.ns)[0].text
        indTot = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indTot', namespaces=self.ns)[0].text
        xPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xPed', namespaces=self.ns)[0].text
        nItemPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nItemPed', namespaces=self.ns)[0].text
        nFCI = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nFCI', namespaces=self.ns)[0].text

        self.assertEqual(cProd, '000328')
        self.assertEqual(cEAN, '1234567890121')
        self.assertEqual(xProd, 'Produto teste')
        self.assertEqual(NCM, '99999999')
        self.assertEqual(CEST, None)
        self.assertEqual(indEscala, None)
        self.assertEqual(CFOP, '5102')
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
        orig = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:orig', namespaces=self.ns)[0].text
        CST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:CST', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:vICMSDeson', namespaces=self.ns)[0].text
        motDesICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS40/ns:motDesICMS', namespaces=self.ns)[0].text

        self.assertEqual(orig, '0')
        self.assertEqual(CST, '50')
        self.assertEqual(vICMSDeson, '10.00')
        self.assertEqual(motDesICMS, '90')

        # Informações Adicionais do produto
        infAdProd = self.xml_assinado.xpath('//ns:det/ns:infAdProd', namespaces=self.ns)[0].text
        self.assertEqual(infAdProd, 'Informacoes adicionais')

        # Totalizadores
        vBC = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBC', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMS', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMSDeson', namespaces=self.ns)[0].text
        vFCP = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCP', namespaces=self.ns)[0].text
        vBCST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBCST', namespaces=self.ns)[0].text
        vST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vST', namespaces=self.ns)[0].text
        vFCPST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPST', namespaces=self.ns)[0].text
        vFCPSTRet = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPSTRet', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vProd', namespaces=self.ns)[0].text
        vFrete = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFrete', namespaces=self.ns)[0].text
        vSeg = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vSeg', namespaces=self.ns)[0].text
        vDesc = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vDesc', namespaces=self.ns)[0].text
        vII = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vII', namespaces=self.ns)[0].text
        vIPI = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPI', namespaces=self.ns)[0].text
        vIPIDevol = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPIDevol', namespaces=self.ns)[0].text
        vPIS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vPIS', namespaces=self.ns)[0].text
        vCOFINS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vCOFINS', namespaces=self.ns)[0].text
        vOutro = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vOutro', namespaces=self.ns)[0].text
        vNF = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vNF', namespaces=self.ns)[0].text
        vTotTrib = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vTotTrib', namespaces=self.ns)[0].text

        self.assertEqual(vBC, '0.00')
        self.assertEqual(vICMS, '0.00')
        self.assertEqual(vICMSDeson, '10.00')
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
        self.assertEqual(vIPI, '0.00')
        self.assertEqual(vIPIDevol, '0.00')
        self.assertEqual(vPIS, '0.00')
        self.assertEqual(vCOFINS, '0.00')
        self.assertEqual(vOutro, '0.00')
        self.assertEqual(vNF, '107.00')
        self.assertEqual(vTotTrib, '21.06')

    def total_e_produto_cst51_test(self):
        # Produto
        cProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cProd', namespaces=self.ns)[0].text
        cEAN = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEAN', namespaces=self.ns)[0].text
        xProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xProd', namespaces=self.ns)[0].text
        NCM = self.xml_assinado.xpath('//ns:det/ns:prod/ns:NCM', namespaces=self.ns)[0].text
        # CEST = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CEST', namespaces=self.ns)[0].text
        # indEscala = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indEscala', namespaces=self.ns)[0].text
        CEST = None
        indEscala = None
        CFOP = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CFOP', namespaces=self.ns)[0].text
        uCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uCom', namespaces=self.ns)[0].text
        qCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qCom', namespaces=self.ns)[0].text
        vUnCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnCom', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vProd', namespaces=self.ns)[0].text
        cEANTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEANTrib', namespaces=self.ns)[0].text
        uTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uTrib', namespaces=self.ns)[0].text
        qTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qTrib', namespaces=self.ns)[0].text
        vUnTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnTrib', namespaces=self.ns)[0].text
        indTot = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indTot', namespaces=self.ns)[0].text
        xPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xPed', namespaces=self.ns)[0].text
        nItemPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nItemPed', namespaces=self.ns)[0].text
        nFCI = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nFCI', namespaces=self.ns)[0].text

        self.assertEqual(cProd, '000328')
        self.assertEqual(cEAN, '1234567890121')
        self.assertEqual(xProd, 'Produto teste')
        self.assertEqual(NCM, '99999999')
        self.assertEqual(CEST, None)
        self.assertEqual(indEscala, None)
        self.assertEqual(CFOP, '5102')
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
        orig = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS51/ns:orig', namespaces=self.ns)[0].text
        CST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS51/ns:CST', namespaces=self.ns)[0].text
        modBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS51/ns:modBC', namespaces=self.ns)[0].text
        # vBCFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS51/ns:vBCFCP', namespaces=self.ns)[0].text
        # pFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS51/ns:pFCP', namespaces=self.ns)[0].text
        # vFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS51/ns:vFCP', namespaces=self.ns)[0].text

        self.assertEqual(orig, '0')
        self.assertEqual(CST, '51')
        self.assertEqual(modBC, '0')
        # self.assertEqual(vBCFCP, '0.00')
        # self.assertEqual(pFCP, '0.00')
        # self.assertEqual(vFCP, '0.00')

        # Informações Adicionais do produto
        infAdProd = self.xml_assinado.xpath('//ns:det/ns:infAdProd', namespaces=self.ns)[0].text
        self.assertEqual(infAdProd, 'Informacoes adicionais')

        # Totalizadores
        vBC = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBC', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMS', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMSDeson', namespaces=self.ns)[0].text
        vFCP = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCP', namespaces=self.ns)[0].text
        vBCST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBCST', namespaces=self.ns)[0].text
        vST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vST', namespaces=self.ns)[0].text
        vFCPST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPST', namespaces=self.ns)[0].text
        vFCPSTRet = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPSTRet', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vProd', namespaces=self.ns)[0].text
        vFrete = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFrete', namespaces=self.ns)[0].text
        vSeg = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vSeg', namespaces=self.ns)[0].text
        vDesc = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vDesc', namespaces=self.ns)[0].text
        vII = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vII', namespaces=self.ns)[0].text
        vIPI = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPI', namespaces=self.ns)[0].text
        vIPIDevol = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPIDevol', namespaces=self.ns)[0].text
        vPIS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vPIS', namespaces=self.ns)[0].text
        vCOFINS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vCOFINS', namespaces=self.ns)[0].text
        vOutro = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vOutro', namespaces=self.ns)[0].text
        vNF = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vNF', namespaces=self.ns)[0].text
        vTotTrib = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vTotTrib', namespaces=self.ns)[0].text

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
        self.assertEqual(vIPI, '0.00')
        self.assertEqual(vIPIDevol, '0.00')
        self.assertEqual(vPIS, '0.00')
        self.assertEqual(vCOFINS, '0.00')
        self.assertEqual(vOutro, '0.00')
        self.assertEqual(vNF, '117.00')
        self.assertEqual(vTotTrib, '21.06')

    def total_e_produto_cst60_test(self):
        # Produto
        cProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cProd', namespaces=self.ns)[0].text
        cEAN = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEAN', namespaces=self.ns)[0].text
        xProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xProd', namespaces=self.ns)[0].text
        NCM = self.xml_assinado.xpath('//ns:det/ns:prod/ns:NCM', namespaces=self.ns)[0].text
        # CEST = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CEST', namespaces=self.ns)[0].text
        # indEscala = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indEscala', namespaces=self.ns)[0].text
        CEST = None
        indEscala = None
        CFOP = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CFOP', namespaces=self.ns)[0].text
        uCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uCom', namespaces=self.ns)[0].text
        qCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qCom', namespaces=self.ns)[0].text
        vUnCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnCom', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vProd', namespaces=self.ns)[0].text
        cEANTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEANTrib', namespaces=self.ns)[0].text
        uTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uTrib', namespaces=self.ns)[0].text
        qTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qTrib', namespaces=self.ns)[0].text
        vUnTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnTrib', namespaces=self.ns)[0].text
        indTot = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indTot', namespaces=self.ns)[0].text
        xPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xPed', namespaces=self.ns)[0].text
        nItemPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nItemPed', namespaces=self.ns)[0].text
        nFCI = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nFCI', namespaces=self.ns)[0].text

        self.assertEqual(cProd, '000328')
        self.assertEqual(cEAN, '1234567890121')
        self.assertEqual(xProd, 'Produto teste')
        self.assertEqual(NCM, '99999999')
        self.assertEqual(CEST, None)
        self.assertEqual(indEscala, None)
        self.assertEqual(CFOP, '5102')
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
        orig = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS60/ns:orig', namespaces=self.ns)[0].text
        CST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS60/ns:CST', namespaces=self.ns)[0].text
        vBCSTRet = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS60/ns:vBCSTRet', namespaces=self.ns)[0].text
        pST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS60/ns:pST', namespaces=self.ns)[0].text
        vICMSSTRet = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS60/ns:vICMSSTRet', namespaces=self.ns)[0].text

        self.assertEqual(orig, '0')
        self.assertEqual(CST, '60')
        self.assertEqual(vBCSTRet, '0')
        self.assertEqual(pST, '0.0000')
        self.assertEqual(vICMSSTRet, '0')

        # Informações Adicionais do produto
        infAdProd = self.xml_assinado.xpath('//ns:det/ns:infAdProd', namespaces=self.ns)[0].text
        self.assertEqual(infAdProd, 'Informacoes adicionais')

        # Totalizadores
        vBC = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBC', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMS', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMSDeson', namespaces=self.ns)[0].text
        vFCP = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCP', namespaces=self.ns)[0].text
        vBCST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBCST', namespaces=self.ns)[0].text
        vST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vST', namespaces=self.ns)[0].text
        vFCPST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPST', namespaces=self.ns)[0].text
        vFCPSTRet = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPSTRet', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vProd', namespaces=self.ns)[0].text
        vFrete = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFrete', namespaces=self.ns)[0].text
        vSeg = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vSeg', namespaces=self.ns)[0].text
        vDesc = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vDesc', namespaces=self.ns)[0].text
        vII = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vII', namespaces=self.ns)[0].text
        vIPI = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPI', namespaces=self.ns)[0].text
        vIPIDevol = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPIDevol', namespaces=self.ns)[0].text
        vPIS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vPIS', namespaces=self.ns)[0].text
        vCOFINS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vCOFINS', namespaces=self.ns)[0].text
        vOutro = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vOutro', namespaces=self.ns)[0].text
        vNF = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vNF', namespaces=self.ns)[0].text
        vTotTrib = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vTotTrib', namespaces=self.ns)[0].text

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
        self.assertEqual(vIPI, '0.00')
        self.assertEqual(vIPIDevol, '0.00')
        self.assertEqual(vPIS, '0.00')
        self.assertEqual(vCOFINS, '0.00')
        self.assertEqual(vOutro, '0.00')
        self.assertEqual(vNF, '117.00')
        self.assertEqual(vTotTrib, '21.06')

    def total_e_produto_cst70_test(self):
        # Produto
        cProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cProd', namespaces=self.ns)[0].text
        cEAN = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEAN', namespaces=self.ns)[0].text
        xProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xProd', namespaces=self.ns)[0].text
        NCM = self.xml_assinado.xpath('//ns:det/ns:prod/ns:NCM', namespaces=self.ns)[0].text
        # CEST = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CEST', namespaces=self.ns)[0].text
        # indEscala = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indEscala', namespaces=self.ns)[0].text
        CEST = None
        indEscala = None
        CFOP = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CFOP', namespaces=self.ns)[0].text
        uCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uCom', namespaces=self.ns)[0].text
        qCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qCom', namespaces=self.ns)[0].text
        vUnCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnCom', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vProd', namespaces=self.ns)[0].text
        cEANTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEANTrib', namespaces=self.ns)[0].text
        uTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uTrib', namespaces=self.ns)[0].text
        qTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qTrib', namespaces=self.ns)[0].text
        vUnTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnTrib', namespaces=self.ns)[0].text
        indTot = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indTot', namespaces=self.ns)[0].text
        xPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xPed', namespaces=self.ns)[0].text
        nItemPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nItemPed', namespaces=self.ns)[0].text
        nFCI = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nFCI', namespaces=self.ns)[0].text

        self.assertEqual(cProd, '000328')
        self.assertEqual(cEAN, '1234567890121')
        self.assertEqual(xProd, 'Produto teste')
        self.assertEqual(NCM, '99999999')
        self.assertEqual(CEST, None)
        self.assertEqual(indEscala, None)
        self.assertEqual(CFOP, '5102')
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
        orig = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:orig', namespaces=self.ns)[0].text
        CST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:CST', namespaces=self.ns)[0].text
        modBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:modBC', namespaces=self.ns)[0].text
        pRedBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:pRedBC', namespaces=self.ns)[0].text
        vBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:vBC', namespaces=self.ns)[0].text
        pICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:pICMS', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:vICMS', namespaces=self.ns)[0].text
        vBCFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:vBCFCP', namespaces=self.ns)[0].text
        pFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:pFCP', namespaces=self.ns)[0].text
        vFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:vFCP', namespaces=self.ns)[0].text

        modBCST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:modBCST', namespaces=self.ns)[0].text
        pMVAST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:pMVAST', namespaces=self.ns)[0].text
        pRedBCST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:pRedBCST', namespaces=self.ns)[0].text
        vBCST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:vBCST', namespaces=self.ns)[0].text
        pICMSST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:pICMSST', namespaces=self.ns)[0].text
        vICMSST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:vICMSST', namespaces=self.ns)[0].text
        vBCFCPST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:vBCFCPST', namespaces=self.ns)[0].text
        pFCPST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:pFCPST', namespaces=self.ns)[0].text
        vFCPST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS70/ns:vFCPST', namespaces=self.ns)[0].text

        self.assertEqual(orig, '0')
        self.assertEqual(CST, '70')
        self.assertEqual(modBC, '0')
        self.assertEqual(vBC, '18.67')
        self.assertEqual(pRedBC, '10.00')
        self.assertEqual(pICMS, '18.00')
        self.assertEqual(vICMS, '3.36')
        self.assertEqual(vBCFCP, '3.36')
        self.assertEqual(pFCP, '2.00')
        self.assertEqual(vFCP, '0.06')

        self.assertEqual(modBCST, '4')
        self.assertEqual(pMVAST, '0.00')
        self.assertEqual(pRedBCST, '10.00')
        self.assertEqual(vBCST, '26.68')
        self.assertEqual(pICMSST, '18.00')
        self.assertEqual(vICMSST, '1.44')
        self.assertEqual(vBCFCPST, '1.44')
        self.assertEqual(pFCPST, '2.00')
        self.assertEqual(vFCPST, '0.02')

        # Informações Adicionais do produto
        infAdProd = self.xml_assinado.xpath('//ns:det/ns:infAdProd', namespaces=self.ns)[0].text
        self.assertEqual(infAdProd, 'Informacoes adicionais')

        # Totais
        vBC = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBC', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMS', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMSDeson', namespaces=self.ns)[0].text
        vFCP = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCP', namespaces=self.ns)[0].text
        vBCST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBCST', namespaces=self.ns)[0].text
        vST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vST', namespaces=self.ns)[0].text
        vFCPST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPST', namespaces=self.ns)[0].text
        vFCPSTRet = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPSTRet', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vProd', namespaces=self.ns)[0].text
        vFrete = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFrete', namespaces=self.ns)[0].text
        vSeg = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vSeg', namespaces=self.ns)[0].text
        vDesc = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vDesc', namespaces=self.ns)[0].text
        vII = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vII', namespaces=self.ns)[0].text
        vIPI = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPI', namespaces=self.ns)[0].text
        vIPIDevol = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPIDevol', namespaces=self.ns)[0].text
        vPIS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vPIS', namespaces=self.ns)[0].text
        vCOFINS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vCOFINS', namespaces=self.ns)[0].text
        vOutro = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vOutro', namespaces=self.ns)[0].text
        vNF = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vNF', namespaces=self.ns)[0].text
        vTotTrib = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vTotTrib', namespaces=self.ns)[0].text

        self.assertEqual(vBC, '18.67')
        self.assertEqual(vICMS, '3.36')
        self.assertEqual(vICMSDeson, '0.00')
        self.assertEqual(vFCP, '0.06')
        self.assertEqual(vBCST, '26.68')
        self.assertEqual(vST, '1.44')
        self.assertEqual(vFCPST, '0.02')
        self.assertEqual(vFCPSTRet, '0.00')
        self.assertEqual(vProd, '117.00')
        self.assertEqual(vFrete, '0.00')
        self.assertEqual(vSeg, '0.00')
        self.assertEqual(vDesc, '0.00')
        self.assertEqual(vII, '0.00')
        self.assertEqual(vIPI, '0.00')
        self.assertEqual(vIPIDevol, '0.00')
        self.assertEqual(vPIS, '0.00')
        self.assertEqual(vCOFINS, '0.00')
        self.assertEqual(vOutro, '0.00')
        self.assertEqual(vNF, '118.46')
        self.assertEqual(vTotTrib, '21.06')

    def total_e_produto_cst90_test(self):
        # Produto
        cProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cProd', namespaces=self.ns)[0].text
        cEAN = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEAN', namespaces=self.ns)[0].text
        xProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xProd', namespaces=self.ns)[0].text
        NCM = self.xml_assinado.xpath('//ns:det/ns:prod/ns:NCM', namespaces=self.ns)[0].text
        # CEST = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CEST', namespaces=self.ns)[0].text
        # indEscala = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indEscala', namespaces=self.ns)[0].text
        CEST = None
        indEscala = None
        CFOP = self.xml_assinado.xpath('//ns:det/ns:prod/ns:CFOP', namespaces=self.ns)[0].text
        uCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uCom', namespaces=self.ns)[0].text
        qCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qCom', namespaces=self.ns)[0].text
        vUnCom = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnCom', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vProd', namespaces=self.ns)[0].text
        cEANTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:cEANTrib', namespaces=self.ns)[0].text
        uTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:uTrib', namespaces=self.ns)[0].text
        qTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:qTrib', namespaces=self.ns)[0].text
        vUnTrib = self.xml_assinado.xpath('//ns:det/ns:prod/ns:vUnTrib', namespaces=self.ns)[0].text
        indTot = self.xml_assinado.xpath('//ns:det/ns:prod/ns:indTot', namespaces=self.ns)[0].text
        xPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:xPed', namespaces=self.ns)[0].text
        nItemPed = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nItemPed', namespaces=self.ns)[0].text
        nFCI = self.xml_assinado.xpath('//ns:det/ns:prod/ns:nFCI', namespaces=self.ns)[0].text

        self.assertEqual(cProd, '000328')
        self.assertEqual(cEAN, '1234567890121')
        self.assertEqual(xProd, 'Produto teste')
        self.assertEqual(NCM, '99999999')
        self.assertEqual(CEST, None)
        self.assertEqual(indEscala, None)
        self.assertEqual(CFOP, '5102')
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
        orig = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS90/ns:orig', namespaces=self.ns)[0].text
        CST = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS90/ns:CST', namespaces=self.ns)[0].text
        modBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS90/ns:modBC', namespaces=self.ns)[0].text
        vBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS90/ns:vBC', namespaces=self.ns)[0].text
        pRedBC = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS90/ns:pRedBC', namespaces=self.ns)[0].text
        pICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS90/ns:pICMS', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS90/ns:vICMS', namespaces=self.ns)[0].text
        # vBCFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS90/ns:vBCFCP', namespaces=self.ns)[0].text
        # pFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS90/ns:pFCP', namespaces=self.ns)[0].text
        # vFCP = self.xml_assinado.xpath('//ns:det/ns:imposto/ns:ICMS/ns:ICMS90/ns:vFCP', namespaces=self.ns)[0].text

        self.assertEqual(orig, '0')
        self.assertEqual(CST, '90')
        self.assertEqual(modBC, '0')
        self.assertEqual(vBC, '117.00')
        self.assertEqual(pRedBC, '0.00')
        self.assertEqual(pICMS, '10.00')
        self.assertEqual(vICMS, '11.70')

        # self.assertEqual(vBCFCP, '0.00')
        # self.assertEqual(pFCP, '0.00')
        # self.assertEqual(vFCP, '0.00')

        # Informações Adicionais do produto
        infAdProd = self.xml_assinado.xpath('//ns:det/ns:infAdProd', namespaces=self.ns)[0].text
        self.assertEqual(infAdProd, 'Informacoes adicionais')

        # Totais
        vBC = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBC', namespaces=self.ns)[0].text
        vICMS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMS', namespaces=self.ns)[0].text
        vICMSDeson = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vICMSDeson', namespaces=self.ns)[0].text
        vFCP = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCP', namespaces=self.ns)[0].text
        vBCST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vBCST', namespaces=self.ns)[0].text
        vST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vST', namespaces=self.ns)[0].text
        vFCPST = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPST', namespaces=self.ns)[0].text
        vFCPSTRet = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFCPSTRet', namespaces=self.ns)[0].text
        vProd = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vProd', namespaces=self.ns)[0].text
        vFrete = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vFrete', namespaces=self.ns)[0].text
        vSeg = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vSeg', namespaces=self.ns)[0].text
        vDesc = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vDesc', namespaces=self.ns)[0].text
        vII = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vII', namespaces=self.ns)[0].text
        vIPI = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPI', namespaces=self.ns)[0].text
        vIPIDevol = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vIPIDevol', namespaces=self.ns)[0].text
        vPIS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vPIS', namespaces=self.ns)[0].text
        vCOFINS = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vCOFINS', namespaces=self.ns)[0].text
        vOutro = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vOutro', namespaces=self.ns)[0].text
        vNF = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vNF', namespaces=self.ns)[0].text
        vTotTrib = self.xml_assinado.xpath('//ns:total/ns:ICMSTot/ns:vTotTrib', namespaces=self.ns)[0].text

        self.assertEqual(vBC, '117.00')
        self.assertEqual(vICMS, '11.70')
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
        self.assertEqual(vIPI, '0.00')
        self.assertEqual(vIPIDevol, '0.00')
        self.assertEqual(vPIS, '0.00')
        self.assertEqual(vCOFINS, '0.00')
        self.assertEqual(vOutro, '0.00')
        self.assertEqual(vNF, '117.00')
        self.assertEqual(vTotTrib, '21.06')

    def notas_produtor_referenciadas_test(self):
        ref_1 = self.xml_assinado.xpath('//ns:ide/ns:NFref/ns:refNFP/ns:nNF', namespaces=self.ns)[0].text
        ref_2 = self.xml_assinado.xpath('//ns:ide/ns:NFref/ns:refNFP/ns:nNF', namespaces=self.ns)[1].text

        self.assertEqual(ref_1, '999999998')
        self.assertEqual(ref_2, '999999999')

    def notas_referenciadas_test(self):
        chave_1 = self.xml_assinado.xpath('//ns:ide/ns:NFref/ns:refNFe', namespaces=self.ns)[0].text
        chave_2 = self.xml_assinado.xpath('//ns:ide/ns:NFref/ns:refNFe', namespaces=self.ns)[1].text

        self.assertEqual(chave_1, '12345678901234567890123456789012345678900001')
        self.assertEqual(chave_2, '12345678901234567890123456789012345678900002')

    def responsavel_tecnico_test(self):
        cnpj = self.xml_assinado.xpath('//ns:infRespTec/ns:CNPJ', namespaces=self.ns)[0].text
        contato = self.xml_assinado.xpath('//ns:infRespTec/ns:xContato', namespaces=self.ns)[0].text
        email = self.xml_assinado.xpath('//ns:infRespTec/ns:email', namespaces=self.ns)[0].text
        fone = self.xml_assinado.xpath('//ns:infRespTec/ns:fone', namespaces=self.ns)[0].text

        self.assertEqual(cnpj, '99999999000199')
        self.assertEqual(contato, 'Teste PyNFe')
        self.assertEqual(email, 'pynfe@pynfe.io')
        self.assertEqual(fone, '11912341234')

    def digestvalue_da_assinatura_test(self):
        DigestValue = self.xml_assinado.xpath('//ns:Signature//ns:SignedInfo/ns:Reference/ns:DigestValue', namespaces=self.ns_sig)[0].text
        self.assertTrue(len(DigestValue) > 0)

    def test_notafiscal_produto_cst00(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_cst00()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.dados_emitente_test()
        self.dados_destinatario_test()
        self.total_e_produto_cst00_test()
        self.notas_referenciadas_test()
        self.responsavel_tecnico_test()
        self.digestvalue_da_assinatura_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()

    def test_notafiscal_produto_cst40(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_cst40()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.dados_emitente_test()
        self.dados_destinatario_test()
        self.total_e_produto_cst40_test()
        self.notas_referenciadas_test()
        self.responsavel_tecnico_test()
        self.digestvalue_da_assinatura_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()

    def test_notafiscal_produto_cst41(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_cst41()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.dados_emitente_test()
        self.dados_destinatario_test()
        self.total_e_produto_cst41_test()
        self.notas_referenciadas_test()
        self.responsavel_tecnico_test()
        self.digestvalue_da_assinatura_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()

    def test_notafiscal_produto_cst50(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_cst50()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.dados_emitente_test()
        self.dados_destinatario_test()
        self.total_e_produto_cst50_test()
        self.notas_referenciadas_test()
        self.responsavel_tecnico_test()
        self.digestvalue_da_assinatura_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()

    def test_notafiscal_produto_cst51(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_cst51()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.dados_emitente_test()
        self.dados_destinatario_test()
        self.total_e_produto_cst51_test()
        self.notas_referenciadas_test()
        self.responsavel_tecnico_test()
        self.digestvalue_da_assinatura_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()

    def test_notafiscal_produto_cst60(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_cst60()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.dados_emitente_test()
        self.dados_destinatario_test()
        self.total_e_produto_cst60_test()
        self.notas_referenciadas_test()
        self.responsavel_tecnico_test()
        self.digestvalue_da_assinatura_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()

    def test_notafiscal_produto_cst70(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_cst70()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.dados_emitente_test()
        self.dados_destinatario_test()
        self.total_e_produto_cst70_test()
        self.notas_referenciadas_test()
        self.responsavel_tecnico_test()
        self.digestvalue_da_assinatura_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()

    def test_notafiscal_produto_cst90(self):
        # Preenche as classes do pynfe
        self.emitente = self.preenche_emitente()
        self.cliente = self.preenche_destinatario()
        self.notafiscal = self.preenche_notafiscal_produto_cst90()

        # Serializa e assina o XML
        self.xml = self.serializa_nfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.dados_emitente_test()
        self.dados_destinatario_test()
        self.total_e_produto_cst90_test()
        self.notas_produtor_referenciadas_test()
        self.responsavel_tecnico_test()
        self.digestvalue_da_assinatura_test()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()


if __name__ == '__main__':
    unittest.main()