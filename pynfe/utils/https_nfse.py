"""
@author: Junior Tada, Leonardo Tada

Classe que sobrescreve metodos da lib suds para comunicação via https com certificado digital

"""

from suds.transport.http import HttpTransport
import urllib.request
import http.client


class HTTPSClientAuthHandler(urllib.request.HTTPSHandler):
    def __init__(self, key, cert):
        urllib.request.HTTPSHandler.__init__(self)
        self.key = key
        self.cert = cert

    def https_open(self, req):
        # Rather than pass in a reference to a connection class, we pass in
        # a reference to a function which, for all intents and purposes,
        # will behave as a constructor
        return self.do_open(self.getConnection, req)

    def getConnection(self, host, timeout=300):
        return http.client.HTTPSConnection(host, key_file=self.key, cert_file=self.cert)


class HttpAuthenticated(HttpTransport):
    def __init__(self, key, cert, endereco, *args, **kwargs):
        HttpTransport.__init__(self, *args, **kwargs)
        self.key = key
        self.cert = cert
        self.endereco = endereco

    # def open(self, request):
    #     opener = urllib.request.build_opener(HTTPSClientAuthHandler(self.key, self.cert))
    #     return opener.open(self.endereco)

    def u2handlers(self):
        return [HTTPSClientAuthHandler(self.key, self.cert)]
