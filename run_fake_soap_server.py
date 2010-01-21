# -*- coding: utf-8 -*-

"""Este script deve ser executado com Python 2.6+ e OpenSSL"""

import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

#from soaplib.wsgi_soap import SimpleWSGISoapApp
#from soaplib.service import soapmethod
#from soaplib.serializers.primitive import String, Integer, Array, Null

#import tornado.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

#class ServidorNFEFalso(SimpleWSGISoapApp):
#    @soapmethod(String, Integer, _returns=Array(String))
#    def ping(self, nome, vezes):
#        ret = [nome for i in range(vezes)]
#        return ret

class HandlerStatusServico(tornado.web.RequestHandler):
    def post(self):
        self.write('<x/>')

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

