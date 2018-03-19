# -*- coding: utf-8 -*-
import re
import ssl
import datetime

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

from pynfe.utils import etree, so_numeros
from pynfe.utils.flags import (
    NAMESPACE_NFE,
    NAMESPACE_XSD,
    NAMESPACE_XSI,
    VERSAO_PADRAO,
    NAMESPACE_SOAP,
    CODIGOS_ESTADOS,
    NAMESPACE_BETHA,
    NAMESPACE_METODO
)
from pynfe.utils.webservices import NFE, NFCE, NFSE
from pynfe.entidades.certificado import CertificadoA1

from .assinatura import AssinaturaA1, AssinaturaA1SignXML


class Comunicacao(object):
    """
    Classe abstrata responsavel por definir os metodos e logica das classes
    de comunicação com os webservices da NF-e.
    """

    _ambiente = 1   # 1 = Produção, 2 = Homologação
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

    def autorizacao(self, modelo, nota_fiscal, id_lote=1, ind_sinc=1):
        """
        Método para realizar autorização da nota de acordo com o modelo
        :param modelo: Modelo
        :param nota_fiscal: XML assinado
        :param id_lote: Id do lote - numero autoincremental gerado pelo sistema
        :param ind_sinc: Indicador de sincrono e assincrono, 0 para assincrono, 1 para sincrono
        :return:  Uma tupla que em caso de sucesso, retorna xml com nfe e protocolo de autorização. Caso contrário,
        envia todo o soap de resposta da Sefaz para decisão do usuário.
        """
        # url do serviço
        url = self._get_url(modelo=modelo, consulta='AUTORIZACAO')

        # Monta XML do corpo da requisição
        raiz = etree.Element('enviNFe', xmlns=NAMESPACE_NFE, versao=VERSAO_PADRAO)
        etree.SubElement(raiz, 'idLote').text = str(id_lote)  # numero autoincremental gerado pelo sistema
        etree.SubElement(raiz, 'indSinc').text = str(ind_sinc)  # 0 para assincrono, 1 para sincrono
        raiz.append(nota_fiscal)

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap('NFeAutorizacao4', raiz)
        # Faz request no Servidor da Sefaz
        retorno = self._post(url, xml)

        # Em caso de sucesso, retorna xml com nfe e protocolo de autorização.
        # Caso contrário, envia todo o soap de resposta da Sefaz para decisão do usuário.
        if retorno.status_code == 200:
            if ind_sinc == 1:
                # Procuta status no xml
                ns = {'ns': 'http://www.portalfiscal.inf.br/nfe'}  # namespace
                try:
                    prot = etree.fromstring(retorno.text)
                except ValueError:
                    # em SP retorno.text apresenta erro
                    prot = etree.fromstring(retorno.content)
                try:
                    # Protocolo com envio OK
                    inf_prot = prot[1][0][0][6]                             # root protNFe
                    status = inf_prot.xpath("ns:infProt/ns:cStat", namespaces=ns)[0].text
                except IndexError:
                    # Protocolo com algum erro no Envio
                    ret_envi = prot[1][0][0]                             # root retEnvi
                    status = ret_envi.xpath("ns:cStat", namespaces=ns)[0].text
                if status == '100':
                    raiz = etree.Element('nfeProc', xmlns=NAMESPACE_NFE, versao=VERSAO_PADRAO)
                    raiz.append(nota_fiscal)
                    raiz.append(inf_prot)
                    return 0, raiz
            else:
                # Retorna id do protocolo para posterior consulta em caso de sucesso.
                ns = {'ns': 'http://www.portalfiscal.inf.br/nfe'}    # namespace
                rec = etree.fromstring(retorno.text)
                rec = rec[1][0][0]
                status = rec.xpath("ns:cStat", namespaces=ns)[0].text
                # Lote Recebido com Sucesso!
                if status == '103':
                    nrec = rec.xpath("ns:infRec/ns:nRec", namespaces=ns)[0].text
                    return 0, nrec, nota_fiscal
        return 1, retorno, nota_fiscal

    def consulta_recibo(self, modelo, numero):
        """
        Este método oferece a consulta do resultado do processamento de um lote de NF-e.
        O aplicativo do Contribuinte deve ser construído de forma a aguardar um tempo mínimo de
        15 segundos entre o envio do Lote de NF-e para processamento e a consulta do resultado
        deste processamento, evitando a obtenção desnecessária do status de erro 105 - "Lote em
        Processamento".
        :param modelo: Modelo da nota
        :param numero: Número da nota
        :return:
        """

        # url do serviço
        url = self._get_url(modelo=modelo, consulta='RECIBO')

        # Monta XML do corpo da requisição
        raiz = etree.Element('consReciNFe', versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'nRec').text = numero

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap('NFeRetAutorizacao4', raiz)
        return self._post(url, xml)

    def consulta_nota(self, modelo, chave):
        """
            Este método oferece a consulta da situação da NF-e/NFC-e na Base de Dados do Portal
            da Secretaria de Fazenda Estadual.
        :param modelo: Modelo da nota
        :param chave: Chave da nota
        :return:
        """

        # url do serviço
        url = self._get_url(modelo=modelo, consulta='CHAVE')

        # Monta XML do corpo da requisição
        raiz = etree.Element('consSitNFe', versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'xServ').text = 'CONSULTAR'
        etree.SubElement(raiz, 'chNFe').text = chave

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap('NFeConsultaProtocolo4', raiz)
        return self._post(url, xml)

    def consulta_notas_cnpj(self, cnpj, nsu=0):
        """
        “Serviço de Consulta da Relação de Documentos Destinados” para um determinado CNPJ de
        destinatário informado na NF-e.
        :param cnpj: CNPJ
        :param nsu:  NSU
        :return:
        """

        # url do serviço
        url = self._get_url_an(consulta='DESTINADAS')

        # Monta XML do corpo da requisição
        raiz = etree.Element('consNFeDest', versao='1.01', xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'xServ').text = 'CONSULTAR NFE DEST'
        etree.SubElement(raiz, 'CNPJ').text = cnpj

        # Indicador de NF-e consultada:
        # 0 = Todas as NF-e;
        # 1 = Somente as NF-e que ainda não tiveram manifestação do destinatário (Desconhecimento da
        # operação, Operação não Realizada ou Confirmação da Operação);
        # 2 = Idem anterior, incluindo as NF-e que também não tiveram a Ciência da Operação.
        etree.SubElement(raiz, 'indNFe').text = '0'

        # Indicador do Emissor da NF-e:
        # 0 = Todos os Emitentes / Remetentes;
        # 1 = Somente as NF-e emitidas por emissores / remetentes que não tenham o mesmo CNPJ-Base do
        # destinatário (para excluir as notas fiscais de transferência entre filiais).
        etree.SubElement(raiz, 'indEmi').text = '0'

        # Último NSU recebido pela Empresa. Caso seja informado com zero, ou com um NSU muito antigo, a consulta
        # retornará unicamente as notas fiscais que tenham sido recepcionadas nos últimos 15 dias.
        etree.SubElement(raiz, 'ultNSU').text = str(nsu)

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap('NfeConsultaDest', raiz)
        return self._post(url, xml)

    def consulta_distribuicao(self, cnpj, nsu=0):
        pass

    def consulta_cadastro(self, modelo, cnpj):
        """
        Consulta de cadastro
        :param modelo: Modelo da nota
        :param cnpj: CNPJ da empresa
        :return:
        """
        # UF que utilizam a SVRS - Sefaz Virtual do RS: Para serviço de Consulta Cadastro: AC, RN, PB, SC 
        lista_svrs = ['AC', 'RN', 'PB', 'SC', 'PI']

        # RS implementa um método diferente na consulta de cadastro
        if self.uf.upper() == 'RS':
            url = NFE['RS']['CADASTRO']
        elif self.uf.upper() in lista_svrs:
            url = NFE['SVRS']['CADASTRO']
        elif self.uf.upper() == 'SVC-RS':
            url = NFE['SVC-RS']['CADASTRO']
        else:
            url = self._get_url(modelo=modelo, consulta='CADASTRO')

        raiz = etree.Element('ConsCad', versao='2.00', xmlns=NAMESPACE_NFE)
        info = etree.SubElement(raiz, 'infCons')
        etree.SubElement(info, 'xServ').text = 'CONS-CAD'
        etree.SubElement(info, 'UF').text = self.uf.upper()
        etree.SubElement(info, 'CNPJ').text = cnpj
        # etree.SubElement(info, 'CPF').text = cpf

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap('CadConsultaCadastro4', raiz)
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
            if evento[0][5].text.startswith('2'):
                url = self._get_url_an(consulta='EVENTOS')
            else:
                url = self._get_url(modelo=modelo, consulta='EVENTOS')
        except Exception:
            url = self._get_url(modelo=modelo, consulta='EVENTOS')

        # Monta XML do corpo da requisição
        raiz = etree.Element('envEvento', versao='1.00', xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'idLote').text = str(id_lote)  # numero autoincremental gerado pelo sistema
        raiz.append(evento)
        xml = self._construir_xml_soap('NFeRecepcaoEvento4', raiz)
        return self._post(url, xml)

    def status_servico(self, modelo):
        """
        Verifica status do servidor da receita.
        :param modelo: modelo é a string com tipo de serviço que deseja consultar, Ex: nfe ou nfce
        :return:
        """
        url = self._get_url(modelo, 'STATUS')
        # Monta XML do corpo da requisição
        raiz = etree.Element('consStatServ', versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'cUF').text = CODIGOS_ESTADOS[self.uf.upper()]
        etree.SubElement(raiz, 'xServ').text = 'STATUS'
        xml = self._construir_xml_soap('NFeStatusServico4', raiz)
        return self._post(url, xml)

    def download(self, cnpj, chave):
        """
        Metodo para download de NFe por parte de destinatário.
        O certificado digital deve ser o mesmo do destinatário da Nfe.
        NT 2012/002
        :param cnpj: CNPJ da empresa
        :param chave: Chave
        :return:
        """

        # url do serviço
        url = self._get_url_an(consulta='DOWNLOAD')

        # Monta XML do corpo da requisição
        raiz = etree.Element('downloadNFe', versao='1.00', xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'xServ').text = 'DOWNLOAD NFE'
        etree.SubElement(raiz, 'CNPJ').text = str(cnpj)
        etree.SubElement(raiz, 'chNFe').text = str(chave)

         # Monta XML para envio da requisição
        xml = self._construir_xml_soap('NfeDownloadNF', raiz)
        return self._post(url, xml)

    def inutilizacao(self, modelo, cnpj, numero_inicial, numero_final, justificativa='', ano=None, serie='1'):
        """
        Serviço destinado ao atendimento de solicitações de inutilização de numeração.
        :param modelo: Modelo da nota
        :param cnpj: CNPJda empresa
        :param numero_inicial: Número inicial
        :param numero_final: Número final
        :param justificativa: Justificativa
        :param ano: Ano
        :param serie:  Série
        :return:
        """

        # url do servico
        url = self._get_url(modelo=modelo, consulta='INUTILIZACAO')

        # Valores default
        ano = str(ano or datetime.date.today().year)[-2:]
        uf = CODIGOS_ESTADOS[self.uf.upper()]
        cnpj = so_numeros(cnpj)

        # Identificador da TAG a ser assinada formada com Código da UF + Ano (2 posições) +
        #  CNPJ + modelo + série + nro inicial e nro final precedida do literal “ID”
        id_unico = 'ID%(uf)s%(ano)s%(cnpj)s%(modelo)s%(serie)s%(num_ini)s%(num_fin)s' % {
            'uf': uf,
            'ano': ano,
            'cnpj': cnpj,
            'modelo': '55',
            'serie': serie.zfill(3),
            'num_ini': str(numero_inicial).zfill(9),
            'num_fin': str(numero_final).zfill(9),
        }

        # Monta XML do corpo da requisição # FIXME
        raiz = etree.Element('inutNFe', versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        inf_inut = etree.SubElement(raiz, 'infInut', Id=id_unico)
        etree.SubElement(inf_inut, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(inf_inut, 'xServ').text = 'INUTILIZAR'
        etree.SubElement(inf_inut, 'cUF').text = uf
        etree.SubElement(inf_inut, 'ano').text = ano
        etree.SubElement(inf_inut, 'CNPJ').text = cnpj
        etree.SubElement(inf_inut, 'mod').text = '55' if modelo == 'nfe' else '65'  # 55=NF-e; 65=NFC-e
        etree.SubElement(inf_inut, 'serie').text = serie
        etree.SubElement(inf_inut, 'nNFIni').text = str(numero_inicial)
        etree.SubElement(inf_inut, 'nNFFin').text = str(numero_final)
        etree.SubElement(inf_inut, 'xJust').text = justificativa

        # assinatura
        a1 = AssinaturaA1SignXML(self.certificado, self.certificado_senha)
        xml = a1.assinar(raiz)

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap('NFeInutilizacao4', xml)
        # Faz request no Servidor da Sefaz e retorna resposta
        return self._post(url, xml)

    def _get_url_an(self, consulta):
        # producao
        if self._ambiente == 1:
            if consulta == 'DISTRIBUICAO':
                ambiente = 'https://www1.'
            else:
                ambiente = 'https://www.'
        # homologacao
        else:
            ambiente = 'https://hom.'

        self.url = ambiente + NFE['AN'][consulta]
        return self.url

    def _get_url(self, modelo, consulta):
        """ Retorna a url para comunicação com o webservice """
        # estado que implementam webservices proprios
        lista = ['PR', 'MS', 'SP', 'AM', 'CE', 'BA', 'GO', 'MG', 'MT', 'PE', 'RS']
        if self.uf.upper() in lista:
            if self._ambiente == 1:
                ambiente = 'HTTPS'
            else:
                ambiente = 'HOMOLOGACAO'
            if modelo == 'nfe':
                # nfe Ex: https://nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3
                self.url = NFE[self.uf.upper()][ambiente] + NFE[self.uf.upper()][consulta]
            elif modelo == 'nfce':
                # PE é o unico UF que possiu NFE proprio e SVRS para NFCe
                if self.uf.upper() == 'PE':
                    self.url = NFCE['SVRS'][ambiente] + NFCE['SVRS'][consulta]
                else:
                    # nfce Ex: https://homologacao.nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3
                    self.url = NFCE[self.uf.upper()][ambiente] + NFCE[self.uf.upper()][consulta]
            else:
                raise Exception('Modelo não encontrado! Defina modelo="nfe" ou "nfce"')
        # Estados que utilizam outros ambientes
        else:
            lista_svrs = ['AC', 'RN', 'PB', 'SC', 'SE', 'PI']
            lista_svan = ['MA','PA']
            if self.uf.upper() in lista_svrs:
                if self._ambiente == 1:
                    ambiente = 'HTTPS'
                else:
                    ambiente = 'HOMOLOGACAO'
                if modelo == 'nfe':
                    # nfe Ex: https://nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3
                    self.url = NFE['SVRS'][ambiente] + NFE['SVRS'][consulta]
                elif modelo == 'nfce':
                    # nfce Ex: https://homologacao.nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3
                    self.url = NFCE['SVRS'][ambiente] + NFCE['SVRS'][consulta]
                else:
                    raise Exception('Modelo não encontrado! Defina modelo="nfe" ou "nfce"')
            elif self.uf.upper() in lista_svan:
                if self._ambiente == 1:
                    ambiente = 'HTTPS'
                else:
                    ambiente = 'HOMOLOGACAO'
                if modelo == 'nfe':
                    # nfe Ex: https://nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3
                    self.url = NFE['SVAN'][ambiente] + NFE['SVAN'][consulta]
                elif modelo == 'nfce':
                    # nfce Ex: https://homologacao.nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3
                    self.url = NFCE['SVAN'][ambiente] + NFCE['SVAN'][consulta]
                else:
                    raise Exception('Modelo não encontrado! Defina modelo="nfe" ou "nfce"')
        return self.url

    def _get_url_uf(self, modelo, consulta):
        """ Estados que implementam url diferente do padrão nacional"""
        # estados que implementam webservice SVRS
        svrs = ['AC', 'AL', 'AP', 'DF', 'ES', 'PB', 'RJ', 'RN', 'RO', 'RR', 'SC', 'SE', 'TO', 'PI']
        svan = ['MA', 'PA']
        # SVRS
        if self.uf.upper() in svrs:
            if self._ambiente == 1:
                ambiente = 'HTTPS'
            else:
                ambiente = 'HOMOLOGACAO'
            if modelo == 'nfe':
                # nfe Ex: https://nfe.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx
                #         https://nfe-homologacao.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx
                self.url = NFE['SVRS'][ambiente] + NFE['SVRS'][consulta]
            elif modelo == 'nfce':
                # nfce Ex: https://nfce.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx
                #          https://nfce-homologacao.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx
                self.url = NFCE['SVRS'][ambiente] + NFCE['SVRS'][consulta]
            else:
                # TODO implementar outros tipos de notas como NFS-e
                pass
        # SVAN
        else:
            if self.uf.upper() in svan:
                if self._ambiente == 1:
                    ambiente = 'HTTPS'
                else:
                    ambiente = 'HOMOLOGACAO'
                if modelo == 'nfe':
                    # nfe Ex: https://nfe.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx
                    #         https://nfe-homologacao.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx
                    self.url = NFE['SVAN'][ambiente] + NFE['SVAN'][consulta]
                elif modelo == 'nfce':
                    # TODO não existe SVAN para nfce
                    pass
                else:
                    # TODO implementar outros tipos de notas como NFS-e
                    pass
        return self.url

    def _cabecalho_soap(self, metodo):
        """Monta o XML do cabeçalho da requisição SOAP"""

        raiz = etree.Element('nfeCabecMsg', xmlns=NAMESPACE_METODO+metodo)
        if metodo == 'RecepcaoEvento':
            etree.SubElement(raiz, 'versaoDados').text = '1.00'
        elif metodo == 'NfeConsultaDest':
            etree.SubElement(raiz, 'versaoDados').text = '1.01'
        elif metodo == 'NfeDownloadNF':
            etree.SubElement(raiz, 'versaoDados').text = '1.00'
        elif metodo == 'CadConsultaCadastro2':
            etree.SubElement(raiz, 'versaoDados').text = '2.00'
        else:
            etree.SubElement(raiz, 'versaoDados').text = VERSAO_PADRAO
        etree.SubElement(raiz, 'cUF').text = CODIGOS_ESTADOS[self.uf.upper()]
        return raiz

    def _construir_xml_soap(self, metodo, dados):
        """Mota o XML para o envio via SOAP"""
        raiz = etree.Element('{%s}Envelope' % NAMESPACE_SOAP, nsmap={
          'xsi': NAMESPACE_XSI, 'xsd': NAMESPACE_XSD,'soap': NAMESPACE_SOAP})
        body = etree.SubElement(raiz, '{%s}Body' % NAMESPACE_SOAP)
        a = etree.SubElement(body, 'nfeDadosMsg', xmlns=NAMESPACE_METODO+metodo)
        a.append(dados)
        return raiz

    def _post_header(self):
        """Retorna um dicionário com os atributos para o cabeçalho da requisição HTTP"""
        return {
            'content-type': 'application/soap+xml; charset=utf-8;',
            'Accept': 'application/soap+xml; charset=utf-8;',
        }

    def _post(self, url, xml):
        certificado_a1 = CertificadoA1(self.certificado)
        chave, cert = certificado_a1.separar_arquivo(self.certificado_senha, caminho=True)
        chave_cert = (cert, chave)
        # Abre a conexão HTTPS
        try:
            xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'

            # limpa xml com caracteres bugados para infNFeSupl em NFC-e
            xml = re.sub(
                '<qrCode>(.*?)</qrCode>',
                lambda x: x.group(0).replace('&lt;', '<').replace('&gt;', '>').replace('amp;', ''),
                etree.tostring(xml, encoding='unicode').replace('\n', '')
            )
            xml = xml_declaration + xml
            # Faz o request com o servidor
            result = requests.post(url, xml, headers=self._post_header(), cert=chave_cert, verify=False)
            result.encoding = 'utf-8'
            return result
        except requests.exceptions.RequestException as e:
            raise e
        finally:
            certificado_a1.excluir()


class ComunicacaoNfse(Comunicacao):
    """ Classe de comunicação que segue o padrão definido para as SEFAZ dos Municípios. """

    _versao = ''
    _namespace = ''

    def __init__(self, certificado, certificado_senha, autorizador, homologacao=False):
        self.certificado = certificado
        self.certificado_senha = certificado_senha
        self._ambiente = 2 if homologacao else 1
        self.autorizador = autorizador.upper()
        if self.autorizador == 'GINFES':
            self._namespace = 'http://www.ginfes.com.br/cabecalho_v03.xsd'
            self._versao = '3'
        elif self.autorizador == 'BETHA':
            self._namespace = NAMESPACE_BETHA
            self._versao = '2.02'
        else:
            raise Exception('Autorizador não encontrado!')

    def autorizacao(self, nota):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'BETHA':
            # xml
            xml = etree.tostring(nota, encoding='unicode', pretty_print=False)
            # comunica via wsdl
            return self._post(url, xml, 'gerar')
        else:
            raise Exception('Este método só esta implementado no autorizador betha.')

    def enviar_lote(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'GINFES':
            # xml
            xml = '<?xml version="1.0" encoding="UTF-8"?>' + xml
            # comunica via wsdl
            return self._post_https(url, xml, 'enviar_lote')
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def consultar(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'GINFES':
            # xml
            xml = '<?xml version="1.0" encoding="UTF-8"?>' + xml
            # comunica via wsdl
            return self._post_https(url, xml, 'consulta')
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def consultar_rps(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'BETHA':
            # comunica via wsdl
            return self._post(url, xml, 'consultaRps')
        elif self.autorizador == 'GINFES':
            return self._post_https(url, xml, 'consultaRps')
        # TODO outros autorizadres
        else:
            raise Exception('Autorizador não encontrado!')

    def consultar_faixa(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'BETHA':
            # comunica via wsdl
            return self._post(url, xml, 'consultaFaixa')
        else:
            raise Exception('Este método só esta implementado no autorizador betha.')

    def consultar_lote(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'GINFES':
            # xml
            xml = '<?xml version="1.0" encoding="UTF-8"?>' + xml
            # comunica via wsdl
            return self._post_https(url, xml, 'consulta_lote')
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def consultar_situacao_lote(self, xml):
        # url do serviço
        url = self._get_url()
        if self.autorizador == 'GINFES':
            # comunica via wsdl
            return self._post_https(url, xml, 'consulta_situacao_lote')
        else:
            raise Exception('Este método só esta implementado no autorizador ginfes.')

    def cancelar(self, xml):
        # url do serviço
        url = self._get_url()
        # Betha
        if self.autorizador == 'BETHA':
            # comunica via wsdl
            return self._post(url, xml, 'cancelar')
        # Ginfes
        elif self.autorizador == 'GINFES':
            # comunica via wsdl com certificado
            return self._post_https(url, xml, 'cancelar')
        # TODO outros autorizadres
        else:
            raise Exception('Autorizador não encontrado!')

    def _cabecalho(self, retorna_string=True):
        """ Monta o XML do cabeçalho da requisição wsdl
            Namespaces padrão homologação (Ginfes) """

        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
        # cabecalho = '<ns2:cabecalho versao="3" xmlns:ns2="http://www.ginfes.com.br/cabecalho_v03.xsd"
        # xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><versaoDados>3</versaoDados></ns2:cabecalho>'
        # cabecalho
        raiz = etree.Element('{%s}cabecalho'%self._namespace, nsmap={'ns2':self._namespace, 'xsi':NAMESPACE_XSI}, versao=self._versao)
        etree.SubElement(raiz, 'versaoDados').text = self._versao

        if retorna_string:
            cabecalho = etree.tostring(raiz, encoding='unicode', pretty_print=False).replace('\n','')
            cabecalho = xml_declaration + cabecalho
            return cabecalho
        else:
            return raiz

    def _cabecalho2(self, retorna_string=True):
        """ Monta o XML do cabeçalho da requisição wsdl
            Namespaces que funcionaram em produção (Ginfes)"""

        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'

        # cabecalho
        raiz = etree.Element('cabecalho', xmlns=self._namespace, versao=self._versao)
        etree.SubElement(raiz, 'versaoDados').text = self._versao

        if retorna_string:
            cabecalho = etree.tostring(raiz, encoding='unicode', pretty_print=False).replace('\n', '')
            cabecalho = xml_declaration + cabecalho
            return cabecalho
        else:
            return raiz

    def _cabecalho_ginfes(self):
        """ Retorna o XML do cabeçalho gerado pelo xsd"""
        from pynfe.processamento.autorizador_nfse import SerializacaoGinfes
        return SerializacaoGinfes().cabecalho()

    def _get_url(self):
        """ Retorna a url para comunicação com o webservice """
        if self._ambiente == 1:
            ambiente = 'HTTPS'
        else:
            ambiente = 'HOMOLOGACAO'
        if self.autorizador in NFSE:
            self.url = NFSE[self.autorizador][ambiente]
        else:
            raise Exception('Autorizador nao encontrado!')
        return self.url

    def _post(self, url, xml, metodo):
        """ Comunicação wsdl (http) sem certificado digital """
        # cabecalho
        cabecalho = self._cabecalho()
        # comunicacao wsdl
        try:
            from suds.client import Client
            cliente = Client(url)
            # gerar nfse
            if metodo == 'gerar':
                return cliente.service.GerarNfse(cabecalho, xml)
            elif metodo == 'consultaRps':
                return cliente.service.ConsultarNfsePorRps(cabecalho, xml)
            elif metodo == 'consultaFaixa':
                return cliente.service.ConsultarNfseFaixa(cabecalho, xml)
            elif metodo == 'cancelar':
                return cliente.service.CancelarNfse(cabecalho, xml)
            # TODO outros metodos
            else:
                raise Exception('Método não implementado no autorizador.')
        except Exception as e:
            raise e

    def _post_https(self, url, xml, metodo):
        """ Comunicação wsdl (https) utilizando certificado do usuário """
        # cabecalho
        cabecalho = self._cabecalho()
        # comunicacao wsdl
        try:
            from suds.client import Client
            from pynfe.utils.https_nfse import HttpAuthenticated

            certificadoA1 = CertificadoA1(self.certificado)
            chave, cert = certificadoA1.separar_arquivo(self.certificado_senha, caminho=True)

            cliente = Client(url, transport = HttpAuthenticated(key=chave, cert=cert, endereco=url))

            # gerar nfse
            if metodo == 'gerar':
                return cliente.service.GerarNfse(cabecalho, xml)
            elif metodo == 'enviar_lote':
                return cliente.service.RecepcionarLoteRpsV3(cabecalho, xml)
            elif metodo == 'consulta':
                return cliente.service.ConsultarNfseV3(cabecalho, xml)
            elif metodo == 'consulta_lote':
                return cliente.service.ConsultarLoteRpsV3(cabecalho, xml)
            elif metodo == 'consulta_situacao_lote':
                return cliente.service.ConsultarSituacaoLoteRpsV3(cabecalho, xml)
            elif metodo == 'consultaRps':
                return cliente.service.ConsultarNfsePorRpsV3(cabecalho, xml)
            elif metodo == 'consultaFaixa':
                return cliente.service.ConsultarNfseFaixa(cabecalho, xml)
            elif metodo == 'cancelar':
                # versão 2
                return cliente.service.CancelarNfse(xml)
                # versão 3
                # return cliente.service.CancelarNfseV3(cabecalho, xml)
            # TODO outros metodos
            else:
                raise Exception('Método não implementado no autorizador.')
        except Exception as e:
            raise e
