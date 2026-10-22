"""
@author: Junior Tada, Leonardo Tada

Host de CONSULTA vs host de AUTORIZADOR
---------------------------------------
Numa UF, o portal publico de consulta (destino do ``<qrCode>``/``<urlChave>``) e o
autorizador (webservices SOAP com mTLS) podem ser servidores DIFERENTES. Por isso as
duas familias de chave sao separadas em ``NFCE`` e nunca devem ser reaproveitadas
uma pela outra:

- ``HTTPS`` / ``HOMOLOGACAO``: prefixo de host do AUTORIZADOR, lido apenas por
  ``ComunicacaoSefaz._get_url`` para montar URLs de webservice.
- ``QR_HOST`` / ``QR_HOST_HOMOLOGACAO``: prefixo de host do portal de CONSULTA, lido
  apenas por ``qrcode_host`` (usado em ``SerializacaoQrcode.gerar_qrcode``).

Apontar webservice para o host de consulta nao gera rejeicao: o portal responde
redirect + HTML, entao a nota nunca recebe veredito da SEFAZ. Ao atualizar o host de
consulta de uma UF, mexa somente nas chaves ``QR_*``.

``qrCode`` vs ``urlChave``
-------------------------
Sao dois campos do ``<infNFeSupl>`` com registros oficiais DIFERENTES, cada um lido da
sua propria entrada - nunca do campo irmao:

- ``<qrCode>``: endereco do leitor de QR Code (``QR``/``QR_HOMOLOGACAO`` sobre
  ``qrcode_host``).
- ``<urlChave>``: endereco da "Consulta por chave de acesso" (``URL-ConsultaNFCe_2.00``
  no registro do ACBr / ENCAT), lido por ``url_consulta_chave``.

Para o ``urlChave`` a chave dedicada e ``CONSULTA_CHAVE`` /
``CONSULTA_CHAVE_HOMOLOGACAO``, que guarda a URL COMPLETA e VERBATIM do registro -
inclusive o esquema quando o registro o traz, e sem esquema quando nao traz. Nenhum
prefixo de host e concatenado nesse valor: foi exatamente essa concatenacao sobre uma
URL ja completa que produziu lixo como ``https://nfce.http://www.dfe.ms.gov.br/...``
nas UFs que ainda dependem do caminho legado ``URL``. Ao registrar uma UF nova,
declare ``CONSULTA_CHAVE`` em vez de mexer em ``URL``.

Usar o endereco de QR Code no ``urlChave`` gera rejeicao 878 em GO ("Endereco do site
da UF da Consulta por chave de acesso diverge do previsto") - DEV-2468. A igualdade entre
os dois campos nao e por si um defeito: em algumas UFs o registro oficial declara o mesmo
endereco nos dois (SC hoje). O conjunto fechado dessas UFs esta travado em
``tests/test_nfce_urlchave_por_uf.py``; compare sempre com a entrada do registro do campo
que voce esta mexendo.
"""

