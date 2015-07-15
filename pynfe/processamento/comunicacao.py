# -*- coding: utf-8 -*-
import datetime
import requests
from pynfe.utils import etree, StringIO, so_numeros
from pynfe.utils.flags import NAMESPACE_NFE, NAMESPACE_SOAP, VERSAO_PADRAO
from pynfe.utils.flags import CODIGOS_ESTADOS, VERSAO_PADRAO
from .assinatura import AssinaturaA1

class Comunicacao(object):
    u"""Classe abstrata responsavel por definir os metodos e logica das classes
    de comunicação com os webservices da NF-e."""

    _ambiente = 2   # 1 = Produção, 2 = Homologação
    servidor = None
    porta = 80
    certificado = None
    certificado_senha = None

    def __init__(self, servidor, porta, certificado, certificado_senha, homologacao=False):
        self.servidor = servidor
        self.porta = porta
        self.certificado = certificado
        self.certificado_senha = certificado_senha
        self._ambiente = 2

class ComunicacaoSefaz(Comunicacao):
    u"""Classe de comunicação que segue o padrão definido para as SEFAZ dos Estados."""

    _versao = VERSAO_PADRAO
    _assinatura = AssinaturaA1

    def transmitir(self, nota_fiscal):
        pass

    def cancelar(self, nota_fiscal):
        pass

    def situacao_nfe(self, nota_fiscal):
        pass

    def status_servico(self):
        post = self.servidor

        # Monta XML do corpo da requisição
        raiz = etree.Element('consStatServ', versao='3.10', xmlns='http://www.portalfiscal.inf.br/nfe')
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'cUF').text = str(41)
        etree.SubElement(raiz, 'xServ').text = 'STATUS'
        dados = etree.tostring(raiz, encoding='UTF-8')
        # Monta XML para envio da requisição
        xml = self._construir_xml_soap(cabecalho=self._cabecalho_soap(), dados=dados)

        # Chama método que efetua a requisição POST no servidor SOAP
        retorno = self._post(post, xml, self._post_header())
        return retorno
        #return bool(retorno)

    def consultar_cadastro(self, instancia):
        #post = '/nfeweb/services/cadconsultacadastro.asmx'
        post = '/nfeweb/services/nfeconsulta.asmx'

    def inutilizar_faixa_numeracao(self, numero_inicial, numero_final, emitente, certificado,
            senha, ano=None, serie='1', justificativa=''):
        post = '/nfeweb/services/nfestatusservico.asmx'

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

    def _cabecalho_soap(self):
        u"""Monta o XML do cabeçalho da requisição SOAP"""

        raiz = etree.Element('nfeCabecMsg')
        etree.SubElement(raiz, 'cUF').text = str(41)
        etree.SubElement(raiz, 'versaoDados').text = VERSAO_PADRAO

        return etree.tostring(raiz, encoding='UTF-8')

    def _construir_xml_soap(self, cabecalho, dados):
        u"""Mota o XML para o envio via SOAP"""

        raiz = etree.Element('{%s}Envelope'%NAMESPACE_SOAP, nsmap={'soap': NAMESPACE_SOAP}, xmlns=self.servidor)
        etree.SubElement(raiz, '{%s}Header'%NAMESPACE_SOAP).text = cabecalho
        body = etree.SubElement(raiz, '{%s}Body'%NAMESPACE_SOAP)
        etree.SubElement(body, 'nfeDadosMsg').text = dados

        return etree.tostring(raiz, encoding='UTF-8', xml_declaration=True)

    def _post_header(self):
        u"""Retorna um dicionário com os atributos para o cabeçalho da requisição HTTP"""
        return {
            u'content-type': u'application/soap+xml; charset=utf-8',
            #u'content-type': u'text/xml; charset=utf-8',
            #u'Accept': u'text/xml; charset=utf-8',
            u'Accept': u'application/soap+xml; charset=utf-8',
            }

    def _post(self, post, xml, header):
        # Separa arquivos de certificado para chave e certificado (sozinho)
        #caminho_chave, caminho_cert = self.certificado.separar_arquivo(senha=self.certificado_senha)
        caminho_chave = '/home/junior/Documentos/Certificados/key.pem'
        caminho_cert = '/home/junior/Documentos/Certificados/cert.pem'

        # Abre a conexão HTTPS
        cert = (caminho_cert, caminho_chave)
        s = str(xml, 'utf-8').replace('&lt;', '<').replace('&gt;', '>').replace('\'', '"').replace('\n', '')
        #headers = {'content-type': 'text/xml'}
        
        try:
            r = requests.post(post, s, headers=self._post_header(), cert=cert, verify=False)
            print (r.content)
            if r == 200:
                return r.text
        except Exception as e:
            pass
        finally:
            pass
