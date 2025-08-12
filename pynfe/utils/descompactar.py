"""
@author: Lucas Resende

classe que descompacta o gzip recebido pela consulta distribuicao

"""

import base64
import gzip
from lxml import etree


class DescompactaGzip(object):
    @staticmethod
    def descompacta(stringZipada: str):
        """
        :paramn stringZipada: String

        :return : Etree
        """
        decoded = base64.b64decode(stringZipada)
        decompress_nfe = gzip.decompress(decoded).decode("utf8")
        return etree.fromstring(decompress_nfe)
