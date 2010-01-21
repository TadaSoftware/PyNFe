# -*- coding: utf-8 -*-

"""Este script deve ser executado com Python 2.6+ e OpenSSL"""

import os, datetime

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

#from soaplib.wsgi_soap import SimpleWSGISoapApp
#from soaplib.service import soapmethod
#from soaplib.serializers.primitive import String, Integer, Array, Null

#import tornado.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

from pynfe.utils import etree, StringIO, extrair_tag
from pynfe.utils.flags import CODIGOS_ESTADOS

#class ServidorNFEFalso(SimpleWSGISoapApp):
#    @soapmethod(String, Integer, _returns=Array(String))
#    def ping(self, nome, vezes):
#        ret = [nome for i in range(vezes)]
#        return ret

class HandlerStatusServico(tornado.web.RequestHandler):
    sigla_servidor = 'GO'

    def post(self):
        # Obtem o body da request
        xml = self.request.body

        # Transforma em etree
        raiz = etree.parse(StringIO(xml))

        # Extrai a tag do método da request
        tag = extrair_tag(raiz.getroot().getchildren()[0].getchildren()[0])

        # Chama o método respectivo para a tag
        print 'Metodo:', tag
        getattr(self, tag)(raiz)

    def nfeStatusServicoNF2(self, raiz):
        data_hora = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        ret = etree.Element('retConsStatServ')
        etree.SubElement(ret, 'versao').text = '1.00' # FIXME
        etree.SubElement(ret, 'tbAmb').text = '2' # Homologação
        etree.SubElement(ret, 'verAplic').text = self.sigla_servidor
        etree.SubElement(ret, 'cStat').text = '1' # FIXME
        etree.SubElement(ret, 'xMotivo').text = 'Servico em funcionamento normal' # FIXME
        etree.SubElement(ret, 'cUF').text = CODIGOS_ESTADOS[self.sigla_servidor]
        etree.SubElement(ret, 'dhRecbto').text = data_hora
        etree.SubElement(ret, 'tMed').text = '10'
        etree.SubElement(ret, 'dhRetorno').text = data_hora
        etree.SubElement(ret, 'xObs').text = 'Nenhuma informacao adicional'

        xml = etree.tostring(ret, encoding='utf-8', xml_declaration=True)
        self.write(xml)

    def nfeInutilizacaoNF(self, raiz):
        data_hora = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        ret = etree.Element('retInutNFe')
        etree.SubElement(ret, 'versao').text = '1.00' # FIXME

        xml_dados = raiz.getroot().getchildren()[0].getchildren()[0].getchildren()[1].text

        xml = etree.tostring(ret, encoding='utf-8', xml_declaration=True)
        self.write(xml)

if __name__ == '__main__':
    porta = 8080

    # Codigo específico da soaplib
    #application = ServidorNFEFalso()
    #container = tornado.wsgi.WSGIContainer(application)
    #http_server = tornado.httpserver.HTTPServer(container)
    
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r'^/nfeweb/services/nfestatusservico.asmx$', HandlerStatusServico), # Consulta de status do serviço
        ])

    ssl_options = {
            'certfile': os.path.join(CUR_DIR, 'tests', 'certificado.pem'),
            'keyfile': os.path.join(CUR_DIR, 'tests', 'key.pem'),
            }

    http_server = tornado.httpserver.HTTPServer(application, ssl_options=ssl_options)
    http_server.listen(porta)
    tornado.ioloop.IOLoop.instance().start()

