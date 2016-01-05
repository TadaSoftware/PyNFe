
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
	    'SP': {
	    	'STATUS': 'nfce.fazenda.sp.gov.br/ws/nfestatusservico2.asmx',
	    	'AUTORIZACAO': 'nfce.fazenda.sp.gov.br/ws/nfeautorizacao.asmx',
	    	'RECIBO': 'nfce.fazenda.sp.gov.br/ws/nferetautorizacao.asmx',
	    	'CHAVE': 'nfce.fazenda.sp.gov.br/ws/nfeconsulta2.asmx',
	    	'INUTILIZACAO': 'nfce.fazenda.sp.gov.br/ws/nfeinutilizacao2.asmx',
	    	'EVENTOS': 'nfce.fazenda.sp.gov.br/ws/recepcaoevento.asmx',
	    	'QR': 'nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?',
	    	'HTTPS': 'https://www.',
	    	'HOMOLOGACAO': 'https://www.homologacao.'
	    },
	    'PR': {
	    	'STATUS': 'nfce.fazenda.pr.gov.br/nfce/NFeStatusServico3',
	    	'AUTORIZACAO': 'nfce.fazenda.pr.gov.br/nfce/NFeAutorizacao3',
	    	'RECIBO': 'nfce.fazenda.pr.gov.br/nfce/NFeRetAutorizacao3',
	    	'CHAVE': 'nfce.fazenda.pr.gov.br/nfce/NFeConsulta3',
	    	'INUTILIZACAO': 'nfce.fazenda.pr.gov.br/nfce/NFeInutilizacao3',
	    	'EVENTOS': 'nfce.fazenda.pr.gov.br/nfce/NFeRecepcaoEvento',
	    	'QR': ' http://www.dfeportal.fazenda.pr.gov.br/dfe-portal/rest/servico/consultaNFCe?',
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
	    	'HTTPS': '',
	    	'HOMOLOGACAO': ''
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
	    	'STATUS': '',
	    	'AUTORIZACAO': '',
	    	'RECIBO': '',
	    	'CHAVE': '',
	    	'INUTILIZACAO': '',
	    	'EVENTOS': '',
	    	'QR': ''
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
NFE = {
		# Alguns serviços são disponibilizados apenas pelo ambiente nacional
		'AN': {
	    	'EVENTOS': 'nfe.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx',	# versao: 1.00
	    	'DISTRIBUICAO': 'nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx',
	    	'DOWNLOAD': 'nfe.fazenda.gov.br/NfeDownloadNF/NfeDownloadNF.asmx', 				# versao: 2.00/3.10
	    	'DESTINADAS': '.nfe.fazenda.gov.br/NFeConsultaDest/NFeConsultaDest.asmx',		# versao: 2.00/3.10
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
	    	'STATUS': 'sefaz.ce.gov.br/nfe2/services/NfeStatusServico2?wsdl',
	    	'AUTORIZACAO': 'sefaz.ce.gov.br/nfe2/services/NfeAutorizacao?wsdl',
	    	'RECIBO': 'sefaz.ce.gov.br/nfe2/services/NfeRetAutorizacao?wsdl',
	    	'CHAVE': 'sefaz.ce.gov.br/nfe2/services/NfeConsulta2?wsdl',
	    	'INUTILIZACAO': 'sefaz.ce.gov.br/nfe2/services/NfeInutilizacao2?wsdl',
	    	'EVENTOS': 'sefaz.ce.gov.br/nfe2/services/RecepcaoEvento?wsdl',
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
	    	'STATUS': 'nfe.fazenda.mg.gov.br/nfe2/services/NfeStatus2',
	    	'AUTORIZACAO': 'nfe.fazenda.mg.gov.br/nfe2/services/NfeAutorizacao',
	    	'RECIBO': 'nfe.fazenda.mg.gov.br/nfe2/services/NfeRetAutorizacao',
	    	'CHAVE': 'nfe.fazenda.mg.gov.br/nfe2/services/NfeConsulta2',
	    	'INUTILIZACAO': 'nfe.fazenda.mg.gov.br/nfe2/services/NfeInutilizacao2',
	    	'EVENTOS': 'nfe.fazenda.mg.gov.br/nfe2/services/RecepcaoEvento',
	    	'CADASTRO': 'nfe.fazenda.mg.gov.br/nfe2/services/cadconsultacadastro2',
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://h'
	    },
	    'SP': {
	    	'STATUS': 'nfe.fazenda.sp.gov.br/ws/nfestatusservico2.asmx',
	    	'AUTORIZACAO': 'nfe.fazenda.sp.gov.br/ws/nfeautorizacao.asmx',
	    	'RECIBO': 'nfe.fazenda.sp.gov.br/ws/nferetautorizacao.asmx',
	    	'CHAVE': 'nfe.fazenda.sp.gov.br/ws/nfeconsulta2.asmx',
	    	'INUTILIZACAO': 'nfe.fazenda.sp.gov.br/ws/nfeinutilizacao2.asmx',
	    	'EVENTOS': 'nfe.fazenda.sp.gov.br/ws/recepcaoevento.asmx',
	    	'CADASTRO': 'nfe.fazenda.sp.gov.br/ws/cadconsultacadastro2.asmx',
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://homologacao.'
	    },
	    'PR': {
	    	'STATUS': 'nfe.fazenda.pr.gov.br/nfe/NFeStatusServico3', 		# CONSULTA STATUS DO SERVICO
	    	'AUTORIZACAO': 'nfe.fazenda.pr.gov.br/nfe/NFeAutorizacao3',		# AUTORIZACAO
	    	'RECIBO': 'nfe.fazenda.pr.gov.br/nfe/NFeRetAutorizacao3',		# CONSULTA RECIBO
	    	'CHAVE': 'nfe.fazenda.pr.gov.br/nfe/NFeConsulta3',				# CONSULTA CHAVE DE ACESSO
	    	'INUTILIZACAO': 'nfe.fazenda.pr.gov.br/nfe/NFeInutilizacao3',	# INUTILIZAÇAO
	    	'EVENTOS': 'nfe.fazenda.pr.gov.br/nfe/NFeRecepcaoEvento',		# REGISTRO DE EVENTOS
	    	'CADASTRO': 'nfe.fazenda.pr.gov.br/nfe/CadConsultaCadastro2',	# CONSULTA CADASTRO
	    	'HTTPS': 'https://',
	    	'HOMOLOGACAO': 'https://homologacao.'
	    },
	    'RS': {
	    	'STATUS': 'sefazrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx',
	    	'AUTORIZACAO': 'sefazrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx',
	    	'RECIBO': 'sefazrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx',
	    	'CHAVE': 'sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx',
	    	'INUTILIZACAO': 'sefazrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao2.asmx',
	    	'EVENTOS': 'sefazrs.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx',
	    	'CADASTRO': 'sefazrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro2.asmx',
	    	'DOWNLOAD': 'sefazrs.rs.gov.br/ws/nfeDownloadNF/nfeDownloadNF.asmx',
	    	'DESTINADAS': 'sefazrs.rs.gov.br/ws/nfeConsultaDest/nfeConsultaDest.asmx',
	    	'HTTPS': 'https://nfe.',
	    	'HOMOLOGACAO': 'https://nfe-homologacao.'
	    },
	    'MS': {
	    	'STATUS': 'nfe.fazenda.ms.gov.br/producao/services2/NfeStatusServico2',
	    	'AUTORIZACAO': 'nfe.fazenda.ms.gov.br/producao/services2/NfeAutorizacao',
	    	'RECIBO': 'nfe.fazenda.ms.gov.br/producao/services2/NfeRetAutorizacao',
	    	'CHAVE': 'nfe.fazenda.ms.gov.br/producao/services2/NfeConsulta2',
	    	'INUTILIZACAO': 'nfe.fazenda.ms.gov.br/producao/services2/NfeInutilizacao2',
	    	'EVENTOS': 'nfe.fazenda.ms.gov.br/producao/services2/RecepcaoEvento',
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
	    	'STATUS': 'sefaz.go.gov.br/nfe/services/v2/NfeStatusServico2?wsdl',
	    	'AUTORIZACAO': 'sefaz.go.gov.br/nfe/services/v2/NfeAutorizacao?wsdl',
	    	'RECIBO': 'sefaz.go.gov.br/nfe/services/v2/NfeRetAutorizacao?wsdl',
	    	'CHAVE': 'sefaz.go.gov.br/nfe/services/v2/NfeConsulta2?wsdl',
	    	'INUTILIZACAO': 'sefaz.go.gov.br/nfe/services/v2/NfeInutilizacao2?wsdl',
	    	'EVENTOS': 'sefaz.go.gov.br/nfe/services/v2/RecepcaoEvento?wsdl',
	    	'CADASTRO': 'sefaz.go.gov.br/nfe/services/v2/CadConsultaCadastro2?wsdl',
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
	    	'STATUS': 'svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx',
	    	'AUTORIZACAO': 'svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx',
	    	'RECIBO': 'svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx',
	    	'CHAVE': 'svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx',
	    	'INUTILIZACAO': 'svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao2.asmx',
	    	'EVENTOS': 'svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx',
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