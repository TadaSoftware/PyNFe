#-*- coding:utf-8 -*-

from os import path
from glob import glob

try:
    from lxml import etree
except ImportError:
    try:
        # Python 2.5 - cElementTree
        import xml.etree.cElementTree as etree
    except ImportError:
        try:
            # Python 2.5 - ElementTree
            import xml.etree.ElementTree as etree
        except ImportError:
            try:
                # Instalacao normal do cElementTree
                import cElementTree as etree
            except ImportError:
                try:
                    # Instalacao normal do ElementTree
                    import elementtree.ElementTree as etree
                except ImportError:
                    raise Exception('Falhou ao importar lxml/ElementTree')

XSD_FOLDER = "data/XSDs/"

XSD_NFE="nfe_v1.10.xsd"
XSD_NFE_PROCESSADA="procNFe_v1.10.xsd"
XSD_PD_CANCELAR_NFE="procCancNFe_v1.07.xsd"
XSD_PD_INUTILIZAR_NFE="procInutNFe_v1.07.xsd"

class Validacao(object):
    '''Valida documentos xml a partir do xsd informado'''
    def __init__(self):
        self.clear_cache()
    
    def clear_cache(self):
        self.MEM_CACHE = {}
    
    def validar_xml(self, xml_path, xsd_file):
        '''Valida um arquivo xml
        Argumentos:
            xml_filepath - caminho para arquivo xml
            xsd_file - caminho para o arquivo xsd
        '''
        return self._validar(etree.parse(xml_path), xsd_file)
    
    def _validar(self, xml_doc, xsd_file):
        xsd_filepath = path.join(XSD_FOLDER, xsd_file)
        
        try:
            xsd_schema = self.MEM_CACHE[xsd_file]
        except:
            xsd_doc = etree.parse(xsd_file)
            xsd_schema = etree.XMLSchema(xsd_doc)
        return xsd_schema.validate(xml_doc)
    
    # alias
    validar_etree = _validar
    