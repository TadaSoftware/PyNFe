from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod

class ServidorNFEFalso(SimpleWSGISoapApp):
    from soaplib.serializers.primitive import String, Integer, Array, Null

    @soapmethod(String, Integer, _returns=String)
    def ping(self, palavra, vezes):
        return ','.join([palavra for i in range(vezes)])

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

