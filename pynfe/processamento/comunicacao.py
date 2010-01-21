# -*- coding: utf-8 -*-
import datetime
from httplib import HTTPSConnection, HTTPResponse

from pynfe.utils import etree, StringIO, so_numeros
from pynfe.utils.flags import NAMESPACE_NFE, NAMESPACE_SOAP, VERSAO_PADRAO
from pynfe.utils.flags import CODIGOS_ESTADOS, VERSAO_PADRAO

class Comunicacao(object):
    u"""Classe abstrata responsavel por definir os metodos e logica das classes
    de comunicação com os webservices da NF-e."""

    _ambiente = 1   # 1 = Produção, 2 = Homologação
    servidor = None
    porta = 80
    certificado = None
    certificado_senha = None

    def __init__(self, servidor, porta, certificado, certificado_senha, homologacao=False):
        self.servidor = servidor
        self.porta = porta
        self.certificado = certificado
        self.certificado_senha = certificado_senha
        self._ambiente = homologacao and 2 or 1

class ComunicacaoSefaz(Comunicacao):
    u"""Classe de comunicação que segue o padrão definido para as SEFAZ dos Estados."""

    _versao = VERSAO_PADRAO
    
    def transmitir(self, nota_fiscal):
        pass

    def cancelar(self, nota_fiscal):
        pass

    def situacao_nfe(self, nota_fiscal):
        pass

    def status_servico(self):
        post = '/nfeweb/services/nfestatusservico.asmx'

        # Monta XML do corpo da requisição # FIXME
        raiz = etree.Element('teste')
        dados = etree.tostring(raiz)

        # Monta XML para envio da requisição
        xml = self._construir_xml_soap(
                metodo='CadConsultaCadastro', # FIXME
                tag_metodo='consultaCadastro', # FIXME
                cabecalho=self._cabecalho_soap(),
                dados=dados,
                )

        # Chama método que efetua a requisição POST no servidor SOAP
        retorno = self._post(post, xml, self._post_header())

        # Transforma o retorno em etree
        #retorno = etree.parse(StringIO(retorno))

        return bool(retorno)

    def consultar_cadastro(self, instancia):
        #post = '/nfeweb/services/cadconsultacadastro.asmx'
        post = '/nfeweb/services/nfeconsulta.asmx'

    def inutilizar_faixa_numeracao(self, numero_inicial, numero_final, emitente, ano=None,
            serie='1', justificativa=''):
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
        inf_inut = etree.SubElement(raiz, 'infInut', Id=id_unico) # FIXME
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
        dados = etree.tostring(raiz, encoding='utf-8', xml_declaration=True)

        # Efetua assinatura
        # Monta XML para envio da requisição
        xml = self._construir_xml_soap(
                metodo='CadConsultaCadastro', # FIXME
                tag_metodo='consultaCadastro', # FIXME
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

        raiz = etree.Element('cabecMsg', xmlns=NAMESPACE_NFE, versao="1.02")
        etree.SubElement(raiz, 'versaoDados').text = self._versao

        return etree.tostring(raiz, encoding='utf-8', xml_declaration=True)

    def _construir_xml_soap(self, metodo, tag_metodo, cabecalho, dados):
        u"""Mota o XML para o envio via SOAP"""

        raiz = etree.Element('{%s}Envelope'%NAMESPACE_SOAP, nsmap={'soap': NAMESPACE_SOAP})

        body = etree.SubElement(raiz, '{%s}Body'%NAMESPACE_SOAP)
        met = etree.SubElement(
                body, tag_metodo, xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/%s"%metodo,
                )

        etree.SubElement(met, 'nfeCabecMsg').text = cabecalho
        etree.SubElement(met, 'nfeDadosMsg').text = dados

        return etree.tostring(raiz, encoding='utf-8', xml_declaration=True)

    def _post_header(self):
        u"""Retorna um dicionário com os atributos para o cabeçalho da requisição HTTP"""
        return {
            u'content-type': u'application/soap+xml; charset=utf-8',
            u'Accept': u'application/soap+xml; charset=utf-8',
            }

    def _post(self, post, xml, header):
        # Separa arquivos de certificado para chave e certificado (sozinho)
        caminho_chave, caminho_cert = self.certificado.separar_arquivo(senha=self.certificado_senha)

        # Abre a conexão HTTPS
        con = HTTPSConnection(self.servidor, self.porta, key_file=caminho_chave, cert_file=caminho_cert)

        try:
            #con.set_debuglevel(100)

            con.request(u'POST', post, xml, header)

            resp = con.getresponse()
        
            # Tudo certo!
            if resp.status == 200:
                return resp.read()
        finally:
            con.close()

