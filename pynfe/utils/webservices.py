
"""
	@author: Junior Tada, Leonardo Tada
"""

# http://nfce.encat.org/desenvolvedor/qrcode/
# http://nfce.encat.org/consumidor/consulte-sua-nota/ 	url consulta por chave
# Nfc-e
NFCE = {
	    'RO': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': 'http://www.nfce.sefin.ro.gov.br/consultanfce/consulta.jsp?',
	    	'URL': 'http://www.nfce.sefin.ro.gov.br'
	    },
	    'AC': {
	    	'QR': 'sefaznet.ac.gov.br/nfce?',
	    	'URL': 'sefaznet.ac.gov.br/nfce/consulta',
	    	'HTTPS': 'http://www.',
	    	'HOMOLOGACAO': 'http://hml.'
	    },
	    'AM': {
	    	# csc_homologacao = '0123456789'
	    	# token_homologacao = '000001'
	    	'STATUS': 'nfce.sefaz.am.gov.br/nfce-services-nac/services/NfeStatusServico2',
	    	'AUTORIZACAO': 'nfce.sefaz.am.gov.br/nfce-services-nac/services/NfeAutorizacao',
	    	'RECIBO': 'nfce.sefaz.am.gov.br/nfce-services-nac/services/NfeRetAutorizacao',
	    	'CHAVE': 'nfce.sefaz.am.gov.br/nfce-services-nac/services/NfeConsulta2',
	    	'INUTILIZACAO': 'nfce.sefaz.am.gov.br/nfce-services-nac/services/NfeInutilizacao2',
	    	'EVENTOS': 'nfce.sefaz.am.gov.br/nfce-services-nac/services/RecepcaoEvento',
	    	'QR': 'sefaz.am.gov.br/nfceweb/consultarNFCe.jsp?',
	    	'URL': 'sefaz.am.gov.br/nfceweb/formConsulta.do',
	    	'HTTPS': 'http://sistemas.',
	    	'HOMOLOGACAO': 'http://homnfce.'
	    },
	    'RR': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': '/nfce/servlet/qrcode?',
	    	'URL': '/nfce/servlet/wp_consulta_nfce',
	    	'HTTPS': 'https://www.sefaz.rr.gov.br',
	    	'HOMOLOGACAO': 'http://200.174.88.103:8080'
	    },
	    'PA': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': 'view/consultas/nfce/nfceForm.seam?',
	    	'URL': 'view/consultas/nfce/consultanfce.seam',
	    	'HTTPS': 'https://appnfc.sefa.pa.gov.br/portal/',
	    	'HOMOLOGACAO': 'https://appnfc.sefa.pa.gov.br/portal-homologacao/'
	    },
	    'AP': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': '/nfcep.php?',
	    	'URL': 'https://www.sefaz.ap.gov.br/sate/seg/SEGf_AcessarFuncao.jsp?cdFuncao=FIS_1261',
	    	'HTTPS': '	https://www.sefaz.ap.gov.br/nfce',
	    	'HOMOLOGACAO': 'https://www.sefaz.ap.gov.br/nfcehml'
	    },
	    'TO': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
	    },
	    'MA': {
	    	'QR': 'nfce.sefaz.ma.gov.br/portal/consultarNFCe.jsp?',
	    	'HTTPS': 'http://www.',
	    	'HOMOLOGACAO': 'http://www.hom.'
	    },
	    'PI': {
	    	'QR': 'sefaz.pi.gov.br/nfceweb/consultarNFCe.jsf?',
	    	'HTTPS': 'http://webas.',
	    	'HOMOLOGACAO': 'http://webas.'
	    },
	    'CE': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': 'http://nfceh.sefaz.ce.gov.br/pages/ShowNFCe.html?',
	    	'URL': 'http://nfceh.sefaz.ce.gov.br/pages/consultaNota.jsf'
	    },
	    'RN': {
	    	#'QR': 'http://www.nfe.rn.gov.br/portal/consultarNFCe.jsp?',
	    	'QR': 'http://nfce.set.rn.gov.br/consultarNFCe.aspx?',
	    	'HTTPS': '',
	    	'HOMOLOGACAO': ''
	    	
	    },
	    'PB': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
	    },
	    'PE': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': 'sefaz.pe.gov.br/nfce-web/consultarNFCe?',
	    	'HTTPS': 'http://nfce.',
	    	'HOMOLOGACAO': 'http://nfcehomolog.',
	    	'URL': 'sefaz.pe.gov.br/nfce-web/consultarNFCe'
	    },
	    'AL': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
	    },
	    'SE': {
	    	'QR': 'nfe.se.gov.br/portal/consultarNFCe.jsp?',
	    	'HTTPS': 'https://www.',
	    	'HOMOLOGACAO': 'http://www.hom.'
	    },
	    'BA': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
	    },	
	    'MG': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
	    },
	    'ES': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
	    },
	    'RJ': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': 'http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?', 
	    	'URL': 'www.nfce.fazenda.rj.gov.br/consulta'
	    },
	    # Os Web Services de homologação da NFC-e 4.00 são: 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeAutorizacao4.asmx 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeStatusServico4.asmx 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeConsultaProtocolo4.asmx 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeRetAutorizacao4.asmx 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeRecepcaoEvento4.asmx 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeInutilizacao4.asmx 
	    'SP': {
	    	'STATUS': 'nfce.fazenda.sp.gov.br/ws/NFeStatusServico4.asmx',
	    	'AUTORIZACAO': 'nfce.fazenda.sp.gov.br/ws/NFeAutorizacao4.asmx',
	    	'RECIBO': 'nfce.fazenda.sp.gov.br/ws/NFeRetAutorizacao4.asmx',
	    	'CHAVE': 'nfce.fazenda.sp.gov.br/ws/NFeConsultaProtocolo4.asmx',
	    	'INUTILIZACAO': 'nfce.fazenda.sp.gov.br/ws/NFeInutilizacao4.asmx',
	    	'EVENTOS': 'nfce.fazenda.sp.gov.br/ws/NFeRecepcaoEvento4.asmx',
	    	'QR': 'nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?',
	    	'URL': 'nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaPublica.aspx',
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://homologacao.'
	    },
	    'PR': {
	    	'STATUS': 'nfce.sefa.pr.gov.br/nfce/NFeStatusServico4?wsdl',
	    	'AUTORIZACAO': 'nfce.sefa.pr.gov.br/nfce/NFeAutorizacao4?wsdl',
	    	'RECIBO': 'nfce.sefa.pr.gov.br/nfce/NFeRetAutorizacao4?wsdl',
	    	'CHAVE': 'nfce.sefa.pr.gov.br/nfce/NFeConsultaProtocolo4?wsdl',
	    	'INUTILIZACAO': 'nfce.sefa.pr.gov.br/nfce/NFeInutilizacao4?wsdl',
	    	'EVENTOS': 'nfce.sefa.pr.gov.br/nfce/NFeRecepcaoEvento4?wsdl',
	    	'CADASTRO': 'nfce.sefa.pr.gov.br/nfce/CadConsultaCadastro4?wsdl',
	    	'QR': 'http://www.fazenda.pr.gov.br/nfce/qrcode?',
	    	'URL': 'http://www.fazenda.pr.gov.br',
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://homologacao.'
	    },
	    'SC': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
	    },
	    'RS': {
	    	'STATUS': 'sefazrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx',
	    	'AUTORIZACAO': 'sefazrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx',
	    	'RECIBO': 'sefazrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
	    	'CHAVE': 'sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx',
	    	'INUTILIZACAO': 'sefazrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx',
	    	'EVENTOS': 'sefazrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx',
	    	'QR': 'https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?',
	    	'URL': 'https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx',
	    	'HTTPS': 'https://nfce.',
	    	'HOMOLOGACAO': 'https://nfce-homologacao.'
	    },
	    'MS': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
	    },
	    'MT': {
	    	'QR': 'sefaz.mt.gov.br/nfce/consultanfce?',
	    	'HTTPS': 'http://www.',
	    	'HOMOLOGACAO': 'http://homologacao.'
	    },
	    'GO': {
	    	'STATUS': 'sefaz.go.gov.br/nfe/services/v2/NfeStatusServico2',
	    	'AUTORIZACAO': 'sefaz.go.gov.br/nfe/services/v2/NfeAutorizacao',
	    	'RECIBO': 'sefaz.go.gov.br/nfe/services/v2/NfeRetAutorizacao',
	    	'CHAVE': 'sefaz.go.gov.br/nfe/services/v2/NfeConsulta2',
	    	'INUTILIZACAO': 'sefaz.go.gov.br/nfe/services/v2/NfeInutilizacao2',
	    	'EVENTOS': 'sefaz.go.gov.br/nfe/services/v2/RecepcaoEvento',
	    	'QR': 'sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe?',
	    	'CADASTRO': 'sefaz.go.gov.br/nfe/services/v2/CadConsultaCadastro2',
	    	'HTTPS': 'http://nfe.',
	    	'HOMOLOGACAO': 'http://homolog.'
	    },
	    # RO, AC, RR, PA, AP, TO, MA, PI, RN, PB, AL, SE, BA, ES, RJ, GO, DF
	    'SVRS': {
	    	'STATUS': 'svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx',
	    	'AUTORIZACAO': 'svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx',
	    	'RECIBO': 'svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
	    	'CHAVE': 'svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx',
	    	'INUTILIZACAO': 'svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx',
	    	'EVENTOS': 'svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx',
	    	'QR': '',
	    	'HTTPS': 'https://nfce.',
	    	'HOMOLOGACAO': 'https://nfce-homologacao.'
	    },
}

