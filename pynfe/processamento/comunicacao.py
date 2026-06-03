# -*- coding: utf-8 -*-
import datetime
import html
import re

import requests
from pynfe.entidades.certificado import CertificadoA1
from pynfe.utils import etree, obter_municipio_por_codigo, so_numeros
from pynfe.utils.flags import (
    CODIGOS_ESTADOS,
    MODELO_MDFE,
    NAMESPACE_CTE,
    NAMESPACE_CTE_METODO,
    NAMESPACE_MDFE,
    NAMESPACE_MDFE_METODO,
    NAMESPACE_METODO,
    NAMESPACE_NFCOM,
    NAMESPACE_NFCOM_METODO,
    NAMESPACE_NFE,
    NAMESPACE_SOAP,
    NAMESPACE_XSD,
    NAMESPACE_XSI,
    VERSAO_CTE,
    VERSAO_MDFE,
    VERSAO_NFCOM,
    VERSAO_PADRAO,
)
from pynfe.utils.webservices import CTE, MDFE, NFCE, NFCOM, NFE, NFSE

from .assinatura import AssinaturaA1


class Comunicacao(object):
    """
    Classe abstrata responsavel por definir os metodos e logica das classes
    de comunicação com os webservices da NF-e.
    """

    _ambiente = 1  # 1 = Produção, 2 = Homologação
    uf = None
    certificado = None
    certificado_senha = None
    url = None

    def __init__(self, uf, certificado, certificado_senha, homologacao=False):
        self.uf = uf
        self.certificado = certificado
        self.certificado_senha = certificado_senha
        self._ambiente = 2 if homologacao else 1


