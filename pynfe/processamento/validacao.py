#-*- coding:utf-8 -*-

from os import path

try:
    from lxml import etree
except ImportError:
    raise Exception('Falhou ao importar modulo lxml')

XSD_FOLDER = "pynfe/data/XSDs/"

XSD_NFE="nfe_v1.10.xsd"
XSD_NFE_PROCESSADA="procNFe_v1.10.xsd"
XSD_PD_CANCELAR_NFE="procCancNFe_v1.07.xsd"
XSD_PD_INUTILIZAR_NFE="procInutNFe_v1.07.xsd"

def get_xsd(xsd_file):
    """Retorna o caminho absoluto para um arquivo xsd.
    Argumentos:
        xsd_file - nome do arquivo xsd (utilizar nomes definidos em validacao.py)
    """
    return path.abspath(path.join(XSD_FOLDER, xsd_file))

class Validacao(object):
    '''Valida documentos xml a partir do xsd informado.'''

    def __init__(self):
        self.clear_cache()

    def clear_cache(self):
        self.MEM_CACHE = {}

    def validar_xml(self, xml_path, xsd_file, use_assert=False):
        '''Valida um arquivo xml.
        Argumentos:
            xml_path - caminho para arquivo xml
            xsd_file - caminho para o arquivo xsd
            use_assert - levantar exceção caso documento não valide?
        '''
        return self.validar_etree(etree.parse(xml_path), xsd_file, use_assert)

    def validar_etree(self, xml_doc, xsd_file, use_assert=False):
        '''Valida um documento lxml diretamente.
        Argumentos:
            xml_doc - documento etree
            xsd_file - caminho para o arquivo xsd
            use_assert - levantar exceção caso documento não valide?
        '''
        #xsd_filepath = get_xsd(xsd_file)

        try:
            # checa se o schema ja existe no cache
            #xsd_schema = self.MEM_CACHE[xsd_filepath]
            xsd_schema = self.MEM_CACHE[xsd_file]
        except:
            # lê xsd e atualiza cache
            #xsd_doc = etree.parse(xsd_filepath)
            xsd_doc = etree.parse(xsd_file)
            xsd_schema = etree.XMLSchema(xsd_doc)
            self.MEM_CACHE[xsd_file] = xsd_schema
        return use_assert and xsd_schema.assertValid(xml_doc) \
               or xsd_schema.validate(xml_doc)
