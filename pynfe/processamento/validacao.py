# -*- coding:utf-8 -*-

from os import path
import io

try:
    from lxml import etree
except ImportError:
    raise Exception("Falhou ao importar modulo lxml")

from pynfe.utils.flags import XSD_FOLDER_NFE


class Validacao(object):
    """Valida documentos xml a partir do xsd informado."""

    def __init__(self):
        self.clear_cache()

    def clear_cache(self):
        self.MEM_CACHE = {}

    def get_xsd(self, xsd_file, xsd_folder=XSD_FOLDER_NFE):
        """Retorna o caminho absoluto para um arquivo xsd.
        Argumentos:
            xsd_file - nome do arquivo xsd (utilizar nomes definidos em validacao.py)
            xsd_folder - pasta onde estão os arquivos xsd, default=XSD_FOLDER_NFE
        Retorno:
            caminho absoluto para o arquivo xsd
        """
        return path.abspath(path.join(xsd_folder, xsd_file))

    def validar_xml(self, xml_path, xsd_file, use_assert=False):
        """Valida um arquivo xml.
        Argumentos:
            xml_path - caminho para arquivo xml
            xsd_file - caminho para o arquivo xsd
            use_assert - levantar exceção caso documento não valide?
        Retorno:
            True se validou, False caso contrário
        """
        return self.validar_etree(etree.parse(xml_path), xsd_file, use_assert)

    def validar_etree(self, xml_doc, xsd_file, use_assert=False):
        """Valida um documento lxml diretamente.
        Argumentos:
            xml_doc - documento etree
            xsd_file - caminho para o arquivo xsd
            use_assert - levantar exceção caso documento não valide?
        Retorno:
            True se validou, False caso contrário
        """
        try:
            # checa se o schema ja existe no cache
            xsd_schema = self.MEM_CACHE[xsd_file]
        except Exception:
            # lê xsd e atualiza cache
            xsd_doc = etree.parse(xsd_file)
            xsd_schema = etree.XMLSchema(xsd_doc)
            self.MEM_CACHE[xsd_file] = xsd_schema

            with io.StringIO() as buffer:
                buffer.write(etree.tostring(xml_doc).decode("utf-8"))
                buffer.seek(0)
                xml_doc = etree.parse(buffer)

        return use_assert and xsd_schema.assertValid(xml_doc) or xsd_schema.validate(xml_doc)
