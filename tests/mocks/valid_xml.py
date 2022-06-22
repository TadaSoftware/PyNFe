
class ConsultaServico:
    def __str__(self):
        return """<retConsStatServ xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00"><tpAmb>1</tpAmb><verAplic>MT_A2RL-4.00</verAplic><cStat>107</cStat><xMotivo>Servico em Operacao</xMotivo><cUF>51</cUF><dhRecbto>2022-06-21T11:26:35-04:00</dhRecbto><tMed>2</tMed></retConsStatServ>"""


class ConsultaNotaAutorizada:
    def __str__(self):
        return """<retConsSitNFe xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00"><tpAmb>2</tpAmb><verAplic>SP_NFE_PL_006e</verAplic><cStat>100</cStat><xMotivo>Autorizado o uso da NF-e</xMotivo><cUF>35</cUF><chNFe>35100610142785000190551100000000014259062380</chNFe><protNFe versao="2.00"><infProt><tpAmb>2</tpAmb><verAplic>SP_NFE_PL_005e</verAplic><chNFe>35100610142785000190551100000000014259062380</chNFe><dhRecbto>2010-06-10T02:04:23</dhRecbto><nProt>135100021500481</nProt><digVal>kcry/2bpeM4KbTsGsRFI/f6MjvU=</digVal><cStat>100</cStat><xMotivo>Autorizado o uso da NF-e</xMotivo></infProt></protNFe></retConsSitNFe>"""


class ConsultaNotaComRejeicao:
    def __str__(self):
        return """<retConsSitNFe xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00"><tpAmb>2</tpAmb><verAplic>SP_NFE_PL_006e</verAplic><cStat>217</cStat><xMotivo>Rejeicao: NF-e nao consta na base de dados da SEFAZ</xMotivo><cUF>35</cUF><chNFe>35100610142785000190551100000000014259062380</chNFe></retConsSitNFe>"""
