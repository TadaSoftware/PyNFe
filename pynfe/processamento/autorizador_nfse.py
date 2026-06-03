import uuid
from importlib import import_module

from lxml import etree
from pyxb import BIND


class InterfaceAutorizador:
    # TODO Colocar raise Exception Not Implemented nos metodos
    def consultar_rps(self):
        pass

    def cancelar(self):
        pass


class SerializacaoOsasco:
    def __init__(self, chave_autenticacao):
        self.chave_autenticacao = chave_autenticacao

    def consultar(
        self,
        cnpj_tomador=None,
        cpf_tomador=None,
        data_inicial=None,
        data_final=None,
        numero_nota_inicial=None,
        numero_nota_final=None,
        numero_rps_inicial=None,
        numero_rps_final=None,
        numero_rps_unico=None,
    ):
        return {
            "ChaveAutenticacao": self.chave_autenticacao,
            "CNPJTomador": cnpj_tomador,
            "CPFTomador": cpf_tomador,
            "DataInicial": data_inicial,
            "DataFinal": data_final,
            "NumeroNotaInicial": numero_nota_inicial,
            "NumeroNotaFinal": numero_nota_final,
            "NumeroReciboInicial": numero_rps_inicial,
            "NumeroReciboFinal": numero_rps_final,
            "NumeroReciboUnico": numero_rps_unico,
        }


class SerializacaoCampinas(InterfaceAutorizador):
    """
    Serialização ABRASF v2.03 – Campinas
    Retorna SOAP XML (SEM assinatura).
    Assinatura e envio ficam fora.
    """

    def _gerar_id(self, prefixo):
        return f"{prefixo}{uuid.uuid4().hex.upper()}"

    def soap_envelope(
        self,
        metodo,
        xml_assinado,
    ):
        NAMESPACE_SOAP = "http://schemas.xmlsoap.org/soap/envelope/"
        NAMESPACE_XSI = "http://www.w3.org/2001/XMLSchema-instance"
        NAMESPACE_XSD = "http://www.w3.org/2001/XMLSchema"
        NAMESPACE_ABRASF = "http://nfse.abrasf.org.br"

        xml_metodo = etree.Element("{%s}" % NAMESPACE_ABRASF + metodo)
        xml_metodo.append(xml_assinado)
        raiz = etree.Element(
            "{%s}Envelope" % NAMESPACE_SOAP,
            nsmap={
                "xsi": NAMESPACE_XSI,
                "xsd": NAMESPACE_XSD,
                "soap": NAMESPACE_SOAP,
                "nfse": NAMESPACE_ABRASF,
            },
        )
        body = etree.SubElement(raiz, "{%s}Body" % NAMESPACE_SOAP)
        body.append(xml_metodo)

        return etree.tostring(raiz, pretty_print=True).decode()

    def consultar_periodo(self, emitente, data_inicio, data_fim, pagina=1):
        raiz = etree.Element("ConsultarNfseServicoPrestadoEnvio")

        prestador = etree.SubElement(raiz, "Prestador")
        cpf_cnpj = etree.SubElement(prestador, "CpfCnpj")
        etree.SubElement(cpf_cnpj, "Cnpj").text = emitente.cnpj
        etree.SubElement(prestador, "InscricaoMunicipal").text = emitente.inscricao_municipal

        periodo = etree.SubElement(raiz, "PeriodoEmissao")
        etree.SubElement(periodo, "DataInicial").text = data_inicio
        etree.SubElement(periodo, "DataFinal").text = data_fim

        etree.SubElement(raiz, "Pagina").text = str(pagina)

        return etree.tostring(raiz, pretty_print=True).decode()

    def consultar_faixa(self, emitente, numero_inicial, numero_final, pagina=1):
        raiz = etree.Element("ConsultarNfseFaixaEnvio")

        prestador = etree.SubElement(raiz, "Prestador")
        cpf_cnpj = etree.SubElement(prestador, "CpfCnpj")
        etree.SubElement(cpf_cnpj, "Cnpj").text = emitente.cnpj
        etree.SubElement(prestador, "InscricaoMunicipal").text = emitente.inscricao_municipal

        faixa = etree.SubElement(raiz, "Faixa")
        etree.SubElement(faixa, "NumeroNfseInicial").text = str(numero_inicial)
        etree.SubElement(faixa, "NumeroNfseFinal").text = str(numero_final)

        etree.SubElement(raiz, "Pagina").text = str(pagina)

        return etree.tostring(raiz, pretty_print=True).decode()


