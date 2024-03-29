# ./servico_consultar_situacao_lote_rps_resposta_v03.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:035a28892901c557b51d91d819be756030433d31
# Generated 2015-12-09 15:20:29.694445 by PyXB version 1.2.4 using Python 3.5.0.final.0
# Namespace http://www.ginfes.com.br/servico_consultar_situacao_lote_rps_resposta_v03.xsd

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
    "urn:uuid:2522bb06-9e99-11e5-a0de-b8ee65084bc8"
)

# Version of PyXB used to generate the bindings
_PyXBVersion = "1.2.4"
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    "http://www.ginfes.com.br/servico_consultar_situacao_lote_rps_resposta_v03.xsd",
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
        (
            "/home/leonardo/Downloads/xsd"
            " ginfes/servico_consultar_situacao_lote_rps_resposta_v03.xsd"
        ),
        6,
        2,
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    __NumeroLote = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NumeroLote"),
        "NumeroLote",
        "__httpwww_ginfes_com_brservico_consultar_situacao_lote_rps_resposta_v03_xsd_CTD_ANON_httpwww_ginfes_com_brservico_consultar_situacao_lote_rps_resposta_v03_xsdNumeroLote",  # noqa: E501
        False,
        pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_situacao_lote_rps_resposta_v03.xsd"
            ),
            9,
            5,
        ),
    )

    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, None)
    __Situacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Situacao"),
        "Situacao",
        "__httpwww_ginfes_com_brservico_consultar_situacao_lote_rps_resposta_v03_xsd_CTD_ANON_httpwww_ginfes_com_brservico_consultar_situacao_lote_rps_resposta_v03_xsdSituacao",  # noqa: E501
        False,
        pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_situacao_lote_rps_resposta_v03.xsd"
            ),
            10,
            5,
        ),
    )

    Situacao = property(__Situacao.value, __Situacao.set, None, None)
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_tipos, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_ginfes_com_brservico_consultar_situacao_lote_rps_resposta_v03_xsd_CTD_ANON_httpwww_ginfes_com_brtipos_v03_xsdListaMensagemRetorno",  # noqa: E501
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
            __NumeroLote.name(): __NumeroLote,
            __Situacao.name(): __Situacao,
            __ListaMensagemRetorno.name(): __ListaMensagemRetorno,
        }
    )
    _AttributeMap.update({})


ConsultarSituacaoLoteRpsResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarSituacaoLoteRpsResposta"),
    CTD_ANON,
    location=pyxb.utils.utility.Location(
        (
            "/home/leonardo/Downloads/xsd"
            " ginfes/servico_consultar_situacao_lote_rps_resposta_v03.xsd"
        ),
        5,
        1,
    ),
)
Namespace.addCategoryObject(
    "elementBinding",
    ConsultarSituacaoLoteRpsResposta.name().localName(),
    ConsultarSituacaoLoteRpsResposta,
)


CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NumeroLote"),
        _ImportedBinding__tipos.tsNumeroLote,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_situacao_lote_rps_resposta_v03.xsd"
            ),
            9,
            5,
        ),
    )
)

CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Situacao"),
        _ImportedBinding__tipos.tsSituacaoLoteRps,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_situacao_lote_rps_resposta_v03.xsd"
            ),
            10,
            5,
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
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NumeroLote")),
        pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_situacao_lote_rps_resposta_v03.xsd"
            ),
            9,
            5,
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
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Situacao")),
        pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_situacao_lote_rps_resposta_v03.xsd"
            ),
            10,
            5,
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(
            pyxb.namespace.ExpandedName(_Namespace_tipos, "ListaMensagemRetorno")
        ),
        pyxb.utils.utility.Location(
            (
                "/home/leonardo/Downloads/xsd"
                " ginfes/servico_consultar_situacao_lote_rps_resposta_v03.xsd"
            ),
            12,
            4,
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON._Automaton = _BuildAutomaton()