# Nfe
# homologação => http://hom.nfe.fazenda.gov.br/PORTAL/WebServices.aspx
# produção    => https://www.nfe.fazenda.gov.br/portal/webServices.aspx
NFE = {
		# Alguns serviços são disponibilizados apenas pelo ambiente nacional
		'AN': {
	    	'EVENTOS': 'nfe.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx',	# versao: 4.00
	    	'DISTRIBUICAO': 'nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx',
	    	'HTTPS': 'https://www',
	    	'HOMOLOGACAO': 'https://hom'
	    },
	    'AM': {
	    	'STATUS': 'nfe.sefaz.am.gov.br/services2/services/NfeStatusServico2',
	    	'AUTORIZACAO': 'nfe.sefaz.am.gov.br/services2/services/NfeAutorizacao',
	    	'RECIBO': 'nfe.sefaz.am.gov.br/services2/services/NfeRetAutorizacao',
	    	'CHAVE': 'nfe.sefaz.am.gov.br/services2/services/NfeConsulta2',
	    	'INUTILIZACAO': 'nfe.sefaz.am.gov.br/services2/services/NfeInutilizacao2',
	    	'EVENTOS': 'nfe.sefaz.am.gov.br/services2/services/RecepcaoEvento',
	    	'CADASTRO': 'nfe.sefaz.am.gov.br/services2/services/cadconsultacadastro2',
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://hom'
	    },
	    'MA': {
	    	'CADASTRO': 'https://sistemas.sefaz.ma.gov.br/wscadastro/CadConsultaCadastro2?wsdl'
	    },
	    'CE': {
	    	'STATUS': 'sefaz.ce.gov.br/nfe4/services/NFeStatusServico4?WSDL',
	    	'AUTORIZACAO': 'sefaz.ce.gov.br/nfe4/services/NFeAutorizacao4?WSDL',
	    	'RECIBO': 'sefaz.ce.gov.br/nfe4/services/NFeRetAutorizacao4?WSDL',
	    	'CHAVE': 'sefaz.ce.gov.br/nfe4/services/NFeConsultaProtocolo4?WSDL',
	    	'INUTILIZACAO': 'sefaz.ce.gov.br/nfe4/services/NFeInutilizacao4?WSDL',
	    	'EVENTOS': 'sefaz.ce.gov.br/nfe4/services/NFeRecepcaoEvento4?WSDL',
	    	'CADASTRO': 'sefaz.ce.gov.br/nfe2/services/CadConsultaCadastro2?wsdl',
	    	'DOWNLOAD': 'sefaz.ce.gov.br/nfe2/services/NfeDownloadNF?wsdl',
	    	'HTTPS': 'https://nfe.',
	    	'HOMOLOGACAO': 'https://nfeh.'
	    },
	    'PE': {
	    	'STATUS': 'sefaz.pe.gov.br/nfe-service/services/NFeStatusServico4',
	    	'AUTORIZACAO': 'sefaz.pe.gov.br/nfe-service/services/NFeAutorizacao4',
	    	'RECIBO': 'sefaz.pe.gov.br/nfe-service/services/NFeRetAutorizacao4',
	    	'CHAVE': 'sefaz.pe.gov.br/nfe-service/services/NFeConsultaProtocolo4',
	    	'INUTILIZACAO': 'sefaz.pe.gov.br/nfe-service/services/NFeInutilizacao4',
	    	'EVENTOS': 'sefaz.pe.gov.br/nfe-service/services/NFeRecepcaoEvento4',
	    	# 'CADASTRO': 'sefaz.pe.gov.br/nfe-service/services/CadConsultaCadastro2',
	    	'HTTPS': 'https://nfe.',
	    	'HOMOLOGACAO': 'https://nfehomolog.'
	    },
	    'BA': {
	    	'STATUS': 'nfe.sefaz.ba.gov.br/webservices/NFeStatusServico4/NFeStatusServico4.asmx',
	    	'AUTORIZACAO': 'nfe.sefaz.ba.gov.br/webservices/NFeAutorizacao4/NFeAutorizacao4.asmx',
	    	'RECIBO': 'nfe.sefaz.ba.gov.br/webservices/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx',
	    	'CHAVE': 'nfe.sefaz.ba.gov.br/webservices/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx',
	    	'INUTILIZACAO': 'nfe.sefaz.ba.gov.br/webservices/NFeInutilizacao4/NFeInutilizacao4.asmx',
	    	'EVENTOS': 'nfe.sefaz.ba.gov.br/webservices/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx',
	    	'CADASTRO': 'nfe.sefaz.ba.gov.br/webservices/CadConsultaCadastro4/CadConsultaCadastro4.asmx',
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://h'
	    },	
	    'MG': {
	    	'STATUS': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeStatusServico4',
	    	'AUTORIZACAO': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeAutorizacao4',
	    	'RECIBO': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeRetAutorizacao4',
	    	'CHAVE': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeConsulta4',
	    	'INUTILIZACAO': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeInutilizacao4',
	    	'EVENTOS': 'nfe.fazenda.mg.gov.br/nfe2/services/RecepcaoEvento',
	    	'CADASTRO': 'nfe.fazenda.mg.gov.br/nfe2/services/cadconsultacadastro2',
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://h'
	    },
	    'SP': {
	    	'STATUS': 'nfe.fazenda.sp.gov.br/ws/NFeStatusServico4.asmx',
	    	'AUTORIZACAO': 'nfe.fazenda.sp.gov.br/ws/nfeautorizacao4.asmx',
	    	'RECIBO': 'nfe.fazenda.sp.gov.br/ws/nferetautorizacao4.asmx',
	    	'CHAVE': 'nfe.fazenda.sp.gov.br/ws/nfeconsulta4.asmx',
	    	'INUTILIZACAO': 'nfe.fazenda.sp.gov.br/ws/nfeinutilizacao4.asmx',
	    	'EVENTOS': 'nfe.fazenda.sp.gov.br/ws/nferecepcaoevento4.asmx',
	    	'CADASTRO': 'nfe.fazenda.sp.gov.br/ws/cadconsultacadastro4.asmx',
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://homologacao.'
	    },
	    'PR': {
	    	'STATUS': 'nfe.sefa.pr.gov.br/nfe/NFeStatusServico4', 		    # CONSULTA STATUS DO SERVICO
	    	'AUTORIZACAO': 'nfe.sefa.pr.gov.br/nfe/NFeAutorizacao4',		# AUTORIZACAO
	    	'RECIBO': 'nfe.sefa.pr.gov.br/nfe/NFeRetAutorizacao4',		    # CONSULTA RECIBO
	    	'CHAVE': 'nfe.sefa.pr.gov.br/nfe/NFeConsultaProtocolo4',		# CONSULTA CHAVE DE ACESSO
	    	'INUTILIZACAO': 'nfe.sefa.pr.gov.br/nfe/NFeInutilizacao4',		# INUTILIZAÇAO
	    	'EVENTOS': 'nfe.sefa.pr.gov.br/nfe/NFeRecepcaoEvento4',			# REGISTRO DE EVENTOS
	    	'CADASTRO': 'nfe.sefa.pr.gov.br/nfe/CadConsultaCadastro4',		# CONSULTA CADASTRO
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://homologacao.'
	    },
	    # https://www.sefaz.rs.gov.br/site/MontaDuvidas.aspx?al=l_rel_end_ws_nfe
	    'RS': {
	    	'STATUS': 'sefazrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx',
	    	'AUTORIZACAO': 'sefazrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx',
	    	'RECIBO': 'sefazrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
	    	'CHAVE': 'sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx',
	    	'INUTILIZACAO': 'sefazrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx',
	    	'EVENTOS': 'sefazrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx',
	    	'CADASTRO': 'https://cad.sefazrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro2.asmx',
	    	'DOWNLOAD': 'sefazrs.rs.gov.br/ws/nfeDownloadNF/nfeDownloadNF.asmx',
	    	'DESTINADAS': 'sefazrs.rs.gov.br/ws/nfeConsultaDest/nfeConsultaDest.asmx',
	    	'HTTPS': 'https://nfe.',
	    	'HOMOLOGACAO': 'https://nfe-homologacao.'
	    },
	    'MS': {
	    	'STATUS': 'nfe.ms.gov.br/ws/NFeStatusServico4',
	    	'AUTORIZACAO': 'nfe.ms.gov.br/ws/NFeAutorizacao4',
	    	'RECIBO': 'nfe.ms.gov.br/ws/NFeRetAutorizacao4',
	    	'CHAVE': 'nfe.ms.gov.br/ws/NFeConsultaProtocolo4',
	    	'INUTILIZACAO': 'nfe.ms.gov.br/ws/NFeInutilizacao4',
	    	'EVENTOS': 'nfe.ms.gov.br/ws/NFeRecepcaoEvento4',
	    	'CADASTRO': 'nfe.fazenda.ms.gov.br/producao/services2/CadConsultaCadastro2',
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://homologacao.'
	    },
	    'MT': {
	    	'STATUS': 'sefaz.mt.gov.br/nfews/v2/services/NfeStatusServico2?wsdl',
	    	'AUTORIZACAO': 'sefaz.mt.gov.br/nfews/v2/services/NfeAutorizacao?wsdl',
	    	'RECIBO': 'sefaz.mt.gov.br/nfews/v2/services/NfeRetAutorizacao?wsdl',
	    	'CHAVE': 'sefaz.mt.gov.br/nfews/v2/services/NfeConsulta2?wsdl',
	    	'INUTILIZACAO': 'sefaz.mt.gov.br/nfews/v2/services/NfeInutilizacao2?wsdl',
	    	'EVENTOS': 'sefaz.mt.gov.br/nfews/v2/services/RecepcaoEvento?wsdl',
	    	'CADASTRO': 'sefaz.mt.gov.br/nfews/v2/services/CadConsultaCadastro2?wsdl',
	    	'HTTPS': 'https://nfe.',
	    	'HOMOLOGACAO': 'https://homologacao.'
	    },
	    'GO': {
	    	'STATUS': 'sefaz.go.gov.br/nfe/services/NFeStatusServico4?wsdl',
	    	'AUTORIZACAO': 'sefaz.go.gov.br/nfe/services/NFeAutorizacao4?wsdl',
	    	'RECIBO': 'sefaz.go.gov.br/nfe/services/NFeRetAutorizacao4?wsdl',
	    	'CHAVE': 'sefaz.go.gov.br/nfe/services/NFeConsultaProtocolo4?wsdl',
	    	'INUTILIZACAO': 'sefaz.go.gov.br/nfe/services/NFeInutilizacao4?wsdl',
	    	'EVENTOS': 'sefaz.go.gov.br/nfe/services/NFeRecepcaoEvento4?wsdl',
	    	'CADASTRO': 'sefaz.go.gov.br/nfe/services/CadConsultaCadastro4?wsdl',
	    	'HTTPS': 'https://nfe.',
	    	'HOMOLOGACAO': 'https://homolog.'
	    },
	    'SVAN': {
	    	'STATUS': 'sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx',
	    	'AUTORIZACAO': 'sefazvirtual.fazenda.gov.br/NFeAutorizacao4/NFeAutorizacao4.asmx',
	    	'RECIBO': 'sefazvirtual.fazenda.gov.br/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx',
	    	'CHAVE': 'sefazvirtual.fazenda.gov.br/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx',
	    	'INUTILIZACAO': 'sefazvirtual.fazenda.gov.br/NFeInutilizacao4/NFeInutilizacao4.asmx',
	    	'EVENTOS': 'sefazvirtual.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx',
	    	'DOWNLOAD': 'sefazvirtual.fazenda.gov.br/NfeDownloadNF/NfeDownloadNF.asmx',
	    	'HTTPS': 'https://www.',
	    	'HOMOLOGACAO': 'https://hom.'
	    },
	    'SVRS': {
	    	'STATUS': 'svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx',
	    	'AUTORIZACAO': 'svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx',
	    	'RECIBO': 'svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
	    	'CHAVE': 'svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx',
	    	'INUTILIZACAO': 'svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx',
	    	'EVENTOS': 'svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx',
	    	'CADASTRO': 'https://cad.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro2.asmx',
	    	'HTTPS': 'https://nfe.',
	    	'HOMOLOGACAO': 'https://nfe-homologacao.'
	    },
	    'SVC-AN': {
	    	'STATUS': 'svc.fazenda.gov.br/NfeStatusServico2/NfeStatusServico2.asmx',
	    	'AUTORIZACAO': 'svc.fazenda.gov.br/NfeAutorizacao/NfeAutorizacao.asmx',
	    	'RECIBO': 'svc.fazenda.gov.br/NfeRetAutorizacao/NfeRetAutorizacao.asmx',
	    	'CHAVE': 'svc.fazenda.gov.br/NfeConsulta2/NfeConsulta2.asmx',
	    	'EVENTOS': 'svc.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx',
	    	'HTTPS': 'https://www.',
	    	'HOMOLOGACAO': 'https://hom.'
	    },
	    'SVC-RS': {
	    	'STATUS': 'svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx',
	    	'AUTORIZACAO': 'svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx',
	    	'RECIBO': 'svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx',
	    	'CHAVE': 'svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx',
	    	'INUTILIZACAO': 'svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao2.asmx',
	    	'EVENTOS': 'svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx',
	    	'HTTPS': 'https://nfe.',
	    	'HOMOLOGACAO': 'https://nfe-homologacao.'
	    },
}