class SerializacaoSpeedgov(InterfaceAutorizador):
    """
    Serialização ABRASF v1.00 – Speedgov
    """

    def _cabecalho(self):
        cabecalho_xml = """<cabecalho xmlns="http://ws.speedgov.com.br/cabecalho_v1.xsd" versao="1"><versaoDados xmlns="">1</versaoDados></cabecalho>""".strip()
        return cabecalho_xml

    def soap_envelope(
        self,
        metodo,
        xml_envio,
    ):
        NAMESPACE_SOAP = "http://schemas.xmlsoap.org/soap/envelope/"
        NAMESPACE_ABRASF = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

        ns_metodo = {
            "ConsultarNfse": "http://ws.speedgov.com.br/consultar_nfse_envio_v1.xsd",
        }

        envelope = etree.Element(
            "{http://schemas.xmlsoap.org/soap/envelope/}Envelope",
            nsmap={
                "soapenv": NAMESPACE_SOAP,
                "nfse": NAMESPACE_ABRASF,
                "consult": ns_metodo[metodo],
            },
        )
        etree.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Header")
        body = etree.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")

        consultar_nfse = etree.SubElement(body, "{%s}" % NAMESPACE_ABRASF + metodo)

        header = etree.SubElement(consultar_nfse, "header")
        header.text = etree.CDATA(self._cabecalho())

        parameters = etree.SubElement(consultar_nfse, "parameters")
        parameters.text = etree.CDATA(xml_envio)

        return etree.tostring(envelope, pretty_print=True).decode()

    def consultar_periodo(self, emitente, data_inicio, data_fim):
        NAMESPACE_SPEEDGOV_CONSULTAR_NFSE_ENVIO = (
            "http://ws.speedgov.com.br/consultar_nfse_envio_v1.xsd"
        )
        raiz = etree.Element(
            "{%s}ConsultarNfseEnvio" % NAMESPACE_SPEEDGOV_CONSULTAR_NFSE_ENVIO,
        )

        prestador = etree.SubElement(raiz, "Prestador")
        etree.SubElement(prestador, "Cnpj").text = emitente.cnpj
        etree.SubElement(prestador, "InscricaoMunicipal").text = emitente.inscricao_municipal

        periodo = etree.SubElement(raiz, "PeriodoEmissao")
        etree.SubElement(periodo, "DataInicial").text = data_inicio
        etree.SubElement(periodo, "DataFinal").text = data_fim

        return etree.tostring(raiz, pretty_print=True).decode()


