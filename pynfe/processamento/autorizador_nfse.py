try:
    from pynfe.utils.nfse.betha import nfse_v202 as nfse_schema
    from pyxb import BIND
except:
    pass  # modulo necessario apenas para NFS-e.


class SerializacaoAutorizador():
    pass


class SerializacaoBetha(SerializacaoAutorizador):
    def __init__(self):
        if 'nfse_schema' not in globals():
            raise ImportError('No module named nfse_v202 or PyXB')

    def serializar_gerar(self, nfse):
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

    def _serializar_lote_sincrono(self, nfse):
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

    def _serializar_emitente(self, emitente, tag_raiz='Prestador', retorna_string=False):
        raiz = etree.Element(tag_raiz)
        documento = etree.SubElement(raiz, 'CpfCnpj')
        etree.SubElement(documento, 'Cnpj').text = emitente.cnpj
        etree.SubElement(raiz, 'InscricaoMunicipal').text = emitente.inscricao_municipal

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_cliente(self, cliente, tag_raiz='Tomador', retorna_string=False):
        raiz = etree.Element(tag_raiz)
        identificacao = etree.SubElement(raiz, 'IdentificacaoTomador')
        documento = etree.SubElement(identificacao, 'CpfCnpj')
        etree.SubElement(documento, cliente.tipo_documento).text = cliente.numero_documento         # Apenas Cnpj ??
        etree.SubElement(identificacao, 'InscricaoMunicipal').text = cliente.inscricao_municipal    # obrigatório??
        etree.SubElement(raiz, 'RazaoSocial').text = cliente.razao_social
        endereco = etree.SubElement(raiz, 'Endereco')
        etree.SubElement(endereco, 'Endereco').text = cliente.endereco_logradouro
        etree.SubElement(endereco, 'Numero').text = cliente.endereco_numero
        if cliente.endereco_complemento:
            etree.SubElement(endereco, 'Complemento').text = cliente.endereco_complemento
        etree.SubElement(endereco, 'Bairro').text = cliente.endereco_bairro
        etree.SubElement(endereco, 'CodigoMunicipio').text = obter_codigo_por_municipio(
            cliente.endereco_municipio, cliente.endereco_uf)
        etree.SubElement(endereco, 'Uf').text = cliente.endereco_uf
        etree.SubElement(endereco, 'CodigoPais').text = cliente.endereco_pais
        etree.SubElement(endereco, 'Cep').text = so_numeros(cliente.endereco_cep)
        contato = etree.SubElement(raiz, 'Contato')
        etree.SubElement(contato, 'Telefone').text = cliente.endereco_telefone
        etree.SubElement(contato, 'Email').text = cliente.email

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_servico(self, servico, tag_raiz='Servico', retorna_string=False):
        raiz = etree.Element(tag_raiz)
        valores = etree.SubElement(raiz, 'Valores')
        etree.SubElement(valores, 'ValorServicos').text = str('{:.2f}').format(servico.valor_servico)
        etree.SubElement(raiz, 'IssRetido').text = str(servico.iss_retido)
        #etree.SubElement(raiz, 'ResponsavelRetencao').text = ''
        etree.SubElement(raiz, 'ItemListaServico').text = servico.item_lista
        #etree.SubElement(raiz, 'CodigoCnae').text = ''
        #etree.SubElement(raiz, 'CodigoTributacaoMunicipio').text = ''
        etree.SubElement(raiz, 'Discriminacao').text = servico.discriminacao
        etree.SubElement(raiz, 'CodigoMunicipio').text = servico.codigo_municipio
        #etree.SubElement(raiz, 'CodigoPais').text = ''
        """
        1 – Exigível;
        2 – Não incidência;
        3 – Isenção;
        4 – Exportação;
        5 – Imunidade;
        6 – Exigibilidade Suspensa por Decisão Judicial;
        7 – Exigibilidade Suspensa por ProcessoAdministrativo
        """
        etree.SubElement(raiz, 'ExigibilidadeISS').text = str(servico.exigibilidade)
        etree.SubElement(raiz, 'MunicipioIncidencia').text = servico.codigo_municipio
        #etree.SubElement(raiz, 'NumeroProcesso').text = ''

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_gerar(self, nfse, tag_raiz='GerarNfseEnvio', retorna_string=False):

        if nfse.autorizador.upper() == 'BETHA':
            raiz = etree.Element(tag_raiz, xmlns=NAMESPACE_BETHA)
        # TODO - implementar outros sistemas autorizadores
        else:
            raiz = etree.Element(tag_raiz)
        rps = etree.SubElement(raiz, 'Rps')
        info = etree.SubElement(rps, 'InfDeclaracaoPrestacaoServico', Id=nfse.identificador)
        etree.SubElement(info, 'Competencia').text = nfse.data_emissao.strftime('%Y-%m-%d')

        # Servico
        info.append(self._serializar_servico(nfse.servico))
        # Emitente/Prestador
        info.append(self._serializar_emitente(nfse.emitente))
        # Cliente/Tomador
        info.append(self._serializar_cliente(nfse.cliente))

        etree.SubElement(info, 'OptanteSimplesNacional').text = str(nfse.simples)   # 1-Sim; 2-Não
        etree.SubElement(info, 'IncentivoFiscal').text = str(nfse.incentivo)        # 1-Sim; 2-Não

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz

    def _serializar_consulta(self, nfse, tag_raiz='ConsultarNfseRpsEnvio', retorna_string=False):
        if nfse.autorizador.upper() == 'BETHA':
           namespace = NAMESPACE_BETHA
           #versao = '2.02'
        raiz = etree.Element(tag_raiz, xmlns=namespace)
        identificacao = etree.SubElement(raiz, 'IdentificacaoRps')
        etree.SubElement(identificacao, 'Numero').text = str(nfse.identificador)
        etree.SubElement(identificacao, 'Serie').text = nfse.serie
        etree.SubElement(identificacao, 'Tipo').text = nfse.tipo
        raiz.append(self._serializar_emitente(nfse.emitente))

        if retorna_string:
            return etree.tostring(raiz, encoding="unicode", pretty_print=True)
        else:
            return raiz
