#-*- coding:utf-8 -*-

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

class Validacao(object):
    pass

