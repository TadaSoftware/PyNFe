#!/usr/bin/env python
# *-* encoding: utf8 *-*

import unittest

from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.entidades.manifesto import (
    Manifesto,
    ManifestoCondutor,
    ManifestoContratante,
    ManifestoDocumentosNFe,
    ManifestoEmitente,
    ManifestoMunicipioCarrega,
    ManifestoPercurso,
    ManifestoRodoviario,
    ManifestoTotais,
    ManifestoVeiculoReboque,
    ManifestoVeiculoTracao,
    ManifestoCIOT,
    ManifestoPedagio,
    ManifestoAverbacao,
)
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.processamento.serializacao import SerializacaoMDFe, SerializacaoQrcodeMDFe
from pynfe.processamento.validacao import Validacao
from pynfe.utils.flags import (
    NAMESPACE_MDFE,
    NAMESPACE_SIG,
    XSD_FOLDER_MDFE,
    XSD_MDFE,
    XSD_MDFE_PROCESSADA,
)
from decimal import Decimal
import datetime


class SerializacaoMDFeTestCase(unittest.TestCase):
    """
    Imprimir o XML completo:
        print(etree.tostring(self.xml_assinado))

    """

    def setUp(self):
        self.certificado = "./tests/certificado.pfx"
        self.senha = bytes("123456", "utf-8")
        self.uf = "pr"
        self.homologacao = True

        self.ns = {"ns": NAMESPACE_MDFE}
        self.ns_sig = {"ns": NAMESPACE_SIG}

        self.validacao = Validacao()
        self.xsd_procMDFe = self.validacao.get_xsd(
            xsd_file=XSD_MDFE_PROCESSADA, xsd_folder=XSD_FOLDER_MDFE
        )
        self.xsd_mdfe = self.validacao.get_xsd(
            xsd_file=XSD_MDFE, xsd_folder=XSD_FOLDER_MDFE
        )

    def preenche_manifesto(self):
        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_viagem = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        # Emitente
        emitente = ManifestoEmitente(
            cpfcnpj="99999999000199",  # cnpj apenas números
            inscricao_estadual="9999999999",  # numero de IE da empresa
            razao_social="NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL",
            nome_fantasia="Nome Fantasia da Empresa",
            endereco_logradouro="RUA UM",
            endereco_numero="111",
            endereco_complemento=None,
            endereco_bairro="CENTRO",
            endereco_municipio="CUIABA",
            endereco_cep="78118000",
            endereco_uf="MT",
            endereco_telefone="65999662821",
            endereco_email="teste@gmail.com",
        )

        # Totais
        totais = ManifestoTotais(qCTe=0, qNFe=2, vCarga=1000, cUnid="KG", qCarga=5000)

        # Municípios de carregamento
        carregamento_1 = ManifestoMunicipioCarrega(
            cMunCarrega="5105101", xMunCarrega="JUARA"
        )
        carregamento_2 = ManifestoMunicipioCarrega(
            cMunCarrega="5107925", xMunCarrega="SORRISO"
        )

        # UFs percurso
        percurso_1 = ManifestoPercurso(UFPer="MS")
        percurso_2 = ManifestoPercurso(UFPer="GO")

        # modal Rodo
        condutor_1 = ManifestoCondutor(
            nome_motorista="JOAO DA SILVA", cpf_motorista="12345678912"
        )
        condutor_2 = ManifestoCondutor(
            nome_motorista="JOSE DA SILVA", cpf_motorista="12345678911"
        )

        veiculo_tracao = []
        veiculo_tracao.append(
            ManifestoVeiculoTracao(
                cInt="001",
                placa="ABC1234",
                RENAVAM="123456789",
                tara=Decimal("5000"),
                capKG=Decimal("4500"),
                capM3=Decimal("400"),
                proprietario=None,
                condutor=[condutor_1, condutor_2],
                tpRod="01",
                tpCar="02",
                UF="MT",
            )
        )

        veiculo_reboque_1 = ManifestoVeiculoReboque(
            cInt="001",
            placa="XYZ4567",
            RENAVAM="123456789",
            tara=Decimal("4000"),
            capKG=Decimal("3000"),
            capM3=Decimal("300"),
            proprietario=None,
            tpCar="02",
            UF="MT",
        )

        veiculo_reboque_2 = ManifestoVeiculoReboque(
            cInt="002",
            placa="XYQ4567",
            RENAVAM="123456781",
            tara=Decimal("4000"),
            capKG=Decimal("3000"),
            capM3=Decimal("300"),
            proprietario=None,
            tpCar="02",
            UF="MT",
        )

        ciot_1 = ManifestoCIOT(numero_ciot="123456789012", cpfcnpj="75961547191")

        pedagio_1 = ManifestoPedagio(
            cnpj_fornecedor="17060943000102",
            cpfcnpj_pagador="75961547191",
            numero_compra="789",
            valor_pedagio=Decimal("2.64"),
        )

        contratante_1 = ManifestoContratante(
            nome="JOAO DA SILVA",
            cpfcnpj="12345678912",
            NroContrato="q26393479sakjd231234",
            vContratoGlobal=Decimal("2342.64"),
        )

        contratante_2 = ManifestoContratante(
            nome="JOSE DA SILVA", cpfcnpj="12345678911"
        )

        modal_rodoviario = ManifestoRodoviario(
            rntrc="12345678",
            ciot=[ciot_1],
            pedagio=[pedagio_1],
            contratante=[contratante_1, contratante_2],
            pagamento=None,
            veiculo_tracao=veiculo_tracao,
            veiculo_reboque=[veiculo_reboque_1, veiculo_reboque_2],
        )

        # Manifesto
        manifesto = Manifesto(
            uf="MT",
            tipo_emitente=2,  # 1=Transportadora; 2=Carga própria; 3=CTe Globalizado
            tipo_transportador=0,  # 0=nenhum; 1=etc; 2=tac; 3=ctc
            modelo=58,
            serie="920",
            numero_mdfe="1",
            modal=1,
            data_emissao=data_emissao,
            forma_emissao="1",  # 1=Emissão normal (não em contingência);
            processo_emissao="0",  # 0=Emissão de NF-e com aplicativo do contribuinte;
            UFIni="MT",
            UFFim="SP",
            infMunCarrega=[carregamento_1, carregamento_2],
            infPercurso=[percurso_1, percurso_2],
            dhIniViagem=data_viagem,
            emitente=emitente,
            modal_rodoviario=modal_rodoviario,
            totais=totais,
            informacoes_complementares_interesse_contribuinte="Mensagem complementar",
        )

        # Documentos vinculados
        nfe_1 = ManifestoDocumentosNFe(
            chave_acesso_nfe="51180917060943000102550010001445371002594517"
        )
        nfe_2 = ManifestoDocumentosNFe(
            chave_acesso_nfe="51191217060943000102550010001800551003198999"
        )
        nfe_3 = ManifestoDocumentosNFe(
            chave_acesso_nfe="51180917060943000102550010001445371002594517"
        )
        nfe_4 = ManifestoDocumentosNFe(
            chave_acesso_nfe="51191217060943000102550010001800551003198999"
        )

        manifesto.adicionar_documentos(
            cMunDescarga="3550308",
            xMunDescarga="Sao Paulo",
            documentos_nfe=[nfe_1, nfe_2],
            documentos_cte=[],
        )
        manifesto.adicionar_documentos(
            cMunDescarga="3530607",
            xMunDescarga="Mogi das Cruzes",
            documentos_nfe=[nfe_3, nfe_4],
            documentos_cte=[],
        )

        # Informações do Seguro
        averbacao_1 = ManifestoAverbacao(numero="00000000000000000000000")
        averbacao_2 = ManifestoAverbacao(numero="11111111111111111111111")

        manifesto.adicionar_seguradora(
            responsavel_seguro="1",
            cnpj_responsavel="75512177000176",
            nome_seguradora="TESTE SEGURADORA SA",
            cnpj_seguradora="75512177000176",
            numero_apolice="00000",
            averbacoes=[averbacao_1, averbacao_2],
        )

        # Produto Predominante
        manifesto.adicionar_produto(
            tipo_carga="01",
            nome_produto="Descricao do Produto",
            cean="78967142344650",
            ncm="01012100",
        )

        # Lacres
        manifesto.adicionar_lacres(nLacre="123")
        manifesto.adicionar_lacres(nLacre="456")
        manifesto.adicionar_lacres(nLacre="789")

        # Responsável técnico
        manifesto.adicionar_responsavel_tecnico(
            cnpj="99999999000199",
            contato="Teste PyNFe",
            email="pynfe@pynfe.io",
            fone="11912341234",
        )

    def preenche_manifesto_sem_rntrc(self):
        utc = datetime.timezone.utc
        data_emissao = datetime.datetime(2021, 1, 14, 12, 0, 0, tzinfo=utc)
        data_viagem = datetime.datetime(2021, 1, 14, 13, 10, 20, tzinfo=utc)

        # Emitente
        emitente = ManifestoEmitente(
            cpfcnpj="99999999000199",  # cnpj apenas números
            inscricao_estadual="9999999999",  # numero de IE da empresa
            razao_social="NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL",
            nome_fantasia="Nome Fantasia da Empresa",
            endereco_logradouro="RUA UM",
            endereco_numero="111",
            endereco_complemento=None,
            endereco_bairro="CENTRO",
            endereco_municipio="CUIABA",
            endereco_cep="78118000",
            endereco_uf="MT",
            endereco_telefone="65999662821",
        )

        # Totais
        totais = ManifestoTotais(qCTe=0, qNFe=2, vCarga=1000, cUnid="KG", qCarga=5000)

        # Municípios de carregamento
        carregamento = ManifestoMunicipioCarrega(
            cMunCarrega="5105101", xMunCarrega="JUARA"
        )

        # modal Rodo
        condutor_1 = ManifestoCondutor(
            nome_motorista="JOAO DA SILVA", cpf_motorista="12345678912"
        )
        condutor_2 = ManifestoCondutor(
            nome_motorista="JOSE DA SILVA", cpf_motorista="12345678911"
        )

        veiculo_tracao = []
        veiculo_tracao.append(
            ManifestoVeiculoTracao(
                cInt="001",
                placa="ABC1234",
                RENAVAM="123456789",
                tara=Decimal("5000"),
                capKG=Decimal("4500"),
                capM3=Decimal("400"),
                proprietario=None,
                condutor=[condutor_1, condutor_2],
                tpRod="01",
                tpCar="02",
                UF="MT",
            )
        )

        contratante = ManifestoContratante(
            nome="JOAO DA SILVA",
            cpfcnpj="12345678912",
            NroContrato="q26393479sakjd231234",
            vContratoGlobal=Decimal("2342.64"),
        )

        modal_rodoviario = ManifestoRodoviario(
            rntrc=None,
            ciot=[],
            pedagio=[],
            contratante=[contratante],
            pagamento=None,
            veiculo_tracao=veiculo_tracao,
            veiculo_reboque=[],
        )

        # Manifesto
        manifesto = Manifesto(
            uf="MT",
            tipo_emitente=2,  # 1=Transportadora; 2=Carga própria; 3=CTe Globalizado
            tipo_transportador=0,  # 0=nenhum; 1=etc; 2=tac; 3=ctc
            modelo=58,
            serie="920",
            numero_mdfe="1",
            modal=1,
            data_emissao=data_emissao,
            forma_emissao="1",  # 1=Emissão normal (não em contingência);
            processo_emissao="0",  # 0=Emissão de NF-e com aplicativo do contribuinte;
            UFIni="MT",
            UFFim="MT",
            infMunCarrega=[carregamento],
            infPercurso=[],
            dhIniViagem=data_viagem,
            emitente=emitente,
            modal_rodoviario=modal_rodoviario,
            totais=totais,
            informacoes_complementares_interesse_contribuinte="Mensagem complementar",
        )

        # Documentos vinculados
        nfe = ManifestoDocumentosNFe(
            chave_acesso_nfe="51180917060943000102550010001445371002594517"
        )

        manifesto.adicionar_documentos(
            cMunDescarga="5102637",
            xMunDescarga="Campo Novo do Parecis",
            documentos_nfe=[nfe],
            documentos_cte=[],
        )

        # Informações do Seguro
        averbacao = ManifestoAverbacao(numero="00000000000000000000000")

        manifesto.adicionar_seguradora(
            responsavel_seguro="1",
            cnpj_responsavel="75512177000176",
            nome_seguradora="TESTE SEGURADORA SA",
            cnpj_seguradora="75512177000176",
            numero_apolice="00000",
            averbacoes=[averbacao],
        )

        # Produto Predominante
        manifesto.adicionar_produto(
            tipo_carga="01",
            nome_produto="Descricao do Produto",
            cean="78967142344650",
            ncm="01012100",
        )

        # Responsável técnico
        manifesto.adicionar_responsavel_tecnico(
            cnpj="99999999000199",
            contato="Teste PyNFe",
            email="pynfe@pynfe.io",
            fone="11912341234",
        )

    def serializa_mdfe(self):
        serializador = SerializacaoMDFe(_fonte_dados, homologacao=self.homologacao)
        return serializador.exportar()

    def assina_xml(self):
        a1 = AssinaturaA1(self.certificado, self.senha)
        assina = a1.assinar(self.xml)

        # Gera e adiciona o qrcode no xml
        return SerializacaoQrcodeMDFe().gerar_qrcode(assina)

    def validacao_com_xsd_do_xml_gerado_sem_processar(self):
        self.validacao.validar_etree(
            xml_doc=self.xml_assinado, xsd_file=self.xsd_mdfe, use_assert=True
        )

    def grupo_ide_test(self):
        cUF = self.xml_assinado.xpath("//ns:ide/ns:cUF", namespaces=self.ns)[0].text
        tpAmb = self.xml_assinado.xpath("//ns:ide/ns:tpAmb", namespaces=self.ns)[0].text
        tpEmit = self.xml_assinado.xpath("//ns:ide/ns:tpEmit", namespaces=self.ns)[
            0
        ].text
        mod = self.xml_assinado.xpath("//ns:ide/ns:mod", namespaces=self.ns)[0].text
        serie = self.xml_assinado.xpath("//ns:ide/ns:serie", namespaces=self.ns)[0].text
        nMDF = self.xml_assinado.xpath("//ns:ide/ns:nMDF", namespaces=self.ns)[0].text
        # cMDF = self.xml_assinado.xpath('//ns:ide/ns:cMDF', namespaces=self.ns)[0].text
        # cDV = self.xml_assinado.xpath('//ns:ide/ns:cDV', namespaces=self.ns)[0].text
        modal = self.xml_assinado.xpath("//ns:ide/ns:modal", namespaces=self.ns)[0].text
        dhEmi = self.xml_assinado.xpath("//ns:ide/ns:dhEmi", namespaces=self.ns)[0].text
        tpEmis = self.xml_assinado.xpath("//ns:ide/ns:tpEmis", namespaces=self.ns)[
            0
        ].text
        procEmi = self.xml_assinado.xpath("//ns:ide/ns:procEmi", namespaces=self.ns)[
            0
        ].text
        verProc = self.xml_assinado.xpath("//ns:ide/ns:verProc", namespaces=self.ns)[
            0
        ].text
        UFIni = self.xml_assinado.xpath("//ns:ide/ns:UFIni", namespaces=self.ns)[0].text
        UFFim = self.xml_assinado.xpath("//ns:ide/ns:UFFim", namespaces=self.ns)[0].text
        dhIniViagem = self.xml_assinado.xpath(
            "//ns:ide/ns:dhIniViagem", namespaces=self.ns
        )[0].text

        self.assertEqual(cUF, "51")
        self.assertEqual(tpAmb, "2")
        self.assertEqual(tpEmit, "2")
        self.assertEqual(mod, "58")
        self.assertEqual(serie, "920")
        self.assertEqual(nMDF, "1")
        # self.assertEqual(cMDF, '39925068')
        # self.assertEqual(cDV, '7')
        self.assertEqual(modal, "1")
        self.assertEqual(dhEmi, "2021-01-14T12:00:00+00:00")
        self.assertEqual(tpEmis, "1")
        self.assertEqual(procEmi, "0")
        self.assertEqual(verProc, "PyNFe 0.4")
        self.assertEqual(UFIni, "MT")
        self.assertEqual(UFFim, "SP")
        self.assertEqual(dhIniViagem, "2021-01-14T13:10:20+00:00")

    def grupo_ide_sem_rntrc_test(self):
        cUF = self.xml_assinado.xpath("//ns:ide/ns:cUF", namespaces=self.ns)[0].text
        tpAmb = self.xml_assinado.xpath("//ns:ide/ns:tpAmb", namespaces=self.ns)[0].text
        tpEmit = self.xml_assinado.xpath("//ns:ide/ns:tpEmit", namespaces=self.ns)[
            0
        ].text
        mod = self.xml_assinado.xpath("//ns:ide/ns:mod", namespaces=self.ns)[0].text
        serie = self.xml_assinado.xpath("//ns:ide/ns:serie", namespaces=self.ns)[0].text
        nMDF = self.xml_assinado.xpath("//ns:ide/ns:nMDF", namespaces=self.ns)[0].text
        modal = self.xml_assinado.xpath("//ns:ide/ns:modal", namespaces=self.ns)[0].text
        dhEmi = self.xml_assinado.xpath("//ns:ide/ns:dhEmi", namespaces=self.ns)[0].text
        tpEmis = self.xml_assinado.xpath("//ns:ide/ns:tpEmis", namespaces=self.ns)[
            0
        ].text
        procEmi = self.xml_assinado.xpath("//ns:ide/ns:procEmi", namespaces=self.ns)[
            0
        ].text
        verProc = self.xml_assinado.xpath("//ns:ide/ns:verProc", namespaces=self.ns)[
            0
        ].text
        UFIni = self.xml_assinado.xpath("//ns:ide/ns:UFIni", namespaces=self.ns)[0].text
        UFFim = self.xml_assinado.xpath("//ns:ide/ns:UFFim", namespaces=self.ns)[0].text
        dhIniViagem = self.xml_assinado.xpath(
            "//ns:ide/ns:dhIniViagem", namespaces=self.ns
        )[0].text

        self.assertEqual(cUF, "51")
        self.assertEqual(tpAmb, "2")
        self.assertEqual(tpEmit, "2")
        self.assertEqual(mod, "58")
        self.assertEqual(serie, "920")
        self.assertEqual(nMDF, "1")
        self.assertEqual(modal, "1")
        self.assertEqual(dhEmi, "2021-01-14T12:00:00+00:00")
        self.assertEqual(tpEmis, "1")
        self.assertEqual(procEmi, "0")
        self.assertEqual(verProc, "PyNFe 0.4")
        self.assertEqual(UFIni, "MT")
        self.assertEqual(UFFim, "MT")
        self.assertEqual(dhIniViagem, "2021-01-14T13:10:20+00:00")

    def grupo_municipio_carregamento(self):
        cMunCarrega_1 = self.xml_assinado.xpath(
            "//ns:ide/ns:infMunCarrega/ns:cMunCarrega", namespaces=self.ns
        )[0].text
        xMunCarrega_1 = self.xml_assinado.xpath(
            "//ns:ide/ns:infMunCarrega/ns:xMunCarrega", namespaces=self.ns
        )[0].text

        cMunCarrega_2 = self.xml_assinado.xpath(
            "//ns:ide/ns:infMunCarrega/ns:cMunCarrega", namespaces=self.ns
        )[1].text
        xMunCarrega_2 = self.xml_assinado.xpath(
            "//ns:ide/ns:infMunCarrega/ns:xMunCarrega", namespaces=self.ns
        )[1].text

        self.assertEqual(cMunCarrega_1, "5105101")
        self.assertEqual(xMunCarrega_1, "JUARA")

        self.assertEqual(cMunCarrega_2, "5107925")
        self.assertEqual(xMunCarrega_2, "SORRISO")

    def grupo_municipio_carregamento_sem_rntrc(self):
        cMunCarrega_1 = self.xml_assinado.xpath(
            "//ns:ide/ns:infMunCarrega/ns:cMunCarrega", namespaces=self.ns
        )[0].text
        xMunCarrega_1 = self.xml_assinado.xpath(
            "//ns:ide/ns:infMunCarrega/ns:xMunCarrega", namespaces=self.ns
        )[0].text

        self.assertEqual(cMunCarrega_1, "5105101")
        self.assertEqual(xMunCarrega_1, "JUARA")

    def grupo_percurso(self):
        UFPer_1 = self.xml_assinado.xpath(
            "//ns:ide/ns:infPercurso/ns:UFPer", namespaces=self.ns
        )[0].text
        UFPer_2 = self.xml_assinado.xpath(
            "//ns:ide/ns:infPercurso/ns:UFPer", namespaces=self.ns
        )[1].text

        self.assertEqual(UFPer_1, "MS")
        self.assertEqual(UFPer_2, "GO")

    def grupo_emitente(self):
        CNPJ = self.xml_assinado.xpath("//ns:emit/ns:CNPJ", namespaces=self.ns)[0].text
        IE = self.xml_assinado.xpath("//ns:emit/ns:IE", namespaces=self.ns)[0].text
        xNome = self.xml_assinado.xpath("//ns:emit/ns:xNome", namespaces=self.ns)[
            0
        ].text
        xFant = self.xml_assinado.xpath("//ns:emit/ns:xFant", namespaces=self.ns)[
            0
        ].text
        xLgr = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:xLgr", namespaces=self.ns
        )[0].text
        nro = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:nro", namespaces=self.ns
        )[0].text
        xBairro = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:xBairro", namespaces=self.ns
        )[0].text
        cMun = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:cMun", namespaces=self.ns
        )[0].text
        xMun = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:xMun", namespaces=self.ns
        )[0].text
        CEP = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:CEP", namespaces=self.ns
        )[0].text
        UF = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:UF", namespaces=self.ns
        )[0].text
        fone = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:fone", namespaces=self.ns
        )[0].text
        email = self.xml_assinado.xpath(
            "//ns:emit/ns:enderEmit/ns:email", namespaces=self.ns
        )

        self.assertEqual(CNPJ, "99999999000199")
        self.assertEqual(IE, "9999999999")
        self.assertEqual(
            xNome, "NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL"
        )
        self.assertEqual(xFant, "Nome Fantasia da Empresa")
        self.assertEqual(xLgr, "RUA UM")
        self.assertEqual(nro, "111")
        self.assertEqual(xBairro, "CENTRO")
        self.assertEqual(cMun, "5103403")
        self.assertEqual(xMun, "CUIABA")
        self.assertEqual(CEP, "78118000")
        self.assertEqual(UF, "MT")
        self.assertEqual(fone, "65999662821")
        if email:
            self.assertEqual(email[0].text, "teste@gmail.com")

    def grupo_inf_antt(self):
        RNTRC = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:RNTRC", namespaces=self.ns
        )[0].text
        self.assertEqual(RNTRC, "12345678")

    def grupo_ciot(self):
        CIOT = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infCIOT/ns:CIOT", namespaces=self.ns
        )[0].text
        CPF = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infCIOT/ns:CPF", namespaces=self.ns
        )[0].text

        self.assertEqual(CIOT, "123456789012")
        self.assertEqual(CPF, "75961547191")

    def grupo_pedagio(self):
        CNPJForn = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:valePed/ns:disp/ns:CNPJForn",
            namespaces=self.ns,
        )[0].text
        CPFPg = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:valePed/ns:disp/ns:CPFPg",
            namespaces=self.ns,
        )[0].text
        nCompra = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:valePed/ns:disp/ns:nCompra",
            namespaces=self.ns,
        )[0].text
        vValePed = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:valePed/ns:disp/ns:vValePed",
            namespaces=self.ns,
        )[0].text

        self.assertEqual(CNPJForn, "17060943000102")
        self.assertEqual(CPFPg, "75961547191")
        self.assertEqual(nCompra, "789")
        self.assertEqual(vValePed, "2.64")

    def grupo_contratante(self):
        xNome_1 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infContratante/ns:xNome",
            namespaces=self.ns,
        )[0].text
        CPF_1 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infContratante/ns:CPF",
            namespaces=self.ns,
        )[0].text
        NroContrato_1 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infContratante/ns:infContrato/ns:NroContrato",
            namespaces=self.ns,
        )[0].text
        vContratoGlobal_1 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infContratante/ns:infContrato/ns:vContratoGlobal",
            namespaces=self.ns,
        )[0].text
        self.assertEqual(xNome_1, "JOAO DA SILVA")
        self.assertEqual(CPF_1, "12345678912")
        self.assertEqual(NroContrato_1, "q26393479sakjd231234")
        self.assertEqual(vContratoGlobal_1, "2342.64")

        xNome_2 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infContratante/ns:xNome",
            namespaces=self.ns,
        )[1].text
        CPF_2 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infContratante/ns:CPF",
            namespaces=self.ns,
        )[1].text
        self.assertEqual(xNome_2, "JOSE DA SILVA")
        self.assertEqual(CPF_2, "12345678911")

    def grupo_contratante_sem_rntrc(self):
        xNome_1 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infContratante/ns:xNome",
            namespaces=self.ns,
        )[0].text
        CPF_1 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infContratante/ns:CPF",
            namespaces=self.ns,
        )[0].text
        NroContrato_1 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infContratante/ns:infContrato/ns:NroContrato",
            namespaces=self.ns,
        )[0].text
        vContratoGlobal_1 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:infANTT/ns:infContratante/ns:infContrato/ns:vContratoGlobal",
            namespaces=self.ns,
        )[0].text
        self.assertEqual(xNome_1, "JOAO DA SILVA")
        self.assertEqual(CPF_1, "12345678912")
        self.assertEqual(NroContrato_1, "q26393479sakjd231234")
        self.assertEqual(vContratoGlobal_1, "2342.64")

    def grupo_veiculos_reboque(self):
        cInt = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicReboque/ns:cInt", namespaces=self.ns
        )[1].text
        placa = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicReboque/ns:placa", namespaces=self.ns
        )[1].text
        RENAVAM = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicReboque/ns:RENAVAM", namespaces=self.ns
        )[1].text
        tara = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicReboque/ns:tara", namespaces=self.ns
        )[1].text
        capKG = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicReboque/ns:capKG", namespaces=self.ns
        )[1].text
        capM3 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicReboque/ns:capM3", namespaces=self.ns
        )[1].text
        tpCar = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicReboque/ns:tpCar", namespaces=self.ns
        )[1].text
        UF = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicReboque/ns:UF", namespaces=self.ns
        )[1].text

        self.assertEqual(cInt, "002")
        self.assertEqual(placa, "XYQ4567")
        self.assertEqual(RENAVAM, "123456781")
        self.assertEqual(tara, "4000")
        self.assertEqual(capKG, "3000")
        self.assertEqual(capM3, "300")
        self.assertEqual(tpCar, "02")
        self.assertEqual(UF, "MT")

    def grupo_veiculo_tracao(self):
        cInt = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:cInt", namespaces=self.ns
        )[0].text
        placa = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:placa", namespaces=self.ns
        )[0].text
        RENAVAM = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:RENAVAM", namespaces=self.ns
        )[0].text
        tara = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:tara", namespaces=self.ns
        )[0].text
        capKG = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:capKG", namespaces=self.ns
        )[0].text
        capM3 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:capM3", namespaces=self.ns
        )[0].text

        xNome_0 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:condutor/ns:xNome",
            namespaces=self.ns,
        )[0].text
        CPF_0 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:condutor/ns:CPF", namespaces=self.ns
        )[0].text
        xNome_1 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:condutor/ns:xNome",
            namespaces=self.ns,
        )[1].text
        CPF_1 = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:condutor/ns:CPF", namespaces=self.ns
        )[1].text

        tpRod = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:tpRod", namespaces=self.ns
        )[0].text
        tpCar = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:tpCar", namespaces=self.ns
        )[0].text
        UF = self.xml_assinado.xpath(
            "//ns:infModal/ns:rodo/ns:veicTracao/ns:UF", namespaces=self.ns
        )[0].text

        self.assertEqual(cInt, "001")
        self.assertEqual(placa, "ABC1234")
        self.assertEqual(RENAVAM, "123456789")
        self.assertEqual(tara, "5000")
        self.assertEqual(capKG, "4500")
        self.assertEqual(capM3, "400")
        self.assertEqual(xNome_0, "JOAO DA SILVA")
        self.assertEqual(CPF_0, "12345678912")
        self.assertEqual(xNome_1, "JOSE DA SILVA")
        self.assertEqual(CPF_1, "12345678911")
        self.assertEqual(tpRod, "01")
        self.assertEqual(tpCar, "02")
        self.assertEqual(UF, "MT")

    def grupo_informacoes_documentos_nfe_vinculados(self):
        """
        <infDoc>
            <infMunDescarga>
                <cMunDescarga>3550308</cMunDescarga>
                <xMunDescarga>Sao Paulo</xMunDescarga>
                <infNFe>
                    <chNFe>51180917060943000102550010001445371002594517</chNFe>
                </infNFe>
                <infNFe>
                    <chNFe>51191217060943000102550010001800551003198999</chNFe>
                </infNFe>
            </infMunDescarga>
            <infMunDescarga>
                <cMunDescarga>3530607</cMunDescarga>
                <xMunDescarga>Mogi das Cruzes</xMunDescarga>
                <infNFe>
                    <chNFe>51180917060943000102550010001445371002594517</chNFe>
                </infNFe>
                <infNFe>
                    <chNFe>51191217060943000102550010001800551003198999</chNFe>
                </infNFe>
            </infMunDescarga>
        </infDoc>
        """
        cMunDescarga_0 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:cMunDescarga",
            namespaces=self.ns,
        )[0].text
        xMunDescarga_0 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:xMunDescarga",
            namespaces=self.ns,
        )[0].text
        chNFe_0_0 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:infNFe/ns:chNFe",
            namespaces=self.ns,
        )[0].text
        chNFe_0_1 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:infNFe/ns:chNFe",
            namespaces=self.ns,
        )[1].text

        cMunDescarga_1 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:cMunDescarga",
            namespaces=self.ns,
        )[1].text
        xMunDescarga_1 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:xMunDescarga",
            namespaces=self.ns,
        )[1].text
        chNFe_1_0 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:infNFe/ns:chNFe",
            namespaces=self.ns,
        )[0].text
        chNFe_1_1 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:infNFe/ns:chNFe",
            namespaces=self.ns,
        )[1].text

        self.assertEqual(cMunDescarga_0, "3550308")
        self.assertEqual(xMunDescarga_0, "Sao Paulo")
        self.assertEqual(chNFe_0_0, "51180917060943000102550010001445371002594517")
        self.assertEqual(chNFe_0_1, "51191217060943000102550010001800551003198999")

        self.assertEqual(cMunDescarga_1, "3530607")
        self.assertEqual(xMunDescarga_1, "Mogi das Cruzes")
        self.assertEqual(chNFe_1_0, "51180917060943000102550010001445371002594517")
        self.assertEqual(chNFe_1_1, "51191217060943000102550010001800551003198999")

    def grupo_informacoes_documentos_nfe_vinculados_sem_rntrc(self):
        cMunDescarga = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:cMunDescarga",
            namespaces=self.ns,
        )[0].text
        xMunDescarga = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:xMunDescarga",
            namespaces=self.ns,
        )[0].text
        chNFe = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:infDoc/ns:infMunDescarga/ns:infNFe/ns:chNFe",
            namespaces=self.ns,
        )[0].text

        self.assertEqual(cMunDescarga, "5102637")
        self.assertEqual(xMunDescarga, "Campo Novo do Parecis")
        self.assertEqual(chNFe, "51180917060943000102550010001445371002594517")

    def grupo_seguro_averbacao(self):
        respSeg = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:infResp/ns:respSeg", namespaces=self.ns
        )[0].text
        CNPJ_resp = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:infResp/ns:CNPJ", namespaces=self.ns
        )[0].text

        xSeg = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:infSeg/ns:xSeg", namespaces=self.ns
        )[0].text
        CNPJ_seg = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:infSeg/ns:CNPJ", namespaces=self.ns
        )[0].text

        nApol = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:nApol", namespaces=self.ns
        )[0].text

        nAver_1 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:nAver", namespaces=self.ns
        )[0].text
        nAver_2 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:nAver", namespaces=self.ns
        )[1].text

        self.assertEqual(respSeg, "1")
        self.assertEqual(CNPJ_resp, "75512177000176")
        self.assertEqual(xSeg, "TESTE SEGURADORA SA")
        self.assertEqual(CNPJ_seg, "75512177000176")
        self.assertEqual(nApol, "00000")
        self.assertEqual(nAver_1, "00000000000000000000000")
        self.assertEqual(nAver_2, "11111111111111111111111")

    def grupo_seguro_averbacao_sem_rntrc(self):
        respSeg = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:infResp/ns:respSeg", namespaces=self.ns
        )[0].text
        CNPJ_resp = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:infResp/ns:CNPJ", namespaces=self.ns
        )[0].text

        xSeg = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:infSeg/ns:xSeg", namespaces=self.ns
        )[0].text
        CNPJ_seg = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:infSeg/ns:CNPJ", namespaces=self.ns
        )[0].text

        nApol = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:nApol", namespaces=self.ns
        )[0].text
        nAver_1 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:seg/ns:nAver", namespaces=self.ns
        )[0].text

        self.assertEqual(respSeg, "1")
        self.assertEqual(CNPJ_resp, "75512177000176")
        self.assertEqual(xSeg, "TESTE SEGURADORA SA")
        self.assertEqual(CNPJ_seg, "75512177000176")
        self.assertEqual(nApol, "00000")
        self.assertEqual(nAver_1, "00000000000000000000000")

    def grupo_produto_predominante(self):
        tpCarga = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:prodPred/ns:tpCarga", namespaces=self.ns
        )[0].text
        xProd = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:prodPred/ns:xProd", namespaces=self.ns
        )[0].text
        cEAN = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:prodPred/ns:cEAN", namespaces=self.ns
        )[0].text
        NCM = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:prodPred/ns:NCM", namespaces=self.ns
        )[0].text

        self.assertEqual(tpCarga, "01")
        self.assertEqual(xProd, "Descricao do Produto")
        self.assertEqual(cEAN, "78967142344650")
        self.assertEqual(NCM, "01012100")

    def grupo_totais(self):
        qNFe = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:tot/ns:qNFe", namespaces=self.ns
        )[0].text
        vCarga = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:tot/ns:vCarga", namespaces=self.ns
        )[0].text
        cUnid = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:tot/ns:cUnid", namespaces=self.ns
        )[0].text
        qCarga = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:tot/ns:qCarga", namespaces=self.ns
        )[0].text

        self.assertEqual(qNFe, "2")
        self.assertEqual(vCarga, "1000.00")
        self.assertEqual(cUnid, "01")
        self.assertEqual(qCarga, "5000.0000")

    def grupo_lacres(self):
        nLacre_1 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:lacres/ns:nLacre", namespaces=self.ns
        )[0].text
        nLacre_2 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:lacres/ns:nLacre", namespaces=self.ns
        )[1].text
        nLacre_3 = self.xml_assinado.xpath(
            "//ns:infMDFe/ns:lacres/ns:nLacre", namespaces=self.ns
        )[2].text

        self.assertEqual(nLacre_1, "123")
        self.assertEqual(nLacre_2, "456")
        self.assertEqual(nLacre_3, "789")

    def grupo_responsavel_tecnico(self):
        cnpj = self.xml_assinado.xpath("//ns:infRespTec/ns:CNPJ", namespaces=self.ns)[
            0
        ].text
        contato = self.xml_assinado.xpath(
            "//ns:infRespTec/ns:xContato", namespaces=self.ns
        )[0].text
        email = self.xml_assinado.xpath("//ns:infRespTec/ns:email", namespaces=self.ns)[
            0
        ].text
        fone = self.xml_assinado.xpath("//ns:infRespTec/ns:fone", namespaces=self.ns)[
            0
        ].text

        self.assertEqual(cnpj, "99999999000199")
        self.assertEqual(contato, "Teste PyNFe")
        self.assertEqual(email, "pynfe@pynfe.io")
        self.assertEqual(fone, "11912341234")

    def digestvalue_da_assinatura(self):
        DigestValue = self.xml_assinado.xpath(
            "//ns:Signature/ns:SignedInfo/ns:Reference/ns:DigestValue",
            namespaces=self.ns_sig,
        )[0].text
        self.assertTrue(len(DigestValue) > 0)

    def grupo_qrcode(self):
        qrCodMDFe = self.xml_assinado.xpath(
            "//ns:infMDFeSupl/ns:qrCodMDFe", namespaces=self.ns
        )[0].text
        self.assertTrue(len(qrCodMDFe) > 0)

    def test_manifesto(self):
        # Preenche as classes do pynfe
        self.manifesto = self.preenche_manifesto()

        # Serializa e assina o XML
        self.xml = self.serializa_mdfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_test()
        self.grupo_municipio_carregamento()
        self.grupo_percurso()
        self.grupo_emitente()

        self.grupo_inf_antt()
        self.grupo_ciot()
        self.grupo_pedagio()
        self.grupo_contratante()
        self.grupo_veiculo_tracao()
        self.grupo_veiculos_reboque()

        self.grupo_informacoes_documentos_nfe_vinculados()
        self.grupo_seguro_averbacao()
        self.grupo_produto_predominante()
        self.grupo_totais()
        self.grupo_lacres()

        self.grupo_responsavel_tecnico()
        # self.grupo_qrcode()
        self.digestvalue_da_assinatura()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()

    def test_manifesto_sem_rntrc(self):
        # Preenche as classes do pynfe
        self.manifesto = self.preenche_manifesto_sem_rntrc()

        # Serializa e assina o XML
        self.xml = self.serializa_mdfe()
        self.xml_assinado = self.assina_xml()

        # Teste do conteúdo das tags do XML
        self.grupo_ide_sem_rntrc_test()
        self.grupo_municipio_carregamento_sem_rntrc()
        self.grupo_emitente()

        # self.grupo_inf_antt()  # não tem o grupo infANTT
        self.grupo_contratante_sem_rntrc()
        self.grupo_veiculo_tracao()

        self.grupo_informacoes_documentos_nfe_vinculados_sem_rntrc()
        self.grupo_seguro_averbacao_sem_rntrc()
        self.grupo_produto_predominante()
        self.grupo_totais()

        self.grupo_responsavel_tecnico()
        self.digestvalue_da_assinatura()

        # Testa a validação do XML com os schemas XSD
        self.validacao_com_xsd_do_xml_gerado_sem_processar()


if __name__ == "__main__":
    unittest.main()
