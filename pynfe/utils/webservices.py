
"""
	@author: Junior Tada, Leonardo Tada
"""

# Nfc-e
NFCE = {
	    'RO': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
	    },
	    'AC': {
	    	'QR': 'sefaznet.ac.gov.br/nfce?',
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
	    	'QR': ''
	    },
	    'PA': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
	    },
	    'AP': {
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
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
	    	'QR': ''
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
	    	'QR': ''
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
	    	'QR': ''
	    },
	    # Os Web Services de homologação da NFC-e 4.00 são: 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeAutorizacao4.asmx 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeStatusServico4.asmx 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeConsultaProtocolo4.asmx 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeRetAutorizacao4.asmx 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeRecepcaoEvento4.asmx 
		# https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeInutilizacao4.asmx 
	    'SP': {
	    	'STATUS': 'nfce.fazenda.sp.gov.br/ws/nfestatusservico2.asmx',
	    	'AUTORIZACAO': 'nfce.fazenda.sp.gov.br/ws/nfeautorizacao.asmx',
	    	'RECIBO': 'nfce.fazenda.sp.gov.br/ws/nferetautorizacao.asmx',
	    	'CHAVE': 'nfce.fazenda.sp.gov.br/ws/nfeconsulta2.asmx',
	    	'INUTILIZACAO': 'nfce.fazenda.sp.gov.br/ws/nfeinutilizacao2.asmx',
	    	'EVENTOS': 'nfce.fazenda.sp.gov.br/ws/recepcaoevento.asmx',
	    	'QR': 'nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?',
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://homologacao.'
	    },
	    'PR': {
	    	'STATUS': 'nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3',
	    	'AUTORIZACAO': 'nfce.fazenda.pr.gov.br/nfce/NFeAutorizacao3',
	    	'RECIBO': 'nfce.fazenda.pr.gov.br/nfce/NFeRetAutorizacao3',
	    	'CHAVE': 'nfce.fazenda.pr.gov.br/nfce/NFeConsulta3',
	    	'INUTILIZACAO': 'nfce.fazenda.pr.gov.br/nfce/NFeInutilizacao3',
	    	'EVENTOS': 'nfce.fazenda.pr.gov.br/nfce/NFeRecepcaoEvento',
	    	'QR': 'http://www.dfeportal.fazenda.pr.gov.br/dfe-portal/rest/servico/consultaNFCe?',
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
	    	'STATUS': 'sefazrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx',
	    	'AUTORIZACAO': 'sefazrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx',
	    	'RECIBO': 'sefazrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx',
	    	'CHAVE': 'sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx',
	    	'INUTILIZACAO': 'sefazrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao2.asmx',
	    	'EVENTOS': 'sefazrs.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx',
	    	'QR': 'https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?',
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
	    	'STATUS': 'svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx',
	    	'AUTORIZACAO': 'svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx',
	    	'RECIBO': 'svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx',
	    	'CHAVE': 'svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx',
	    	'INUTILIZACAO': 'svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao2.asmx',
	    	'EVENTOS': 'svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx',
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
	    	'DOWNLOAD': 'nfe.fazenda.gov.br/NfeDownloadNF/NfeDownloadNF.asmx', 				# versao: 2.00/3.10
	    	'DESTINADAS': 'nfe.fazenda.gov.br/NFeConsultaDest/NFeConsultaDest.asmx',		# versao: 2.00/3.10
	    	'HTTPS': 'https://www.',
	    	'HOMOLOGACAO': 'https://hom.'
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
	    	'STATUS': 'sefaz.pe.gov.br/nfe-service/services/NfeStatusServico2',
	    	'AUTORIZACAO': 'sefaz.pe.gov.br/nfe-service/services/NfeAutorizacao?wsdl',
	    	'RECIBO': 'sefaz.pe.gov.br/nfe-service/services/NfeRetAutorizacao?wsdl',
	    	'CHAVE': 'sefaz.pe.gov.br/nfe-service/services/NfeConsulta2',
	    	'INUTILIZACAO': 'sefaz.pe.gov.br/nfe-service/services/NfeInutilizacao2',
	    	'EVENTOS': 'sefaz.pe.gov.br/nfe-service/services/RecepcaoEvento',
	    	'CADASTRO': 'sefaz.pe.gov.br/nfe-service/services/CadConsultaCadastro2',
	    	'HTTPS': 'https://nfe.',
	    	'HOMOLOGACAO': 'https://nfehomolog.'
	    },
	    'BA': {
	    	'STATUS': 'nfe.sefaz.ba.gov.br/webservices/NfeStatusServico/NfeStatusServico.asmx',
	    	'AUTORIZACAO': 'nfe.sefaz.ba.gov.br/webservices/NfeAutorizacao/NfeAutorizacao.asmx',
	    	'RECIBO': 'nfe.sefaz.ba.gov.br/webservices/NfeRetAutorizacao/NfeRetAutorizacao.asmx',
	    	'CHAVE': 'nfe.sefaz.ba.gov.br/webservices/NfeConsulta/NfeConsulta.asmx',
	    	'INUTILIZACAO': 'nfe.sefaz.ba.gov.br/webservices/NfeInutilizacao/NfeInutilizacao.asmx',
	    	'EVENTOS': 'nfe.sefaz.ba.gov.br/webservices/sre/recepcaoevento.asmx',
	    	'CADASTRO': 'nfe.sefaz.ba.gov.br/webservices/nfenw/CadConsultaCadastro2.asmx',
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
	    	'STATUS': 'sefazvirtual.fazenda.gov.br/NfeStatusServico2/NfeStatusServico2.asmx',
	    	'AUTORIZACAO': 'sefazvirtual.fazenda.gov.br/NfeAutorizacao/NfeAutorizacao.asmx',
	    	'RECIBO': 'sefazvirtual.fazenda.gov.br/NfeRetAutorizacao/NfeRetAutorizacao.asmx',
	    	'CHAVE': 'sefazvirtual.fazenda.gov.br/NfeConsulta2/NfeConsulta2.asmx',
	    	'INUTILIZACAO': 'sefazvirtual.fazenda.gov.br/NfeInutilizacao2/NfeInutilizacao2.asmx',
	    	'EVENTOS': 'sefazvirtual.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx',
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