# http://nfce.encat.org/desenvolvedor/qrcode/
# http://nfce.encat.org/consumidor/consulte-sua-nota/ 	url consulta por chave
# Nfc-e
NFCE = {
    "RO": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "http://www.nfce.sefin.ro.gov.br/consultanfce/consulta.jsp?",
        "URL": "http://www.nfce.sefin.ro.gov.br",
    },
    "AC": {
        "QR": "sefaznet.ac.gov.br/nfce?",
        "URL": "sefaznet.ac.gov.br/nfce/consulta",
        "HTTPS": "http://www.",
        "HOMOLOGACAO": "http://hml.",
    },
    "AM": {
        # csc_homologacao = '0123456789'
        # token_homologacao = '000001'
        "STATUS": "nfce.sefaz.am.gov.br/nfce-services/services/NfeStatusServico4",
        "AUTORIZACAO": "nfce.sefaz.am.gov.br/nfce-services/services/NfeAutorizacao4",
        "RECIBO": "nfce.sefaz.am.gov.br/nfce-services/services/NfeRetAutorizacao4",
        "CHAVE": "nfce.sefaz.am.gov.br/nfce-services/services/NfeConsulta4",
        "INUTILIZACAO": "nfce.sefaz.am.gov.br/nfce-services/services/NfeInutilizacao4",
        "EVENTOS": "nfce.sefaz.am.gov.br/nfce-services/services/RecepcaoEvento4",
        "QR": "sefaz.am.gov.br/nfceweb/consultarNFCe.jsp?",
        "QR_HOMOLOGACAO": "sefaz.am.gov.br/nfceweb-hom/consultarNFCe.jsp?",
        "URL": "sefaz.am.gov.br/nfceweb/formConsulta.do",
        # Host do AUTORIZADOR (webservices SOAP, mTLS) - os caminhos acima ja embutem o
        # subdominio "nfce.", entao o prefixo de producao e apenas o esquema.
        "HTTPS": "https://",
        "HOMOLOGACAO": "https://hom",
        # Host do portal de CONSULTA (qrCode/urlChave).
        "QR_HOST": "https://sistemas.",
        "QR_HOST_HOMOLOGACAO": "https://sistemas.",
    },
    "RR": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "/nfce/servlet/qrcode?",
        "URL": "/nfce/servlet/wp_consulta_nfce",
        "HTTPS": "https://www.sefaz.rr.gov.br",
        "HOMOLOGACAO": "http://200.174.88.103:8080",
    },
    "PA": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "view/consultas/nfce/nfceForm.seam?",
        "URL": "view/consultas/nfce/consultanfce.seam",
        "HTTPS": "https://appnfc.sefa.pa.gov.br/portal/",
        "HOMOLOGACAO": "https://appnfc.sefa.pa.gov.br/portal-homologacao/",
    },
    "AP": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "/nfcep.php?",
        "URL": "https://www.sefaz.ap.gov.br/sate/seg/SEGf_AcessarFuncao.jsp?cdFuncao=FIS_1261",
        "HTTPS": "https://www.sefaz.ap.gov.br/nfce",
        "HOMOLOGACAO": "https://www.sefaz.ap.gov.br/nfcehml",
    },
    "TO": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "",
    },
    "MA": {
        "QR": "nfce.sefaz.ma.gov.br/portal/consultarNFCe.jsp?",
        "HTTPS": "http://www.",
        "HOMOLOGACAO": "http://www.hom.",
    },
    "PI": {
        "QR": "sefaz.pi.gov.br/nfceweb/consultarNFCe.jsf?",
        "HTTPS": "http://webas.",
        "HOMOLOGACAO": "http://webas.",
    },
    "CE": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "http://nfceh.sefaz.ce.gov.br/pages/ShowNFCe.html?",
        "URL": "http://nfceh.sefaz.ce.gov.br/pages/consultaNota.jsf",
    },
    "RN": {
        # 'QR': 'http://www.nfe.rn.gov.br/portal/consultarNFCe.jsp?',
        "QR": "http://nfce.set.rn.gov.br/consultarNFCe.aspx?",
        "HTTPS": "",
        "HOMOLOGACAO": "",
    },
    "PB": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "http://www.sefaz.pb.gov.br/nfce",
    },
    "PE": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "sefaz.pe.gov.br/nfce-web/consultarNFCe",
        "HTTPS": "http://nfce.",
        "HOMOLOGACAO": "http://nfcehomolog.",
        "URL": "sefaz.pe.gov.br/nfce/consulta",
    },
    "AL": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "",
    },
    "SE": {
        "QR": "nfe.se.gov.br/portal/consultarNFCe.jsp?",
        "HTTPS": "https://www.",
        "HOMOLOGACAO": "http://www.hom.",
        "URL": "nfe.se.gov.br/nfce/consulta",
    },
    "BA": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "sefaz.ba.gov.br/servicos/nfce/qrcode.aspx?",
        "HTTPS": "http://nfe.",
        "HOMOLOGACAO": "http://hnfe.",
        "URL": "http://hinternet.sefaz.ba.gov.br/nfce/consulta",
        # ACBrNFeServicos.ini [NFCe_BA_P]/[NFCe_BA_H] URL-ConsultaNFCe_2.00. O "URL" acima
        # era o valor de homologacao, emitido tambem em producao.
        "CONSULTA_CHAVE": "http://www.sefaz.ba.gov.br/nfce/consulta",
        "CONSULTA_CHAVE_HOMOLOGACAO": "http://hinternet.sefaz.ba.gov.br/nfce/consulta",
    },
    "MG": {
        "STATUS": "fazenda.mg.gov.br/nfce/services/NFeStatusServico4",
        "AUTORIZACAO": "fazenda.mg.gov.br/nfce/services/NFeAutorizacao4",
        "RECIBO": "fazenda.mg.gov.br/nfce/services/NFeRetAutorizacao4",
        "CHAVE": "fazenda.mg.gov.br/nfce/services/NFeConsultaProtocolo4",
        "INUTILIZACAO": "fazenda.mg.gov.br/nfce/services/NFeInutilizacao4",
        "EVENTOS": "fazenda.mg.gov.br/nfce/services/NFeRecepcaoEvento4",
        "CADASTRO": "fazenda.mg.gov.br/nfce/services/CadConsultaCadastro4",
        "QR": "https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml",
        "HTTPS": "https://nfce.",
        "HOMOLOGACAO": "https://hnfce.",
        "URL": "fazenda.mg.gov.br/portalnfce",
    },
    "ES": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "sefaz.es.gov.br/ConsultaNFCe/qrcode.aspx?",
        "HTTPS": "http://nfe.",
        "HOMOLOGACAO": "http://homologacao.",
        "URL": "www.sefaz.es.gov.br/nfce/consulta",
    },
    "RJ": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?",
        "URL": "www.fazenda.rj.gov.br/nfce/consulta",
    },
    # Os Web Services de homologação da NFC-e 4.00 são:
    # https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeAutorizacao4.asmx
    # https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeStatusServico4.asmx
    # https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeConsultaProtocolo4.asmx
    # https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeRetAutorizacao4.asmx
    # https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeRecepcaoEvento4.asmx
    # https://homologacao.nfce.fazenda.sp.gov.br/ws/NFeInutilizacao4.asmx
    "SP": {
        "STATUS": "nfce.fazenda.sp.gov.br/ws/NFeStatusServico4.asmx",
        "AUTORIZACAO": "nfce.fazenda.sp.gov.br/ws/NFeAutorizacao4.asmx",
        "RECIBO": "nfce.fazenda.sp.gov.br/ws/NFeRetAutorizacao4.asmx",
        "CHAVE": "nfce.fazenda.sp.gov.br/ws/NFeConsultaProtocolo4.asmx",
        "INUTILIZACAO": "nfce.fazenda.sp.gov.br/ws/NFeInutilizacao4.asmx",
        "EVENTOS": "nfce.fazenda.sp.gov.br/ws/NFeRecepcaoEvento4.asmx",
        "QR": "nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?",
        "URL": "nfce.fazenda.sp.gov.br/consulta",
        "HTTPS": "https://",
        "HOMOLOGACAO": "https://homologacao.",
        "QR_HOST": "https://www.",
        "QR_HOST_HOMOLOGACAO": "https://www.homologacao.",
    },
    "PR": {
        "STATUS": "nfce.sefa.pr.gov.br/nfce/NFeStatusServico4?wsdl",
        "AUTORIZACAO": "nfce.sefa.pr.gov.br/nfce/NFeAutorizacao4?wsdl",
        "RECIBO": "nfce.sefa.pr.gov.br/nfce/NFeRetAutorizacao4?wsdl",
        "CHAVE": "nfce.sefa.pr.gov.br/nfce/NFeConsultaProtocolo4?wsdl",
        "INUTILIZACAO": "nfce.sefa.pr.gov.br/nfce/NFeInutilizacao4?wsdl",
        "EVENTOS": "nfce.sefa.pr.gov.br/nfce/NFeRecepcaoEvento4?wsdl",
        "CADASTRO": "nfce.sefa.pr.gov.br/nfce/CadConsultaCadastro4?wsdl",
        "QR": "http://www.fazenda.pr.gov.br/nfce/qrcode?",
        "URL": "http://www.fazenda.pr.gov.br/nfce/consulta",
        # ACBrNFeServicos.ini [NFCe_PR_P]/[NFCe_PR_H] URL-ConsultaNFCe_2.00 - mesmo valor nos
        # dois ambientes, byte-identico ao que o caminho legado ja emitia.
        "CONSULTA_CHAVE": "http://www.fazenda.pr.gov.br/nfce/consulta",
        "CONSULTA_CHAVE_HOMOLOGACAO": "http://www.fazenda.pr.gov.br/nfce/consulta",
        "HTTPS": "https://",
        "HOMOLOGACAO": "https://homologacao.",
    },
    "SC": {
        "STATUS": "",
        "AUTORIZACAO": "",
        "RECIBO": "",
        "CHAVE": "",
        "INUTILIZACAO": "",
        "EVENTOS": "",
        "QR": "sat.sef.sc.gov.br/nfce/consulta?",
        "HTTPS": "https://",
        "HOMOLOGACAO": "https://hom.",
        "URL": "sat.sef.sc.gov.br/nfce/consulta",
    },
    "RS": {
        "STATUS": "sefazrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
        "AUTORIZACAO": "sefazrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
        "RECIBO": "sefazrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        "CHAVE": "sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
        "INUTILIZACAO": "sefazrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
        "EVENTOS": "sefazrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
        "QR": "https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?",
        "URL": "https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx",
        "HTTPS": "https://nfce.",
        "HOMOLOGACAO": "https://nfce-homologacao.",
    },
    "MS": {
        "STATUS": "sefaz.ms.gov.br/ws/NFeStatusServico4?wsdl",
        "AUTORIZACAO": "sefaz.ms.gov.br/ws/NFeAutorizacao4?wsdl",
        "RECIBO": "sefaz.ms.gov.br/ws/NFeRetAutorizacao4?wsdl",
        "CHAVE": "sefaz.ms.gov.br/ws/NFeConsultaProtocolo4?wsdl",
        "INUTILIZACAO": "sefaz.ms.gov.br/ws/NFeInutilizacao4?wsdl",
        "EVENTOS": "sefaz.ms.gov.br/ws/NFeRetAutorizacao4",
        "QR": "http://www.dfe.ms.gov.br/nfce/qrcode",
        "URL": "http://www.dfe.ms.gov.br/nfce/consulta",
        "HTTPS": "https://nfce.",
        "HOMOLOGACAO": "https://hom.nfce.",
    },
    "MT": {
        "QR": "sefaz.mt.gov.br/nfce/consultanfce?",
        "HTTPS": "http://www.",
        "HOMOLOGACAO": "http://homologacao.",
    },
    "GO": {
        "STATUS": "sefaz.go.gov.br/nfe/services/NFeStatusServico4?wsdl",
        "AUTORIZACAO": "sefaz.go.gov.br/nfe/services/NFeAutorizacao4?wsdl",
        "RECIBO": "sefaz.go.gov.br/nfe/services/NFeRetAutorizacao4?wsdl",
        "CHAVE": "sefaz.go.gov.br/nfe/services/NFeConsultaProtocolo4?wsdl",
        "INUTILIZACAO": "sefaz.go.gov.br/nfe/services/NFeInutilizacao4?wsdl",
        "EVENTOS": "sefaz.go.gov.br/nfe/services/NFeRecepcaoEvento4?wsdl",
        "QR": "sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe?",
        "CADASTRO": "sefaz.go.gov.br/nfe/services/CadConsultaCadastro4?wsdl",
        # Host do AUTORIZADOR (webservices SOAP, mTLS) - igual ao de NFE["GO"].
        "HTTPS": "https://nfe.",
        "HOMOLOGACAO": "https://homolog.",
        # Host do portal de CONSULTA (qrCode/urlChave) - IT 2025.003, DEV-2177.
        "QR_HOST": "https://nfeweb.",
        "QR_HOST_HOMOLOGACAO": "https://nfewebhomolog.",
        "URL": "sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe",
        # ACBrNFeServicos.ini [NFCe_GO_P]/[NFCe_GO_H] URL-ConsultaNFCe_2.00, confirmado pelo
        # registro ENCAT. O IT 2025.003 definiu somente a URL do QR Code, por isso o "URL"
        # acima ficou apontando para o leitor de QR e GO passou a rejeitar 878.
        "CONSULTA_CHAVE": "http://www.sefaz.go.gov.br/nfce/consulta",
        "CONSULTA_CHAVE_HOMOLOGACAO": (
            "http://www.nfce.go.gov.br/post/ver/214413/consulta-nfc-e-homologacao"
        ),
    },
    "DF": {
        "QR": "http://www.fazenda.df.gov.br/nfce/qrcode?",
        "URL": "www.fazenda.df.gov.br/nfce/consulta",
    },
    # RO, AC, RR, PA, AP, TO, MA, PI, RN, PB, AL, SE, BA, ES, RJ, GO, DF
    "SVRS": {
        "STATUS": "svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
        "AUTORIZACAO": "svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
        "RECIBO": "svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        "CHAVE": "svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
        "INUTILIZACAO": "svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
        "EVENTOS": "svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
        "QR": "",
        "HTTPS": "https://nfce.",
        "HOMOLOGACAO": "https://nfce-homologacao.",
    },
}