class SerializacaoGiss(InterfaceAutorizador):
    """
    Serialização ABRASF v2.04 – GISS
    """

    NAMESPACE_SOAP = "http://schemas.xmlsoap.org/soap/envelope/"
    NAMESPACE_XSI = "http://www.w3.org/2001/XMLSchema-instance"
    NAMESPACE_XSD = "http://www.w3.org/2001/XMLSchema"
    NAMESPACE_ABRASF = "http://nfse.abrasf.org.br"
    NAMESPACE_METODO = "http://www.giss.com.br/consultar-nfse-servico-prestado-envio-v2_04.xsd"
    NAMESPACE_TIPOS = "http://www.giss.com.br/tipos-v2_04.xsd"
    NAMESPACE_CABECALHO = "http://www.giss.com.br/cabecalho-v2_04.xsd"

    def _cabecalho(self):
        cabecalho_xml = f"""<cabecalho xmlns="{self.NAMESPACE_CABECALHO}" versao="2.04"><versaoDados>2.04</versaoDados></cabecalho>""".strip()
        return cabecalho_xml

    def soap_envelope(
        self,
        metodo,
        xml_assinado,
    ):
        NAMESPACE_SOAP = "http://schemas.xmlsoap.org/soap/envelope/"
        NAMESPACE_XSI = "http://www.w3.org/2001/XMLSchema-instance"
        NAMESPACE_XSD = "http://www.w3.org/2001/XMLSchema"
        NAMESPACE_ABRASF = "http://nfse.abrasf.org.br"

        envelope = etree.Element(
            f"{{{self.NAMESPACE_SOAP}}}Envelope",
            nsmap={
                "xsi": NAMESPACE_XSI,
                "xsd": NAMESPACE_XSD,
                "soap": NAMESPACE_SOAP,
                "nfse": NAMESPACE_ABRASF,
            },
        )
        body = etree.SubElement(envelope, f"{{{self.NAMESPACE_SOAP}}}Body")

        consultar_nfse = etree.SubElement(
            body, f"{{{self.NAMESPACE_ABRASF}}}{metodo}Request"
        )

        header = etree.SubElement(consultar_nfse, "nfseCabecMsg")
        header.text = etree.CDATA(self._cabecalho())

        parameters = etree.SubElement(consultar_nfse, "nfseDadosMsg")
        parameters.text = etree.CDATA(xml_assinado)

        return (
            '<?xml version="1.0" encoding="utf-8"?>'
            + etree.tostring(envelope, pretty_print=True).decode()
        )

    def consultar_periodo(self, emitente, data_inicio, data_fim, pagina=1):
        return f"""<ConsultarNfseServicoPrestadoEnvio
            xmlns="{self.NAMESPACE_METODO}"
            xmlns:tipos="{self.NAMESPACE_TIPOS}">

            <Prestador>
                <tipos:CpfCnpj>
                <tipos:Cnpj>{emitente.cnpj}</tipos:Cnpj>
                </tipos:CpfCnpj>
                <tipos:InscricaoMunicipal>{emitente.inscricao_municipal}</tipos:InscricaoMunicipal>
            </Prestador>
            <PeriodoCompetencia>
                <DataInicial>{data_inicio}</DataInicial>
                <DataFinal>{data_fim}</DataFinal>
            </PeriodoCompetencia>
            <Pagina>{pagina}</Pagina>
        </ConsultarNfseServicoPrestadoEnvio>""".strip()


