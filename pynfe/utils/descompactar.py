"""
@author: Lucas Resende

classe que descompacta o gzip recebido pela consulta distribuicao

"""

from io import BytesIO
import base64
import gzip
from lxml import etree


class DescompactaGzip(object):
    @staticmethod
    def descompacta(stringZipada):
        """
        :paramn stringZipada: String

        :return : Etree
        """
        arq = BytesIO()
        arq.write(base64.b64decode(stringZipada))
        arq.seek(0)
        zip = gzip.GzipFile(fileobj=arq)
        texto = zip.read()
        arq.close()
        zip.close()
        descompactado = texto.decode("utf-8").encode()
        return etree.fromstring(descompactado)
