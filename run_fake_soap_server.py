from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod

class ServidorNFEFalso(SimpleWSGISoapApp):
    from soaplib.serializers.primitive import String, Integer, Array, Null

    @soapmethod(_returns=Null)
    def finalizar(self):
        import sys
        sys.exit(0)

    @soapmethod(_returns=String)
    def ping(self):
        return 'eu estou aqui'

if __name__ == '__main__':
    porta = 8081

    # Via Tornado
    #import tornado.httpserver
    #import tornado.ioloop
    #http_server = tornado.httpserver.HTTPServer(ServidorNFEFalso())
    #http_server.listen(porta)
    #tornado.ioloop.IOLoop.instance().start()

    # Via CherryPy
    from cherrypy.wsgiserver import CherryPyWSGIServer
    server = CherryPyWSGIServer(('localhost', porta), ServidorNFEFalso())
    server.start()

