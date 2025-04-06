# flake8: noqa
# pynfe/utils/nfse/ginfes/servico_enviar_lote_rps_envio_v03.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:712dac5bd3f3f6cf5f89daa94c22f15b489de55b
# Generated 2025-04-06 00:00:52.138071 by PyXB version 1.2.6 using Python 3.12.9.final.0
# Namespace http://www.ginfes.com.br/servico_enviar_lote_rps_envio_v03.xsd

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:39de2bfc-9ae4-40e1-bb37-494b66bc6a8d')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
from pynfe.utils.nfse.ginfes import _dsig as _ImportedBinding__dsig
from pynfe.utils.nfse.ginfes import _tipos as _ImportedBinding__tipos
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.ginfes.com.br/servico_enviar_lote_rps_envio_v03.xsd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_dsig = _ImportedBinding__dsig.Namespace
_Namespace_dsig.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/servico_enviar_lote_rps_envio_v03.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ginfes.com.br/servico_enviar_lote_rps_envio_v03.xsd}LoteRps uses Python identifier LoteRps
    __LoteRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LoteRps'), 'LoteRps', '__httpwww_ginfes_com_brservico_enviar_lote_rps_envio_v03_xsd_CTD_ANON_httpwww_ginfes_com_brservico_enviar_lote_rps_envio_v03_xsdLoteRps', False, pyxb.utils.utility.Location('/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/servico_enviar_lote_rps_envio_v03.xsd', 9, 4), )

    
    LoteRps = property(__LoteRps.value, __LoteRps.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), 'Signature', '__httpwww_ginfes_com_brservico_enviar_lote_rps_envio_v03_xsd_CTD_ANON_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd', 41, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __LoteRps.name() : __LoteRps,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


EnviarLoteRpsEnvio = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EnviarLoteRpsEnvio'), CTD_ANON, location=pyxb.utils.utility.Location('/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/servico_enviar_lote_rps_envio_v03.xsd', 6, 1))
Namespace.addCategoryObject('elementBinding', EnviarLoteRpsEnvio.name().localName(), EnviarLoteRpsEnvio)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LoteRps'), _ImportedBinding__tipos.tcLoteRps, scope=CTD_ANON, location=pyxb.utils.utility.Location('/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/servico_enviar_lote_rps_envio_v03.xsd', 9, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), _ImportedBinding__dsig.SignatureType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd', 41, 0)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/servico_enviar_lote_rps_envio_v03.xsd', 10, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LoteRps')), pyxb.utils.utility.Location('/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/servico_enviar_lote_rps_envio_v03.xsd', 9, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature')), pyxb.utils.utility.Location('/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/servico_enviar_lote_rps_envio_v03.xsd', 10, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

