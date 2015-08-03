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

    def autorizacao(self, modelo, nota_fiscal, idlote=1):
        # url do serviço
        url = self._get_url(modelo=modelo, consulta='AUTORIZACAO')
        # Monta XML do corpo da requisição
        raiz = etree.Element('enviNFe', xmlns=NAMESPACE_NFE, versao=VERSAO_PADRAO)
        etree.SubElement(raiz, 'idLote').text = str(idlote) # numero autoincremental gerado pelo sistema
        etree.SubElement(raiz, 'indSinc').text = str(1) # 0 para assincrono, 1 para sincrono
        raiz.append(nota_fiscal)
        # Monta XML para envio da requisição
        xml = self._construir_xml_status_pr(cabecalho=self._cabecalho_soap(metodo='NfeAutorizacao'), metodo='NfeAutorizacao', dados=raiz)
        
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
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'nRec').text = numero
        # Monta XML para envio da requisição
        xml = self._construir_xml_status_pr(cabecalho=self._cabecalho_soap(metodo='NfeRetAutorizacao'), metodo='NfeRetAutorizacao', dados=raiz)
        
        return self._post(url, xml)

    def consulta_nota(self, modelo, chave):
        """
            Este método oferece a consulta da situação da NF-e/NFC-e na Base de Dados do Portal da Secretaria de Fazenda Estadual.
        """
        # url do serviço
        url = self._get_url(modelo=modelo, consulta='CHAVE')
        # Monta XML do corpo da requisição
        raiz = etree.Element('consSitNFe', versao=VERSAO_PADRAO, xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'xServ').text = 'CONSULTAR'
        etree.SubElement(raiz, 'chNFe').text = chave
        # Monta XML para envio da requisição
        xml = self._construir_xml_status_pr(cabecalho=self._cabecalho_soap(metodo='NfeConsulta2'), metodo='NfeConsulta2', dados=raiz)
        
        return self._post(url, xml)

    def cancelar(self, modelo, evento, idlote=1):
        """ Envia um evento de cancelamento de nota fiscal """
        # url do serviço
        url = self._get_url(modelo=modelo, consulta='EVENTOS')
        # Monta XML do corpo da requisição
        raiz = etree.Element('envEvento', versao='1.00', xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'idLote').text = str(idlote) # numero autoincremental gerado pelo sistema
        raiz.append(evento)
        xml = self._construir_xml_status_pr(cabecalho=self._cabecalho_soap(metodo='RecepcaoEvento'), metodo='RecepcaoEvento', dados=raiz)
        return self._post(url, xml)

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
        # RS utiliza um formato de url diferente dos outros estados
        if self.uf.upper() == 'RS':
            if modelo == 'nfe':
                if consulta == 'CADASTRO':
                    self.url = 'https://cad.' + NFE[self.uf.upper()][consulta]
                else:
                    # nfe Ex: https://nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3
                    if self._ambiente == 1:
                        self.url = 'https://nfe.' + NFE[self.uf.upper()][consulta]
                    else:
                        self.url = 'https://nfe-homologacao.' + NFE[self.uf.upper()][consulta]
            elif modelo == 'nfce':
                # nfce Ex: https://homologacao.nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3
                if self._ambiente == 1:
                    self.url = 'https://nfce.' + NFCE[self.uf.upper()][consulta]
                else:
                    self.url = 'https://nfce-homologacao.' + NFCE[self.uf.upper()][consulta]
            else:
                # TODO implementar outros tipos de notas como NFS-e
                pass
        else:
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

        raiz = etree.Element('nfeCabecMsg', xmlns=NAMESPACE_METODO+metodo)
        if metodo == 'RecepcaoEvento':
            etree.SubElement(raiz, 'versaoDados').text = '1.00'
        else:
            etree.SubElement(raiz, 'versaoDados').text = VERSAO_PADRAO
        etree.SubElement(raiz, 'cUF').text = CODIGOS_ESTADOS[self.uf.upper()]
        return raiz

    def _construir_xml_soap(self, cabecalho, metodo, dados):
        """Mota o XML para o envio via SOAP"""

        raiz = etree.Element('{%s}Envelope'%NAMESPACE_SOAP, nsmap={'soap12': NAMESPACE_SOAP})
        c= etree.SubElement(raiz, '{%s}Header'%NAMESPACE_SOAP)
        c.append(cabecalho)
        body = etree.SubElement(raiz, '{%s}Body'%NAMESPACE_SOAP)
        a = etree.SubElement(body, 'nfeDadosMsg', xmlns=NAMESPACE_METODO+metodo)
        a.append(dados)
        return raiz

    def _construir_xml_status_pr(self, cabecalho, metodo, dados):
        u"""Mota o XML para o envio via SOAP"""

        raiz = etree.Element('{%s}Envelope'%NAMESPACE_SOAP, nsmap={'xsi': NAMESPACE_XSI, 'xsd': NAMESPACE_XSD,'soap': NAMESPACE_SOAP})
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
            xml_declaration='<?xml version="1.0" encoding="utf-8"?>'
            xml = etree.tostring(xml, encoding='unicode', pretty_print=False).replace('\n','')
            xml = xml_declaration + xml
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