# Nfs-e
NFSE = {
	# 
	'BETHA': {
		'AUTORIZACAO':'GerarNfse',
		'CANCELAR':'CancelarNfse',
		'CONSULTA_RPS':'consultarNfsePorRps',
		'CONSULTA_FAIXA':'ConsultarNfseFaixa',
		'CONSULTA_SERVICO':'ConsultarNfseServicoPrestado',
		'CONSULTA_SERVICO_TOMADO':'ConsultarNfseServicoTomado',
		'SUBSTITUIR':'SubstituirNfse',
		'HTTPS':'http://e-gov.betha.com.br/e-nota-contribuinte-ws/nfseWS?wsdl',
		'HOMOLOGACAO':'http://e-gov.betha.com.br/e-nota-contribuinte-test-ws/nfseWS?wsdl'
	},
	#
	'GINFES':{
		'AUTORIZACAO':'GerarNfse',
		'CANCELAR':'CancelarNfse',
		'CONSULTA_RPS':'ConsultarNfsePorRps',
		'CONSULTA_FAIXA':'ConsultarNfseFaixa',
		'CONSULTA_SERVICO':'ConsultarNfseServicoPrestado',
		'CONSULTA_SERVICO_TOMADO':'ConsultarNfseServicoTomado',
		'SUBSTITUIR':'SubstituirNfse',
		'HTTPS':'https://producao.ginfes.com.br/ServiceGinfesImpl?wsdl',
		'HOMOLOGACAO':'https://homologacao.ginfes.com.br/ServiceGinfesImpl?wsdl'
	}
}