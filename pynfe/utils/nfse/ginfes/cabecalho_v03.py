# ./cabecalho_v03.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1981a932e981e99644ad0c4bcf57cfb2bf9f2e12
# Generated 2015-12-21 11:05:54.422726 by PyXB version 1.2.4 using Python 3.5.1.final.0
# Namespace http://www.ginfes.com.br/cabecalho_v03.xsd

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9150f830-a7e3-11e5-9c9b-b8ee65084bc8')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
from pynfe.utils.nfse.ginfes import _tipos as _ImportedBinding__tipos
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.ginfes.com.br/cabecalho_v03.xsd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/leonardo/Downloads/cabecalho_v03.xsd', 8, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element versaoDados uses Python identifier versaoDados
    __versaoDados = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'versaoDados'), 'versaoDados', '__httpwww_ginfes_com_brcabecalho_v03_xsd_CTD_ANON_versaoDados', False, pyxb.utils.utility.Location('/home/leonardo/Downloads/cabecalho_v03.xsd', 10, 4), )

    
    versaoDados = property(__versaoDados.value, __versaoDados.set, None, None)

    
    # Attribute versao uses Python identifier versao
    __versao = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'versao'), 'versao', '__httpwww_ginfes_com_brcabecalho_v03_xsd_CTD_ANON_versao', _ImportedBinding__tipos.tsVersao, required=True)
    __versao._DeclarationLocation = pyxb.utils.utility.Location('/home/leonardo/Downloads/cabecalho_v03.xsd', 13, 3)
    __versao._UseLocation = pyxb.utils.utility.Location('/home/leonardo/Downloads/cabecalho_v03.xsd', 13, 3)
    
    versao = property(__versao.value, __versao.set, None, None)

    _ElementMap.update({
        __versaoDados.name() : __versaoDados
    })
    _AttributeMap.update({
        __versao.name() : __versao
    })



cabecalho = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cabecalho'), CTD_ANON, location=pyxb.utils.utility.Location('/home/leonardo/Downloads/cabecalho_v03.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', cabecalho.name().localName(), cabecalho)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'versaoDados'), _ImportedBinding__tipos.tsVersao, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/leonardo/Downloads/cabecalho_v03.xsd', 10, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'versaoDados')), pyxb.utils.utility.Location('/home/leonardo/Downloads/cabecalho_v03.xsd', 10, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

