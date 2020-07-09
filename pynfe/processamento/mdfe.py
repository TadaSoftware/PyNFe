# -*- coding: utf-8 -*-
import time
import re
import requests
from io import StringIO
import base64

from pynfe.utils.flags import (
    NAMESPACE_MDFE,
    MODELO_MDFE,
    VERSAO_MDFE,
    NAMESPACE_MDFE_METODO,
    NAMESPACE_SOAP,
    NAMESPACE_XSI,
    NAMESPACE_XSD,
    CODIGOS_ESTADOS
)
from pynfe.utils.webservices import MDFE
from pynfe.entidades.certificado import CertificadoA1
from pynfe.utils import etree, extrai_id_srtxml
from .comunicacao import Comunicacao
from .resposta import analisar_retorno

MDFE_SITUACAO_JA_ENVIADO = ('100', '101', '132')


class ComunicacaoMDFe(Comunicacao):

    _modelo = MODELO_MDFE
    _namespace = NAMESPACE_MDFE
    _versao = VERSAO_MDFE
    _header = 'mdfeCabecMsg'
    _envio_mensagem = 'mdfeDadosMsg'
    _retorno_mensagem = 'mdfeRecepcaoResult'
    _namespace_metodo = NAMESPACE_MDFE_METODO

    _accept = True
    _soap_action = False
    _namespace_soap = NAMESPACE_SOAP
    _namespace_xsi = NAMESPACE_XSI
    _namespace_xsd = NAMESPACE_XSD
    _soap_version = 'soap12'
    _edoc_situacao_ja_enviado = MDFE_SITUACAO_JA_ENVIADO
    _edoc_situacao_arquivo_recebido_com_sucesso = '103'
    _edoc_situacao_lote_processado = '104'
    _edoc_situacao_em_processamento = '105'
    _edoc_situacao_servico_em_operacao = '107'

    consulta_servico_ao_enviar = True
    maximo_tentativas_consulta_recibo = 5

    def autorizacao(self, manifesto, id_lote=1, ind_sinc=1):
        """
        Método para realizar autorização do manifesto
        :param manifesto: XML assinado
        :param id_lote: Id do lote - numero autoincremental gerado pelo sistema
        :param ind_sinc: Indicador de sincrono e assincrono, 0 para assincrono, 1 para sincrono
        :return:  Uma tupla que em caso de sucesso, retorna xml com manifesto e protocolo de autorização. 
        Caso contrário, envia todo o soap de resposta da Sefaz para decisão do usuário.
        """
        # url do serviço
        if ind_sinc == 0:
            url = self._get_url(consulta='RECEPCAO')
        elif ind_sinc == 1:
            url = self._get_url(consulta='RECEPCAO_SINC')
        else:
            raise f'ind_sinc deve ser 0=assincrono ou 1=sincrono'

        # Monta XML do corpo da requisição
        raiz = etree.Element('enviMDFe', xmlns=NAMESPACE_MDFE, versao=VERSAO_MDFE)
        etree.SubElement(raiz, 'idLote').text = str(id_lote)  # numero autoincremental gerado pelo sistema
        raiz.append(manifesto)

        # Monta XML para envio da requisição
        if ind_sinc == 0:
            xml = self._construir_xml_soap('MDFeRecepcao', raiz)
        elif ind_sinc == 1:
            xml = self._construir_xml_soap('MDFeRecepcaoSinc', raiz)

        # Faz request no Servidor da Sefaz
        retorno = self._post(url, xml)

        # Em caso de sucesso, retorna xml com o mdfe e protocolo de autorização.
        # Caso contrário, envia todo o soap de resposta da Sefaz para decisão do usuário.
        if retorno.status_code == 200:
            # namespace
            ns = {'ns': NAMESPACE_MDFE}
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
                        status = prot_mdfe.xpath('ns:infProt/ns:cStat', namespaces=ns)[0].text

                        # autorizado uso do MDF-e
                        # retorna xml final (protMDFe + MDFe)
                        if status in self._edoc_situacao_ja_enviado:  # if status == '100':
                            raiz = etree.Element('mdfeProc', xmlns=NAMESPACE_MDFE, versao=VERSAO_MDFE)
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
                if status == self._edoc_situacao_arquivo_recebido_com_sucesso:
                    nrec = rec.xpath("ns:retEnviMDFe/ns:infRec/ns:nRec", namespaces=ns)[0].text
                    return 0, nrec, manifesto
        return 1, retorno, manifesto

    def status_servico(self):
        url = self._get_url('STATUS')
        # Monta XML do corpo da requisição
        raiz = etree.Element('consStatServMDFe', versao=self._versao, xmlns=NAMESPACE_MDFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'xServ').text = 'STATUS'
        xml = self._construir_xml_soap('MDFeStatusServico', raiz)
        return self._post(url, xml)

    def consulta(self, chave):
        url = self._get_url('CONSULTA')
        # Monta XML do corpo da requisição
        raiz = etree.Element('consSitMDFe', versao=self._versao, xmlns=NAMESPACE_MDFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'xServ').text = 'CONSULTAR'
        etree.SubElement(raiz, 'chMDFe').text = chave
        # Monta XML para envio da requisição
        xml = self._construir_xml_soap('MDFeConsulta', raiz)
        return self._post(url, xml)

    def consulta_nao_encerrados(self, cpfcnpj):
        url = self._get_url('NAO_ENCERRADOS')
        # Monta XML do corpo da requisição
        raiz = etree.Element('consMDFeNaoEnc', xmlns=NAMESPACE_MDFE, versao=self._versao)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'xServ').text = 'CONSULTAR NÃO ENCERRADOS'
        if len(cpfcnpj) == 11:
            etree.SubElement(raiz, 'CPF').text = cpfcnpj.zfill(11)
        else:
            etree.SubElement(raiz, 'CNPJ').text = cpfcnpj.zfill(14)
        # Monta XML para envio da requisição
        xml = self._construir_xml_soap('MDFeConsNaoEnc', raiz)
        return self._post(url, xml)

    def consulta_recibo(self, numero):
        url = self._get_url('RET_RECEPCAO')
        # Monta XML do corpo da requisição
        raiz = etree.Element('consReciMDFe', versao=self._versao, xmlns=NAMESPACE_MDFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self._ambiente)
        etree.SubElement(raiz, 'nRec').text = numero.zfill(15)
        # Monta XML para envio da requisição
        xml = self._construir_xml_soap('MDFeRetRecepcao', raiz)
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
        url = self._get_url('EVENTOS')
        # Monta XML do corpo da requisição
        xml = self._construir_xml_soap('MDFeRecepcaoEvento', evento)
        return self._post(url, xml)

    def _construir_xml_soap(self, metodo, dados):
        """Mota o XML para o envio via SOAP"""

        raiz = etree.Element(
            '{%s}Envelope' % NAMESPACE_SOAP,
            nsmap={
                'xsi': self._namespace_xsi,
                'xsd': self._namespace_xsd,
                self._soap_version: self._namespace_soap
            }
        )

        if self._header:
            cabecalho = self._cabecalho_soap(metodo)
            c = etree.SubElement(raiz, '{%s}Header' % self._namespace_soap)
            c.append(cabecalho)

        body = etree.SubElement(raiz, '{%s}Body' % self._namespace_soap)

        a = etree.SubElement(
            body,
            self._envio_mensagem,
            xmlns=self._namespace_metodo+metodo
        )

        # if metodo == 'MDFeRecepcaoSinc':
        #     body_base64 = base64.b16encode(a).decode()

        a.append(dados)
        return raiz

    def _post_header(self, soap_webservice_method=False):
        """Retorna um dicionário com os atributos para o cabeçalho da requisição HTTP"""
        header = {
            b'content-type': b'text/xml; charset=utf-8;',
        }

        # PE é a únca UF que exige SOAPAction no header
        if soap_webservice_method:
            header[b'SOAPAction'] = \
                (self._namespace_metodo + soap_webservice_method).encode('utf-8')

        if self._accept:
            header[b'Accept'] = b'application/soap+xml; charset=utf-8;'

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
                '<qrCodMDFe>(.*?)</qrCodMDFe>',
                lambda x: x.group(0).replace('&lt;', '<').replace('&gt;', '>').replace('amp;', ''),
                etree.tostring(xml, encoding='unicode').replace('\n', '')
            )
            xml = xml_declaration + xml
            xml = xml.encode('utf8')  # necessário para o evento "CONSULTAR NÃO ENCERRADOS"

            # Faz o request com o servidor
            result = requests.post(
                url,
                xml,
                headers=self._post_header(),
                cert=chave_cert,
                verify=False
            )
            result.encoding = 'utf-8'
            return result
        except requests.exceptions.RequestException as e:
            raise e
        finally:
            certificado_a1.excluir()

    def _cabecalho_soap(self, metodo):
        """Monta o XML do cabeçalho da requisição SOAP"""

        raiz = etree.Element(
            self._header,
            xmlns=self._namespace_metodo + metodo
        )
        etree.SubElement(raiz, 'cUF').text = CODIGOS_ESTADOS[self.uf.upper()]
        etree.SubElement(raiz, 'versaoDados').text = '3.00'
        return raiz

    def _get_url(self, consulta):
        # producao
        if self._ambiente == 1:
            ambiente = MDFE['SVRS']['HTTPS']
        # homologacao
        else:
            ambiente = MDFE['SVRS']['HOMOLOGACAO']

        self.url = ambiente + MDFE['SVRS'][consulta]
        return self.url
