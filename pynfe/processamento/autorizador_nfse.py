from pyxb import BIND
from importlib import import_module


class InterfaceAutorizador():
    #TODO Colocar raise Exception Not Implemented nos metodos
    def consultar_rps(self):
        pass

    def cancelar(self):
        pass


class SerializacaoBetha(InterfaceAutorizador):
    def __init__(self):
        # importa
        global nfse_schema
        nfse_schema = import_module('pynfe.utils.nfse.betha.nfse_v202')

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
        rps.DataEmissao = nfse.data_emissao.strftime('%Y-%m-%d')
        rps.Status = 1

        inf_declaracao_servico = nfse_schema.tcInfDeclaracaoPrestacaoServico()
        inf_declaracao_servico.Competencia = nfse.data_emissao.strftime('%Y-%m-%d')
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

        return gnfse.toxml(element_name='GerarNfseEnvio')

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

        consulta = consulta.toxml(element_name='ConsultarNfseRpsEnvio').replace('ns1:','').replace(':ns1','').replace('<?xml version="1.0" ?>','')

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

        consulta = consulta.toxml(element_name='ConsultarNfseFaixaEnvio').replace('ns1:','').replace(':ns1','').replace('<?xml version="1.0" ?>','')

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
        info_pedido.Id = '1'
        info_pedido.IdentificacaoNfse = id_nfse
        #pedido.CodigoCancelamento =

        # Pedido
        pedido = nfse_schema.tcPedidoCancelamento()
        pedido.InfPedidoCancelamento = info_pedido

        # Cancelamento
        cancelar = nfse_schema.CancelarNfseEnvio()
        cancelar.Pedido = pedido

        return cancelar.toxml(element_name='CancelarNfseEnvio')

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
        rps.DataEmissao = nfse.data_emissao.strftime('%Y-%m-%d')
        rps.Status = 1

        inf_declaracao_servico = nfse_schema.tcInfDeclaracaoPrestacaoServico()
        inf_declaracao_servico.Competencia = nfse.data_emissao.strftime('%Y-%m-%d')
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
        if nfse.autorizador.upper() == 'BETHA':
            lote.versao = '2.02'
        lote.ListaRps = BIND(declaracao_servico)

        gnfse = nfse_schema.EnviarLoteRpsSincronoEnvio()
        gnfse.LoteRps = lote

        return gnfse.toxml(element_name='EnviarLoteRpsSincronoEnvio')