def qrcode_host(uf, producao=True):
    """Prefixo de host do portal de consulta usado no ``<qrCode>``.

    Prefere as chaves dedicadas ``QR_HOST``/``QR_HOST_HOMOLOGACAO``; para UFs que nao
    declaram host de consulta proprio (portal e autorizador no mesmo servidor), cai no
    host de webservice, preservando o comportamento historico.

    Uma UF com ``CONSULTA_CHAVE`` nunca passa por aqui para montar o ``<urlChave>`` -
    esse campo tem registro proprio e URL completa, ver ``url_consulta_chave``. So o
    caminho legado (UF sem ``CONSULTA_CHAVE``) ainda concatena este prefixo sobre ``URL``,
    e e por isso que corrigir ``HTTPS``/``HOMOLOGACAO`` de uma dessas UFs move tambem o
    ``urlChave`` dela: declare ``QR_HOST``/``QR_HOST_HOMOLOGACAO`` antes de mexer no host
    de autorizador, como foi feito em AM e SP.
    """
    dados = NFCE[uf]
    chave_qr = "QR_HOST" if producao else "QR_HOST_HOMOLOGACAO"
    if dados.get(chave_qr):
        return dados[chave_qr]
    return dados["HTTPS"] if producao else dados["HOMOLOGACAO"]