class SerializacaoBetha(InterfaceAutorizador):
    def __init__(self):
        # importa
        global nfse_schema
        nfse_schema = import_module("pynfe.utils.nfse.betha.nfse_v202")

    def gerar(self, nfse):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        servico = nfse_schema.tcDadosServico()
        valores_servico = nfse_schema.tcValoresDeclaracaoServico()
        valores_servico.ValorServicos = nfse.servico.valor_servico

        servico.IssRetido = nfse.servico.iss_retido
        servico.ItemListaServico = nfse.servico.item_lista
        servico.Discriminacao = nfse.servico.discriminacao
        servico.CodigoMunicipio = nfse.servico.codigo_municipio
        servico.ExigibilidadeISS = nfse.servico.exigibilidade
        servico.MunicipioIncidencia = nfse.servico.municipio_incidencia
        servico.Valores = valores_servico

        # Prestador
        id_prestador = nfse_schema.tcIdentificacaoPrestador()
        id_prestador.CpfCnpj = nfse.emitente.cnpj
        id_prestador.InscricaoMunicipal = nfse.emitente.inscricao_municipal

        # Cliente
        id_tomador = nfse_schema.tcIdentificacaoTomador()
        id_tomador.CpfCnpj = nfse.cliente.numero_documento
        if nfse.cliente.inscricao_municipal:
            id_tomador.InscricaoMunicipal = nfse.cliente.inscricao_municipal

        endereco_tomador = nfse_schema.tcEndereco()
        endereco_tomador.Endereco = nfse.cliente.endereco_logradouro
        endereco_tomador.Numero = nfse.cliente.endereco_numero
        endereco_tomador.Bairro = nfse.cliente.endereco_bairro
        endereco_tomador.CodigoMunicipio = nfse.cliente.endereco_cod_municipio
        endereco_tomador.Uf = nfse.cliente.endereco_uf
        endereco_tomador.CodigoPais = nfse.cliente.endereco_pais
        endereco_tomador.Cep = nfse.cliente.endereco_cep

        tomador = nfse_schema.tcDadosTomador()
        tomador.IdentificacaoPrestador = id_tomador
        tomador.RazaoSocial = nfse.cliente.razao_social
        tomador.Endereco = endereco_tomador

        id_rps = nfse_schema.tcIdentificacaoRps()
        id_rps.Numero = nfse.identificador
        id_rps.Serie = nfse.serie
        id_rps.Tipo = nfse.tipo

        rps = nfse_schema.tcInfRps()
        rps.IdentificacaoRps = id_rps
        rps.DataEmissao = nfse.data_emissao.strftime("%Y-%m-%d")
        rps.Status = 1

        inf_declaracao_servico = nfse_schema.tcInfDeclaracaoPrestacaoServico()
        inf_declaracao_servico.Competencia = nfse.data_emissao.strftime("%Y-%m-%d")
        inf_declaracao_servico.Servico = servico
        inf_declaracao_servico.Prestador = id_prestador
        inf_declaracao_servico.Tomador = tomador
        inf_declaracao_servico.OptanteSimplesNacional = nfse.simples
        inf_declaracao_servico.IncentivoFiscal = nfse.incentivo
        inf_declaracao_servico.Id = nfse.identificador
        inf_declaracao_servico.Rps = rps

        declaracao_servico = nfse_schema.tcDeclaracaoPrestacaoServico()
        declaracao_servico.InfDeclaracaoPrestacaoServico = inf_declaracao_servico

        gnfse = nfse_schema.GerarNfseEnvio()
        gnfse.Rps = declaracao_servico

        gnfse = (
            gnfse.toxml(encoding="utf-8", element_name="GerarNfseEnvio")
            .replace("ns1:", "")
            .replace(":ns1", "")
            .replace('<?xml version="1.0" ?>', "")
        )

        return gnfse

    def consultar_rps(self, nfse):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        # Rps
        id_rps = nfse_schema.tcIdentificacaoRps()
        id_rps.Numero = nfse.identificador
        id_rps.Serie = nfse.serie
        id_rps.Tipo = nfse.tipo

        # Prestador
        id_prestador = nfse_schema.tcIdentificacaoPrestador()
        id_prestador.CpfCnpj = nfse.emitente.cnpj
        id_prestador.InscricaoMunicipal = nfse.emitente.inscricao_municipal

        consulta = nfse_schema.ConsultarNfseRpsEnvio()
        consulta.IdentificacaoRps = id_rps
        consulta.Prestador = id_prestador

        consulta = (
            consulta.toxml(encoding="utf-8", element_name="ConsultarNfseRpsEnvio")
            .replace("ns1:", "")
            .replace(":ns1", "")
            .replace('<?xml version="1.0" ?>', "")
        )

        return consulta

    def consultar_faixa(self, emitente, inicio, fim, pagina):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        # Prestador
        id_prestador = nfse_schema.tcIdentificacaoPrestador()
        id_prestador.CpfCnpj = emitente.cnpj
        id_prestador.InscricaoMunicipal = emitente.inscricao_municipal

        consulta = nfse_schema.ConsultarNfseFaixaEnvio()
        consulta.Prestador = id_prestador
        consulta.Pagina = pagina
        # É necessário BIND antes de atribuir numero final e numero inicial
        consulta.Faixa = BIND()
        consulta.Faixa.NumeroNfseInicial = inicio
        consulta.Faixa.NumeroNfseFinal = fim

        consulta = (
            consulta.toxml(encoding="utf-8", element_name="ConsultarNfseFaixaEnvio")
            .replace("ns1:", "")
            .replace(":ns1", "")
            .replace('<?xml version="1.0" ?>', "")
        )

        return consulta

    def cancelar(self, nfse):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        # id nfse
        id_nfse = nfse_schema.tcIdentificacaoNfse()
        id_nfse.Numero = nfse.identificador
        id_nfse.CpfCnpj = nfse.emitente.cnpj
        id_nfse.InscricaoMunicipal = nfse.emitente.inscricao_municipal
        id_nfse.CodigoMunicipio = nfse.emitente.endereco_cod_municipio

        # Info Pedido de cancelamento
        info_pedido = nfse_schema.tcInfPedidoCancelamento()
        info_pedido.Id = "1"
        info_pedido.IdentificacaoNfse = id_nfse
        # pedido.CodigoCancelamento =

        # Pedido
        pedido = nfse_schema.tcPedidoCancelamento()
        pedido.InfPedidoCancelamento = info_pedido

        # Cancelamento
        cancelar = nfse_schema.CancelarNfseEnvio()
        cancelar.Pedido = pedido

        return cancelar.toxml(encoding="utf-8", element_name="CancelarNfseEnvio")

    def serializar_lote_sincrono(self, nfse):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        servico = nfse_schema.tcDadosServico()
        valores_servico = nfse_schema.tcValoresDeclaracaoServico()
        valores_servico.ValorServicos = nfse.servico.valor_servico

        servico.IssRetido = nfse.servico.iss_retido
        servico.ItemListaServico = nfse.servico.item_lista
        servico.Discriminacao = nfse.servico.discriminacao
        servico.CodigoMunicipio = nfse.servico.codigo_municipio
        servico.ExigibilidadeISS = nfse.servico.exigibilidade
        servico.MunicipioIncidencia = nfse.servico.municipio_incidencia
        servico.Valores = valores_servico

        # Prestador
        id_prestador = nfse_schema.tcIdentificacaoPrestador()
        id_prestador.CpfCnpj = nfse.emitente.cnpj
        id_prestador.InscricaoMunicipal = nfse.emitente.inscricao_municipal

        # Cliente
        id_tomador = nfse_schema.tcIdentificacaoTomador()
        id_tomador.CpfCnpj = nfse.cliente.numero_documento
        if nfse.cliente.inscricao_municipal:
            id_tomador.InscricaoMunicipal = nfse.cliente.inscricao_municipal

        endereco_tomador = nfse_schema.tcEndereco()
        endereco_tomador.Endereco = nfse.cliente.endereco_logradouro
        endereco_tomador.Numero = nfse.cliente.endereco_numero
        endereco_tomador.Bairro = nfse.cliente.endereco_bairro
        endereco_tomador.CodigoMunicipio = nfse.cliente.endereco_cod_municipio
        endereco_tomador.Uf = nfse.cliente.endereco_uf
        endereco_tomador.CodigoPais = nfse.cliente.endereco_pais
        endereco_tomador.Cep = nfse.cliente.endereco_cep

        tomador = nfse_schema.tcDadosTomador()
        tomador.IdentificacaoPrestador = id_tomador
        tomador.RazaoSocial = nfse.cliente.razao_social
        tomador.Endereco = endereco_tomador

        id_rps = nfse_schema.tcIdentificacaoRps()
        id_rps.Numero = nfse.identificador
        id_rps.Serie = nfse.serie
        id_rps.Tipo = nfse.tipo

        rps = nfse_schema.tcInfRps()
        rps.IdentificacaoRps = id_rps
        rps.DataEmissao = nfse.data_emissao.strftime("%Y-%m-%d")
        rps.Status = 1

        inf_declaracao_servico = nfse_schema.tcInfDeclaracaoPrestacaoServico()
        inf_declaracao_servico.Competencia = nfse.data_emissao.strftime("%Y-%m-%d")
        inf_declaracao_servico.Servico = servico
        inf_declaracao_servico.Prestador = id_prestador
        inf_declaracao_servico.Tomador = tomador
        inf_declaracao_servico.OptanteSimplesNacional = nfse.simples
        inf_declaracao_servico.IncentivoFiscal = nfse.incentivo
        inf_declaracao_servico.Id = nfse.identificador
        inf_declaracao_servico.Rps = rps

        declaracao_servico = nfse_schema.tcDeclaracaoPrestacaoServico()
        declaracao_servico.InfDeclaracaoPrestacaoServico = inf_declaracao_servico

        lote = nfse_schema.tcLoteRps()
        lote.NumeroLote = 1
        lote.Id = 1
        lote.CpfCnpj = nfse.emitente.cnpj
        lote.InscricaoMunicipal = nfse.emitente.inscricao_municipal
        lote.QuantidadeRps = 1
        if nfse.autorizador.upper() == "BETHA":
            lote.versao = "2.02"
        lote.ListaRps = BIND(declaracao_servico)

        gnfse = nfse_schema.EnviarLoteRpsSincronoEnvio()
        gnfse.LoteRps = lote

        return gnfse.toxml(encoding="utf-8", element_name="EnviarLoteRpsSincronoEnvio")