class SerializacaoGinfes(InterfaceAutorizador):
    def __init__(self):
        # importa
        global _tipos, servico_consultar_nfse_envio_v03
        global servico_enviar_lote_rps_envio_v03, cabecalho_v03
        _tipos = import_module('pynfe.utils.nfse.ginfes._tipos')
        servico_consultar_nfse_envio_v03 = import_module('pynfe.utils.nfse.ginfes.servico_consultar_nfse_envio_v03')
        servico_enviar_lote_rps_envio_v03 = import_module('pynfe.utils.nfse.ginfes.servico_enviar_lote_rps_envio_v03')
        cabecalho_v03 = import_module('pynfe.utils.nfse.ginfes.cabecalho_v03')

    def consultar_rps(self, nfse):
        """Retorna string de um XML de consulta por Rps gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        # Rps
        id_rps = _tipos.tcIdentificacaoRps()
        id_rps.Numero = nfse.identificador
        id_rps.Serie = nfse.serie
        id_rps.Tipo = nfse.tipo

        # Prestador
        id_prestador = _tipos.tcIdentificacaoPrestador()
        id_prestador.CpfCnpj = nfse.emitente.cnpj
        id_prestador.InscricaoMunicipal = nfse.emitente.inscricao_municipal

        consulta = servico_consultar_nfse_rps_envio_v03.ConsultarNfseRpsEnvio()
        consulta.IdentificacaoRps = id_rps
        consulta.Prestador = id_prestador

        consulta = consulta.toxml(element_name='ConsultarNfseRpsEnvio')

        return consulta

    def consultar_nfse(self, emitente, numero=None, inicio=None, fim=None):
        # Prestador
        id_prestador = _tipos.tcIdentificacaoPrestador()
        id_prestador.Cnpj = emitente.cnpj
        id_prestador.InscricaoMunicipal = emitente.inscricao_municipal

        consulta = servico_consultar_nfse_envio_v03.ConsultarNfseEnvio()
        consulta.Prestador = id_prestador
        # Consulta por Numero
        if numero is not None:
            consulta.NumeroNfse = numero
        else:
            # consulta por Data
            consulta.PeriodoEmissao = BIND()
            consulta.PeriodoEmissao.DataInicial = inicio
            consulta.PeriodoEmissao.DataFinal = fim

        return consulta.toxml(element_name='ns1:ConsultarNfseEnvio')

    def serializar_lote_assincrono(self, nfse):
        "Serializa lote de envio, baseado no servico_enviar_lote_rps_envio_v03.xsd"

        servico = _tipos.tcDadosServico()
        valores_servico = _tipos.tcValores()
        valores_servico.ValorServicos = nfse.servico.valor_servico
        valores_servico.IssRetido = nfse.servico.iss_retido

        servico.Valores = valores_servico
        servico.ItemListaServico = nfse.servico.item_lista
        ## dois campos opcionais aqui no meio se der errado # TODO retirar
        servico.Discriminacao = nfse.servico.discriminacao
        servico.CodigoMunicipio = nfse.servico.codigo_municipio

        # endereco tomador
        endereco_tomador = _tipos.tcEndereco()
        endereco_tomador.Endereco = nfse.cliente.endereco_logradouro
        endereco_tomador.Numero = nfse.cliente.endereco_numero
        endereco_tomador.Bairro = nfse.cliente.endereco_bairro
        endereco_tomador.CodigoMunicipio = nfse.cliente.endereco_cod_municipio
        endereco_tomador.Uf = nfse.cliente.endereco_uf
        endereco_tomador.Cep = nfse.cliente.endereco_cep
        # identificacao Tomador
        id_tomador = _tipos.tcIdentificacaoTomador()
        id_tomador.CpfCnpj = nfse.cliente.numero_documento
        if nfse.cliente.inscricao_municipal:
            id_tomador.InscricaoMunicipal = nfse.cliente.inscricao_municipal
        # Tomador
        tomador = _tipos.tcDadosTomador()
        tomador.IdentificacaoTomador = id_tomador
        tomador.RazaoSocial = nfse.cliente.razao_social
        tomador.Endereco = endereco_tomador

        # Prestador
        id_prestador = _tipos.tcIdentificacaoPrestador()
        id_prestador.Cnpj = nfse.emitente.cnpj
        id_prestador.InscricaoMunicipal = nfse.emitente.inscricao_municipal

        # identificacao rps
        id_rps = _tipos.tcIdentificacaoRps()
        id_rps.Numero = nfse.identificador
        id_rps.Serie = nfse.serie
        id_rps.Tipo = nfse.tipo
        # inf rps
        inf_rps = _tipos.tcInfRps()
        inf_rps.IdentificacaoRps = id_rps
        inf_rps.DataEmissao = nfse.data_emissao.strftime('%Y-%m-%dT%H:%M:%S')
        inf_rps.NaturezaOperacao = 1  # tributacao no municipio
        inf_rps.RegimeEspecialTributacao = None  # opcional
        inf_rps.OptanteSimplesNacional = nfse.simples
        inf_rps.IncentivadorCultural = 2  # Nao
        inf_rps.Status = 1
        inf_rps.RpsSubstituido = None  # opcional
        inf_rps.Servico = servico
        inf_rps.Prestador = id_prestador
        inf_rps.Tomador = tomador
        inf_rps.IntermediarioServico = None  # opcional
        inf_rps.ConstrucaoCivil = None  # opcional
        inf_rps.Id = nfse.identificador

        rps = _tipos.tcRps()
        rps.InfRps = inf_rps

        lote = _tipos.tcLoteRps()
        lote.NumeroLote = 1
        lote.Id = 1
        lote.Cnpj = nfse.emitente.cnpj
        lote.InscricaoMunicipal = nfse.emitente.inscricao_municipal
        lote.QuantidadeRps = 1
        lote.ListaRps = BIND()
        lote.ListaRps.append(rps)

        enviarLote = servico_enviar_lote_rps_envio_v03.EnviarLoteRpsEnvio()
        enviarLote.LoteRps = lote
        return enviarLote.toxml(element_name='ns1:EnviarLoteRpsEnvio')

    def cabecalho(self):
        # info
        cabecalho = cabecalho_v03.cabecalho()
        cabecalho.versao = '3'
        cabecalho.versaoDados = '3'
        return cabecalho.toxml(element_name='cabecalho')
