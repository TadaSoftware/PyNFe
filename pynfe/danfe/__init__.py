# -*- coding: utf-8 -*-
# © 2017 Edson Bernardino, ITK Soft
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# Classe para geração de PDF da DANFE a partir de xml etree.fromstring

import os
from io import BytesIO
from textwrap import wrap

from reportlab.lib import utils
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, gray
from reportlab.graphics.barcode import code128
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import pytz
from datetime import datetime, timedelta


def chunks(cString, nLen):
    for start in range(0, len(cString), nLen):
        yield cString[start:start + nLen]


def format_cnpj_cpf(value):
    if len(value) < 12:  # CPF
        cValue = '%s.%s.%s-%s' % (value[:-8], value[-8:-5],
                                  value[-5:-2], value[-2:])
    else:
        cValue = '%s.%s.%s/%s-%s' % (value[:-12], value[-12:-9],
                                     value[-9:-6], value[-6:-2], value[-2:])
    return cValue


def getdateByTimezone(cDateUTC, timezone=None):

    '''
    Esse método trata a data recebida de acordo com o timezone do
    usuário. O seu retorno é dividido em duas partes:
    1) A data em si;
    2) As horas;
    :param cDateUTC: string contendo as informações da data
    :param timezone: timezone do usuário do sistema
    :return: data e hora convertidos para a timezone do usuário
    '''

    # Aqui cortamos a informação do timezone da string (+03:00)
    dt = cDateUTC[0:19]

    # Verificamos se a string está completa (data + hora + timezone)
    if timezone and len(cDateUTC) == 25:

        # tz irá conter informações da timezone contida em cDateUTC
        tz = cDateUTC[19:25]
        tz = int(tz.split(':')[0])

        dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')

        # dt agora será convertido para o horario em UTC
        dt = dt - timedelta(hours=tz)

        # tzinfo passará a apontar para <UTC>
        dt = pytz.utc.localize(dt)

        # valor de dt é convertido para a timezone do usuário
        dt = timezone.normalize(dt)
        dt = dt.strftime('%Y-%m-%dT%H:%M:%S')

    cDt = dt[0:10].split('-')
    cDt.reverse()
    return '/'.join(cDt), dt[11:16]


def format_number(cNumber):
    if cNumber:
        return cNumber.replace(",", "X").replace(".", ",").replace("X", ".")
    return ""


def tagtext(oNode=None, cTag=None):
    try:
        xpath = ".//{http://www.portalfiscal.inf.br/nfe}%s" % (cTag)
        cText = oNode.find(xpath).text
    except:
        cText = ''
    return cText


REGIME_TRIBUTACAO = {
    '1': 'Simples Nacional',
    '2': 'Simples Nacional, excesso sublimite de receita bruta',
    '3': 'Regime Normal'
}


def get_image(path, width=1 * cm):
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    return Image(path, width=width, height=(width * aspect))