class SerializacaoGinfes(InterfaceAutorizador):
    def __init__(self):
        pass
    

    def consultar_periodo(self, emitente, data_inicio, data_fim, pagina=1):
        NS = "http://www.ginfes.com.br/servico_consultar_nfse_servico_prestado_envio_v03.xsd"
        DS = "http://www.w3.org/2000/09/xmldsig#"

        nsmap = {None: NS, "ds": DS}

        root = etree.Element(f"{{{NS}}}ConsultarNfseServicoPrestadoEnvio", nsmap=nsmap)

        # ID obrigatório (antes da assinatura)
        root.attrib["Id"] = f"CNFSESP{uuid.uuid4().hex.upper()}"

        # Prestador
        prestador = etree.SubElement(root, f"{{{NS}}}Prestador")
        cpf_cnpj = etree.SubElement(prestador, f"{{{NS}}}CpfCnpj")
        etree.SubElement(cpf_cnpj, f"{{{NS}}}Cnpj").text = emitente.cnpj
        etree.SubElement(prestador, f"{{{NS}}}InscricaoMunicipal").text = (
            emitente.inscricao_municipal
        )

        # Período
        periodo = etree.SubElement(root, f"{{{NS}}}PeriodoEmissao")
        etree.SubElement(periodo, f"{{{NS}}}DataInicial").text = data_inicio
        etree.SubElement(periodo, f"{{{NS}}}DataFinal").text = data_fim

        # Página
        etree.SubElement(root, f"{{{NS}}}Pagina").text = str(pagina)

        return etree.tostring(root, encoding="utf-8", xml_declaration=True)

    def consultar_faixa(self, emitente, numero_inicial, numero_final, pagina=1):
        NS = "http://www.ginfes.com.br/servico_consultar_nfse_faixa_envio_v03.xsd"
        DS = "http://www.w3.org/2000/09/xmldsig#"

        nsmap = {None: NS, "ds": DS}

        root = etree.Element(f"{{{NS}}}ConsultarNfseFaixaEnvio", nsmap=nsmap)

        # Id obrigatório (ANTES da assinatura)
        root.attrib["Id"] = f"CNFSEFAIXA{uuid.uuid4().hex.upper()}"

        # Prestador
        prestador = etree.SubElement(root, f"{{{NS}}}Prestador")
        cpf_cnpj = etree.SubElement(prestador, f"{{{NS}}}CpfCnpj")
        etree.SubElement(cpf_cnpj, f"{{{NS}}}Cnpj").text = emitente.cnpj
        etree.SubElement(prestador, f"{{{NS}}}InscricaoMunicipal").text = (
            emitente.inscricao_municipal
        )

        # Faixa
        faixa = etree.SubElement(root, f"{{{NS}}}Faixa")
        etree.SubElement(faixa, f"{{{NS}}}NumeroNfseInicial").text = str(numero_inicial)
        etree.SubElement(faixa, f"{{{NS}}}NumeroNfseFinal").text = str(numero_final)

        # Página
        etree.SubElement(root, f"{{{NS}}}Pagina").text = str(pagina)

        return etree.tostring(root, encoding="utf-8", xml_declaration=True)

    def cabecalho(self):
        NS = "http://www.ginfes.com.br/cabecalho_v03.xsd"

        nsmap = {None: NS}

        cabecalho = etree.Element(f"{{{NS}}}cabecalho", nsmap=nsmap)
        cabecalho.attrib["versao"] = "3"
        versao_dados = etree.SubElement(cabecalho, f"{{{NS}}}versaoDados")
        versao_dados.text = "3"

        return etree.tostring(cabecalho, encoding="utf-8", xml_declaration=True)
