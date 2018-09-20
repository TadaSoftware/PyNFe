from pynfe.processamento.serializacao import SerializacaoQrcode
from pynfe.processamento.assinatura import AssinaturaA1
uf = 'pr'
homologacao = 'True'
certificado = "certificado/lam.pfx"
senha = '1234'


from lxml import etree
nfe = '<NFe xmlns="http://www.portalfiscal.inf.br/nfe"><infNFe versao="4.00" Id="NFe29180921011279000260650020000000531000001513"><ide><cUF>29</cUF><cNF>00000151</cNF><natOp>VENDA</natOp><mod>65</mod><serie>2</serie><nNF>53</nNF><dhEmi>2018-09-03T14:06:20-03:00</dhEmi><tpNF>1</tpNF><idDest>1</idDest><cMunFG>2918407</cMunFG><tpImp>4</tpImp><tpEmis>1</tpEmis><cDV>3</cDV><tpAmb>2</tpAmb><finNFe>1</finNFe><indFinal>1</indFinal><indPres>1</indPres><procEmi>0</procEmi><verProc>KYAN VERSAO 3.0</verProc></ide><emit><CNPJ>21011279000260</CNPJ><xNome>DONDON COM. VAREJISTA DE CALC. LTDA ME</xNome><xFant>MUNDI SHOES SHOPPING</xFant><enderEmit><xLgr>RODOVIA LOMANTO JUNIOR</xLgr><nro>S N</nro><xCpl>SHOPP.JUA GARDEN 1-B</xCpl><xBairro>JOAO XXIII</xBairro><cMun>2918407</cMun><xMun>JUAZEIRO</xMun><UF>BA</UF><CEP>48900365</CEP><cPais>1058</cPais><xPais>BRASIL</xPais><fone>7436148567</fone></enderEmit><IE>146961742</IE><CRT>1</CRT></emit><det nItem="1"><prod><cProd>001 0205 622-23</cProd><cEAN>SEM GTIN</cEAN><xProd>NOTA FISCAL EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL</xProd><NCM>64041900</NCM><CEST>2803800</CEST><CFOP>5102</CFOP><uCom>PAR</uCom><qCom>1.0000</qCom><vUnCom>78.90</vUnCom><vProd>78.90</vProd><cEANTrib>SEM GTIN</cEANTrib><uTrib>PAR</uTrib><qTrib>1.0000</qTrib><vUnTrib>78.90</vUnTrib><indTot>1</indTot></prod><imposto><ICMS><ICMSSN102><orig>0</orig><CSOSN>102</CSOSN></ICMSSN102></ICMS><PIS><PISOutr><CST>99</CST><qBCProd>0.0000</qBCProd><vAliqProd>0.0000</vAliqProd><vPIS>0.00</vPIS></PISOutr></PIS><COFINS><COFINSOutr><CST>99</CST><qBCProd>0.0000</qBCProd><vAliqProd>0.0000</vAliqProd><vCOFINS>0.00</vCOFINS></COFINSOutr></COFINS></imposto></det><total><ICMSTot><vBC>0.00</vBC><vICMS>0.00</vICMS><vICMSDeson>0.00</vICMSDeson><vFCPUFDest>0.00</vFCPUFDest><vICMSUFDest>0.00</vICMSUFDest><vICMSUFRemet>0.00</vICMSUFRemet><vFCP>0.00</vFCP><vBCST>0.00</vBCST><vST>0.00</vST><vFCPST>0.00</vFCPST><vFCPSTRet>0.00</vFCPSTRet><vProd>78.90</vProd><vFrete>0.00</vFrete><vSeg>0.00</vSeg><vDesc>0.00</vDesc><vII>0.00</vII><vIPI>0.00</vIPI><vIPIDevol>0.00</vIPIDevol><vPIS>0.00</vPIS><vCOFINS>0.00</vCOFINS><vOutro>0.00</vOutro><vNF>78.90</vNF><vTotTrib>0.00</vTotTrib></ICMSTot></total><transp><modFrete>9</modFrete></transp><pag><detPag><tPag>01</tPag><vPag>78.90</vPag></detPag></pag></infNFe></NFe>'


nfe = etree.fromstring(nfe)

# # assinatura
a1 = AssinaturaA1(certificado, senha)
xml = a1.assinar(nfe)



# # token de homologacao
token = '000001'

# # # csc de homologação
csc = '5AB5F679-EA09-42CA-803B-6625B6107E2E'




# # # gera e adiciona o qrcode no xml NT2015/003
xml_com_qrcode = SerializacaoQrcode().gerar_qrcode(token, csc, xml,qrcode_emissao="1")

print(etree.tostring(xml_com_qrcode, encoding='unicode').replace('\n','').replace('&lt;','<').replace('&gt;','>').replace('amp;',''))
