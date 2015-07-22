# -*- coding: utf-8 -*-
import datetime
import time
import requests
from pynfe.utils import etree, so_numeros
from pynfe.utils.flags import NAMESPACE_NFE, NAMESPACE_SOAP, NAMESPACE_XSI, NAMESPACE_XSD, NAMESPACE_METODO, VERSAO_PADRAO, CODIGOS_ESTADOS
from pynfe.utils.webservices import NFCE, NFE
from .assinatura import AssinaturaA1
from pynfe.entidades.certificado import CertificadoA1

class Comunicacao(object):
    u"""Classe abstrata responsavel por definir os metodos e logica das classes
    de comunicação com os webservices da NF-e."""

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
    u"""Classe de comunicação que segue o padrão definido para as SEFAZ dos Estados."""

    _versao = VERSAO_PADRAO
    _assinatura = AssinaturaA1

    def autorizacao(self, modelo, nota_fiscal):
        # url do serviço
        url = self._get_url(modelo=modelo, consulta='AUTORIZACAO')
        # Monta XML do corpo da requisição
        raiz = etree.Element('enviNFe', versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        #etree.SubElement(raiz, 'versao').text = self._versao
        etree.SubElement(raiz, 'idLote').text = str(1) # numero autoincremental gerado pelo sistema
        etree.SubElement(raiz, 'indSinc').text = str(1) # 0 para assincrono, 1 para sincrono
        #etree.SubElement(raiz, 'NFe').text = nota_fiscal # conjunto de nfe tramistidas (max 50)
        raiz.append(nota_fiscal)
        # Monta XML para envio da requisição
        xml = self._construir_xml_status_pr(cabecalho=self._cabecalho_soap(metodo='NfeAutorizacao'), metodo='NfeAutorizacao', dados=raiz)
        #print (xml)
        return self._post(url, xml)

    def consulta_recibo(self, modelo, numero):
        """
            Este método oferece a consulta do resultado do processamento de um lote de NF-e.
            O aplicativo do Contribuinte deve ser construído de forma a aguardar um tempo mínimo de
            15 segundos entre o envio do Lote de NF-e para processamento e a consulta do resultado
            deste processamento, evitando a obtenção desnecessária do status de erro 105 - "Lote em
            Processamento".
        """
        # url do serviço
        url = self._get_url(modelo=modelo, consulta='RECIBO')
        # Monta XML do corpo da requisição
        raiz = etree.Element('consReciNFe', versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'versao').text = self._versao
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'nRec').text = numero
        # Monta XML para envio da requisição
        xml = self._construir_xml_status_pr(cabecalho=self._cabecalho_soap(metodo='NfeRetAutorizacao'), metodo='NfeRetAutorizacao', dados=raiz)
        #print (xml)
        return self._post(url, xml)

    def cancelar(self, modelo, xml):
        """ Envia um evento de cancelamento de nota fiscal """
        # timezone Brasília -03:00
        tz = time.strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])

        # url do serviço
        url = self._get_url(modelo=modelo, consulta='EVENTOS')
        # Monta XML do corpo da requisição
        raiz = etree.Element('envEvento')
        #etree.SubElement(raiz, 'versao').text = self._versao # Na documentaçao 6.0 está desta forma
        etree.SubElement(raiz, 'versaoDados').text = self._versao # Na documentaçao 6.0 está desta forma
        etree.SubElement(raiz, 'idLote').text = str(1) # numero autoincremental gerado pelo sistema
        evento = etree.SubElement(raiz, 'evento')
        etree.SubElement(evento, 'versao').text = '1' # versao do leiaute do evento (cancelamento = 1)
        etree.SubElement(raiz, 'infEvento').text = xml # Evento, um lote pode conter até 20 eventos
        dados = etree.tostring(raiz, encoding="unicode")
        xml = self._construir_xml_status_pr(cabecalho=self._cabecalho_soap(metodo='RecepcaoEvento'), metodo='RecepcaoEvento', dados=dados)
        xml = str(xml).replace('&amp;','').replace('lt;','<').replace('gt;','>').replace('&','')
        return xml
        #return self._post(url, xml)

    def situacao_nfe(self, nota_fiscal):
        pass

    def status_servico(self, modelo):
        """ Verifica status do servidor da receita. """
        """ modelo é a string com tipo de serviço que deseja consultar
            Ex: nfe ou nfce 
        """
        url = self._get_url(modelo=modelo, consulta='STATUS')

        # Monta XML do corpo da requisição
        raiz = etree.Element('consStatServ', versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'cUF').text = CODIGOS_ESTADOS[self.uf.upper()]
        etree.SubElement(raiz, 'xServ').text = 'STATUS'
        # Monta XML para envio da requisição
        xml = self._construir_xml_status_pr(cabecalho=self._cabecalho_soap(metodo='NfeStatusServico2'), metodo='NfeStatusServico2', dados=raiz)
        # Chama método que efetua a requisição POST no servidor SOAP
        return self._post(url, xml)

    def consultar_cadastro(self, instancia):
        #post = '/nfeweb/services/cadconsultacadastro.asmx'
        post = '/nfeweb/services/nfeconsulta.asmx'

    def inutilizar_faixa_numeracao(self, numero_inicial, numero_final, emitente, certificado, senha, ano=None, serie='1', justificativa=''):
        post = '/nfeweb/services/nfestatusservico.asmx'
        metodo = 'NfeInutilizacao2'

        # Valores default
        ano = str(ano or datetime.date.today().year)[-2:]
        uf = CODIGOS_ESTADOS[emitente.endereco_uf]
        cnpj = so_numeros(emitente.cnpj)

        # Identificador da TAG a ser assinada formada com Código da UF + Ano (2 posições) +
        #  CNPJ + modelo + série + nro inicial e nro final precedida do literal “ID”
        id_unico = 'ID%(uf)s%(ano)s%(cnpj)s%(modelo)s%(serie)s%(num_ini)s%(num_fin)s'%{
                'uf': uf,
                'ano': ano,
                'cnpj': cnpj,
                'modelo': '55',
                'serie': serie.zfill(3),
                'num_ini': str(numero_inicial).zfill(9),
                'num_fin': str(numero_final).zfill(9),
                }

        # Monta XML do corpo da requisição # FIXME
        raiz = etree.Element('inutNFe', xmlns="http://www.portalfiscal.inf.br/nfe", versao="1.07")
        inf_inut = etree.SubElement(raiz, 'infInut', Id=id_unico)
        etree.SubElement(inf_inut, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(inf_inut, 'xServ').text = 'INUTILIZAR'
        etree.SubElement(inf_inut, 'cUF').text = uf
        etree.SubElement(inf_inut, 'ano').text = ano
        etree.SubElement(inf_inut, 'CNPJ').text = emitente.cnpj
        etree.SubElement(inf_inut, 'mod').text = '55'
        etree.SubElement(inf_inut, 'serie').text = serie
        etree.SubElement(inf_inut, 'nNFIni').text = str(numero_inicial)
        etree.SubElement(inf_inut, 'nNFFin').text = str(numero_final)
        etree.SubElement(inf_inut, 'xJust').text = justificativa
        #dados = etree.tostring(raiz, encoding='utf-8', xml_declaration=True)

        # Efetua assinatura
        assinatura = self._assinatura(certificado, senha)
        dados = assinatura.assinar_etree(etree.ElementTree(raiz), retorna_xml=True)

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap(
                metodo='nfeRecepcao2', # XXX
                tag_metodo='nfeInutilizacaoNF', # XXX
                cabecalho=self._cabecalho_soap(),
                dados=dados,
                )

        # Chama método que efetua a requisição POST no servidor SOAP
        retorno = self._post(post, xml, self._post_header())

        # Transforma o retorno em etree # TODO
        #retorno = etree.parse(StringIO(retorno))

        return retorno

    def _get_url(self, modelo, consulta):
        if self._ambiente == 1:
            ambiente = 'https://'
        else:
            ambiente = 'https://homologacao.'
        if modelo == 'nfe':
            # nfe Ex: https://nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3
            self.url = ambiente + NFE[self.uf.upper()][consulta]
        elif modelo == 'nfce':
            # nfce Ex: https://homologacao.nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3
            self.url = ambiente + NFCE[self.uf.upper()][consulta]
        else:
            # TODO implementar outros tipos de notas como NFS-e
            pass
        return self.url

    def _cabecalho_soap(self, metodo):
        u"""Monta o XML do cabeçalho da requisição SOAP"""

        raiz = etree.Element('nfeCabecMsg')
        etree.SubElement(raiz, 'cUF').text = CODIGOS_ESTADOS[self.uf.upper()]
        etree.SubElement(raiz, 'versaoDados').text = VERSAO_PADRAO
        return raiz

    def _construir_xml_soap(self, cabecalho, metodo, dados):
        """Mota o XML para o envio via SOAP"""

        raiz = etree.Element('{%s}Envelope'%NAMESPACE_SOAP, nsmap={'xsi': NAMESPACE_XSI, 'xsd': NAMESPACE_XSD, 'soap12': NAMESPACE_SOAP})
        etree.SubElement(raiz, '{%s}Header'%NAMESPACE_SOAP).text = cabecalho
        body = etree.SubElement(raiz, '{%s}Body'%NAMESPACE_SOAP)
        etree.SubElement(body, 'nfeDadosMsg').text = dados
        return raiz

    def _construir_xml_status_pr(self, cabecalho, metodo, dados):
        u"""Mota o XML para o envio via SOAP"""

        raiz = etree.Element('{%s}Envelope'%NAMESPACE_SOAP, nsmap={'soap': NAMESPACE_SOAP}, xmlns=NAMESPACE_METODO+metodo)
        c = etree.SubElement(raiz, '{%s}Header'%NAMESPACE_SOAP)
        c.append(cabecalho)
        body = etree.SubElement(raiz, '{%s}Body'%NAMESPACE_SOAP)
        a = etree.SubElement(body, 'nfeDadosMsg', xmlns=NAMESPACE_METODO+metodo)
        a.append(dados)
        return raiz

    def _post_header(self):
        u"""Retorna um dicionário com os atributos para o cabeçalho da requisição HTTP"""
        return {
            u'content-type': u'application/soap+xml; charset=utf-8;',
            u'Accept': u'application/soap+xml; charset=utf-8;',
            }

    def _post(self, url, xml):
        certificadoA1 = CertificadoA1(self.certificado)
        chave, cert = certificadoA1.separar_arquivo(self.certificado_senha, caminho=True)
        chave_cert = (cert, chave)
        # Abre a conexão HTTPS
        try:
            # Passa o lxml.etree para string
            xml = etree.tostring(xml, encoding='unicode', pretty_print=False).replace('ds:','')
            # Faz o request com o servidor
            print (xml)
            result = requests.post(url, xml, headers=self._post_header(), cert=chave_cert, verify=False)
            if result == 200:
                result.encoding='utf-8'
                return result
            else:
                return result
        except requests.exceptions.ConnectionError as e:
            raise e
        finally:
            certificadoA1.excluir()