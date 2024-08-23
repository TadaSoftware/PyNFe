# ./servico_consultar_nfse_resposta_v03.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b5175c71df88b0c3a415c5fe507e64e89cd44743
# Generated 2015-12-09 15:18:47.481617 by PyXB version 1.2.4 using Python 3.5.0.final.0
# Namespace http://www.ginfes.com.br/servico_consultar_nfse_resposta_v03.xsd

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import pyxb.utils.six as _six

# Import bindings for namespaces imported into schema
import _tipos as _ImportedBinding__tipos
import pyxb.binding.datatypes

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    "urn:uuid:e82c30a6-9e98-11e5-ac26-b8ee65084bc8"
)

# Version of PyXB used to generate the bindings
_PyXBVersion = "1.2.4"
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    "http://www.ginfes.com.br/servico_consultar_nfse_resposta_v03.xsd",
    create_if_missing=True,
)
Namespace.configureCategories(["typeBinding", "elementBinding"])
_Namespace_tipos = _ImportedBinding__tipos.Namespace
_Namespace_tipos.configureCategories(["typeBinding", "elementBinding"])


def CreateFromDocument(xml_text, default_namespace=None, location_base=None):
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
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=default_namespace, location_base=location_base
    )
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}.
    """
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/leonardo/Downloads/xsd ginfes/servico_consultar_nfse_resposta_v03.xsd",
        6,
        2,
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    __ListaNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        "ListaNfse",
        "__httpwww_ginfes_com_brservico_consultar_nfse_resposta_v03_xsd_CTD_ANON_httpwww_ginfes_com_brservico_consultar_nfse_resposta_v03_xsdListaNfse",  # noqa: E501
        False,
        pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_nfse_resposta_v03.xsd"
            ),
            8,
            4,
        ),
    )

    ListaNfse = property(__ListaNfse.value, __ListaNfse.set, None, None)
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_tipos, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_ginfes_com_brservico_consultar_nfse_resposta_v03_xsd_CTD_ANON_httpwww_ginfes_com_brtipos_v03_xsdListaMensagemRetorno",  # noqa: E501
        False,
        pyxb.utils.utility.Location(
            "/home/leonardo/Downloads/xsd ginfes/tipos_v03.xsd", 508, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    _ElementMap.update(
        {
            __ListaNfse.name(): __ListaNfse,
            __ListaMensagemRetorno.name(): __ListaMensagemRetorno,
        }
    )
    _AttributeMap.update({})


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/leonardo/Downloads/xsd ginfes/servico_consultar_nfse_resposta_v03.xsd",
        9,
        5,
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    __CompNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        "CompNfse",
        "__httpwww_ginfes_com_brservico_consultar_nfse_resposta_v03_xsd_CTD_ANON__httpwww_ginfes_com_brservico_consultar_nfse_resposta_v03_xsdCompNfse",  # noqa: E501
        True,
        pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_nfse_resposta_v03.xsd"
            ),
            11,
            7,
        ),
    )

    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    _ElementMap.update({__CompNfse.name(): __CompNfse})
    _AttributeMap.update({})


ConsultarNfseResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarNfseResposta"),
    CTD_ANON,
    location=pyxb.utils.utility.Location(
        "/home/leonardo/Downloads/xsd ginfes/servico_consultar_nfse_resposta_v03.xsd",
        5,
        1,
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ConsultarNfseResposta.name().localName(), ConsultarNfseResposta
)


CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        CTD_ANON_,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_nfse_resposta_v03.xsd"
            ),
            8,
            4,
        ),
    )
)

CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_tipos, "ListaMensagemRetorno"),
        _ImportedBinding__tipos.CTD_ANON,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            "/home/leonardo/Downloads/xsd ginfes/tipos_v03.xsd", 508, 1
        ),
    )
)


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaNfse")),
        pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_nfse_resposta_v03.xsd"
            ),
            8,
            4,
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(
            pyxb.namespace.ExpandedName(_Namespace_tipos, "ListaMensagemRetorno")
        ),
        pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_nfse_resposta_v03.xsd"
            ),
            15,
            4,
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON._Automaton = _BuildAutomaton()


CTD_ANON_._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        _ImportedBinding__tipos.tcCompNfse,
        scope=CTD_ANON_,
        location=pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_nfse_resposta_v03.xsd"
            ),
            11,
            7,
        ),
    )
)


def _BuildAutomaton_(): # noqa
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_nfse_resposta_v03.xsd"
            ),
            11,
            7,
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CompNfse")),
        pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_nfse_resposta_v03.xsd"
            ),
            11,
            7,
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_._Automaton = _BuildAutomaton_()