class ComunicacaoSefaz(Comunicacao):
    """Classe de comunicação que segue o padrão definido para as SEFAZ dos Estados."""

    _versao = VERSAO_PADRAO
    _assinatura = AssinaturaA1

    def autorizacao(
        self, modelo, nota_fiscal, id_lote=1, ind_sinc=1, contingencia=False, timeout=None
    ):
        """
        Método para realizar autorização da nota de acordo com o modelo
        :param modelo: Modelo
        :param nota_fiscal: XML assinado
        :param id_lote: Id do lote - numero autoincremental gerado pelo sistema
        :param ind_sinc: Indicador de sincrono e assincrono, 0 para assincrono, 1 para sincrono
        :param contingencia: Indica se o envio é em contingência ou não
        :return:  Uma tupla que em caso de sucesso, retorna xml com nfe e protocolo de autorização.
        Caso contrário, envia todo o soap de resposta da Sefaz para decisão do usuário.
        """
        # url do serviço
        url = self._get_url(modelo=modelo, consulta="AUTORIZACAO", contingencia=contingencia)

        # Monta XML do corpo da requisição
        raiz = etree.Element("enviNFe", xmlns=NAMESPACE_NFE, versao=VERSAO_PADRAO)
        etree.SubElement(raiz, "idLote").text = str(
            id_lote
        )  # numero autoincremental gerado pelo sistema
        etree.SubElement(raiz, "indSinc").text = str(ind_sinc)  # 0 para assincrono, 1 para sincrono
        raiz.append(nota_fiscal)

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap("NFeAutorizacao4", raiz)
        # Faz request no Servidor da Sefaz
        retorno = self._post(url, xml, timeout)

        # Em caso de sucesso, retorna xml com nfe e protocolo de autorização.
        # Caso contrário, envia todo o soap de resposta da Sefaz para decisão do usuário.
        if retorno.status_code == 200:
            # namespace
            ns = {"ns": NAMESPACE_NFE}
            # Procuta status no xml
            try:
                prot = etree.fromstring(retorno.text)
            except ValueError:
                # em SP retorno.text apresenta erro
                prot = etree.fromstring(retorno.content)
            if ind_sinc == 1:
                try:
                    # Protocolo com envio OK
                    try:
                        inf_prot = prot[0][0]  # root protNFe
                    except IndexError:
                        # Estados como GO vem com a tag header
                        inf_prot = prot[1][0]

                    lote_status = inf_prot.xpath("ns:retEnviNFe/ns:cStat", namespaces=ns)[0].text
                    # Lote processado
                    if lote_status == "104":
                        prot_nfe = inf_prot.xpath("ns:retEnviNFe/ns:protNFe", namespaces=ns)[0]
                        status = prot_nfe.xpath("ns:infProt/ns:cStat", namespaces=ns)[0].text
                        # autorizado usa da NF-e
                        # retorna xml final (protNFe+NFe)
                        if status in ["100", "150"]:
                            raiz = etree.Element(
                                "nfeProc", xmlns=NAMESPACE_NFE, versao=VERSAO_PADRAO
                            )
                            raiz.append(nota_fiscal)
                            raiz.append(prot_nfe)
                            return 0, raiz
                except IndexError:
                    # Protocolo com algum erro no Envio
                    return 1, retorno, nota_fiscal
            else:
                # Retorna id do protocolo para posterior consulta em caso de sucesso.
                rec = prot[0][0]
                status = rec.xpath("ns:retEnviNFe/ns:cStat", namespaces=ns)[0].text
                # Lote Recebido com Sucesso!
                if status == "103":
                    nrec = rec.xpath("ns:retEnviNFe/ns:infRec/ns:nRec", namespaces=ns)[0].text
                    return 0, nrec, nota_fiscal
        return 1, retorno, nota_fiscal

    def consulta_recibo(self, modelo, numero, contingencia=False):
        """
        Este método oferece a consulta do resultado do processamento de um lote de NF-e.
        O aplicativo do Contribuinte deve ser construído de forma a aguardar um tempo mínimo de
        15 segundos entre o envio do Lote de NF-e para processamento e a consulta do resultado
        deste processamento, evitando a obtenção desnecessária do status de erro 105 - "Lote em
        Processamento".
        :param modelo: Modelo da nota
        :param numero: Número da nota
        :param contingencia: Indica se o envio é em contingência ou não
        :return:
        """

        # url do serviço
        url = self._get_url(modelo=modelo, consulta="RECIBO", contingencia=contingencia)

        # Monta XML do corpo da requisição
        raiz = etree.Element("consReciNFe", versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
        etree.SubElement(raiz, "nRec").text = numero

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap("NFeRetAutorizacao4", raiz)
        return self._post(url, xml)

    def consulta_nota(self, modelo, chave, contingencia=False):
        """
            Este método oferece a consulta da situação da NF-e/NFC-e na Base de Dados do Portal
            da Secretaria de Fazenda Estadual.
        :param modelo: Modelo da nota
        :param chave: Chave da nota
        :param contingencia: Indica se o envio é em contingência ou não
        :return:
        """
        # url do serviço
        url = self._get_url(modelo=modelo, consulta="CHAVE", contingencia=contingencia)
        if modelo == "nfcom":
            raiz = etree.Element("consSitNFCom", versao=VERSAO_NFCOM, xmlns=NAMESPACE_NFCOM)
            etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
            etree.SubElement(raiz, "xServ").text = "CONSULTAR"
            etree.SubElement(raiz, "chNFCom").text = chave
            xml = self._construir_xml_soap("NFComConsulta", raiz)
        else:
            # Monta XML do corpo da requisição
            raiz = etree.Element("consSitNFe", versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
            etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
            etree.SubElement(raiz, "xServ").text = "CONSULTAR"
            etree.SubElement(raiz, "chNFe").text = chave
            # Monta XML para envio da requisição
            xml = self._construir_xml_soap("NFeConsultaProtocolo4", raiz)
        return self._post(url, xml)

    def download_nota(self, modelo, chave, contingencia=False):
        """
        Download da NFCom via Portal SVRS (HTML + extração do XML via JS).
        """

        url = self._get_url(modelo=modelo, consulta="DOWNLOAD", contingencia=contingencia)

        if modelo != "nfcom":
            raise NotImplementedError("Download not implemented for this model yet.")

        # validação da chave
        if not chave or not chave.isdigit() or len(chave) != 44:
            raise ValueError("Chave NFCom inválida (esperado 44 dígitos numéricos)")

        certificado_a1 = CertificadoA1(self.certificado)

        try:
            key_path, cert_path = certificado_a1.separar_arquivo(
                self.certificado_senha, caminho=True
            )
            cert = (cert_path, key_path)

            session = requests.Session()

            response = session.post(
                url,
                files={
                    "sistema": (None, "Nfcom"),
                    "OrigemSite": (None, "0"),
                    "Ambiente": (None, str(self._ambiente)),
                    "ChaveAcessoDfe": (None, chave),
                },
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Referer": "https://dfe-portal.svrs.rs.gov.br/Nfcom",
                },
                cert=cert,
                verify=False,
                timeout=30,
            )

            html_body = response.text

            # 🚫 BLOQUEIO POR IP (rate limit)
            if "textoErro" in html_body and "IP não autorizado" in html_body:
                raise PermissionError(
                    "SVRS bloqueou o IP por múltiplas consultas simultâneas. "
                    "Aguarde liberação ou utilize outro IP."
                )

            # 🔍 extrai o XML do JS
            pattern = r'var\s+stringJson\s*=\s*\{\s*"xml"\s*:\s*"(.+?)"\s*\};'
            match = re.search(pattern, html_body, re.DOTALL)

            if not match:
                raise ValueError(
                    "XML não encontrado no HTML retornado pelo portal SVRS. "
                    "Pode ser chave inexistente, ambiente incorreto ou NFCom sem permissão."
                )

            xml_js = match.group(1)

            # remove escapes JavaScript
            xml = bytes(xml_js, "utf-8").decode("unicode_escape")

            # converte entidades HTML (&amp; etc)
            xml = html.unescape(xml)

            return xml.strip()

        finally:
            certificado_a1.excluir()

    def consulta_distribuicao(
        self, cnpj=None, cpf=None, chave=None, nsu=0, consulta_nsu_especifico=False
    ):
        """
        O XML do pedido de distribuição suporta três tipos de consultas
        que são definidas de acordo com a tag informada no XML.

        As tags são distNSU, consNSU e consChNFe:
        a) distNSU – Distribuição de Conjunto de DF-e a Partir do NSU Informado
        b) consNSU – Consulta DF-e Vinculado ao NSU Informado
        c) consChNFe – Consulta de NF-e por Chave de Acesso Informada

        :param cnpj: CNPJ do interessado
        :param cpf: CPF do interessado
        :param chave: Chave da NF-e a ser consultada
        :param nsu: Ultimo nsu ou nsu específico para ser consultado
        :param consulta_nsu_especifico:
            True para consulta por nsu específico
            False para consulta por nsu último
        :return: xml do resultado da consulta

        Exemplos de usos:
        * consChNFe: consulta_distribuicao(cnpj=CNPJ, chave=CHAVE)
        * distNSU: consulta_distribuicao(cnpj=CNPJ, chave=None, nsu=0,
            consulta_nsu_especifico=False)
        * consNSU: consulta_distribuicao(cnpj=CNPJ, chave=None, nsu=10,
            consulta_nsu_especifico=True)
        """

        # url
        url = self._get_url_an(consulta="DISTRIBUICAO")
        # Monta XML para envio da requisição
        raiz = etree.Element("distDFeInt", versao="1.01", xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
        if self.uf:
            etree.SubElement(raiz, "cUFAutor").text = CODIGOS_ESTADOS[self.uf.upper()]
        if cnpj:
            etree.SubElement(raiz, "CNPJ").text = cnpj
        else:
            etree.SubElement(raiz, "CPF").text = cpf

        if not chave and not consulta_nsu_especifico:
            distNSU = etree.SubElement(raiz, "distNSU")
            etree.SubElement(distNSU, "ultNSU").text = str(nsu).zfill(15)
        if chave:
            consChNFe = etree.SubElement(raiz, "consChNFe")
            etree.SubElement(consChNFe, "chNFe").text = chave
        if consulta_nsu_especifico:
            consNSU = etree.SubElement(raiz, "consNSU")
            etree.SubElement(consNSU, "NSU").text = str(nsu).zfill(15)

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap("NFeDistribuicaoDFe", raiz)

        return self._post(url, xml)

    def consulta_cadastro(self, modelo, documento, tipo="CNPJ", uf=None):
        """
        Consulta de cadastro
        :param modelo: Modelo da nota
        :param documento: Documento (CNPJ, CPF ou IE)
        :tipo do documento: CNPJ, CPF, IE
        :param uf: UF
        :return:
        """
        # UF que utilizam a SVRS - Sefaz Virtual do RS:
        lista_svrs = [
            "AC",
            "AL",
            "AP",
            "CE",
            "DF",
            "ES",
            "PA",
            "PB",
            "PI",
            "RJ",
            "RN",
            "RO",
            "RR",
            "SC",
            "SE",
            "TO",
        ]

        # Se não informada UF nos parâmetros da função,
        # utiliza a UF do construtor
        if not uf:
            uf = self.uf

        # RS implementa um método diferente na consulta de cadastro
        # usa o mesmo url para produção e homologação
        # não tem url para NFCE
        if uf.upper() == "RS":
            url = NFE["RS"]["CADASTRO"]
        elif uf.upper() in lista_svrs:
            url = NFE["SVRS"]["CADASTRO"]
        elif uf.upper() == "SVC-RS":
            url = NFE["SVC-RS"]["CADASTRO"]
        else:
            url = self._get_url(modelo=modelo, consulta="CADASTRO")

        raiz = etree.Element("ConsCad", versao="2.00", xmlns=NAMESPACE_NFE)
        info = etree.SubElement(raiz, "infCons")
        etree.SubElement(info, "xServ").text = "CONS-CAD"
        etree.SubElement(info, "UF").text = uf.upper()

        # Monta tipo de documento CNPJ, CPF ou IE
        etree.SubElement(info, tipo.upper()).text = documento

        # etree.SubElement(info, 'CPF').text = cpf

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap("CadConsultaCadastro4", raiz)
        # Chama método que efetua a requisição POST no servidor SOAP
        return self._post(url, xml)

    def evento(self, modelo, evento, id_lote=1):
        """
        Envia um evento de nota fiscal (cancelamento e carta de correção)
        :param modelo: Modelo da nota
        :param evento: Eventro
        :param id_lote: Id do lote
        :return:
        """

        # url do serviço
        try:
            # manifestacao url é do AN
            if evento[0][5].text.startswith("2"):
                url = self._get_url_an(consulta="EVENTOS")
            else:
                url = self._get_url(modelo=modelo, consulta="EVENTOS")
        except Exception:
            url = self._get_url(modelo=modelo, consulta="EVENTOS")

        # Monta XML do corpo da requisição
        raiz = etree.Element("envEvento", versao="1.00", xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, "idLote").text = str(
            id_lote
        )  # numero autoincremental gerado pelo sistema
        raiz.append(evento)
        xml = self._construir_xml_soap("NFeRecepcaoEvento4", raiz)
        return self._post(url, xml)

    def status_servico(self, modelo, timeout=None):
        """
        Verifica status do servidor da receita.
        :param modelo: modelo é a string com tipo de serviço que deseja consultar, Ex: nfe ou nfce
        :return:
        """
        url = self._get_url(modelo, "STATUS")
        # Monta XML do corpo da requisição
        raiz = etree.Element("consStatServ", versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
        etree.SubElement(raiz, "cUF").text = CODIGOS_ESTADOS[self.uf.upper()]
        etree.SubElement(raiz, "xServ").text = "STATUS"
        xml = self._construir_xml_soap("NFeStatusServico4", raiz)
        return self._post(url, xml, timeout)

    def inutilizacao(
        self,
        modelo,
        cnpj,
        numero_inicial,
        numero_final,
        justificativa="",
        ano=None,
        serie="1",
    ):
        """
        Serviço destinado ao atendimento de solicitações de inutilização de numeração.
        :param modelo: Modelo da nota
        :param cnpj: CNPJ ou CPF da empresa
        :param numero_inicial: Número inicial
        :param numero_final: Número final
        :param justificativa: Justificativa
        :param ano: Ano
        :param serie:  Série
        :return:
        """

        # url do servico
        url = self._get_url(modelo=modelo, consulta="INUTILIZACAO")

        # Valores default
        ano = str(ano or datetime.date.today().year)[-2:]
        uf = CODIGOS_ESTADOS[self.uf.upper()]
        cnpj = so_numeros(cnpj)

        if len(cnpj) == 14:
            cnpjcpf_chaveacesso = cnpj
        elif len(cnpj) == 11:
            cnpjcpf_chaveacesso = str(cnpj).zfill(14)

        # Identificador da TAG a ser assinada formada com Código da UF + Ano (2 posições) +
        #  CNPJ + modelo + série + nro inicial e nro final precedida do literal “ID”
        id_unico = "ID%(uf)s%(ano)s%(cnpj)s%(modelo)s%(serie)s%(num_ini)s%(num_fin)s" % {
            "uf": uf,
            "ano": ano,
            "cnpj": cnpjcpf_chaveacesso,
            "modelo": "55" if modelo == "nfe" else "65",  # 55=NF-e; 65=NFC-e;
            "serie": str(serie).zfill(3),
            "num_ini": str(numero_inicial).zfill(9),
            "num_fin": str(numero_final).zfill(9),
        }

        # Monta XML do corpo da requisição # FIXME
        raiz = etree.Element("inutNFe", versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        inf_inut = etree.SubElement(raiz, "infInut", Id=id_unico)
        etree.SubElement(inf_inut, "tpAmb").text = str(self._ambiente)
        etree.SubElement(inf_inut, "xServ").text = "INUTILIZAR"
        etree.SubElement(inf_inut, "cUF").text = uf
        etree.SubElement(inf_inut, "ano").text = ano
        if len(cnpj) == 14:
            etree.SubElement(inf_inut, "CNPJ").text = cnpj
        else:
            etree.SubElement(inf_inut, "CPF").text = cnpj
        etree.SubElement(inf_inut, "mod").text = (
            "55" if modelo == "nfe" else "65"
        )  # 55=NF-e; 65=NFC-e
        etree.SubElement(inf_inut, "serie").text = str(serie)
        etree.SubElement(inf_inut, "nNFIni").text = str(numero_inicial)
        etree.SubElement(inf_inut, "nNFFin").text = str(numero_final)
        etree.SubElement(inf_inut, "xJust").text = justificativa

        # assinatura
        a1 = AssinaturaA1(self.certificado, self.certificado_senha)
        xml = a1.assinar(raiz)

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap("NFeInutilizacao4", xml)
        # Faz request no Servidor da Sefaz e retorna resposta
        return self._post(url, xml)

    def _get_url_an(self, consulta):
        # producao
        if self._ambiente == 1:
            if consulta == "DISTRIBUICAO":
                ambiente = "https://www1."
            else:
                ambiente = "https://www."
        # homologacao
        else:
            ambiente = "https://hom1."

        self.url = ambiente + NFE["AN"][consulta]
        return self.url

    def _get_url(self, modelo, consulta, contingencia=False):
        """Retorna a url para comunicação com o webservice"""
        if contingencia:
            contingencia_svrs = ["AM", "BA", "CE", "GO", "MA", "MS", "MT", "PE", "PR"]
            contingencia_svan = [
                "AC",
                "AL",
                "AP",
                "DF",
                "ES",
                "MG",
                "PA",
                "PB",
                "PI",
                "RJ",
                "RN",
                "RO",
                "RR",
                "RS",
                "SC",
                "SE",
                "SP",
                "TO",
            ]

            if self.uf.upper() in contingencia_svrs:
                if self._ambiente == 1:
                    ambiente = "HTTPS"
                else:
                    ambiente = "HOMOLOGACAO"
                if modelo == "nfe":
                    # nfe Ex: https://nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3
                    self.url = NFE["SVRS"][ambiente] + NFE["SVRS"][consulta]
                elif modelo == "nfce":
                    # nfce Ex: https://homologacao.nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3
                    self.url = NFCE["SVRS"][ambiente] + NFCE["SVRS"][consulta]
                else:
                    raise Exception('Modelo não encontrado! Defina modelo="nfe" ou "nfce"')
            elif self.uf.upper() in contingencia_svan:
                if self._ambiente == 1:
                    ambiente = "HTTPS"
                else:
                    ambiente = "HOMOLOGACAO"
                if modelo == "nfe":
                    # nfe Ex: https://nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3
                    self.url = NFE["SVAN"][ambiente] + NFE["SVAN"][consulta]
                elif modelo == "nfce":
                    # nfce Ex: https://homologacao.nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3
                    self.url = NFCE["SVRS"][ambiente] + NFCE["SVRS"][consulta]
                else:
                    raise Exception('Modelo não encontrado! Defina modelo="nfe" ou "nfce"')
            return self.url

        # estado que implementam webservices proprios
        lista = ["PR", "MS", "SP", "AM", "CE", "BA", "GO", "MG", "MT", "PE", "RS"]
        if self.uf.upper() in lista:
            if self._ambiente == 1:
                ambiente = "HTTPS"
            else:
                ambiente = "HOMOLOGACAO"
            if modelo == "nfe":
                # CE é a única UF que possuem NFE SVRS e NFCe próprio
                if self.uf.upper() == "CE":
                    self.url = NFE["SVRS"][ambiente] + NFE["SVRS"][consulta]
                else:
                    # nfe Ex: https://nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3
                    self.url = NFE[self.uf.upper()][ambiente] + NFE[self.uf.upper()][consulta]
            elif modelo == "nfce":
                # PE e BA são as únicas UF'sque possuem NFE proprio e SVRS para NFCe
                if self.uf.upper() == "PE" or self.uf.upper() == "BA":
                    self.url = NFCE["SVRS"][ambiente] + NFCE["SVRS"][consulta]
                else:
                    # nfce Ex: https://homologacao.nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3
                    self.url = NFCE[self.uf.upper()][ambiente] + NFCE[self.uf.upper()][consulta]
            elif modelo == "nfcom":
                if consulta == "DOWNLOAD":
                    self.url = NFCOM["SVRS"][consulta]
                else:
                    if self.uf.upper() in ["MG", "MT", "MS"]:
                        self.url = (
                            NFCOM[self.uf.upper()][ambiente] + NFCOM[self.uf.upper()][consulta]
                        )
                    else:
                        self.url = NFCOM["SVRS"][ambiente] + NFCOM["SVRS"][consulta]

            else:
                raise Exception('Modelo não encontrado! Defina modelo="nfe" ou "nfce" ou "nfcom"')
        # Estados que utilizam outros ambientes
        else:
            lista_svrs = [
                "AC",
                "AL",
                "AP",
                "DF",
                "ES",
                "PB",
                "PI",
                "RJ",
                "RN",
                "RO",
                "RR",
                "SC",
                "SE",
                "TO",
                "PA",
            ]
            if self.uf.upper() in lista_svrs:
                if self._ambiente == 1:
                    ambiente = "HTTPS"
                else:
                    ambiente = "HOMOLOGACAO"
                if modelo == "nfe":
                    # nfe Ex: https://nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3
                    self.url = NFE["SVRS"][ambiente] + NFE["SVRS"][consulta]
                elif modelo == "nfce":
                    # nfce Ex: https://homologacao.nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3
                    self.url = NFCE["SVRS"][ambiente] + NFCE["SVRS"][consulta]
                elif modelo == "nfcom":
                    self.url = NFCOM["SVRS"][ambiente] + NFCOM["SVRS"][consulta]
                else:
                    raise Exception(
                        'Modelo não encontrado! Defina modelo="nfe" ou "nfce" ou "nfcom"'
                    )
            # unico UF que utiliza SVAN ainda para NF-e
            # SVRS para NFC-e
            elif self.uf.upper() == "MA":
                if self._ambiente == 1:
                    ambiente = "HTTPS"
                else:
                    ambiente = "HOMOLOGACAO"
                if modelo == "nfe":
                    # nfe Ex: https://nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3
                    self.url = NFE["SVAN"][ambiente] + NFE["SVAN"][consulta]
                elif modelo == "nfce":
                    # nfce Ex: https://homologacao.nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3
                    self.url = NFCE["SVRS"][ambiente] + NFCE["SVRS"][consulta]
                elif modelo == "nfcom":
                    self.url = NFCOM["SVRS"][ambiente] + NFCOM["SVRS"][consulta]
                else:
                    raise Exception(
                        'Modelo não encontrado! Defina modelo="nfe" ou "nfce" ou "nfcom"'
                    )
            else:
                raise Exception(f"Url não encontrada para {modelo} e {consulta} {self.uf.upper()}")
        return self.url

    def _construir_xml_soap(self, metodo, dados, cabecalho=False):
        """Monta o XML para o envio via SOAP"""
        raiz = etree.Element(
            "{%s}Envelope" % NAMESPACE_SOAP,
            nsmap={
                "xsi": NAMESPACE_XSI,
                "xsd": NAMESPACE_XSD,
                "soap": NAMESPACE_SOAP,
            },
        )

        body = etree.SubElement(raiz, "{%s}Body" % NAMESPACE_SOAP)

        # === NFe Distribuição ===
        if metodo == "NFeDistribuicaoDFe":
            x = etree.SubElement(body, "nfeDistDFeInteresse", xmlns=NAMESPACE_METODO + metodo)
            a = etree.SubElement(x, "nfeDadosMsg")

        # === Cadastro MT ===
        elif metodo == "CadConsultaCadastro4" and self.uf.upper() == "MT":
            x = etree.SubElement(body, "consultaCadastro", xmlns=NAMESPACE_METODO + metodo)
            a = etree.SubElement(x, "nfeDadosMsg")

        # === NFCOM Consulta ===
        elif metodo == "NFComConsulta":
            a = etree.SubElement(body, "nfcomDadosMsg", xmlns=NAMESPACE_NFCOM_METODO + metodo)

        # === Default (NFe / NFCe / CTe etc) ===
        else:
            a = etree.SubElement(body, "nfeDadosMsg", xmlns=NAMESPACE_METODO + metodo)

        a.append(dados)
        return raiz

    def _post_header(self):
        """Retorna um dicionário com os atributos para o cabeçalho da requisição HTTP"""
        # PE é a única UF que exige SOAPAction no header
        response = {
            "content-type": "application/soap+xml; charset=utf-8;",
            "Accept": "application/soap+xml; charset=utf-8;",
        }
        if self.uf.upper() == "PE":
            response["SOAPAction"] = ""

        return response

    def _post(self, url, xml, timeout=None):
        certificado_a1 = CertificadoA1(self.certificado)
        chave, cert = certificado_a1.separar_arquivo(self.certificado_senha, caminho=True)
        chave_cert = (cert, chave)
        # Abre a conexão HTTPS
        try:
            xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'

            # limpa xml com caracteres bugados para infNFeSupl em NFC-e
            xml = re.sub(
                "<qrCode>(.*?)</qrCode>",
                lambda x: x.group(0).replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", ""),
                etree.tostring(xml, encoding="unicode").replace("\n", ""),
            )
            xml = xml_declaration + xml
            print(xml)
            print("URL:", url)
            # Faz o request com o servidor
            result = requests.post(
                url,
                xml,
                headers=self._post_header(),
                cert=chave_cert,
                verify=False,
                timeout=timeout,
            )
            result.encoding = "utf-8"
            return result
        except requests.exceptions.RequestException as e:
            raise e
        finally:
            certificado_a1.excluir()


class ComunicacaoNfse(Comunicacao):
    """Classe de comunicação que segue o padrão definido para as SEFAZ dos Municípios."""

    _versao = ""
    _namespace = ""

    def __init__(
        self, autorizador, certificado=None, certificado_senha=None, homologacao=False, **kwargs
    ):
        self.certificado = certificado
        self.certificado_senha = certificado_senha
        self._ambiente = 2 if homologacao else 1
        self.autorizador = autorizador.upper()
        if self.autorizador == "GINFES":
            self._namespace = "http://www.ginfes.com.br/cabecalho_v03.xsd"
            self._versao = "3"
        elif self.autorizador == "SAO_PAULO":
            self._namespace = "http://www.prefeitura.sp.gov.br/nfe"
            self._versao = "2"
        elif self.autorizador == "BARUERI":
            self._namespace = "http://www.barueri.sp.gov.br/nfeservice"
        elif self.autorizador == "OSASCO":
            pass
        elif self.autorizador == "CAMPINAS":
            pass
        elif self.autorizador == "SPEEDGOV":
            if not kwargs.get("codigo_municipio"):
                raise Exception(
                    "Para o autorizador SPEEDGOV é necessário informar o código do município."
                )
            self.codigo_municipio = kwargs.get("codigo_municipio")
        elif self.autorizador == "GISS":
            if not kwargs.get("codigo_municipio"):
                raise Exception(
                    "Para o autorizador GISS é necessário informar o código do município."
                )
            self.codigo_municipio = kwargs.get("codigo_municipio")
        else:
            raise Exception("Autorizador não encontrado!")

    def consultar_nfse(self, payload):
        # url do serviço
        url = self._get_url()

        if self.autorizador == "OSASCO":
            # comunica via wsdl
            return self._post_zeep(url, NFSE[self.autorizador]["CONSULTA_COMPLETA"], payload)
        else:
            raise Exception("Este método não esta implementado para o autorizador.")

    def consultar_rps(self, payload):
        # url do serviço
        url = self._get_url()
        if self.autorizador == "CAMPINAS":
            from pynfe.processamento.autorizador_nfse import SerializacaoCampinas

            xml_assinado = AssinaturaA1(self.certificado, self.certificado_senha).assinar(payload)
            envelope_xml = SerializacaoCampinas().soap_envelope(
                NFSE[self.autorizador]["CONSULTA_RPS"], xml_assinado
            )
            return self._post_soap_raw(url, envelope_xml)
        elif self.autorizador == "OSASCO":
            # comunica via wsdl
            return self._post_zeep(url, NFSE[self.autorizador]["CONSULTA"], payload)
        else:
            raise Exception("Este método não esta implementado para o autorizador.")

    def consultar_faixa(self, payload):
        # url do serviço
        url = self._get_url()
        if self.autorizador == "CAMPINAS":
            from pynfe.processamento.autorizador_nfse import SerializacaoCampinas

            xml_assinado = AssinaturaA1(self.certificado, self.certificado_senha).assinar(payload)
            envelope_xml = SerializacaoCampinas().soap_envelope(
                NFSE[self.autorizador]["CONSULTA_FAIXA"], xml_assinado
            )
            return self._post_soap_raw(url, envelope_xml)
        elif self.autorizador == "OSASCO":
            # comunica via wsdl
            return self._post_zeep(url, NFSE[self.autorizador]["CONSULTA"], payload)
        else:
            raise Exception("Este método não esta implementado para o autorizador.")

    def consultar_periodo(self, payload):
        # url do serviço
        url = self._get_url()
        if self.autorizador == "CAMPINAS":
            from pynfe.processamento.autorizador_nfse import SerializacaoCampinas

            xml_assinado = AssinaturaA1(self.certificado, self.certificado_senha).assinar(payload)
            envelope_xml = SerializacaoCampinas().soap_envelope(
                NFSE[self.autorizador]["CONSULTA_SERVICO"], xml_assinado
            )
            return self._post_soap_raw(url, envelope_xml)
        elif self.autorizador == "SPEEDGOV":
            from pynfe.processamento.autorizador_nfse import SerializacaoSpeedgov

            envelope_xml = SerializacaoSpeedgov().soap_envelope(
                NFSE[self.autorizador]["CONSULTA_SERVICO"], payload
            )
            return self._post_soap_raw(url, envelope_xml)
        elif self.autorizador == "GISS":
            from pynfe.processamento.autorizador_nfse import SerializacaoGiss

            xml_assinado = AssinaturaA1(self.certificado, self.certificado_senha).assinar(
                payload, retorna_string=True
            )
            envelope_xml = SerializacaoGiss().soap_envelope(
                NFSE[self.autorizador]["CONSULTA_SERVICO"], xml_assinado
            )
            return self._post_soap_raw(url, envelope_xml)
        elif self.autorizador == "OSASCO":
            # comunica via wsdl
            return self._post_zeep(url, NFSE[self.autorizador]["CONSULTA"], payload)
        elif self.autorizador == "GINFES":
            # xml
            xml = '<?xml version="1.0" encoding="UTF-8"?>' +  payload.decode("utf-8")
            # comunica via wsdl
            return self._post_https(url, xml, "consulta")
        else:
            raise Exception("Este método não esta implementado para o autorizador.")

    def consultar_lote(self, payload):
        raise Exception("Este método não esta implementado para o autorizador.")

    def consultar_situacao_lote(self, payload):
        raise Exception("Este método não esta implementado para o autorizador.")

    def cancelar(self, payload):
        raise Exception("Este método não esta implementado para o autorizador.")

    def _cabecalho(self, retorna_string=True):
        """Monta o XML do cabeçalho da requisição wsdl
        Namespaces padrão homologação (Ginfes)"""

        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
        raiz = etree.Element(
            "{%s}cabecalho" % self._namespace,
            nsmap={"ns2": self._namespace, "xsi": NAMESPACE_XSI},
            versao=self._versao,
        )
        etree.SubElement(raiz, "{%s}versaoDados" % self._namespace).text = self._versao

        if retorna_string:
            cabecalho = etree.tostring(raiz, encoding="unicode", pretty_print=False).replace(
                "\n", ""
            )
            cabecalho = xml_declaration + cabecalho
            return cabecalho
        else:
            return raiz

    def _cabecalho2(self, retorna_string=True):
        """Monta o XML do cabeçalho da requisição wsdl
        Namespaces que funcionaram em produção (Ginfes)"""

        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'

        # cabecalho
        raiz = etree.Element("cabecalho", xmlns=self._namespace, versao=self._versao)
        etree.SubElement(raiz, "versaoDados").text = self._versao

        if retorna_string:
            cabecalho = etree.tostring(raiz, encoding="unicode", pretty_print=False).replace(
                "\n", ""
            )
            cabecalho = xml_declaration + cabecalho
            return cabecalho
        else:
            return raiz

    def _get_url(self):
        """Retorna a url para comunicação com o webservice"""
        if self._ambiente == 1:
            ambiente = "HTTPS"
        elif self._ambiente != 1 and self.autorizador == "SAO_PAULO":
            raise Exception("São Paulo só opera em produção.")
        else:
            ambiente = "HOMOLOGACAO"
        if self.autorizador in NFSE:
            self.url = NFSE[self.autorizador][ambiente]
            if self.autorizador == "GISS":
                municipio = obter_municipio_por_codigo(
                    str(self.codigo_municipio), uf=str(self.codigo_municipio)[:2], normalizado=True
                )
                self.url = self.url.replace("{municipio}", str(municipio.lower()))
            if self.autorizador == "SPEEDGOV":
                self.url = self.url.replace(
                    "{suffix_municipio}",
                    NFSE[self.autorizador]["SUFFIX_MUNICIPIO"][str(self.codigo_municipio)],
                )
        else:
            raise Exception("Autorizador nao encontrado!")
        return self.url

    def _post(self, url, xml, metodo):
        """Comunicação wsdl (http) sem certificado digital"""
        # cabecalho
        cabecalho = self._cabecalho()
        # comunicacao wsdl
        try:
            from suds.client import Client

            cliente = Client(url)
            # gerar nfse
            if metodo == "gerar":
                return cliente.service.GerarNfse(cabecalho, xml)
            elif metodo == "consultaRps":
                return cliente.service.ConsultarNfsePorRps(cabecalho, xml)
            elif metodo == "consultaFaixa":
                return cliente.service.ConsultarNfseFaixa(cabecalho, xml)
            elif metodo == "cancelar":
                return cliente.service.CancelarNfse(cabecalho, xml)
            # TODO outros metodos
            else:
                raise Exception("Método não implementado no autorizador.")
        except Exception as e:
            raise e

    def _post_soap_raw(self, url, soap_xml):
        certificado_a1 = CertificadoA1(self.certificado)
        key, cert = certificado_a1.separar_arquivo(self.certificado_senha, caminho=True)
        return requests.post(
            url,
            data=soap_xml.encode("utf-8"),
            cert=(cert, key),
            verify=False,
            headers={"Content-Type": "text/xml; charset=utf-8"},
        )

    def _post_https(self, url, xml, metodo):
        """Comunicação wsdl (https) utilizando certificado do usuário"""
        # cabecalho
        cabecalho = self._cabecalho()
        # comunicacao wsdl
        try:
            from pynfe.utils.https_nfse import HttpAuthenticated
            from suds.client import Client

            certificadoA1 = CertificadoA1(self.certificado)
            chave, cert = certificadoA1.separar_arquivo(self.certificado_senha, caminho=True)

            cliente = Client(url, transport=HttpAuthenticated(key=chave, cert=cert, endereco=url))

            # gerar nfse
            if metodo == "gerar":
                return cliente.service.GerarNfse(cabecalho, xml)
            elif metodo == "enviar_lote":
                return cliente.service.RecepcionarLoteRpsV3(cabecalho, xml)
            elif metodo == "consulta":
                return cliente.service.ConsultarNfseV3(cabecalho, xml)
            elif metodo == "consulta_lote":
                return cliente.service.ConsultarLoteRpsV3(cabecalho, xml)
            elif metodo == "consulta_situacao_lote":
                return cliente.service.ConsultarSituacaoLoteRpsV3(cabecalho, xml)
            elif metodo == "consultaRps":
                return cliente.service.ConsultarNfsePorRpsV3(cabecalho, xml)
            elif metodo == "consultaFaixa":
                return cliente.service.ConsultarNfseFaixa(cabecalho, xml)
            elif metodo == "cancelar":
                # versão 2
                return cliente.service.CancelarNfse(xml)
                # versão 3
                # return cliente.service.CancelarNfseV3(cabecalho, xml)
            # TODO outros metodos
            else:
                raise Exception("Método não implementado no autorizador.")
        except Exception as e:
            raise e


    def enviar_barueri(self, xml, operation):
        url = self._get_url()

        if not self.autorizador == "BARUERI":
            raise Exception(f"Enviar RPS não implementado para {self.autorizador}")

        return self._post_barueri_requests(url, xml, operation)

    def consultar_rps_barueri(self, xml, operation):
        url = self._get_url()

        if not self.autorizador == "BARUERI":
            raise Exception(f"Consultar RPS não implementado para {self.autorizador}")

        return self._post_barueri_requests(url, xml, operation)

    def baixar_rps_barueri(self, xml, operation):
        url = self._get_url()

        if not self.autorizador == "BARUERI":
            raise Exception(f"Baixar RPS não implementado para {self.autorizador}")

        return self._post_barueri_requests(url, xml, operation)

    def _post_barueri_requests(self, url, xml, operation):
        """
        Comunicação SOAP usando requests diretamente (como NFe)
        Recebe o envelope SOAP completo já montado
        """
        import requests

        certificado_a1 = CertificadoA1(self.certificado)
        try:
            chave, cert = certificado_a1.separar_arquivo(self.certificado_senha, caminho=True)
            chave_cert = (cert, chave)

            if operation == "enviar_rps":
                soap_action = "http://www.barueri.sp.gov.br/nfe/NFeLoteEnviarArquivo"
            elif operation == "consultar_rps":
                soap_action = "http://www.barueri.sp.gov.br/nfe/NFeLoteStatusArquivo"
            elif operation == "listar_rps":
                soap_action = "http://www.barueri.sp.gov.br/nfe/NFeLoteListarArquivos"
            elif operation == "baixar_nfse":
                soap_action = "http://www.barueri.sp.gov.br/nfe/NFeLoteBaixarArquivo"
            else:
                raise Exception(f"Operação {operation} não implementada para Barueri.")

            headers = {"Content-Type": "text/xml; charset=utf-8", "SOAPAction": f'"{soap_action}"'}

            return requests.post(
                url,
                data=xml.encode("utf-8"),
                headers=headers,
                cert=chave_cert,
                verify=False,
                timeout=30,
            )

        except requests.exceptions.RequestException as e:
            raise e
        finally:
            certificado_a1.excluir()

    def _post_barueri_https(self, url, xml, metodo):
        """
        LEGACY: Comunicação wsdl (https) utilizando certificado do usuário
        Este método usa SUDS e não é mais usado pelo Barueri.
        Usar _post_barueri_requests() para Barueri.
        """
        # comunicacao wsdl

        certificadoA1 = CertificadoA1(self.certificado)
        try:
            from pynfe.utils.https_nfse import HttpAuthenticated
            from suds.client import Client

            chave, cert = certificadoA1.separar_arquivo(self.certificado_senha, caminho=True)

            cliente = Client(url, transport=HttpAuthenticated(key=chave, cert=cert, endereco=url))

            # gerar nfse

            if metodo == "enviar_rps":
                return cliente.service.NFeLoteEnviarArquivo(VersaoSchema=1, MensagemXML=xml)
            elif metodo == "consultar_rps":
                return cliente.service.NFeLoteStatusArquivo(VersaoSchema=1, MensagemXML=xml)
            elif metodo == "listar_rps":
                return cliente.service.NFeLoteListarArquivos(VersaoSchema=1, MensagemXML=xml)
            elif metodo == "baixar_nfse":
                return cliente.service.NFeLoteBaixarArquivo(VersaoSchema=1, MensagemXML=xml)
            elif metodo == "cancelar":
                return cliente.service.CancelamentoNFe(VersaoSchema=1, MensagemXML=xml)
            # TODO outros metodos
            else:
                raise Exception(f"Método {metodo} não implementado no autorizador Barueri.")
        except Exception as e:
            raise e
        finally:
            certificadoA1.excluir()

    def enviar_sp(self, xml, operation, versao_schema=2):
        """
        Send XML to São Paulo NFS-e webservice.

        Args:
            xml: XML string to send
            operation: Operation name (enviar_rps, teste_envio_lote_rps, envio_lote_rps, consultar_rps, cancelar)
            versao_schema: Schema version (1 for v1, 2 for v2 - Reforma Tributária 2026)

        Returns:
            WebService response
        """
        url = self._get_url()
        if self.autorizador == "SAO_PAULO":
            return self._post_sp_https(url, xml, operation, versao_schema)
        else:
            raise Exception(f"Enviar RPS não implementado para {self.autorizador}")

    def _post_sp_https(self, url, xml, metodo, versao_schema=2):
        """
        Comunicação wsdl (https) utilizando certificado do usuário.

        According to São Paulo NFS-e manual v3.3.4:
        - VersaoSchema=2: Schema version 2 (Reforma Tributária 2026)

        Args:
            url: WebService URL
            xml: XML message string
            metodo: Method name
            versao_schema: Schema version (1 or 2)
        """
        certificadoA1 = CertificadoA1(self.certificado)
        try:
            from pynfe.utils.https_nfse import HttpAuthenticated
            from suds.client import Client

            chave, cert = certificadoA1.separar_arquivo(self.certificado_senha, caminho=True)

            cliente = Client(url, transport=HttpAuthenticated(key=chave, cert=cert, endereco=url))

            # São Paulo NFS-e WebService methods
            # Manual v3.3.4 section 4.3.1: All methods receive VersaoSchema and MensagemXML
            if metodo == "enviar_rps":
                return cliente.service.EnvioRPS(VersaoSchema=versao_schema, MensagemXML=xml)
            elif metodo == "teste_envio_lote_rps":
                return cliente.service.TesteEnvioLoteRPS(
                    VersaoSchema=versao_schema, MensagemXML=xml
                )
            elif metodo == "envio_lote_rps":
                return cliente.service.EnvioLoteRPS(VersaoSchema=versao_schema, MensagemXML=xml)
            elif metodo == "consultar_rps":
                return cliente.service.ConsultaNFe(VersaoSchema=versao_schema, MensagemXML=xml)
            elif metodo == "cancelar":
                return cliente.service.CancelamentoNFe(VersaoSchema=versao_schema, MensagemXML=xml)
            else:
                raise Exception(f"Método {metodo} não implementado no autorizador São Paulo.")
        except Exception as e:
            raise e
        finally:
            certificadoA1.excluir()

    def _post_zeep(self, wsdl, metodo, payload, wcf_compatibility=True):
        """
        Comunicação wsdl utilizando a biblioteca zeep )
        Recebe o wsdl, o método a ser chamado e o payload (XML ou objeto)
        """
        try:
            import requests
            from zeep import Client
            from zeep.helpers import serialize_object
            from zeep.settings import Settings
            from zeep.transports import Transport

            session = requests.Session()
            session.verify = False

            # certificado A1
            if self.certificado:
                certificadoA1 = CertificadoA1(self.certificado)
                chave, cert = certificadoA1.separar_arquivo(self.certificado_senha, caminho=True)
                session.cert = (cert, chave)

            transport = Transport(session=session, timeout=60)

            settings = Settings(strict=not wcf_compatibility, xml_huge_tree=True)

            client = Client(wsdl=wsdl, transport=transport, settings=settings)

            # DEBUG ÚTIL
            print("SOAP endpoint:", client.service._binding_options["address"])

            if not hasattr(client.service, metodo):
                raise Exception(f"Método {metodo} não existe no WSDL")

            print("Chamando método:", metodo)
            print("payload:", payload)

            service = getattr(client.service, metodo)

            response = service(payload)
            return serialize_object(response)

        finally:
            if self.certificado:
                certificadoA1.excluir()


class ComunicacaoMDFe(Comunicacao):
    MDFE_SITUACAO_JA_ENVIADO = ("100", "101", "132")

    _modelo = MODELO_MDFE
    _namespace = NAMESPACE_MDFE
    _versao = VERSAO_MDFE
    _header = "mdfeCabecMsg"
    _envio_mensagem = "mdfeDadosMsg"
    _retorno_mensagem = "mdfeRecepcaoResult"
    _namespace_metodo = NAMESPACE_MDFE_METODO

    _accept = True
    _soap_action = False
    _namespace_soap = NAMESPACE_SOAP
    _namespace_xsi = NAMESPACE_XSI
    _namespace_xsd = NAMESPACE_XSD
    _soap_version = "soap12"
    _edoc_situacao_ja_enviado = MDFE_SITUACAO_JA_ENVIADO
    _edoc_situacao_arquivo_recebido_com_sucesso = "103"
    _edoc_situacao_lote_processado = "104"
    _edoc_situacao_em_processamento = "105"
    _edoc_situacao_servico_em_operacao = "107"

    consulta_servico_ao_enviar = True
    maximo_tentativas_consulta_recibo = 5

    def autorizacao(self, manifesto, id_lote=1, ind_sinc=1):
        """
        Método para realizar autorização do manifesto
        :param manifesto: XML assinado
        :param id_lote: Id do lote - numero autoincremental gerado pelo sistema
        :param ind_sinc: Indicador de sincrono e assincrono, 0 para assincrono, 1 para sincrono
        :return:  Uma tupla que em caso de sucesso,
            retorna xml com manifesto e protocolo de autorização.
        Caso contrário, envia todo o soap de resposta da Sefaz para decisão do usuário.
        """
        # url do serviço
        if ind_sinc == 0:
            url = self._get_url(consulta="RECEPCAO")
        elif ind_sinc == 1:
            url = self._get_url(consulta="RECEPCAO_SINC")
        else:
            raise "ind_sinc deve ser 0=assincrono ou 1=sincrono"

        # Monta XML do corpo da requisição
        raiz = etree.Element("enviMDFe", xmlns=NAMESPACE_MDFE, versao=VERSAO_MDFE)
        etree.SubElement(raiz, "idLote").text = str(
            id_lote
        )  # numero autoincremental gerado pelo sistema
        # etree.SubElement(raiz, 'indSinc').text = str(ind_sinc)
        # # 0 para assincrono, 1 para sincrono
        raiz.append(manifesto)

        # Monta XML para envio da requisição
        if ind_sinc == 0:
            xml = self._construir_xml_soap("MDFeRecepcao", raiz)
        elif ind_sinc == 1:
            xml = self._construir_xml_soap("MDFeRecepcaoSinc", raiz)

        # Faz request no Servidor da Sefaz
        retorno = self._post(url, xml)

        # Em caso de sucesso, retorna xml com o mdfe e protocolo de autorização.
        # Caso contrário, envia todo o soap de resposta da Sefaz para decisão do usuário.
        if retorno.status_code == 200:
            # namespace
            ns = {"ns": NAMESPACE_MDFE}
            # Procuta status no xml
            try:
                prot = etree.fromstring(retorno.text)
            except ValueError:
                # em SP retorno.text apresenta erro
                prot = etree.fromstring(retorno.content)

            if ind_sinc == 1:
                try:
                    # Protocolo com envio OK
                    inf_prot = prot[1][0]
                    lote_status = inf_prot.xpath("ns:retEnviMDFe/ns:cStat", namespaces=ns)[0].text

                    # Lote processado
                    if lote_status == self._edoc_situacao_lote_processado:
                        prot_mdfe = inf_prot.xpath("ns:retEnviMDFe/ns:protMDFe", namespaces=ns)[0]
                        status = prot_mdfe.xpath("ns:infProt/ns:cStat", namespaces=ns)[0].text

                        # autorizado uso do MDF-e
                        # retorna xml final (protMDFe + MDFe)
                        if status in self._edoc_situacao_ja_enviado:  # if status == '100':
                            raiz = etree.Element(
                                "mdfeProc", xmlns=NAMESPACE_MDFE, versao=VERSAO_MDFE
                            )
                            raiz.append(manifesto)
                            raiz.append(prot_mdfe)
                            return 0, raiz
                except IndexError:
                    # Protocolo com algum erro no Envio
                    return 1, retorno, manifesto
            else:
                # Retorna id do protocolo para posterior consulta em caso de sucesso.
                rec = prot[1][0]
                status = rec.xpath("ns:retEnviMDFe/ns:cStat", namespaces=ns)[0].text
                # Lote Recebido com Sucesso!
                if status in (
                    self._edoc_situacao_arquivo_recebido_com_sucesso,
                    self._edoc_situacao_em_processamento,
                ):
                    nrec = rec.xpath("ns:retEnviMDFe/ns:infRec/ns:nRec", namespaces=ns)[0].text
                    return 0, nrec, manifesto
        return 1, retorno, manifesto

    def status_servico(self):
        url = self._get_url("STATUS")
        # Monta XML do corpo da requisição
        raiz = etree.Element("consStatServMDFe", versao=self._versao, xmlns=NAMESPACE_MDFE)
        etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
        etree.SubElement(raiz, "xServ").text = "STATUS"
        xml = self._construir_xml_soap("MDFeStatusServico", raiz)
        return self._post(url, xml)

    def consulta(self, chave):
        url = self._get_url("CONSULTA")
        # Monta XML do corpo da requisição
        raiz = etree.Element("consSitMDFe", versao=self._versao, xmlns=NAMESPACE_MDFE)
        etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
        etree.SubElement(raiz, "xServ").text = "CONSULTAR"
        etree.SubElement(raiz, "chMDFe").text = chave
        # Monta XML para envio da requisição
        xml = self._construir_xml_soap("MDFeConsulta", raiz)
        return self._post(url, xml)

    def consulta_nao_encerrados(self, cpfcnpj):
        url = self._get_url("NAO_ENCERRADOS")
        # Monta XML do corpo da requisição
        raiz = etree.Element("consMDFeNaoEnc", xmlns=NAMESPACE_MDFE, versao=self._versao)
        etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
        etree.SubElement(raiz, "xServ").text = "CONSULTAR NÃO ENCERRADOS"
        if len(cpfcnpj) == 11:
            etree.SubElement(raiz, "CPF").text = cpfcnpj.zfill(11)
        else:
            etree.SubElement(raiz, "CNPJ").text = cpfcnpj.zfill(14)
        # Monta XML para envio da requisição
        xml = self._construir_xml_soap("MDFeConsNaoEnc", raiz)
        return self._post(url, xml)

    def consulta_recibo(self, numero):
        url = self._get_url("RET_RECEPCAO")
        # Monta XML do corpo da requisição
        raiz = etree.Element("consReciMDFe", versao=self._versao, xmlns=NAMESPACE_MDFE)
        etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
        etree.SubElement(raiz, "nRec").text = numero.zfill(15)
        # Monta XML para envio da requisição
        xml = self._construir_xml_soap("MDFeRetRecepcao", raiz)
        return self._post(url, xml)

    def evento(self, evento):
        """
        Envia eventos do MDFe como:
            Encerramento
            Cancelamento
            Inclusao Condutor
            Inclusao DF-e
            Pagamento Operacao MDF-e
        :param evento: Nome do Evento
        :return:
        """
        # url do serviço
        url = self._get_url("EVENTOS")
        # Monta XML do corpo da requisição
        xml = self._construir_xml_soap("MDFeRecepcaoEvento", evento)
        return self._post(url, xml)

    def _construir_xml_soap(self, metodo, dados):
        """Mota o XML para o envio via SOAP"""

        raiz = etree.Element(
            "{%s}Envelope" % NAMESPACE_SOAP,
            nsmap={
                "xsi": self._namespace_xsi,
                "xsd": self._namespace_xsd,
                self._soap_version: self._namespace_soap,
            },
        )

        if self._header:
            cabecalho = self._cabecalho_soap(metodo)
            c = etree.SubElement(raiz, "{%s}Header" % self._namespace_soap)
            c.append(cabecalho)

        body = etree.SubElement(raiz, "{%s}Body" % self._namespace_soap)

        a = etree.SubElement(body, self._envio_mensagem, xmlns=self._namespace_metodo + metodo)

        # if metodo == 'MDFeRecepcaoSinc':
        #     body_base64 = base64.b16encode(a).decode()

        a.append(dados)
        return raiz

    def _post_header(self, soap_webservice_method=False):
        """Retorna um dicionário com os atributos para o cabeçalho da requisição HTTP"""
        header = {
            b"content-type": b"text/xml; charset=utf-8;",
        }

        # PE é a únca UF que exige SOAPAction no header
        if soap_webservice_method:
            header[b"SOAPAction"] = (self._namespace_metodo + soap_webservice_method).encode(
                "utf-8"
            )

        if self._accept:
            header[b"Accept"] = b"application/soap+xml; charset=utf-8;"

        return header

    def _post(self, url, xml):
        certificado_a1 = CertificadoA1(self.certificado)
        chave, cert = certificado_a1.separar_arquivo(self.certificado_senha, caminho=True)
        chave_cert = (cert, chave)
        # Abre a conexão HTTPS
        try:
            xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'

            # limpa xml com caracteres bugados para infMDFeSupl em NFC-e
            xml = re.sub(
                "<qrCodMDFe>(.*?)</qrCodMDFe>",
                lambda x: x.group(0).replace("&lt;", "<").replace("&gt;", ">").replace("amp;", ""),
                etree.tostring(xml, encoding="unicode").replace("\n", ""),
            )
            xml = xml_declaration + xml
            xml = xml.encode("utf8")  # necessário para o evento "CONSULTAR NÃO ENCERRADOS"

            print(xml)
            print("-" * 20)

            # Faz o request com o servidor
            result = requests.post(
                url,
                xml,
                headers=self._post_header(),
                cert=chave_cert,
                verify=False,
                timeout=50,
            )
            result.encoding = "utf-8"
            return result
        except requests.exceptions.Timeout as e:
            raise e
        except requests.exceptions.RequestException as e:
            raise e
        finally:
            certificado_a1.excluir()

    def _cabecalho_soap(self, metodo):
        """Monta o XML do cabeçalho da requisição SOAP"""

        raiz = etree.Element(self._header, xmlns=self._namespace_metodo + metodo)
        etree.SubElement(raiz, "cUF").text = CODIGOS_ESTADOS[self.uf.upper()]
        etree.SubElement(raiz, "versaoDados").text = "3.00"
        return raiz

    def _get_url(self, consulta):
        # producao
        if self._ambiente == 1:
            ambiente = MDFE["SVRS"]["HTTPS"]
        # homologacao
        else:
            ambiente = MDFE["SVRS"]["HOMOLOGACAO"]

        self.url = ambiente + MDFE["SVRS"][consulta]
        return self.url


class ComunicacaoCTe(Comunicacao):
    """Classe de comunicação que segue o padrão definido para as SEFAZ dos Estados."""

    _versao = VERSAO_CTE
    _assinatura = AssinaturaA1
    _namespace = NAMESPACE_CTE
    _header = "cteCabecMsg"
    _envio_mensagem = "cteDadosMsg"
    _namespace_metodo = NAMESPACE_CTE_METODO
    _accept = False
    _namespace_soap = NAMESPACE_SOAP
    _namespace_xsi = NAMESPACE_XSI
    _namespace_xsd = NAMESPACE_XSD
    _soap_version = "soap"

    def status_servico(self):
        """
        Verifica status do servidor da receita.
        :return:
        """
        url = self._get_url("STATUS")
        # Monta XML do corpo da requisição
        raiz = etree.Element("consStatServCte", versao=self._versao, xmlns=NAMESPACE_CTE)
        etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
        etree.SubElement(raiz, "xServ").text = "STATUS"
        xml = self._construir_xml_soap("CteStatusServico", raiz)
        return self._post(url, xml)

    def consulta_distribuicao(
        self, cnpj=None, cpf=None, chave=None, nsu=0, consulta_nsu_especifico=False
    ):
        """
            O XML do pedido de distribuição suporta três tipos de consultas que são
            definidas de acordo com a tag informada no XML.
            As tags são distNSU, consNSU e consChCTe.
            a) distNSU – Distribuição de Conjunto de DF-e a Partir do NSU Informado
            b) consNSU – Consulta DF-e Vinculado ao NSU Informado
            c) consChCTe – Consulta de NF-e por Chave de Acesso Informada
        :param cnpj: CNPJ do interessado
        :param cpf: CPF do interessado
        :param chave: Chave do CT-e a ser consultada
        :param nsu: Ultimo nsu ou nsu específico para ser consultado.
        :param consulta_nsu_especifico:
            True para consulta por nsu específico
            False para consulta por nsu último
        :return: xml do resultado da consulta

        Exemplos de usos:
        * consChNFe: consulta_distribuicao(cnpj=CNPJ, chave=CHAVE)
        * distNSU: consulta_distribuicao(cnpj=CNPJ, chave=None, nsu=0,
            consulta_nsu_especifico=False)
        * consNSU: consulta_distribuicao(cnpj=CNPJ, chave=None, nsu=10,
            consulta_nsu_especifico=True)
        """

        # url
        url = self._get_url_an(consulta="DISTRIBUICAO")
        # Monta XML para envio da requisição
        raiz = etree.Element("distDFeInt", versao="1.00", xmlns=NAMESPACE_CTE)
        etree.SubElement(raiz, "tpAmb").text = str(self._ambiente)
        if self.uf:
            etree.SubElement(raiz, "cUFAutor").text = CODIGOS_ESTADOS[self.uf.upper()]
        if cnpj:
            etree.SubElement(raiz, "CNPJ").text = cnpj
        else:
            etree.SubElement(raiz, "CPF").text = cpf

        if not chave and not consulta_nsu_especifico:
            distNSU = etree.SubElement(raiz, "distNSU")
            etree.SubElement(distNSU, "ultNSU").text = str(nsu).zfill(15)
        if chave:
            consChCTe = etree.SubElement(raiz, "consChCTe")
            etree.SubElement(consChCTe, "chCTe").text = chave
        if consulta_nsu_especifico:
            consNSU = etree.SubElement(raiz, "consNSU")
            etree.SubElement(consNSU, "NSU").text = str(nsu).zfill(15)

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap("CTeDistribuicaoDFe", raiz)
        return self._post(url, xml)

    def _get_url_an(self, consulta):
        ambiente = "https://www1."  # produção
        if self._ambiente == 2:  # homologacao
            ambiente = "https://hom1."

        self.url = ambiente + CTE["AN"][consulta]
        return self.url

    def _cabecalho_soap(self, metodo):
        """Monta o XML do cabeçalho da requisição SOAP"""

        raiz = etree.Element(self._header, xmlns=self._namespace_metodo + metodo)
        etree.SubElement(raiz, "cUF").text = CODIGOS_ESTADOS[self.uf.upper()]
        etree.SubElement(raiz, "versaoDados").text = "3.00"
        return raiz

    def _get_url(self, consulta):
        """Retorna a url para comunicação com o webservice"""

        # Estados que implementam webservices proprios
        lista = ["MT", "MS", "MG", "PR", "RS", "SP"]
        if self.uf.upper() in lista:
            if self._ambiente == 1:
                ambiente = "HTTPS"
            else:
                ambiente = "HOMOLOGACAO"
            self.url = CTE[self.uf.upper()][ambiente] + CTE[self.uf.upper()][consulta]

        # Estados que utilizam outros ambientes
        else:
            lista_svrs = [
                "AC",
                "AL",
                "AM",
                "BA",
                "CE",
                "DF",
                "ES",
                "GO",
                "MA",
                "PA",
                "PB",
                "PI",
                "RJ",
                "RN",
                "RO",
                "SC",
                "SE",
                "TO",
            ]
            lista_svsp = ["AP", "PE", "RR"]

            # SVRS
            if self.uf.upper() in lista_svrs:
                if self._ambiente == 1:
                    ambiente = "HTTPS"
                else:
                    ambiente = "HOMOLOGACAO"
                self.url = CTE["SVRS"][ambiente] + CTE["SVRS"][consulta]
            # SVSP
            elif self.uf.upper() in lista_svsp:
                if self._ambiente == 1:
                    ambiente = "HTTPS"
                else:
                    ambiente = "HOMOLOGACAO"
                self.url = CTE["SVSP"][ambiente] + CTE["SVSP"][consulta]
            else:
                raise Exception(f"Url não encontrada para {consulta} {self.uf.upper()}")
        return self.url

    def evento(self, evento):
        """
        Envia eventos do CTe como:
            Comprovante de Entrega do CT-e
            Cancelamento do Comprovante de Entrega do CT-e
            Insucesso na Entrega do CT-e
            Cancelamento do Insucesso de Entrega do CT-e
            Prestação do Serviço em Desacordo
            Cancelamento Prestação do Serviço em Desacordo
        :param evento: Nome do Evento
        :return:
        """

        # url do serviço
        url = self._get_url("EVENTOS")

        # Monta XML do corpo da requisição
        xml = self._construir_xml_soap("CTeRecepcaoEventoV4", evento)
        return self._post(url, xml)

    def _construir_xml_soap(self, metodo, dados, cabecalho=False):
        """Monta o XML para o envio via SOAP"""

        raiz = etree.Element(
            "{%s}Envelope" % NAMESPACE_SOAP,
            nsmap={"soap": NAMESPACE_SOAP, "xsi": NAMESPACE_XSI, "xsd": NAMESPACE_XSD},
        )
        if self._header and metodo != "CTeRecepcaoEventoV4":
            cabecalho = self._cabecalho_soap(metodo)
            c = etree.SubElement(raiz, "{%s}Header" % self._namespace_soap)
            c.append(cabecalho)

        body = etree.SubElement(raiz, "{%s}Body" % NAMESPACE_SOAP)

        # distribuição tem um corpo de xml diferente
        if metodo == "CTeDistribuicaoDFe":
            x = etree.SubElement(body, "cteDistDFeInteresse", xmlns=NAMESPACE_CTE_METODO + metodo)
            a = etree.SubElement(x, "cteDadosMsg")
        else:
            a = etree.SubElement(body, "cteDadosMsg", xmlns=NAMESPACE_CTE_METODO + metodo)
        a.append(dados)
        return raiz

    def _post_header(self):
        """Retorna um dicionário com os atributos para o cabeçalho da requisição HTTP"""
        response = {
            "content-type": "application/soap+xml; charset=utf-8;",
            "Accept": "application/soap+xml; charset=utf-8;",
        }
        response["SOAPAction"] = ""
        return response

    def _post(self, url, xml):
        certificado_a1 = CertificadoA1(self.certificado)
        chave, cert = certificado_a1.separar_arquivo(self.certificado_senha, caminho=True)
        chave_cert = (cert, chave)
        # Abre a conexão HTTPS
        try:
            xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'

            # limpa xml com caracteres bugados para infNFeSupl em NFC-e
            xml = re.sub(
                "<qrCode>(.*?)</qrCode>",
                lambda x: x.group(0).replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", ""),
                etree.tostring(xml, encoding="unicode").replace("\n", ""),
            )
            xml = xml_declaration + xml

            # Faz o request com o servidor
            result = requests.post(
                url,
                xml,
                headers=self._post_header(),
                cert=chave_cert,
                verify=False,
                timeout=300,
            )
            result.encoding = "utf-8"
            return result
        except requests.exceptions.Timeout as e:
            raise e
        except requests.exceptions.RequestException as e:
            raise e
        finally:
            certificado_a1.excluir()