# UFs cujo ``URL`` legado ja e a urlChave completa, sem prefixo de host. Lista fechada:
# UFs novas devem declarar ``CONSULTA_CHAVE`` em vez de entrar aqui.
UFS_URLCHAVE_SEM_HOST = frozenset({"CE", "DF", "RJ", "RO", "RS"})


def url_consulta_chave(uf, producao=True):
    """URL completa de consulta por chave de acesso, para o ``<urlChave>``.

    Prefere ``CONSULTA_CHAVE``/``CONSULTA_CHAVE_HOMOLOGACAO``, que guardam o valor
    verbatim do registro oficial e sao devolvidos sem nenhuma concatenacao. Sem essas
    chaves, reproduz o caminho legado (``URL``, com prefixo de host onde a UF nunca
    declarou host no proprio ``URL``).
    """
    dados = NFCE[uf]
    chave = "CONSULTA_CHAVE" if producao else "CONSULTA_CHAVE_HOMOLOGACAO"
    if dados.get(chave):
        return dados[chave]
    if uf in UFS_URLCHAVE_SEM_HOST:
        return dados["URL"]
    return qrcode_host(uf, producao=producao) + dados["URL"]


# Nfe
# homologação => http://hom.nfe.fazenda.gov.br/PORTAL/WebServices.aspx
# produção    => https://www.nfe.fazenda.gov.br/portal/webServices.aspx
NFE = {
    # Alguns serviços são disponibilizados apenas pelo ambiente nacional
    "AN": {
        "EVENTOS": (
            "nfe.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx"
        ),  # versao: 4.00
        "DISTRIBUICAO": "nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx",
        "HTTPS": "https://www",
        "HOMOLOGACAO": "https://hom1",
    },
    "AM": {
        "STATUS": "nfe.sefaz.am.gov.br/services2/services/NfeStatusServico4",
        "AUTORIZACAO": "nfe.sefaz.am.gov.br/services2/services/NfeAutorizacao4",
        "RECIBO": "nfe.sefaz.am.gov.br/services2/services/NfeRetAutorizacao4",
        "CHAVE": "nfe.sefaz.am.gov.br/services2/services/NfeConsulta4",
        "INUTILIZACAO": "nfe.sefaz.am.gov.br/services2/services/NfeInutilizacao4",
        "EVENTOS": "nfe.sefaz.am.gov.br/services2/services/RecepcaoEvento4",
        "CADASTRO": "nfe.sefaz.am.gov.br/services2/services/cadconsultacadastro2",
        "HTTPS": "https://",
        "HOMOLOGACAO": "https://hom",
    },
    "MA": {"CADASTRO": ("https://sistemas.sefaz.ma.gov.br/wscadastro/CadConsultaCadastro2?wsdl")},
    "PE": {
        "STATUS": "sefaz.pe.gov.br/nfe-service/services/NFeStatusServico4",
        "AUTORIZACAO": "sefaz.pe.gov.br/nfe-service/services/NFeAutorizacao4",
        "RECIBO": "sefaz.pe.gov.br/nfe-service/services/NFeRetAutorizacao4",
        "CHAVE": "sefaz.pe.gov.br/nfe-service/services/NFeConsultaProtocolo4",
        "INUTILIZACAO": "sefaz.pe.gov.br/nfe-service/services/NFeInutilizacao4",
        "EVENTOS": "sefaz.pe.gov.br/nfe-service/services/NFeRecepcaoEvento4",
        "CADASTRO": "sefaz.pe.gov.br/nfe-service/services/CadConsultaCadastro4?wsdl",
        "HTTPS": "https://nfe.",
        "HOMOLOGACAO": "https://nfehomolog.",
    },
    "BA": {
        "STATUS": ("nfe.sefaz.ba.gov.br/webservices/NFeStatusServico4/NFeStatusServico4.asmx"),
        "AUTORIZACAO": ("nfe.sefaz.ba.gov.br/webservices/NFeAutorizacao4/NFeAutorizacao4.asmx"),
        "RECIBO": ("nfe.sefaz.ba.gov.br/webservices/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx"),
        "CHAVE": (
            "nfe.sefaz.ba.gov.br/webservices/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx"
        ),
        "INUTILIZACAO": ("nfe.sefaz.ba.gov.br/webservices/NFeInutilizacao4/NFeInutilizacao4.asmx"),
        "EVENTOS": ("nfe.sefaz.ba.gov.br/webservices/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx"),
        "CADASTRO": (
            "nfe.sefaz.ba.gov.br/webservices/CadConsultaCadastro4/CadConsultaCadastro4.asmx"
        ),
        "HTTPS": "https://",
        "HOMOLOGACAO": "https://h",
    },
    "MG": {
        "STATUS": "nfe.fazenda.mg.gov.br/nfe2/services/NFeStatusServico4",
        "AUTORIZACAO": "nfe.fazenda.mg.gov.br/nfe2/services/NFeAutorizacao4",
        "RECIBO": "nfe.fazenda.mg.gov.br/nfe2/services/NFeRetAutorizacao4",
        "CHAVE": "nfe.fazenda.mg.gov.br/nfe2/services/NFeConsultaProtocolo4",
        "INUTILIZACAO": "nfe.fazenda.mg.gov.br/nfe2/services/NFeInutilizacao4",
        "EVENTOS": "nfe.fazenda.mg.gov.br/nfe2/services/NFeRecepcaoEvento4",
        "CADASTRO": "nfe.fazenda.mg.gov.br/nfe2/services/CadConsultaCadastro4",
        "HTTPS": "https://",
        "HOMOLOGACAO": "https://h",
    },
    "SP": {
        "STATUS": "nfe.fazenda.sp.gov.br/ws/nfestatusservico4.asmx",
        "AUTORIZACAO": "nfe.fazenda.sp.gov.br/ws/nfeautorizacao4.asmx",
        "RECIBO": "nfe.fazenda.sp.gov.br/ws/nferetautorizacao4.asmx",
        "CHAVE": "nfe.fazenda.sp.gov.br/ws/nfeconsultaprotocolo4.asmx",
        "INUTILIZACAO": "nfe.fazenda.sp.gov.br/ws/nfeinutilizacao4.asmx",
        "EVENTOS": "nfe.fazenda.sp.gov.br/ws/nferecepcaoevento4.asmx",
        "CADASTRO": "nfe.fazenda.sp.gov.br/ws/cadconsultacadastro4.asmx",
        "HTTPS": "https://",
        "HOMOLOGACAO": "https://homologacao.",
    },
    "PR": {
        "STATUS": ("nfe.sefa.pr.gov.br/nfe/NFeStatusServico4"),  # CONSULTA STATUS DO SERVICO
        "AUTORIZACAO": "nfe.sefa.pr.gov.br/nfe/NFeAutorizacao4",  # AUTORIZACAO
        "RECIBO": "nfe.sefa.pr.gov.br/nfe/NFeRetAutorizacao4",  # CONSULTA RECIBO
        "CHAVE": ("nfe.sefa.pr.gov.br/nfe/NFeConsultaProtocolo4"),  # CONSULTA CHAVE DE ACESSO
        "INUTILIZACAO": "nfe.sefa.pr.gov.br/nfe/NFeInutilizacao4",  # INUTILIZAÇAO
        "EVENTOS": "nfe.sefa.pr.gov.br/nfe/NFeRecepcaoEvento4",  # REGISTRO DE EVENTOS
        "CADASTRO": "nfe.sefa.pr.gov.br/nfe/CadConsultaCadastro4",  # CONSULTA CADASTRO
        "HTTPS": "https://",
        "HOMOLOGACAO": "https://homologacao.",
    },
    # https://www.sefaz.rs.gov.br/site/MontaDuvidas.aspx?al=l_rel_end_ws_nfe
    "RS": {
        "STATUS": "sefazrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
        "AUTORIZACAO": "sefazrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
        "RECIBO": "sefazrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        "CHAVE": "sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
        "INUTILIZACAO": "sefazrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
        "EVENTOS": "sefazrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
        "CADASTRO": (
            "https://cad.sefazrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx"
        ),
        "DOWNLOAD": "sefazrs.rs.gov.br/ws/nfeDownloadNF/nfeDownloadNF.asmx",
        "DESTINADAS": "sefazrs.rs.gov.br/ws/nfeConsultaDest/nfeConsultaDest.asmx",
        "HTTPS": "https://nfe.",
        "HOMOLOGACAO": "https://nfe-homologacao.",
    },
    "MS": {
        "STATUS": "nfe.sefaz.ms.gov.br/ws/NFeStatusServico4",
        "AUTORIZACAO": "nfe.sefaz.ms.gov.br/ws/NFeAutorizacao4",
        "RECIBO": "nfe.sefaz.ms.gov.br/ws/NFeRetAutorizacao4",
        "CHAVE": "nfe.sefaz.ms.gov.br/ws/NFeConsultaProtocolo4",
        "INUTILIZACAO": "nfe.sefaz.ms.gov.br/ws/NFeInutilizacao4",
        "EVENTOS": "nfe.sefaz.ms.gov.br/ws/NFeRecepcaoEvento4",
        "CADASTRO": "nfe.sefaz.ms.gov.br/ws/CadConsultaCadastro4",
        "HTTPS": "https://",
        "HOMOLOGACAO": "https://hom.",
    },
    "MT": {
        "STATUS": "sefaz.mt.gov.br/nfews/v2/services/NfeStatusServico4?wsdl",
        "AUTORIZACAO": "sefaz.mt.gov.br/nfews/v2/services/NfeAutorizacao4?wsdl",
        "RECIBO": "sefaz.mt.gov.br/nfews/v2/services/NfeRetAutorizacao4?wsdl",
        "CHAVE": "sefaz.mt.gov.br/nfews/v2/services/NfeConsulta4?wsdl",
        "INUTILIZACAO": "sefaz.mt.gov.br/nfews/v2/services/NfeInutilizacao4?wsdl",
        "EVENTOS": "sefaz.mt.gov.br/nfews/v2/services/RecepcaoEvento4?wsdl",
        "CADASTRO": "sefaz.mt.gov.br/nfews/v2/services/CadConsultaCadastro4?wsdl",
        "HTTPS": "https://nfe.",
        "HOMOLOGACAO": "https://homologacao.",
    },
    "GO": {
        "STATUS": "sefaz.go.gov.br/nfe/services/NFeStatusServico4?wsdl",
        "AUTORIZACAO": "sefaz.go.gov.br/nfe/services/NFeAutorizacao4?wsdl",
        "RECIBO": "sefaz.go.gov.br/nfe/services/NFeRetAutorizacao4?wsdl",
        "CHAVE": "sefaz.go.gov.br/nfe/services/NFeConsultaProtocolo4?wsdl",
        "INUTILIZACAO": "sefaz.go.gov.br/nfe/services/NFeInutilizacao4?wsdl",
        "EVENTOS": "sefaz.go.gov.br/nfe/services/NFeRecepcaoEvento4?wsdl",
        "CADASTRO": "sefaz.go.gov.br/nfe/services/CadConsultaCadastro4?wsdl",
        "HTTPS": "https://nfe.",
        "HOMOLOGACAO": "https://homolog.",
    },
    "SVAN": {
        "STATUS": ("sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx"),
        "AUTORIZACAO": ("sefazvirtual.fazenda.gov.br/NFeAutorizacao4/NFeAutorizacao4.asmx"),
        "RECIBO": ("sefazvirtual.fazenda.gov.br/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx"),
        "CHAVE": "sefazvirtual.fazenda.gov.br/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx",
        "INUTILIZACAO": ("sefazvirtual.fazenda.gov.br/NFeInutilizacao4/NFeInutilizacao4.asmx"),
        "EVENTOS": ("sefazvirtual.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx"),
        "DOWNLOAD": "sefazvirtual.fazenda.gov.br/NfeDownloadNF/NfeDownloadNF.asmx",
        "HTTPS": "https://www.",
        "HOMOLOGACAO": "https://hom.",
    },
    "SVRS": {
        "STATUS": "svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
        "AUTORIZACAO": "svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
        "RECIBO": "svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        "CHAVE": "svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
        "INUTILIZACAO": "svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
        "EVENTOS": "svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
        "CADASTRO": "https://cad.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
        "HTTPS": "https://nfe.",
        "HOMOLOGACAO": "https://nfe-homologacao.",
    },
    "SVC-AN": {
        "STATUS": "svc.fazenda.gov.br/NfeStatusServico2/NfeStatusServico2.asmx",
        "AUTORIZACAO": "svc.fazenda.gov.br/NfeAutorizacao/NfeAutorizacao.asmx",
        "RECIBO": "svc.fazenda.gov.br/NfeRetAutorizacao/NfeRetAutorizacao.asmx",
        "CHAVE": "svc.fazenda.gov.br/NfeConsulta2/NfeConsulta2.asmx",
        "EVENTOS": "svc.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx",
        "HTTPS": "https://www.",
        "HOMOLOGACAO": "https://hom.",
    },
    "SVC-RS": {
        "STATUS": "svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx",
        "AUTORIZACAO": "svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx",
        "RECIBO": "svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx",
        "CHAVE": "svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx",
        "INUTILIZACAO": "svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao2.asmx",
        "EVENTOS": "svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx",
        "HTTPS": "https://nfe.",
        "HOMOLOGACAO": "https://nfe-homologacao.",
    },
}

