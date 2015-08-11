# -*- coding: utf-8 -*-

import base64
import hashlib
from pynfe.utils.flags import VERSAO_QRCODE
from pynfe.utils.webservices import NFCE

class Danfe(object):
	""" Classe abstrata para a geração do Danfe. """
	pass

class DanfeNfce(Danfe):
	""" Classe para geração de Danfe para Nota Fiscal de Consumidor Eletrônica (NFC-e). """
	
	def gerar_qrcode(self, token, csc, xml, uf):
		""" Classe para gerar url do qrcode da NFC-e """
		try:
			# Procura atributos no xml
			ns = {'ns':'http://www.portalfiscal.inf.br/nfe'}
			sig = {'sig':'http://www.w3.org/2000/09/xmldsig#'}
			# Tag Raiz NFe Ex: <NFe>
			nfe = xml[0]
			chave = nfe[0].attrib['Id'].replace('NFe','')
			data = nfe.xpath('ns:infNFe/ns:ide/ns:dhEmi/text()', namespaces=ns)[0].encode()
			tpamb = nfe.xpath('ns:infNFe/ns:ide/ns:tpAmb/text()', namespaces=ns)[0]
			try:
				cpf = nfe.xpath('ns:infNFe/ns:dest/ns:CPF/text()', namespaces=ns)[0]
			except IndexError:
				cpf = None
			total = nfe.xpath('ns:infNFe/ns:total/ns:ICMSTot/ns:vNF/text()', namespaces=ns)[0]
			icms = nfe.xpath('ns:infNFe/ns:total/ns:ICMSTot/ns:vICMS/text()', namespaces=ns)[0]
			digest = nfe.xpath('sig:Signature/sig:SignedInfo/sig:Reference/sig:DigestValue/text()', namespaces=sig)[0].encode()

			data = base64.b16encode(data).decode()
			digest = base64.b16encode(digest).decode()

			if cpf is None:
				url = 'chNFe={}&nVersao={}&tpAmb={}&dhEmi={}&vNF={}&vICMS={}&digVal={}&cIdToken={}'.format(
				       chave, VERSAO_QRCODE, tpamb, data.lower(), total, icms, digest.lower(), token)			
			else:
				url = 'chNFe={}&nVersao={}&tpAmb={}&cDest={}&dhEmi={}&vNF={}&vICMS={}&digVal={}&cIdToken={}'.format(
				       chave, VERSAO_QRCODE, tpamb, cpf, data.lower(), total, icms, digest.lower(), token)

			url_hash = hashlib.sha1(url.encode()+csc.encode()).digest()
			url_hash = base64.b16encode(url_hash).decode()

			url = url + '&cHashQRCode=' + url_hash.upper()

			return NFCE[uf.upper()]['QR'] + url
		except Exception as e:
			raise e