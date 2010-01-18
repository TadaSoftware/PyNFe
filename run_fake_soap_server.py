from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers.primitive import String, Integer, Array, Null

class ServidorNFEFalso(SimpleWSGISoapApp):
    @soapmethod(String, Integer, _returns=Array(String))
    def ping(self, nome, vezes):
        ret = [nome for i in range(vezes)]
        print ret
        return ret

if __name__ == '__main__':
    porta = 8080

    # Via Tornado
    import tornado.wsgi
    import tornado.httpserver
    import tornado.ioloop
    application = ServidorNFEFalso()
    container = tornado.wsgi.WSGIContainer(application)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(porta)
    tornado.ioloop.IOLoop.instance().start()