class DANFE(object):

    def __init__(self, sizepage=A4, list_xml=None, recibo=True,
                 orientation='portrait', logo=None, cce_xml=None,
                 timezone=None):

        path = os.path.join(os.path.dirname(__file__), 'fonts')
        pdfmetrics.registerFont(
            TTFont('NimbusSanL-Regu',
                   os.path.join(path, 'NimbusSanL Regular.ttf')))
        pdfmetrics.registerFont(
            TTFont('NimbusSanL-Bold',
                   os.path.join(path, 'NimbusSanL Bold.ttf')))
        self.width = 210    # 21 x 29,7cm
        self.height = 297
        self.nLeft = 10
        self.nRight = 10
        self.nTop = 7
        self.nBottom = 8
        self.nlin = self.nTop
        self.logo = logo
        self.oFrete = {'0': '0 - Emitente',
                       '1': '1 - Destinatário',
                       '2': '2 - Terceiros',
                       '9': '9 - Sem Frete'}

        self.oPDF_IO = BytesIO()
        if orientation == 'landscape':
            raise NameError('Rotina não implementada')
        else:
            size = sizepage

        self.canvas = canvas.Canvas(self.oPDF_IO, pagesize=size)
        self.canvas.setTitle('DANFE')
        self.canvas.setStrokeColor(black)

        for oXML in list_xml:
            oXML_cobr = oXML.find(
                ".//{http://www.portalfiscal.inf.br/nfe}cobr")

            self.NrPages = 1
            self.Page = 1

            # Calculando total linhas usadas para descrições dos itens
            # Com bloco fatura, apenas 25 linhas para itens na primeira folha
            nNr_Lin_Pg_1 = 30 if oXML_cobr is None else 26
            # [ rec_ini , rec_fim , lines , limit_lines ]
            oPaginator = [[0, 0, 0, nNr_Lin_Pg_1]]
            el_det = oXML.findall(".//{http://www.portalfiscal.inf.br/nfe}det")
            if el_det is not None:
                list_desc = []
                list_cod_prod = []
                nPg = 0
                for nId, item in enumerate(el_det):
                    el_prod = item.find(
                        ".//{http://www.portalfiscal.inf.br/nfe}prod")
                    infAdProd = item.find(
                        ".//{http://www.portalfiscal.inf.br/nfe}infAdProd")

                    list_ = wrap(tagtext(oNode=el_prod, cTag='xProd'), 56)
                    if infAdProd is not None:
                        list_.extend(wrap(infAdProd.text, 56))
                    list_desc.append(list_)

                    list_cProd = wrap(tagtext(oNode=el_prod, cTag='cProd'), 14)
                    list_cod_prod.append(list_cProd)

                    # Nr linhas necessárias p/ descrição item
                    nLin_Itens = len(list_)

                    if (oPaginator[nPg][2] + nLin_Itens) >= oPaginator[nPg][3]:
                        oPaginator.append([0, 0, 0, 77])
                        nPg += 1
                        oPaginator[nPg][0] = nId
                        oPaginator[nPg][1] = nId + 1
                        oPaginator[nPg][2] = nLin_Itens
                    else:
                        # adiciona-se 1 pelo funcionamento de xrange
                        oPaginator[nPg][1] = nId + 1
                        oPaginator[nPg][2] += nLin_Itens

                self.NrPages = len(oPaginator)   # Calculando nr. páginas

            if recibo:
                self.recibo_entrega(oXML=oXML, timezone=timezone)

            self.ide_emit(oXML=oXML, timezone=timezone)
            self.destinatario(oXML=oXML, timezone=timezone)

            if oXML_cobr is not None:
                self.faturas(oXML=oXML_cobr, timezone=timezone)

            self.impostos(oXML=oXML)
            self.transportes(oXML=oXML)
            self.produtos(oXML=oXML, el_det=el_det, oPaginator=oPaginator[0],
                          list_desc=list_desc, list_cod_prod=list_cod_prod)

            self.adicionais(oXML=oXML)

            # Gera o restante das páginas do XML
            for oPag in oPaginator[1:]:
                self.newpage()
                self.ide_emit(oXML=oXML, timezone=timezone)
                self.produtos(oXML=oXML, el_det=el_det, oPaginator=oPag,
                              list_desc=list_desc, nHeight=77,
                              list_cod_prod=list_cod_prod)

            self.newpage()
        if cce_xml:
            for xml in cce_xml:
                self._generate_cce(cce_xml=xml, oXML=oXML, timezone=timezone)
                self.newpage()
        self.canvas.save()

    def ide_emit(self, oXML=None, timezone=None):
        elem_infNFe = oXML.find(
            ".//{http://www.portalfiscal.inf.br/nfe}infNFe")
        elem_protNFe = oXML.find(
            ".//{http://www.portalfiscal.inf.br/nfe}protNFe")
        elem_emit = oXML.find(".//{http://www.portalfiscal.inf.br/nfe}emit")
        elem_ide = oXML.find(".//{http://www.portalfiscal.inf.br/nfe}ide")
        elem_evento = oXML.find(
            ".//{http://www.portalfiscal.inf.br/nfe}infEvento")

        cChave = elem_infNFe.attrib.get('Id')[3:]
        barcode128 = code128.Code128(
            cChave, barHeight=10 * mm, barWidth=0.25 * mm)

        self.canvas.setLineWidth(.5)
        self.rect(self.nLeft, self.nlin + 1, self.nLeft + 75, 32)
        self.rect(self.nLeft + 115, self.nlin + 1,
                  self.width - self.nLeft - self.nRight - 115, 39)

        self.hline(self.nLeft + 85, self.nlin + 1, 125)

        self.rect(self.nLeft + 116, self.nlin + 15,
                  self.width - self.nLeft - self.nRight - 117, 6)

        self.rect(self.nLeft, self.nlin + 33,
                  self.width - self.nLeft - self.nRight, 14)
        self.hline(self.nLeft, self.nlin + 40, self.width - self.nRight)
        self.vline(self.nLeft + 60, self.nlin + 40, 7)
        self.vline(self.nLeft + 100, self.nlin + 40, 7)

        # Labels
        self.canvas.setFont('NimbusSanL-Bold', 12)
        self.stringcenter(self.nLeft + 98, self.nlin + 5, 'DANFE')
        self.stringcenter(self.nLeft + 109, self.nlin + 19.5,
                          tagtext(oNode=elem_ide, cTag='tpNF'))
        self.canvas.setFont('NimbusSanL-Bold', 8)
        cNF = tagtext(oNode=elem_ide, cTag='nNF')
        cNF = '{0:011,}'.format(int(cNF)).replace(",", ".")
        self.stringcenter(self.nLeft + 100, self.nlin + 25, "Nº %s" % (cNF))

        self.stringcenter(self.nLeft + 100, self.nlin + 29, "SÉRIE %s" % (
            tagtext(oNode=elem_ide, cTag='serie')))
        cPag = "Página %s de %s" % (str(self.Page), str(self.NrPages))
        self.stringcenter(self.nLeft + 100, self.nlin + 32, cPag)
        self.canvas.setFont('NimbusSanL-Regu', 6)
        self.string(self.nLeft + 86, self.nlin + 8, 'Documento Auxiliar da')
        self.string(self.nLeft + 86, self.nlin +
                    10.5, 'Nota Fiscal Eletrônica')
        self.string(self.nLeft + 86, self.nlin + 16, '0 - Entrada')
        self.string(self.nLeft + 86, self.nlin + 19, '1 - Saída')
        self.rect(self.nLeft + 105, self.nlin + 15, 8, 6)

        self.stringcenter(
            self.nLeft + 152, self.nlin + 25,
            'Consulta de autenticidade no portal nacional da NF-e')
        self.stringcenter(
            self.nLeft + 152, self.nlin + 28,
            'www.nfe.fazenda.gov.br/portal ou no site da SEFAZ Autorizadora')
        self.canvas.setFont('NimbusSanL-Regu', 5)
        self.string(self.nLeft + 117, self.nlin + 16.7, 'CHAVE DE ACESSO')
        self.string(self.nLeft + 116, self.nlin + 2.7, 'CONTROLE DO FISCO')

        self.string(self.nLeft + 1, self.nlin + 34.7, 'NATUREZA DA OPERAÇÃO')
        self.string(self.nLeft + 116, self.nlin + 34.7,
                    'PROTOCOLO DE AUTORIZAÇÃO DE USO')
        self.string(self.nLeft + 1, self.nlin + 41.7, 'INSCRIÇÃO ESTADUAL')
        self.string(self.nLeft + 61, self.nlin + 41.7,
                    'INSCRIÇÃO ESTADUAL DO SUBST. TRIB.')
        self.string(self.nLeft + 101, self.nlin + 41.7, 'CNPJ')

        # Conteúdo campos
        barcode128.drawOn(self.canvas, (self.nLeft + 111.5) * mm,
                          (self.height - self.nlin - 14) * mm)
        self.canvas.setFont('NimbusSanL-Bold', 6)
        nW_Rect = (self.width - self.nLeft - self.nRight - 117) / 2
        self.stringcenter(self.nLeft + 116.5 + nW_Rect, self.nlin + 19.5,
                          ' '.join(chunks(cChave, 4)))  # Chave
        self.canvas.setFont('NimbusSanL-Regu', 8)
        cDt, cHr = getdateByTimezone(
            tagtext(oNode=elem_protNFe, cTag='dhRecbto'), timezone)
        cProtocolo = tagtext(oNode=elem_protNFe, cTag='nProt')
        cDt = cProtocolo + ' - ' + cDt + ' ' + cHr
        nW_Rect = (self.width - self.nLeft - self.nRight - 110) / 2
        self.stringcenter(self.nLeft + 115 + nW_Rect, self.nlin + 38.7, cDt)
        self.canvas.setFont('NimbusSanL-Regu', 8)
        self.string(self.nLeft + 1, self.nlin + 38.7,
                    tagtext(oNode=elem_ide, cTag='natOp'))
        self.string(self.nLeft + 1, self.nlin + 46,
                    tagtext(oNode=elem_emit, cTag='IE'))
        self.string(self.nLeft + 101, self.nlin + 46,
                    format_cnpj_cpf(tagtext(oNode=elem_emit, cTag='CNPJ')))

        styles = getSampleStyleSheet()
        styleN = styles['Normal']
        styleN.fontSize = 10
        styleN.fontName = 'NimbusSanL-Bold'
        styleN.alignment = TA_CENTER

        # Razão Social emitente
        P = Paragraph(tagtext(oNode=elem_emit, cTag='xNome'), styleN)
        w, h = P.wrap(55 * mm, 40 * mm)
        P.drawOn(self.canvas, (self.nLeft + 30) * mm,
                 (self.height - self.nlin - ((4.3*h + 12)/12)) * mm)

        if self.logo:
            img = get_image(self.logo, width=2 * cm)
            img.drawOn(self.canvas, (self.nLeft + 5) * mm,
                       (self.height - self.nlin - 22) * mm)

        cEnd = tagtext(oNode=elem_emit, cTag='xLgr') + ', ' + tagtext(
            oNode=elem_emit, cTag='nro') + ' - '
        cEnd += tagtext(oNode=elem_emit, cTag='xBairro') + '<br />' + tagtext(
            oNode=elem_emit, cTag='xMun') + ' - '
        cEnd += 'Fone: ' + tagtext(oNode=elem_emit, cTag='fone') + '<br />'
        cEnd += tagtext(oNode=elem_emit, cTag='UF') + ' - ' + tagtext(
            oNode=elem_emit, cTag='CEP')

        regime = tagtext(oNode=elem_emit, cTag='CRT')
        cEnd += '<br />Regime Tributário: %s' % (REGIME_TRIBUTACAO[regime])

        styleN.fontName = 'NimbusSanL-Regu'
        styleN.fontSize = 7
        styleN.leading = 10
        P = Paragraph(cEnd, styleN)
        w, h = P.wrap(55 * mm, 30 * mm)
        P.drawOn(self.canvas, (self.nLeft + 30) * mm,
                 (self.height - self.nlin - 33) * mm)

        # Homologação
        if tagtext(oNode=elem_ide, cTag='tpAmb') == '2':
            self.canvas.saveState()
            self.canvas.rotate(90)
            self.canvas.setFont('Times-Bold', 40)
            self.canvas.setFillColorRGB(0.57, 0.57, 0.57)
            self.string(self.nLeft + 65, 449, 'SEM VALOR FISCAL')
            self.canvas.restoreState()

        # Cancelado
        if tagtext(oNode=elem_evento, cTag='cStat') == '135':
            self.canvas.saveState()
            self.canvas.rotate(45)
            self.canvas.setFont('NimbusSanL-Bold', 60)
            self.canvas.setFillColorRGB(1, 0.2, 0.2)
            self.string(self.nLeft + 80, 275, 'CANCELADO')
            self.canvas.restoreState()

        self.nlin += 48

    def destinatario(self, oXML=None, timezone=None):
        elem_ide = oXML.find(".//{http://www.portalfiscal.inf.br/nfe}ide")
        elem_dest = oXML.find(".//{http://www.portalfiscal.inf.br/nfe}dest")
        nMr = self.width - self.nRight

        self.nlin += 1

        self.canvas.setFont('NimbusSanL-Bold', 7)
        self.string(self.nLeft + 1, self.nlin + 1, 'DESTINATÁRIO/REMETENTE')
        self.rect(self.nLeft, self.nlin + 2,
                  self.width - self.nLeft - self.nRight, 20)
        self.vline(nMr - 25, self.nlin + 2, 20)
        self.hline(self.nLeft, self.nlin + 8.66, self.width - self.nLeft)
        self.hline(self.nLeft, self.nlin + 15.32, self.width - self.nLeft)
        self.vline(nMr - 70, self.nlin + 2, 6.66)
        self.vline(nMr - 53, self.nlin + 8.66, 6.66)
        self.vline(nMr - 99, self.nlin + 8.66, 6.66)
        self.vline(nMr - 90, self.nlin + 15.32, 6.66)
        self.vline(nMr - 102, self.nlin + 15.32, 6.66)
        self.vline(nMr - 136, self.nlin + 15.32, 6.66)
        # Labels/Fields
        self.canvas.setFont('NimbusSanL-Bold', 5)
        self.string(self.nLeft + 1, self.nlin + 3.7, 'NOME/RAZÃO SOCIAL')
        self.string(nMr - 69, self.nlin + 3.7, 'CNPJ/CPF')
        self.string(nMr - 24, self.nlin + 3.7, 'DATA DA EMISSÃO')
        self.string(self.nLeft + 1, self.nlin + 10.3, 'ENDEREÇO')
        self.string(nMr - 98, self.nlin + 10.3, 'BAIRRO/DISTRITO')
        self.string(nMr - 52, self.nlin + 10.3, 'CEP')
        self.string(nMr - 24, self.nlin + 10.3, 'DATA DE ENTRADA/SAÍDA')
        self.string(self.nLeft + 1, self.nlin + 17.1, 'MUNICÍPIO')
        self.string(nMr - 135, self.nlin + 17.1, 'FONE/FAX')
        self.string(nMr - 101, self.nlin + 17.1, 'UF')
        self.string(nMr - 89, self.nlin + 17.1, 'INSCRIÇÃO ESTADUAL')
        self.string(nMr - 24, self.nlin + 17.1, 'HORA DE ENTRADA/SAÍDA')
        # Conteúdo campos
        self.canvas.setFont('NimbusSanL-Regu', 8)
        self.string(self.nLeft + 1, self.nlin + 7.5,
                    tagtext(oNode=elem_dest, cTag='xNome'))
        cnpj_cpf = tagtext(oNode=elem_dest, cTag='CNPJ')
        if cnpj_cpf:
            cnpj_cpf = format_cnpj_cpf(cnpj_cpf)
        else:
            cnpj_cpf = format_cnpj_cpf(tagtext(oNode=elem_dest, cTag='CPF'))
        self.string(nMr - 69, self.nlin + 7.5, cnpj_cpf)
        cDt, cHr = getdateByTimezone(tagtext(oNode=elem_ide, cTag='dhEmi'),
                                     timezone)
        self.string(nMr - 24, self.nlin + 7.7, cDt + ' ' + cHr)
        cDt, cHr = getdateByTimezone(
            tagtext(oNode=elem_ide, cTag='dhSaiEnt'), timezone)
        self.string(nMr - 24, self.nlin + 14.3, cDt + ' ' + cHr)  # Dt saída
        cEnd = tagtext(oNode=elem_dest, cTag='xLgr') + ', ' + tagtext(
            oNode=elem_dest, cTag='nro')
        self.string(self.nLeft + 1, self.nlin + 14.3, cEnd)
        self.string(nMr - 98, self.nlin + 14.3,
                    tagtext(oNode=elem_dest, cTag='xBairro'))
        self.string(nMr - 52, self.nlin + 14.3,
                    tagtext(oNode=elem_dest, cTag='CEP'))
        self.string(self.nLeft + 1, self.nlin + 21.1,
                    tagtext(oNode=elem_dest, cTag='xMun'))
        self.string(nMr - 135, self.nlin + 21.1,
                    tagtext(oNode=elem_dest, cTag='fone'))
        self.string(nMr - 101, self.nlin + 21.1,
                    tagtext(oNode=elem_dest, cTag='UF'))
        self.string(nMr - 89, self.nlin + 21.1,
                    tagtext(oNode=elem_dest, cTag='IE'))

        self.nlin += 24  # Nr linhas ocupadas pelo bloco

    def faturas(self, oXML=None, timezone=None):

        nMr = self.width - self.nRight

        self.canvas.setFont('NimbusSanL-Bold', 7)
        self.string(self.nLeft + 1, self.nlin + 1, 'FATURA')
        self.rect(self.nLeft, self.nlin + 2,
                  self.width - self.nLeft - self.nRight, 13)
        self.vline(nMr - 47.5, self.nlin + 2, 13)
        self.vline(nMr - 95, self.nlin + 2, 13)
        self.vline(nMr - 142.5, self.nlin + 2, 13)
        self.hline(nMr - 47.5, self.nlin + 8.5, self.width - self.nLeft)
        # Labels
        self.canvas.setFont('NimbusSanL-Regu', 5)
        self.string(nMr - 46.5, self.nlin + 3.8, 'CÓDIGO VENDEDOR')
        self.string(nMr - 46.5, self.nlin + 10.2, 'NOME VENDEDOR')
        self.string(nMr - 93.5, self.nlin + 3.8,
                    'FATURA          VENCIMENTO           VALOR')
        self.string(nMr - 140.5, self.nlin + 3.8,
                    'FATURA          VENCIMENTO           VALOR')
        self.string(self.nLeft + 2, self.nlin + 3.8,
                    'FATURA         VENCIMENTO            VALOR')

        # Conteúdo campos
        self.canvas.setFont('NimbusSanL-Bold', 6)
        nLin = 7
        nPar = 1
        nCol = 0
        nAju = 0

        line_iter = iter(oXML[1:10])  # Salta elemt 1 e considera os próximos 9
        for oXML_dup in line_iter:

            cDt, cHr = getdateByTimezone(tagtext(oNode=oXML_dup, cTag='dVenc'),
                                         timezone)
            self.string(self.nLeft + nCol + 1, self.nlin + nLin,
                        tagtext(oNode=oXML_dup, cTag='nDup'))
            self.string(self.nLeft + nCol + 17, self.nlin + nLin, cDt)
            self.stringRight(
                self.nLeft + nCol + 47, self.nlin + nLin,
                format_number(tagtext(oNode=oXML_dup, cTag='vDup')))

            if nPar == 3:
                nLin = 7
                nPar = 1
                nCol += 47
                nAju += 1
                nCol += nAju * (0.3)
            else:
                nLin += 3.3
                nPar += 1

        # Campos adicionais XML - Condicionados a existencia de financeiro
        elem_infAdic = oXML.getparent().find(
            ".//{http://www.portalfiscal.inf.br/nfe}infAdic")
        if elem_infAdic is not None:
            codvend = elem_infAdic.find(
                ".//{http://www.portalfiscal.inf.br/nfe}obsCont\
[@xCampo='CodVendedor']")
            self.string(nMr - 46.5, self.nlin + 7.7,
                        tagtext(oNode=codvend, cTag='xTexto'))
            vend = elem_infAdic.find(".//{http://www.portalfiscal.inf.br/nfe}\
obsCont[@xCampo='NomeVendedor']")
            self.string(nMr - 46.5, self.nlin + 14.3,
                        tagtext(oNode=vend, cTag='xTexto')[:36])

        self.nlin += 16  # Nr linhas ocupadas pelo bloco

    def impostos(self, oXML=None):
        # Impostos
        el_total = oXML.find(".//{http://www.portalfiscal.inf.br/nfe}total")
        nMr = self.width - self.nRight
        self.nlin += 1
        self.canvas.setFont('NimbusSanL-Bold', 7)
        self.string(self.nLeft + 1, self.nlin + 1, 'CÁLCULO DO IMPOSTO')
        self.rect(self.nLeft, self.nlin + 2,
                  self.width - self.nLeft - self.nRight, 13)
        self.hline(self.nLeft, self.nlin + 8.5, self.width - self.nLeft)
        self.vline(nMr - 35, self.nlin + 2, 6.5)
        self.vline(nMr - 65, self.nlin + 2, 6.5)
        self.vline(nMr - 95, self.nlin + 2, 6.5)
        self.vline(nMr - 125, self.nlin + 2, 6.5)
        self.vline(nMr - 155, self.nlin + 2, 6.5)
        self.vline(nMr - 35, self.nlin + 8.5, 6.5)
        self.vline(nMr - 65, self.nlin + 8.5, 6.5)
        self.vline(nMr - 95, self.nlin + 8.5, 6.5)
        self.vline(nMr - 125, self.nlin + 8.5, 6.5)
        self.vline(nMr - 155, self.nlin + 8.5, 6.5)
        # Labels
        self.canvas.setFont('NimbusSanL-Regu', 5)
        self.string(self.nLeft + 1, self.nlin + 3.8, 'BASE DE CÁLCULO DO ICMS')
        self.string(nMr - 154, self.nlin + 3.8, 'VALOR DO ICMS')
        self.string(nMr - 124, self.nlin + 3.8, 'BASE DE CÁLCULO DO ICMS ST')
        self.string(nMr - 94, self.nlin + 3.8, 'VALOR DO ICMS ST')
        self.string(nMr - 64, self.nlin + 3.8, 'VALOR APROX TRIBUTOS')
        self.string(nMr - 34, self.nlin + 3.8, 'VALOR TOTAL DOS PRODUTOS')

        self.string(self.nLeft + 1, self.nlin + 10.2, 'VALOR DO FRETE')
        self.string(nMr - 154, self.nlin + 10.2, 'VALOR DO SEGURO')
        self.string(nMr - 124, self.nlin + 10.2, 'DESCONTO')
        self.string(nMr - 94, self.nlin + 10.2, 'OUTRAS DESP. ACESSÓRIAS')
        self.string(nMr - 64, self.nlin + 10.2, 'VALOR DO IPI')
        self.string(nMr - 34, self.nlin + 10.2, 'VALOR TOTAL DA NOTA')

        # Conteúdo campos
        self.canvas.setFont('NimbusSanL-Regu', 8)
        self.stringRight(
            self.nLeft + 34, self.nlin + 7.7,
            format_number(tagtext(oNode=el_total, cTag='vBC')))
        self.stringRight(
            self.nLeft + 64, self.nlin + 7.7,
            format_number(tagtext(oNode=el_total, cTag='vICMS')))
        self.stringRight(
            self.nLeft + 94, self.nlin + 7.7,
            format_number(tagtext(oNode=el_total, cTag='vBCST')))
        self.stringRight(
            nMr - 66, self.nlin + 7.7,
            format_number(tagtext(oNode=el_total, cTag='vST')))
        self.stringRight(
            nMr - 36, self.nlin + 7.7,
            format_number(tagtext(oNode=el_total, cTag='vTotTrib')))
        self.stringRight(
            nMr - 1, self.nlin + 7.7,
            format_number(tagtext(oNode=el_total, cTag='vProd')))
        self.stringRight(
            self.nLeft + 34, self.nlin + 14.1,
            format_number(tagtext(oNode=el_total, cTag='vFrete')))
        self.stringRight(
            self.nLeft + 64, self.nlin + 14.1,
            format_number(tagtext(oNode=el_total, cTag='vSeg')))
        self.stringRight(
            self.nLeft + 94, self.nlin + 14.1,
            format_number(tagtext(oNode=el_total, cTag='vDesc')))
        self.stringRight(
            self.nLeft + 124, self.nlin + 14.1,
            format_number(tagtext(oNode=el_total, cTag='vOutro')))
        self.stringRight(
            self.nLeft + 154, self.nlin + 14.1,
            format_number(tagtext(oNode=el_total, cTag='vIPI')))
        self.stringRight(
            nMr - 1, self.nlin + 14.1,
            format_number(tagtext(oNode=el_total, cTag='vNF')))

        self.nlin += 17   # Nr linhas ocupadas pelo bloco

    def transportes(self, oXML=None):
        el_transp = oXML.find(".//{http://www.portalfiscal.inf.br/nfe}transp")
        veic_transp = oXML.find(
            ".//{http://www.portalfiscal.inf.br/nfe}veicTransp")
        nMr = self.width - self.nRight

        self.canvas.setFont('NimbusSanL-Bold', 7)
        self.string(self.nLeft + 1, self.nlin + 1,
                    'TRANSPORTADOR/VOLUMES TRANSPORTADOS')
        self.canvas.setFont('NimbusSanL-Regu', 5)
        self.rect(self.nLeft, self.nlin + 2,
                  self.width - self.nLeft - self.nRight, 20)
        self.hline(self.nLeft, self.nlin + 8.6, self.width - self.nLeft)
        self.hline(self.nLeft, self.nlin + 15.2, self.width - self.nLeft)
        self.vline(nMr - 40, self.nlin + 2, 13.2)
        self.vline(nMr - 49, self.nlin + 2, 20)
        self.vline(nMr - 92, self.nlin + 2, 6.6)
        self.vline(nMr - 120, self.nlin + 2, 6.6)
        self.vline(nMr - 75, self.nlin + 2, 6.6)
        self.vline(nMr - 26, self.nlin + 15.2, 6.6)
        self.vline(nMr - 102, self.nlin + 8.6, 6.6)
        self.vline(nMr - 85, self.nlin + 15.2, 6.6)
        self.vline(nMr - 121, self.nlin + 15.2, 6.6)
        self.vline(nMr - 160, self.nlin + 15.2, 6.6)
        # Labels/Fields
        self.string(nMr - 39, self.nlin + 3.8, 'CNPJ/CPF')
        self.string(nMr - 74, self.nlin + 3.8, 'PLACA DO VEÍCULO')
        self.string(nMr - 91, self.nlin + 3.8, 'CÓDIGO ANTT')
        self.string(nMr - 119, self.nlin + 3.8, 'FRETE POR CONTA')
        self.string(self.nLeft + 1, self.nlin + 3.8, 'RAZÃO SOCIAL')
        self.string(nMr - 48, self.nlin + 3.8, 'UF')
        self.string(nMr - 39, self.nlin + 10.3, 'INSCRIÇÃO ESTADUAL')
        self.string(nMr - 48, self.nlin + 10.3, 'UF')
        self.string(nMr - 101, self.nlin + 10.3, 'MUNICÍPIO')
        self.string(self.nLeft + 1, self.nlin + 10.3, 'ENDEREÇO')
        self.string(nMr - 48, self.nlin + 17, 'PESO BRUTO')
        self.string(nMr - 25, self.nlin + 17, 'PESO LÍQUIDO')
        self.string(nMr - 84, self.nlin + 17, 'NUMERAÇÃO')
        self.string(nMr - 120, self.nlin + 17, 'MARCA')
        self.string(nMr - 159, self.nlin + 17, 'ESPÉCIE')
        self.string(self.nLeft + 1, self.nlin + 17, 'QUANTIDADE')
        # Conteúdo campos
        self.canvas.setFont('NimbusSanL-Regu', 8)
        self.string(self.nLeft + 1, self.nlin + 7.7,
                    tagtext(oNode=el_transp, cTag='xNome')[:40])
        self.string(self.nLeft + 71, self.nlin + 7.7,
                    self.oFrete[tagtext(oNode=el_transp, cTag='modFrete')])
        self.string(self.nLeft + 99, self.nlin + 7.7,
                    tagtext(oNode=el_transp, cTag='RNTC'))
        self.string(self.nLeft + 116, self.nlin + 7.7,
                    tagtext(oNode=el_transp, cTag='placa'))
        self.string(self.nLeft + 142, self.nlin + 7.7,
                    tagtext(oNode=veic_transp, cTag='UF'))
        self.string(nMr - 39, self.nlin + 7.7,
                    format_cnpj_cpf(tagtext(oNode=el_transp, cTag='CNPJ')))
        self.string(self.nLeft + 1, self.nlin + 14.2,
                    tagtext(oNode=el_transp, cTag='xEnder')[:45])
        self.string(self.nLeft + 89, self.nlin + 14.2,
                    tagtext(oNode=el_transp, cTag='xMun'))
        self.string(nMr - 48, self.nlin + 14.2,
                    tagtext(oNode=el_transp, cTag='UF'))
        self.string(nMr - 39, self.nlin + 14.2,
                    tagtext(oNode=el_transp, cTag='IE'))
        self.string(self.nLeft + 1, self.nlin + 21.2,
                    tagtext(oNode=el_transp, cTag='qVol'))
        self.string(self.nLeft + 31, self.nlin + 21.2,
                    tagtext(oNode=el_transp, cTag='esp'))
        self.string(self.nLeft + 70, self.nlin + 21.2,
                    tagtext(oNode=el_transp, cTag='marca'))
        self.string(self.nLeft + 106, self.nlin + 21.2,
                    tagtext(oNode=el_transp, cTag='nVol'))
        self.stringRight(
            nMr - 27, self.nlin + 21.2,
            format_number(tagtext(oNode=el_transp, cTag='pesoB')))
        self.stringRight(
            nMr - 1, self.nlin + 21.2,
            format_number(tagtext(oNode=el_transp, cTag='pesoL')))

        self.nlin += 23

    def produtos(self, oXML=None, el_det=None, oPaginator=None,
                 list_desc=None, list_cod_prod=None, nHeight=29):

        nMr = self.width - self.nRight
        nStep = 2.5  # Passo entre linhas
        nH = 7.5 + (nHeight * nStep)  # cabeçalho 7.5
        self.nlin += 1

        self.canvas.setFont('NimbusSanL-Bold', 7)
        self.string(self.nLeft + 1, self.nlin + 1, 'DADOS DO PRODUTO/SERVIÇO')
        self.rect(self.nLeft, self.nlin + 2,
                  self.width - self.nLeft - self.nRight, nH)
        self.hline(self.nLeft, self.nlin + 8, self.width - self.nLeft)

        self.canvas.setFont('NimbusSanL-Regu', 5.5)
        # Colunas
        self.vline(self.nLeft + 15, self.nlin + 2, nH)
        self.stringcenter(self.nLeft + 7.5, self.nlin + 5.5, 'CÓDIGO')
        self.vline(nMr - 7, self.nlin + 2, nH)
        self.stringcenter(nMr - 3.5, self.nlin + 4.5, 'ALÍQ')
        self.stringcenter(nMr - 3.5, self.nlin + 6.5, 'IPI')
        self.vline(nMr - 14, self.nlin + 2, nH)
        self.stringcenter(nMr - 10.5, self.nlin + 4.5, 'ALÍQ')
        self.stringcenter(nMr - 10.5, self.nlin + 6.5, 'ICMS')
        self.vline(nMr - 26, self.nlin + 2, nH)
        self.stringcenter(nMr - 20, self.nlin + 5.5, 'VLR. IPI')
        self.vline(nMr - 38, self.nlin + 2, nH)
        self.stringcenter(nMr - 32, self.nlin + 5.5, 'VLR. ICMS')
        self.vline(nMr - 50, self.nlin + 2, nH)
        self.stringcenter(nMr - 44, self.nlin + 5.5, 'BC ICMS')
        self.vline(nMr - 64, self.nlin + 2, nH)
        self.stringcenter(nMr - 57, self.nlin + 5.5, 'VLR TOTAL')
        self.vline(nMr - 78, self.nlin + 2, nH)
        self.stringcenter(nMr - 70.5, self.nlin + 5.5, 'VLR UNIT')
        self.vline(nMr - 90, self.nlin + 2, nH)
        self.stringcenter(nMr - 83.8, self.nlin + 5.5, 'QTD')
        self.vline(nMr - 96, self.nlin + 2, nH)
        self.stringcenter(nMr - 93, self.nlin + 5.5, 'UNID')
        self.vline(nMr - 102, self.nlin + 2, nH)
        self.stringcenter(nMr - 99, self.nlin + 5.5, 'CFOP')
        self.vline(nMr - 108, self.nlin + 2, nH)
        self.stringcenter(nMr - 105, self.nlin + 5.5, 'CST')
        self.vline(nMr - 117, self.nlin + 2, nH)
        self.stringcenter(nMr - 112.5, self.nlin + 5.5, 'NCM/SH')

        nWidth_Prod = nMr - 135 - self.nLeft - 11
        nCol_ = self.nLeft + 20 + (nWidth_Prod / 2)
        self.stringcenter(nCol_, self.nlin + 5.5,
                          'DESCRIÇÃO DO PRODUTO/SERVIÇO')

        # Conteúdo campos
        self.canvas.setFont('NimbusSanL-Regu', 5)
        nLin = self.nlin + 10.5

        for id in range(oPaginator[0], oPaginator[1]):
            item = el_det[id]
            el_prod = item.find(".//{http://www.portalfiscal.inf.br/nfe}prod")
            el_imp = item.find(
                ".//{http://www.portalfiscal.inf.br/nfe}imposto")

            el_imp_ICMS = el_imp.find(
                ".//{http://www.portalfiscal.inf.br/nfe}ICMS")
            el_imp_IPI = el_imp.find(
                ".//{http://www.portalfiscal.inf.br/nfe}IPI")
            cCST = tagtext(oNode=el_imp_ICMS, cTag='orig') + \
                (tagtext(oNode=el_imp_ICMS, cTag='CST') or
                 tagtext(oNode=el_imp_ICMS, cTag='CSOSN'))
            vBC = tagtext(oNode=el_imp_ICMS, cTag='vBC')
            vICMS = tagtext(oNode=el_imp_ICMS, cTag='vICMS')
            pICMS = tagtext(oNode=el_imp_ICMS, cTag='pICMS')

            vIPI = tagtext(oNode=el_imp_IPI, cTag='vIPI')
            pIPI = tagtext(oNode=el_imp_IPI, cTag='pIPI')

            self.stringcenter(nMr - 112.5, nLin,
                              tagtext(oNode=el_prod, cTag='NCM'))
            self.stringcenter(nMr - 105, nLin, cCST)
            self.stringcenter(nMr - 99, nLin,
                              tagtext(oNode=el_prod, cTag='CFOP'))
            self.stringcenter(nMr - 93, nLin,
                              tagtext(oNode=el_prod, cTag='uCom'))
            self.stringRight(nMr - 78.5, nLin, format_number(
                tagtext(oNode=el_prod, cTag='qCom')))
            self.stringRight(nMr - 64.5, nLin, format_number(
                tagtext(oNode=el_prod, cTag='vUnCom')))
            self.stringRight(nMr - 50.5, nLin,
                             tagtext(oNode=el_prod, cTag='vProd'))
            self.stringRight(nMr - 38.5, nLin, format_number(vBC))
            self.stringRight(nMr - 26.5, nLin, format_number(vICMS))
            self.stringRight(nMr - 7.5, nLin, format_number(pICMS))

            if vIPI:
                self.stringRight(nMr - 14.5, nLin, format_number(vIPI))
            if pIPI:
                self.stringRight(nMr - 0.5, nLin, format_number(pIPI))

            # Código Item
            line_cod = nLin
            for des in list_cod_prod[id]:
                self.string(self.nLeft + 0.2, line_cod, des)
                line_cod += nStep

            # Descrição Item
            line_desc = nLin
            for des in list_desc[id]:
                self.string(self.nLeft + 15.5, line_desc, des)
                line_desc += nStep

            nLin = max(line_cod, line_desc)
            self.canvas.setStrokeColor(gray)
            self.hline(self.nLeft, nLin - 2, self.width - self.nLeft)
            self.canvas.setStrokeColor(black)

        self.nlin += nH + 3

    def adicionais(self, oXML=None):
        el_infAdic = oXML.find(
            ".//{http://www.portalfiscal.inf.br/nfe}infAdic")

        self.nlin += 2
        self.canvas.setFont('NimbusSanL-Bold', 6)
        self.string(self.nLeft + 1, self.nlin + 1, 'DADOS ADICIONAIS')
        self.canvas.setFont('NimbusSanL-Regu', 5)
        self.string(self.nLeft + 1, self.nlin + 4,
                    'INFORMAÇÕES COMPLEMENTARES')
        self.string((self.width / 2) + 1, self.nlin + 4, 'RESERVADO AO FISCO')
        self.rect(self.nLeft, self.nlin + 2,
                  self.width - self.nLeft - self.nRight, 42)
        self.vline(self.width / 2, self.nlin + 2, 42)
        # Conteúdo campos
        styles = getSampleStyleSheet()
        styleN = styles['Normal']
        styleN.fontSize = 6
        styleN.fontName = 'NimbusSanL-Regu'
        styleN.leading = 7
        fisco = tagtext(oNode=el_infAdic, cTag='infAdFisco')
        observacoes = tagtext(oNode=el_infAdic, cTag='infCpl')
        if fisco:
            observacoes = fisco + ' ' + observacoes
        P = Paragraph(observacoes, styles['Normal'])
        w, h = P.wrap(92 * mm, 32 * mm)
        altura = (self.height - self.nlin - 5) * mm
        P.drawOn(self.canvas, (self.nLeft + 1) * mm, altura - h)
        self.nlin += 36

    def recibo_entrega(self, oXML=None, timezone=None):
        el_ide = oXML.find(".//{http://www.portalfiscal.inf.br/nfe}ide")
        el_dest = oXML.find(".//{http://www.portalfiscal.inf.br/nfe}dest")
        el_total = oXML.find(".//{http://www.portalfiscal.inf.br/nfe}total")
        el_emit = oXML.find(".//{http://www.portalfiscal.inf.br/nfe}emit")

        # self.nlin = self.height-self.nBottom-18  # 17 altura recibo
        nW = 40
        nH = 17
        self.canvas.setLineWidth(.5)
        self.rect(self.nLeft, self.nlin,
                  self.width - (self.nLeft + self.nRight), nH)
        self.hline(self.nLeft, self.nlin + 8.5, self.width - self.nRight - nW)
        self.vline(self.width - self.nRight - nW, self.nlin, nH)
        self.vline(self.nLeft + nW, self.nlin + 8.5, 8.5)

        # Labels
        self.canvas.setFont('NimbusSanL-Regu', 5)
        self.string(self.nLeft + 1, self.nlin + 10.2, 'DATA DE RECEBIMENTO')
        self.string(self.nLeft + 41, self.nlin + 10.2,
                    'IDENTIFICAÇÃO E ASSINATURA DO RECEBEDOR')
        self.stringcenter(self.width - self.nRight -
                          (nW / 2), self.nlin + 2, 'NF-e')
        # Conteúdo campos
        self.canvas.setFont('NimbusSanL-Bold', 8)
        cNF = tagtext(oNode=el_ide, cTag='nNF')
        cNF = '{0:011,}'.format(int(cNF)).replace(",", ".")
        self.string(self.width - self.nRight - nW +
                    2, self.nlin + 8, "Nº %s" % (cNF))
        self.string(self.width - self.nRight - nW + 2, self.nlin + 14,
                    "SÉRIE %s" % (tagtext(oNode=el_ide, cTag='serie')))

        cDt, cHr = getdateByTimezone(
            tagtext(oNode=el_ide, cTag='dhEmi'), timezone)
        cTotal = format_number(tagtext(oNode=el_total, cTag='vNF'))

        cEnd = tagtext(oNode=el_dest, cTag='xNome') + ' - '
        cEnd += tagtext(oNode=el_dest, cTag='xLgr') + ', ' + tagtext(
            oNode=el_dest, cTag='nro') + ', '
        cEnd += tagtext(oNode=el_dest, cTag='xBairro') + ', ' + tagtext(
            oNode=el_dest, cTag='xMun') + ' - '
        cEnd += tagtext(oNode=el_dest, cTag='UF')

        cString = """
        RECEBEMOS DE %s OS PRODUTOS/SERVIÇOS CONSTANTES DA NOTA FISCAL INDICADA
        ABAIXO. EMISSÃO: %s VALOR TOTAL: %s
        DESTINATARIO: %s""" % (tagtext(oNode=el_emit, cTag='xNome'),
                               cDt, cTotal, cEnd)

        styles = getSampleStyleSheet()
        styleN = styles['Normal']
        styleN.fontName = 'NimbusSanL-Regu'
        styleN.fontSize = 6
        styleN.leading = 7

        P = Paragraph(cString, styleN)
        w, h = P.wrap(149 * mm, 7 * mm)
        P.drawOn(self.canvas, (self.nLeft + 1) * mm,
                 ((self.height - self.nlin) * mm) - h)

        self.nlin += 20
        self.hline(self.nLeft, self.nlin, self.width - self.nRight)
        self.nlin += 2

    def newpage(self):
        self.nlin = self.nTop
        self.Page += 1
        self.canvas.showPage()

    def hline(self, x, y, width):
        y = self.height - y
        self.canvas.line(x * mm, y * mm, width * mm, y * mm)

    def vline(self, x, y, width):
        width = self.height - y - width
        y = self.height - y
        self.canvas.line(x * mm, y * mm, x * mm, width * mm)

    def rect(self, col, lin, nWidth, nHeight, fill=False):
        lin = self.height - nHeight - lin
        self.canvas.rect(col * mm, lin * mm, nWidth * mm, nHeight * mm,
                         stroke=True, fill=fill)

    def string(self, x, y, value):
        y = self.height - y
        self.canvas.drawString(x * mm, y * mm, value)

    def stringRight(self, x, y, value):
        y = self.height - y
        self.canvas.drawRightString(x * mm, y * mm, value)

    def stringcenter(self, x, y, value):
        y = self.height - y
        self.canvas.drawCentredString(x * mm, y * mm, value)

    def writeto_pdf(self, fileObj):
        pdf_out = self.oPDF_IO.getvalue()
        self.oPDF_IO.close()
        fileObj.write(pdf_out)

    def _generate_cce(self, cce_xml=None, oXML=None, timezone=None):
        self.canvas.setLineWidth(.2)

        # labels
        self.canvas.setFont('NimbusSanL-Bold', 12)
        self.stringcenter(105, 10, u"Carta de Correção")
        self.canvas.setFont('NimbusSanL-Regu', 6)
        self.string(10, 18, u"RAZÃO SOCIAL DO EMITENTE")
        self.string(10, 24, u"CNPJ DO EMITENTE")
        self.string(10, 30, u"CHAVE DE ACESSO DA NF-E")
        self.string(10, 36, u"DATA DA CORREÇÃO")
        self.string(10, 42, u"ID")
        self.stringcenter(105, 48, u"CORREÇÃO")

        # lines
        self.hline(9, 14, 200)
        self.hline(9, 20, 200)
        self.hline(9, 26, 200)
        self.hline(9, 32, 200)
        self.hline(9, 38, 200)
        self.hline(9, 44, 200)
        self.hline(9, 50, 200)

        # values
        infNFe = oXML.find(
            ".//{http://www.portalfiscal.inf.br/nfe}infNFe")
        res_partner = infNFe.find(
            ".//{http://www.portalfiscal.inf.br/nfe}xNome")

        elem_infNFe = cce_xml.find(
            ".//{http://www.portalfiscal.inf.br/nfe}infEvento")

        res_partner = tagtext(oNode=infNFe, cTag='xNome')
        self.string(82, 18, res_partner)
        cnpj = format_cnpj_cpf(tagtext
                               (oNode=elem_infNFe, cTag='CNPJ'))
        self.string(82, 24, cnpj)
        chave_acesso = tagtext(oNode=elem_infNFe, cTag='chNFe')
        self.string(82, 30, chave_acesso)
        data_correcao = getdateByTimezone(tagtext(
            oNode=elem_infNFe, cTag='dhEvento'), timezone)
        data_correcao = data_correcao[0] + "  " + data_correcao[1]
        self.string(82, 36, data_correcao)
        cce_id = elem_infNFe.values()[0]
        self.string(82, 42, cce_id)

        correcao = tagtext(oNode=elem_infNFe, cTag='xCorrecao')

        w, h, paragraph = self._paragraph(
            correcao, 'NimbusSanL-Regu', 10, 190 * mm, 20 * mm)
        paragraph.drawOn(self.canvas, 10 * mm, (297 - 52) * mm - h)

        self.hline(9, 54 + (h / mm), 200)
        self.stringcenter(105, 58 + (h / mm), u"CONDIÇÃO DE USO")
        self.hline(9, 60 + (h / mm), 200)

        condicoes = tagtext(oNode=elem_infNFe, cTag='xCondUso')

        w2, h2, paragraph = self._paragraph(
            condicoes, 'NimbusSanL-Regu', 10, 190 * mm, 20 * mm)
        paragraph.drawOn(self.canvas, 10 * mm, (297 - 62) * mm - h - h2)

        self.hline(9, 68 + ((h + h2) / mm), 200)

        self.vline(80, 14, 30)
        self.vline(9, 14, 54 + ((h + h2) / mm))
        self.vline(200, 14, 54 + ((h + h2) / mm))

    def _paragraph(self, text, font, font_size, x, y):
        ptext = '<font size=%s>%s</font>' % (font_size, text)
        style = ParagraphStyle(name='Normal',
                               fontName=font,
                               fontSize=font_size,
                               )
        paragraph = Paragraph(ptext, style=style)
        w, h = paragraph.wrapOn(self.canvas, x, y)
        return w, h, paragraph