# Nfs-e
NFSE = {
    #
    "BETHA": {
        "AUTORIZACAO": "GerarNfse",
        "CANCELAR": "CancelarNfse",
        "CONSULTA_RPS": "consultarNfsePorRps",
        "CONSULTA_FAIXA": "ConsultarNfseFaixa",
        "CONSULTA_SERVICO": "ConsultarNfseServicoPrestado",
        "CONSULTA_SERVICO_TOMADO": "ConsultarNfseServicoTomado",
        "SUBSTITUIR": "SubstituirNfse",
        "HTTPS": "http://e-gov.betha.com.br/e-nota-contribuinte-ws/nfseWS?wsdl",
        "HOMOLOGACAO": ("http://e-gov.betha.com.br/e-nota-contribuinte-test-ws/nfseWS?wsdl"),
    },
    #
    "GINFES": {
        "AUTORIZACAO": "GerarNfse",
        "CANCELAR": "CancelarNfse",
        "CONSULTA_RPS": "ConsultarNfsePorRps",
        "CONSULTA_FAIXA": "ConsultarNfseFaixa",
        "CONSULTA_SERVICO": "ConsultarNfseServicoPrestado",
        "CONSULTA_SERVICO_TOMADO": "ConsultarNfseServicoTomado",
        "SUBSTITUIR": "SubstituirNfse",
        "HTTPS": "https://producao.ginfes.com.br/ServiceGinfesImpl?wsdl",
        "HOMOLOGACAO": "https://homologacao.ginfes.com.br/ServiceGinfesImpl?wsdl",
    },
}

