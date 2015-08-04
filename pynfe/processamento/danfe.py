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
		# Procura atributos no xml
		nfe = xml[1][0][0][2]
		chave = nfe[0].attrib['Id'].replace('NFe','')
		data = nfe[0][0][7].text.encode()
		tpamb = nfe[0][0][14].text
		cpf = nfe[0][2][0].text
		total = nfe[0][4][0][14].text
		icms = nfe[0][4][0][1].text
		digest = nfe[1][0][2][2].text.encode()

		data = base64.b16encode(data).decode()
		digest = base64.b16encode(digest).decode()

		url = 'chNFe={}&nVersao={}&tpAmb={}&cDest={}&dhEmi={}&vNF={}&vICMS={}&digVal={}&cIdToken={}'.format(
		       chave, VERSAO_QRCODE, tpamb, cpf, data.lower(), total, icms, digest.lower(), token)

		url_hash = hashlib.sha1(url.encode()+csc.encode()).digest()
		url_hash = base64.b16encode(url_hash).decode()

		url = url + '&cHashQRCode=' + url_hash.upper()

		return NFCE[uf.upper()]['QR'] + url