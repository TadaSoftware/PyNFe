from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers.primitive import String, Integer, Array

import tornado.httpserver
import tornado.ioloop

class ServidorNFEFalso(SimpleWSGISoapApp):
    @soapmethod(String,Integer,_returns=Array(String))
    def ping(self,name,times):
        results = []
        for i in range(0,times):
            results.append('Hello, %s'%name)
        return results

if __name__ == '__main__':
    porta = 8080

    http_server = tornado.httpserver.HTTPServer(ServidorNFEFalso())
    http_server.listen(porta)
    tornado.ioloop.IOLoop.instance().start()