# MDF-e
MDFE = {
    # unico autorizador de MDF-e
    "SVRS": {
        "RECEPCAO": "MDFeRecepcao/MDFeRecepcao.asmx",
        "RECEPCAO_SINC": "MDFeRecepcaoSinc/MDFeRecepcaoSinc.asmx",
        "RET_RECEPCAO": "mdferetrecepcao/MDFeRetRecepcao.asmx",
        "EVENTOS": "mdferecepcaoevento/MDFeRecepcaoEvento.asmx",
        "CONSULTA": "mdfeconsulta/MDFeConsulta.asmx",
        "STATUS": "mdfestatusservico/MDFeStatusServico.asmx",
        "NAO_ENCERRADOS": "mdfeconsnaoenc/MDFeConsNaoEnc.asmx",
        "HTTPS": "https://mdfe.svrs.rs.gov.br/ws/",
        "HOMOLOGACAO": "https://mdfe-homologacao.svrs.rs.gov.br/ws/",
        "QRCODE": "https://dfe-portal.svrs.rs.gov.br/mdfe/qrCode",
    }
}

CTE = {
    "AN": {
        "DISTRIBUICAO": "cte.fazenda.gov.br/CTeDistribuicaoDFe/CTeDistribuicaoDFe.asmx",
        "HTTPS": "https://www1",
        "HOMOLOGACAO": "https://hom1",
    },
    "MT": {
        "STATUS": "sefaz.mt.gov.br/ctews/services/CteStatusServico",
        "CONSULTA": "sefaz.mt.gov.br/ctews2/services/CTeConsultaV4?wsdl",
        "HTTPS": "https://cte.",
        "HOMOLOGACAO": "https://homologacao.",
    },
    "MS": {
        "STATUS": "cte.ms.gov.br/ws/CteStatusServico",
        "CONSULTA": "cte.ms.gov.br/ws/CTeConsultaV4",
        "HTTPS": "https://producao.",
        "HOMOLOGACAO": "https://homologacao.",
    },
    "MG": {
        "STATUS": "fazenda.mg.gov.br/cte/services/CteStatusServico",
        "CONSULTA": "fazenda.mg.gov.br/cte/services/CTeConsultaV4",
        "HTTPS": "https://cte.",
        "HOMOLOGACAO": "https://hcte.",
    },
    "PR": {
        "STATUS": "fazenda.pr.gov.br/cte/CteStatusServico?wsdl",
        "CONSULTA": "fazenda.pr.gov.br/cte4/CTeConsultaV4?wsdl",
        "HTTPS": "https://cte.",
        "HOMOLOGACAO": "https://homologacao.",
    },
    "RS": {
        "STATUS": "svrs.rs.gov.br/ws/ctestatusservico/CteStatusServico.asmx",
        "CONSULTA": "svrs.rs.gov.br/ws/CTeConsultaV4/CTeConsultaV4.asmx",
        "HTTPS": "https://cte.",
        "HOMOLOGACAO": "https://cte-homologacao.",
    },
    "SP": {
        "STATUS": "fazenda.sp.gov.br/cteWEB/services/cteStatusServico.asmx",
        "CONSULTA": "fazenda.sp.gov.br/CTeWS/WS/CTeConsultaV4.asmx",
        "HTTPS": "https://nfe.",
        "HOMOLOGACAO": "https://homologacao.nfe.",
    },
    "SVRS": {
        "STATUS": "svrs.rs.gov.br/ws/ctestatusservico/CteStatusServico.asmx",
        "CONSULTA": "svrs.rs.gov.br/ws/CTeConsultaV4/CTeConsultaV4.asmx",
        "HTTPS": "https://cte.",
        "HOMOLOGACAO": "https://cte-homologacao.",
    },
    "SVSP": {
        "STATUS": "fazenda.sp.gov.br/cteWEB/services/CteStatusServico.asmx",
        "CONSULTA": "fazenda.sp.gov.br/CTeWS/WS/CTeConsultaV4.asmx",
        "HTTPS": "https://nfe.",
        "HOMOLOGACAO": "https://homologacao.nfe.",
    },
}
