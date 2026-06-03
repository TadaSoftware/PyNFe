# flake8: noqa
# pynfe/utils/nfse/betha/nfse_v202.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:6ff0610f3dc7942f55c7a7b98d5ad53ba974a7b2
# Generated 2025-04-06 00:00:39.105723 by PyXB version 1.2.6 using Python 3.12.9.final.0
# Namespace http://www.betha.com.br/e-nota-contribuinte-ws

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    "urn:uuid:770a0200-e52e-48b5-9080-7379d189705e"
)

# Version of PyXB used to generate the bindings
_PyXBVersion = "1.2.6"

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
from pynfe.utils.nfse.betha import _dsig as _ImportedBinding__dsig
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    "http://www.betha.com.br/e-nota-contribuinte-ws", create_if_missing=True
)
Namespace.configureCategories(["typeBinding", "elementBinding"])
_Namespace_dsig = _ImportedBinding__dsig.Namespace
_Namespace_dsig.configureCategories(["typeBinding", "elementBinding"])


def CreateFromDocument(
    xml_text, fallback_namespace=None, location_base=None, default_namespace=None
):
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
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=fallback_namespace, location_base=location_base
    )
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsNumeroNfse
class tsNumeroNfse(pyxb.binding.datatypes.nonNegativeInteger):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 10, 1
    )
    _Documentation = None


tsNumeroNfse._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(15)
)
tsNumeroNfse._InitializeFacetMap(tsNumeroNfse._CF_totalDigits)
Namespace.addCategoryObject("typeBinding", "tsNumeroNfse", tsNumeroNfse)
_module_typeBindings.tsNumeroNfse = tsNumeroNfse


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCodigoVerificacao
class tsCodigoVerificacao(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoVerificacao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 15, 1
    )
    _Documentation = None


tsCodigoVerificacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(9)
)
tsCodigoVerificacao._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsCodigoVerificacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCodigoVerificacao._InitializeFacetMap(
    tsCodigoVerificacao._CF_maxLength,
    tsCodigoVerificacao._CF_minLength,
    tsCodigoVerificacao._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsCodigoVerificacao", tsCodigoVerificacao)
_module_typeBindings.tsCodigoVerificacao = tsCodigoVerificacao


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsStatusRps
class tsStatusRps(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsStatusRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 22, 1
    )
    _Documentation = None


tsStatusRps._CF_pattern = pyxb.binding.facets.CF_pattern()
tsStatusRps._CF_pattern.addPattern(pattern="1|2")
tsStatusRps._InitializeFacetMap(tsStatusRps._CF_pattern)
Namespace.addCategoryObject("typeBinding", "tsStatusRps", tsStatusRps)
_module_typeBindings.tsStatusRps = tsStatusRps


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsStatusNfse
class tsStatusNfse(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsStatusNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 27, 1
    )
    _Documentation = None


tsStatusNfse._CF_pattern = pyxb.binding.facets.CF_pattern()
tsStatusNfse._CF_pattern.addPattern(pattern="1|2")
tsStatusNfse._InitializeFacetMap(tsStatusNfse._CF_pattern)
Namespace.addCategoryObject("typeBinding", "tsStatusNfse", tsStatusNfse)
_module_typeBindings.tsStatusNfse = tsStatusNfse


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsExigibilidadeISS
class tsExigibilidadeISS(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsExigibilidadeISS")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 32, 1
    )
    _Documentation = None


tsExigibilidadeISS._CF_pattern = pyxb.binding.facets.CF_pattern()
tsExigibilidadeISS._CF_pattern.addPattern(pattern="1|2|3|4|5|6|7")
tsExigibilidadeISS._InitializeFacetMap(tsExigibilidadeISS._CF_pattern)
Namespace.addCategoryObject("typeBinding", "tsExigibilidadeISS", tsExigibilidadeISS)
_module_typeBindings.tsExigibilidadeISS = tsExigibilidadeISS


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsNumeroProcesso
class tsNumeroProcesso(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroProcesso")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 37, 1
    )
    _Documentation = None


tsNumeroProcesso._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(30)
)
tsNumeroProcesso._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsNumeroProcesso._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsNumeroProcesso._InitializeFacetMap(
    tsNumeroProcesso._CF_maxLength, tsNumeroProcesso._CF_minLength, tsNumeroProcesso._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsNumeroProcesso", tsNumeroProcesso)
_module_typeBindings.tsNumeroProcesso = tsNumeroProcesso


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsRegimeEspecialTributacao
class tsRegimeEspecialTributacao(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsRegimeEspecialTributacao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 44, 1
    )
    _Documentation = None


tsRegimeEspecialTributacao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsRegimeEspecialTributacao._CF_pattern.addPattern(pattern="1|2|3|4|5|6")
tsRegimeEspecialTributacao._InitializeFacetMap(tsRegimeEspecialTributacao._CF_pattern)
Namespace.addCategoryObject("typeBinding", "tsRegimeEspecialTributacao", tsRegimeEspecialTributacao)
_module_typeBindings.tsRegimeEspecialTributacao = tsRegimeEspecialTributacao


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsSimNao
class tsSimNao(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsSimNao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 49, 1
    )
    _Documentation = None


tsSimNao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsSimNao._CF_pattern.addPattern(pattern="1|2")
tsSimNao._InitializeFacetMap(tsSimNao._CF_pattern)
Namespace.addCategoryObject("typeBinding", "tsSimNao", tsSimNao)
_module_typeBindings.tsSimNao = tsSimNao


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsResponsavelRetencao
class tsResponsavelRetencao(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsResponsavelRetencao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 54, 1
    )
    _Documentation = None


tsResponsavelRetencao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsResponsavelRetencao._CF_pattern.addPattern(pattern="1|2")
tsResponsavelRetencao._InitializeFacetMap(tsResponsavelRetencao._CF_pattern)
Namespace.addCategoryObject("typeBinding", "tsResponsavelRetencao", tsResponsavelRetencao)
_module_typeBindings.tsResponsavelRetencao = tsResponsavelRetencao


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsPagina
class tsPagina(pyxb.binding.datatypes.nonNegativeInteger):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsPagina")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 59, 1
    )
    _Documentation = None


tsPagina._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(
    value=pyxb.binding.datatypes.nonNegativeInteger(999999), value_datatype=tsPagina
)
tsPagina._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(
    value=pyxb.binding.datatypes.nonNegativeInteger(1), value_datatype=tsPagina
)
tsPagina._InitializeFacetMap(tsPagina._CF_maxInclusive, tsPagina._CF_minInclusive)
Namespace.addCategoryObject("typeBinding", "tsPagina", tsPagina)
_module_typeBindings.tsPagina = tsPagina


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsNumeroRps
class tsNumeroRps(pyxb.binding.datatypes.nonNegativeInteger):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 65, 1
    )
    _Documentation = None


tsNumeroRps._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(15)
)
tsNumeroRps._InitializeFacetMap(tsNumeroRps._CF_totalDigits)
Namespace.addCategoryObject("typeBinding", "tsNumeroRps", tsNumeroRps)
_module_typeBindings.tsNumeroRps = tsNumeroRps


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsSerieRps
class tsSerieRps(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsSerieRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 70, 1
    )
    _Documentation = None


tsSerieRps._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(5)
)
tsSerieRps._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsSerieRps._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsSerieRps._InitializeFacetMap(
    tsSerieRps._CF_maxLength, tsSerieRps._CF_minLength, tsSerieRps._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsSerieRps", tsSerieRps)
_module_typeBindings.tsSerieRps = tsSerieRps


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsTipoRps
class tsTipoRps(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsTipoRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 77, 1
    )
    _Documentation = None


tsTipoRps._CF_pattern = pyxb.binding.facets.CF_pattern()
tsTipoRps._CF_pattern.addPattern(pattern="1|2|3")
tsTipoRps._InitializeFacetMap(tsTipoRps._CF_pattern)
Namespace.addCategoryObject("typeBinding", "tsTipoRps", tsTipoRps)
_module_typeBindings.tsTipoRps = tsTipoRps


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsOutrasInformacoes
class tsOutrasInformacoes(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsOutrasInformacoes")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 82, 1
    )
    _Documentation = None


tsOutrasInformacoes._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(255)
)
tsOutrasInformacoes._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsOutrasInformacoes._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsOutrasInformacoes._InitializeFacetMap(
    tsOutrasInformacoes._CF_maxLength,
    tsOutrasInformacoes._CF_minLength,
    tsOutrasInformacoes._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsOutrasInformacoes", tsOutrasInformacoes)
_module_typeBindings.tsOutrasInformacoes = tsOutrasInformacoes


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsValor
class tsValor(pyxb.binding.datatypes.decimal):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsValor")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 89, 1
    )
    _Documentation = None


tsValor._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(
    value=pyxb.binding.datatypes.nonNegativeInteger(2)
)
tsValor._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(
    value=pyxb.binding.datatypes.decimal("0.0"), value_datatype=tsValor
)
tsValor._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(15)
)
tsValor._InitializeFacetMap(
    tsValor._CF_fractionDigits, tsValor._CF_minInclusive, tsValor._CF_totalDigits
)
Namespace.addCategoryObject("typeBinding", "tsValor", tsValor)
_module_typeBindings.tsValor = tsValor


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsItemListaServico
class tsItemListaServico(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsItemListaServico")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 96, 1
    )
    _Documentation = None


tsItemListaServico._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(5)
)
tsItemListaServico._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsItemListaServico._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsItemListaServico._InitializeFacetMap(
    tsItemListaServico._CF_maxLength,
    tsItemListaServico._CF_minLength,
    tsItemListaServico._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsItemListaServico", tsItemListaServico)
_module_typeBindings.tsItemListaServico = tsItemListaServico


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCodigoCnae
class tsCodigoCnae(pyxb.binding.datatypes.int):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoCnae")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 103, 1
    )
    _Documentation = None


tsCodigoCnae._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(7)
)
tsCodigoCnae._InitializeFacetMap(tsCodigoCnae._CF_totalDigits)
Namespace.addCategoryObject("typeBinding", "tsCodigoCnae", tsCodigoCnae)
_module_typeBindings.tsCodigoCnae = tsCodigoCnae


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCodigoTributacao
class tsCodigoTributacao(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoTributacao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 108, 1
    )
    _Documentation = None


tsCodigoTributacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(20)
)
tsCodigoTributacao._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsCodigoTributacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCodigoTributacao._InitializeFacetMap(
    tsCodigoTributacao._CF_maxLength,
    tsCodigoTributacao._CF_minLength,
    tsCodigoTributacao._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsCodigoTributacao", tsCodigoTributacao)
_module_typeBindings.tsCodigoTributacao = tsCodigoTributacao


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsAliquota
class tsAliquota(pyxb.binding.datatypes.decimal):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsAliquota")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 115, 1
    )
    _Documentation = None


tsAliquota._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(
    value=pyxb.binding.datatypes.nonNegativeInteger(4)
)
tsAliquota._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(
    value=pyxb.binding.datatypes.decimal("0.0"), value_datatype=tsAliquota
)
tsAliquota._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(6)
)
tsAliquota._InitializeFacetMap(
    tsAliquota._CF_fractionDigits, tsAliquota._CF_minInclusive, tsAliquota._CF_totalDigits
)
Namespace.addCategoryObject("typeBinding", "tsAliquota", tsAliquota)
_module_typeBindings.tsAliquota = tsAliquota


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsDiscriminacao
class tsDiscriminacao(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsDiscriminacao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 122, 1
    )
    _Documentation = None


tsDiscriminacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(2000)
)
tsDiscriminacao._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsDiscriminacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsDiscriminacao._InitializeFacetMap(
    tsDiscriminacao._CF_maxLength, tsDiscriminacao._CF_minLength, tsDiscriminacao._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsDiscriminacao", tsDiscriminacao)
_module_typeBindings.tsDiscriminacao = tsDiscriminacao


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCodigoMunicipioIbge
class tsCodigoMunicipioIbge(pyxb.binding.datatypes.int):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoMunicipioIbge")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 129, 1
    )
    _Documentation = None


tsCodigoMunicipioIbge._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(7)
)
tsCodigoMunicipioIbge._InitializeFacetMap(tsCodigoMunicipioIbge._CF_totalDigits)
Namespace.addCategoryObject("typeBinding", "tsCodigoMunicipioIbge", tsCodigoMunicipioIbge)
_module_typeBindings.tsCodigoMunicipioIbge = tsCodigoMunicipioIbge


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsInscricaoMunicipal
class tsInscricaoMunicipal(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsInscricaoMunicipal")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 134, 1
    )
    _Documentation = None


tsInscricaoMunicipal._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(15)
)
tsInscricaoMunicipal._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsInscricaoMunicipal._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsInscricaoMunicipal._InitializeFacetMap(
    tsInscricaoMunicipal._CF_maxLength,
    tsInscricaoMunicipal._CF_minLength,
    tsInscricaoMunicipal._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsInscricaoMunicipal", tsInscricaoMunicipal)
_module_typeBindings.tsInscricaoMunicipal = tsInscricaoMunicipal


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsRazaoSocial
class tsRazaoSocial(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsRazaoSocial")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 141, 1
    )
    _Documentation = None


tsRazaoSocial._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(150)
)
tsRazaoSocial._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsRazaoSocial._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsRazaoSocial._InitializeFacetMap(
    tsRazaoSocial._CF_maxLength, tsRazaoSocial._CF_minLength, tsRazaoSocial._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsRazaoSocial", tsRazaoSocial)
_module_typeBindings.tsRazaoSocial = tsRazaoSocial


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsNomeFantasia
class tsNomeFantasia(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNomeFantasia")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 148, 1
    )
    _Documentation = None


tsNomeFantasia._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(60)
)
tsNomeFantasia._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsNomeFantasia._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsNomeFantasia._InitializeFacetMap(
    tsNomeFantasia._CF_maxLength, tsNomeFantasia._CF_minLength, tsNomeFantasia._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsNomeFantasia", tsNomeFantasia)
_module_typeBindings.tsNomeFantasia = tsNomeFantasia


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCnpj
class tsCnpj(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCnpj")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 155, 1
    )
    _Documentation = None


tsCnpj._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(14)
)
tsCnpj._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCnpj._InitializeFacetMap(tsCnpj._CF_length, tsCnpj._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsCnpj", tsCnpj)
_module_typeBindings.tsCnpj = tsCnpj


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsEndereco
class tsEndereco(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsEndereco")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 161, 1
    )
    _Documentation = None


tsEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(125)
)
tsEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsEndereco._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsEndereco._InitializeFacetMap(
    tsEndereco._CF_maxLength, tsEndereco._CF_minLength, tsEndereco._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsEndereco", tsEndereco)
_module_typeBindings.tsEndereco = tsEndereco


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsNumeroEndereco
class tsNumeroEndereco(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroEndereco")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 168, 1
    )
    _Documentation = None


tsNumeroEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(10)
)
tsNumeroEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsNumeroEndereco._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsNumeroEndereco._InitializeFacetMap(
    tsNumeroEndereco._CF_maxLength, tsNumeroEndereco._CF_minLength, tsNumeroEndereco._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsNumeroEndereco", tsNumeroEndereco)
_module_typeBindings.tsNumeroEndereco = tsNumeroEndereco


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsComplementoEndereco
class tsComplementoEndereco(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsComplementoEndereco")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 175, 1
    )
    _Documentation = None


tsComplementoEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(60)
)
tsComplementoEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsComplementoEndereco._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsComplementoEndereco._InitializeFacetMap(
    tsComplementoEndereco._CF_maxLength,
    tsComplementoEndereco._CF_minLength,
    tsComplementoEndereco._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsComplementoEndereco", tsComplementoEndereco)
_module_typeBindings.tsComplementoEndereco = tsComplementoEndereco


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsBairro
class tsBairro(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsBairro")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 182, 1
    )
    _Documentation = None


tsBairro._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(60)
)
tsBairro._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsBairro._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsBairro._InitializeFacetMap(
    tsBairro._CF_maxLength, tsBairro._CF_minLength, tsBairro._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsBairro", tsBairro)
_module_typeBindings.tsBairro = tsBairro


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsUf
class tsUf(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsUf")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 189, 1
    )
    _Documentation = None


tsUf._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tsUf._InitializeFacetMap(tsUf._CF_length)
Namespace.addCategoryObject("typeBinding", "tsUf", tsUf)
_module_typeBindings.tsUf = tsUf


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCodigoPaisBacen
class tsCodigoPaisBacen(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoPaisBacen")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 194, 1
    )
    _Documentation = None


tsCodigoPaisBacen._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(4)
)
tsCodigoPaisBacen._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCodigoPaisBacen._InitializeFacetMap(
    tsCodigoPaisBacen._CF_length, tsCodigoPaisBacen._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsCodigoPaisBacen", tsCodigoPaisBacen)
_module_typeBindings.tsCodigoPaisBacen = tsCodigoPaisBacen


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCep
class tsCep(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCep")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 200, 1
    )
    _Documentation = None


tsCep._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(8))
tsCep._InitializeFacetMap(tsCep._CF_length)
Namespace.addCategoryObject("typeBinding", "tsCep", tsCep)
_module_typeBindings.tsCep = tsCep


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsEmail
class tsEmail(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsEmail")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 205, 1
    )
    _Documentation = None


tsEmail._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(80)
)
tsEmail._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsEmail._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsEmail._InitializeFacetMap(tsEmail._CF_maxLength, tsEmail._CF_minLength, tsEmail._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsEmail", tsEmail)
_module_typeBindings.tsEmail = tsEmail


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsTelefone
class tsTelefone(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsTelefone")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 212, 1
    )
    _Documentation = None


tsTelefone._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(20)
)
tsTelefone._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsTelefone._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsTelefone._InitializeFacetMap(
    tsTelefone._CF_maxLength, tsTelefone._CF_minLength, tsTelefone._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsTelefone", tsTelefone)
_module_typeBindings.tsTelefone = tsTelefone


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCpf
class tsCpf(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCpf")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 219, 1
    )
    _Documentation = None


tsCpf._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(11)
)
tsCpf._InitializeFacetMap(tsCpf._CF_length)
Namespace.addCategoryObject("typeBinding", "tsCpf", tsCpf)
_module_typeBindings.tsCpf = tsCpf


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCodigoObra
class tsCodigoObra(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoObra")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 224, 1
    )
    _Documentation = None


tsCodigoObra._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(15)
)
tsCodigoObra._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsCodigoObra._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCodigoObra._InitializeFacetMap(
    tsCodigoObra._CF_maxLength, tsCodigoObra._CF_minLength, tsCodigoObra._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsCodigoObra", tsCodigoObra)
_module_typeBindings.tsCodigoObra = tsCodigoObra


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsArt
class tsArt(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsArt")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 231, 1
    )
    _Documentation = None


tsArt._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(15)
)
tsArt._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsArt._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsArt._InitializeFacetMap(tsArt._CF_maxLength, tsArt._CF_minLength, tsArt._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsArt", tsArt)
_module_typeBindings.tsArt = tsArt


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsNumeroLote
class tsNumeroLote(pyxb.binding.datatypes.nonNegativeInteger):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroLote")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 238, 1
    )
    _Documentation = None


tsNumeroLote._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(15)
)
tsNumeroLote._InitializeFacetMap(tsNumeroLote._CF_totalDigits)
Namespace.addCategoryObject("typeBinding", "tsNumeroLote", tsNumeroLote)
_module_typeBindings.tsNumeroLote = tsNumeroLote


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsNumeroProtocolo
class tsNumeroProtocolo(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroProtocolo")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 243, 1
    )
    _Documentation = None


tsNumeroProtocolo._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(50)
)
tsNumeroProtocolo._InitializeFacetMap(tsNumeroProtocolo._CF_maxLength)
Namespace.addCategoryObject("typeBinding", "tsNumeroProtocolo", tsNumeroProtocolo)
_module_typeBindings.tsNumeroProtocolo = tsNumeroProtocolo


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsSituacaoLoteRps
class tsSituacaoLoteRps(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsSituacaoLoteRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 248, 1
    )
    _Documentation = None


tsSituacaoLoteRps._CF_pattern = pyxb.binding.facets.CF_pattern()
tsSituacaoLoteRps._CF_pattern.addPattern(pattern="1|2|3|4")
tsSituacaoLoteRps._InitializeFacetMap(tsSituacaoLoteRps._CF_pattern)
Namespace.addCategoryObject("typeBinding", "tsSituacaoLoteRps", tsSituacaoLoteRps)
_module_typeBindings.tsSituacaoLoteRps = tsSituacaoLoteRps


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsQuantidadeRps
class tsQuantidadeRps(pyxb.binding.datatypes.int):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsQuantidadeRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 253, 1
    )
    _Documentation = None


tsQuantidadeRps._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "tsQuantidadeRps", tsQuantidadeRps)
_module_typeBindings.tsQuantidadeRps = tsQuantidadeRps


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCodigoMensagemAlerta
class tsCodigoMensagemAlerta(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoMensagemAlerta")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 257, 1
    )
    _Documentation = None


tsCodigoMensagemAlerta._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(4)
)
tsCodigoMensagemAlerta._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsCodigoMensagemAlerta._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCodigoMensagemAlerta._InitializeFacetMap(
    tsCodigoMensagemAlerta._CF_maxLength,
    tsCodigoMensagemAlerta._CF_minLength,
    tsCodigoMensagemAlerta._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsCodigoMensagemAlerta", tsCodigoMensagemAlerta)
_module_typeBindings.tsCodigoMensagemAlerta = tsCodigoMensagemAlerta


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsDescricaoMensagemAlerta
class tsDescricaoMensagemAlerta(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsDescricaoMensagemAlerta")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 264, 1
    )
    _Documentation = None


tsDescricaoMensagemAlerta._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(200)
)
tsDescricaoMensagemAlerta._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsDescricaoMensagemAlerta._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsDescricaoMensagemAlerta._InitializeFacetMap(
    tsDescricaoMensagemAlerta._CF_maxLength,
    tsDescricaoMensagemAlerta._CF_minLength,
    tsDescricaoMensagemAlerta._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsDescricaoMensagemAlerta", tsDescricaoMensagemAlerta)
_module_typeBindings.tsDescricaoMensagemAlerta = tsDescricaoMensagemAlerta


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsCodigoCancelamentoNfse
class tsCodigoCancelamentoNfse(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoCancelamentoNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 271, 1
    )
    _Documentation = None


tsCodigoCancelamentoNfse._CF_pattern = pyxb.binding.facets.CF_pattern()
tsCodigoCancelamentoNfse._CF_pattern.addPattern(pattern="1|2|3|4|5")
tsCodigoCancelamentoNfse._InitializeFacetMap(tsCodigoCancelamentoNfse._CF_pattern)
Namespace.addCategoryObject("typeBinding", "tsCodigoCancelamentoNfse", tsCodigoCancelamentoNfse)
_module_typeBindings.tsCodigoCancelamentoNfse = tsCodigoCancelamentoNfse


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsIdTag
class tsIdTag(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsIdTag")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 276, 1
    )
    _Documentation = None


tsIdTag._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(255)
)
tsIdTag._InitializeFacetMap(tsIdTag._CF_maxLength)
Namespace.addCategoryObject("typeBinding", "tsIdTag", tsIdTag)
_module_typeBindings.tsIdTag = tsIdTag


# Atomic simple type: {http://www.betha.com.br/e-nota-contribuinte-ws}tsVersao
class tsVersao(pyxb.binding.datatypes.token):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsVersao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 282, 1
    )
    _Documentation = None


tsVersao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsVersao._CF_pattern.addPattern(pattern="[1-9]{1}[0-9]{0,1}\\.[0-9]{2}")
tsVersao._InitializeFacetMap(tsVersao._CF_pattern)
Namespace.addCategoryObject("typeBinding", "tsVersao", tsVersao)
_module_typeBindings.tsVersao = tsVersao


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcCpfCnpj with content type ELEMENT_ONLY
class tcCpfCnpj(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcCpfCnpj with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcCpfCnpj")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 289, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Cpf uses Python identifier Cpf
    __Cpf = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Cpf"),
        "Cpf",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcCpfCnpj_httpwww_betha_com_bre_nota_contribuinte_wsCpf",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 291, 3
        ),
    )

    Cpf = property(__Cpf.value, __Cpf.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Cnpj uses Python identifier Cnpj
    __Cnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Cnpj"),
        "Cnpj",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcCpfCnpj_httpwww_betha_com_bre_nota_contribuinte_wsCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 293, 3
        ),
    )

    Cnpj = property(__Cnpj.value, __Cnpj.set, None, None)

    _ElementMap.update({__Cpf.name(): __Cpf, __Cnpj.name(): __Cnpj})
    _AttributeMap.update({})


_module_typeBindings.tcCpfCnpj = tcCpfCnpj
Namespace.addCategoryObject("typeBinding", "tcCpfCnpj", tcCpfCnpj)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcEndereco with content type ELEMENT_ONLY
class tcEndereco(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcEndereco with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcEndereco")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 298, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Endereco uses Python identifier Endereco
    __Endereco = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        "Endereco",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcEndereco_httpwww_betha_com_bre_nota_contribuinte_wsEndereco",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 300, 3
        ),
    )

    Endereco = property(__Endereco.value, __Endereco.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        "Numero",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcEndereco_httpwww_betha_com_bre_nota_contribuinte_wsNumero",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 302, 3
        ),
    )

    Numero = property(__Numero.value, __Numero.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Complemento uses Python identifier Complemento
    __Complemento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Complemento"),
        "Complemento",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcEndereco_httpwww_betha_com_bre_nota_contribuinte_wsComplemento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 304, 3
        ),
    )

    Complemento = property(__Complemento.value, __Complemento.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Bairro uses Python identifier Bairro
    __Bairro = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Bairro"),
        "Bairro",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcEndereco_httpwww_betha_com_bre_nota_contribuinte_wsBairro",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 306, 3
        ),
    )

    Bairro = property(__Bairro.value, __Bairro.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        "CodigoMunicipio",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcEndereco_httpwww_betha_com_bre_nota_contribuinte_wsCodigoMunicipio",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 308, 3
        ),
    )

    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Uf uses Python identifier Uf
    __Uf = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Uf"),
        "Uf",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcEndereco_httpwww_betha_com_bre_nota_contribuinte_wsUf",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 310, 3
        ),
    )

    Uf = property(__Uf.value, __Uf.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoPais uses Python identifier CodigoPais
    __CodigoPais = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoPais"),
        "CodigoPais",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcEndereco_httpwww_betha_com_bre_nota_contribuinte_wsCodigoPais",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 312, 3
        ),
    )

    CodigoPais = property(__CodigoPais.value, __CodigoPais.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Cep uses Python identifier Cep
    __Cep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Cep"),
        "Cep",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcEndereco_httpwww_betha_com_bre_nota_contribuinte_wsCep",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 314, 3
        ),
    )

    Cep = property(__Cep.value, __Cep.set, None, None)

    _ElementMap.update(
        {
            __Endereco.name(): __Endereco,
            __Numero.name(): __Numero,
            __Complemento.name(): __Complemento,
            __Bairro.name(): __Bairro,
            __CodigoMunicipio.name(): __CodigoMunicipio,
            __Uf.name(): __Uf,
            __CodigoPais.name(): __CodigoPais,
            __Cep.name(): __Cep,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcEndereco = tcEndereco
Namespace.addCategoryObject("typeBinding", "tcEndereco", tcEndereco)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcContato with content type ELEMENT_ONLY
class tcContato(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcContato with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcContato")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 319, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Telefone uses Python identifier Telefone
    __Telefone = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Telefone"),
        "Telefone",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcContato_httpwww_betha_com_bre_nota_contribuinte_wsTelefone",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 321, 3
        ),
    )

    Telefone = property(__Telefone.value, __Telefone.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Email uses Python identifier Email
    __Email = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Email"),
        "Email",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcContato_httpwww_betha_com_bre_nota_contribuinte_wsEmail",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 323, 3
        ),
    )

    Email = property(__Email.value, __Email.set, None, None)

    _ElementMap.update({__Telefone.name(): __Telefone, __Email.name(): __Email})
    _AttributeMap.update({})


_module_typeBindings.tcContato = tcContato
Namespace.addCategoryObject("typeBinding", "tcContato", tcContato)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoOrgaoGerador with content type ELEMENT_ONLY
class tcIdentificacaoOrgaoGerador(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoOrgaoGerador with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoOrgaoGerador")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 328, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        "CodigoMunicipio",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoOrgaoGerador_httpwww_betha_com_bre_nota_contribuinte_wsCodigoMunicipio",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 330, 3
        ),
    )

    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Uf uses Python identifier Uf
    __Uf = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Uf"),
        "Uf",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoOrgaoGerador_httpwww_betha_com_bre_nota_contribuinte_wsUf",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 332, 3
        ),
    )

    Uf = property(__Uf.value, __Uf.set, None, None)

    _ElementMap.update({__CodigoMunicipio.name(): __CodigoMunicipio, __Uf.name(): __Uf})
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoOrgaoGerador = tcIdentificacaoOrgaoGerador
Namespace.addCategoryObject(
    "typeBinding", "tcIdentificacaoOrgaoGerador", tcIdentificacaoOrgaoGerador
)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoRps with content type ELEMENT_ONLY
class tcIdentificacaoRps(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoRps with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 337, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        "Numero",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoRps_httpwww_betha_com_bre_nota_contribuinte_wsNumero",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 339, 3
        ),
    )

    Numero = property(__Numero.value, __Numero.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Serie uses Python identifier Serie
    __Serie = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Serie"),
        "Serie",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoRps_httpwww_betha_com_bre_nota_contribuinte_wsSerie",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 341, 3
        ),
    )

    Serie = property(__Serie.value, __Serie.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Tipo uses Python identifier Tipo
    __Tipo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Tipo"),
        "Tipo",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoRps_httpwww_betha_com_bre_nota_contribuinte_wsTipo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 343, 3
        ),
    )

    Tipo = property(__Tipo.value, __Tipo.set, None, None)

    _ElementMap.update({__Numero.name(): __Numero, __Serie.name(): __Serie, __Tipo.name(): __Tipo})
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoRps = tcIdentificacaoRps
Namespace.addCategoryObject("typeBinding", "tcIdentificacaoRps", tcIdentificacaoRps)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoPrestador with content type ELEMENT_ONLY
class tcIdentificacaoPrestador(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoPrestador with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoPrestador")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 348, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CpfCnpj uses Python identifier CpfCnpj
    __CpfCnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        "CpfCnpj",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoPrestador_httpwww_betha_com_bre_nota_contribuinte_wsCpfCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 350, 3
        ),
    )

    CpfCnpj = property(__CpfCnpj.value, __CpfCnpj.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoPrestador_httpwww_betha_com_bre_nota_contribuinte_wsInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 352, 3
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    _ElementMap.update(
        {__CpfCnpj.name(): __CpfCnpj, __InscricaoMunicipal.name(): __InscricaoMunicipal}
    )
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoPrestador = tcIdentificacaoPrestador
Namespace.addCategoryObject("typeBinding", "tcIdentificacaoPrestador", tcIdentificacaoPrestador)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoTomador with content type ELEMENT_ONLY
class tcIdentificacaoTomador(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoTomador with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoTomador")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 357, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CpfCnpj uses Python identifier CpfCnpj
    __CpfCnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        "CpfCnpj",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoTomador_httpwww_betha_com_bre_nota_contribuinte_wsCpfCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 359, 3
        ),
    )

    CpfCnpj = property(__CpfCnpj.value, __CpfCnpj.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoTomador_httpwww_betha_com_bre_nota_contribuinte_wsInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 361, 3
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    _ElementMap.update(
        {__CpfCnpj.name(): __CpfCnpj, __InscricaoMunicipal.name(): __InscricaoMunicipal}
    )
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoTomador = tcIdentificacaoTomador
Namespace.addCategoryObject("typeBinding", "tcIdentificacaoTomador", tcIdentificacaoTomador)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoConsulente with content type ELEMENT_ONLY
class tcIdentificacaoConsulente(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoConsulente with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoConsulente")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 366, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CpfCnpj uses Python identifier CpfCnpj
    __CpfCnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        "CpfCnpj",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoConsulente_httpwww_betha_com_bre_nota_contribuinte_wsCpfCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 368, 3
        ),
    )

    CpfCnpj = property(__CpfCnpj.value, __CpfCnpj.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoConsulente_httpwww_betha_com_bre_nota_contribuinte_wsInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 370, 3
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    _ElementMap.update(
        {__CpfCnpj.name(): __CpfCnpj, __InscricaoMunicipal.name(): __InscricaoMunicipal}
    )
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoConsulente = tcIdentificacaoConsulente
Namespace.addCategoryObject("typeBinding", "tcIdentificacaoConsulente", tcIdentificacaoConsulente)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoIntermediario with content type ELEMENT_ONLY
class tcIdentificacaoIntermediario(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoIntermediario with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoIntermediario")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 375, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CpfCnpj uses Python identifier CpfCnpj
    __CpfCnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        "CpfCnpj",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoIntermediario_httpwww_betha_com_bre_nota_contribuinte_wsCpfCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 377, 15
        ),
    )

    CpfCnpj = property(__CpfCnpj.value, __CpfCnpj.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoIntermediario_httpwww_betha_com_bre_nota_contribuinte_wsInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 378, 14
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    _ElementMap.update(
        {__CpfCnpj.name(): __CpfCnpj, __InscricaoMunicipal.name(): __InscricaoMunicipal}
    )
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoIntermediario = tcIdentificacaoIntermediario
Namespace.addCategoryObject(
    "typeBinding", "tcIdentificacaoIntermediario", tcIdentificacaoIntermediario
)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDadosTomador with content type ELEMENT_ONLY
class tcDadosTomador(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDadosTomador with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcDadosTomador")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 382, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}IdentificacaoTomador uses Python identifier IdentificacaoTomador
    __IdentificacaoTomador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoTomador"),
        "IdentificacaoTomador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosTomador_httpwww_betha_com_bre_nota_contribuinte_wsIdentificacaoTomador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 384, 3
        ),
    )

    IdentificacaoTomador = property(
        __IdentificacaoTomador.value, __IdentificacaoTomador.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}RazaoSocial uses Python identifier RazaoSocial
    __RazaoSocial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        "RazaoSocial",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosTomador_httpwww_betha_com_bre_nota_contribuinte_wsRazaoSocial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 386, 3
        ),
    )

    RazaoSocial = property(__RazaoSocial.value, __RazaoSocial.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Endereco uses Python identifier Endereco
    __Endereco = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        "Endereco",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosTomador_httpwww_betha_com_bre_nota_contribuinte_wsEndereco",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 388, 3
        ),
    )

    Endereco = property(__Endereco.value, __Endereco.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Contato uses Python identifier Contato
    __Contato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Contato"),
        "Contato",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosTomador_httpwww_betha_com_bre_nota_contribuinte_wsContato",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 390, 3
        ),
    )

    Contato = property(__Contato.value, __Contato.set, None, None)

    _ElementMap.update(
        {
            __IdentificacaoTomador.name(): __IdentificacaoTomador,
            __RazaoSocial.name(): __RazaoSocial,
            __Endereco.name(): __Endereco,
            __Contato.name(): __Contato,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcDadosTomador = tcDadosTomador
Namespace.addCategoryObject("typeBinding", "tcDadosTomador", tcDadosTomador)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDadosIntermediario with content type ELEMENT_ONLY
class tcDadosIntermediario(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDadosIntermediario with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcDadosIntermediario")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 395, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}IdentificacaoIntermediario uses Python identifier IdentificacaoIntermediario
    __IdentificacaoIntermediario = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoIntermediario"),
        "IdentificacaoIntermediario",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosIntermediario_httpwww_betha_com_bre_nota_contribuinte_wsIdentificacaoIntermediario",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 397, 12
        ),
    )

    IdentificacaoIntermediario = property(
        __IdentificacaoIntermediario.value, __IdentificacaoIntermediario.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}RazaoSocial uses Python identifier RazaoSocial
    __RazaoSocial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        "RazaoSocial",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosIntermediario_httpwww_betha_com_bre_nota_contribuinte_wsRazaoSocial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 398, 12
        ),
    )

    RazaoSocial = property(__RazaoSocial.value, __RazaoSocial.set, None, None)

    _ElementMap.update(
        {
            __IdentificacaoIntermediario.name(): __IdentificacaoIntermediario,
            __RazaoSocial.name(): __RazaoSocial,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcDadosIntermediario = tcDadosIntermediario
Namespace.addCategoryObject("typeBinding", "tcDadosIntermediario", tcDadosIntermediario)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcValoresDeclaracaoServico with content type ELEMENT_ONLY
class tcValoresDeclaracaoServico(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcValoresDeclaracaoServico with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcValoresDeclaracaoServico")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 402, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorServicos uses Python identifier ValorServicos
    __ValorServicos = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorServicos"),
        "ValorServicos",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsValorServicos",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 404, 3
        ),
    )

    ValorServicos = property(__ValorServicos.value, __ValorServicos.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorDeducoes uses Python identifier ValorDeducoes
    __ValorDeducoes = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorDeducoes"),
        "ValorDeducoes",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsValorDeducoes",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 406, 3
        ),
    )

    ValorDeducoes = property(__ValorDeducoes.value, __ValorDeducoes.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorPis uses Python identifier ValorPis
    __ValorPis = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorPis"),
        "ValorPis",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsValorPis",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 408, 3
        ),
    )

    ValorPis = property(__ValorPis.value, __ValorPis.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorCofins uses Python identifier ValorCofins
    __ValorCofins = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorCofins"),
        "ValorCofins",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsValorCofins",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 410, 3
        ),
    )

    ValorCofins = property(__ValorCofins.value, __ValorCofins.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorInss uses Python identifier ValorInss
    __ValorInss = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorInss"),
        "ValorInss",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsValorInss",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 412, 3
        ),
    )

    ValorInss = property(__ValorInss.value, __ValorInss.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorIr uses Python identifier ValorIr
    __ValorIr = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorIr"),
        "ValorIr",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsValorIr",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 414, 3
        ),
    )

    ValorIr = property(__ValorIr.value, __ValorIr.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorCsll uses Python identifier ValorCsll
    __ValorCsll = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorCsll"),
        "ValorCsll",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsValorCsll",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 416, 3
        ),
    )

    ValorCsll = property(__ValorCsll.value, __ValorCsll.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}OutrasRetencoes uses Python identifier OutrasRetencoes
    __OutrasRetencoes = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "OutrasRetencoes"),
        "OutrasRetencoes",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsOutrasRetencoes",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 418, 3
        ),
    )

    OutrasRetencoes = property(__OutrasRetencoes.value, __OutrasRetencoes.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorIss uses Python identifier ValorIss
    __ValorIss = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorIss"),
        "ValorIss",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsValorIss",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 420, 3
        ),
    )

    ValorIss = property(__ValorIss.value, __ValorIss.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Aliquota uses Python identifier Aliquota
    __Aliquota = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Aliquota"),
        "Aliquota",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsAliquota",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 422, 3
        ),
    )

    Aliquota = property(__Aliquota.value, __Aliquota.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DescontoIncondicionado uses Python identifier DescontoIncondicionado
    __DescontoIncondicionado = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DescontoIncondicionado"),
        "DescontoIncondicionado",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsDescontoIncondicionado",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 424, 3
        ),
    )

    DescontoIncondicionado = property(
        __DescontoIncondicionado.value, __DescontoIncondicionado.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DescontoCondicionado uses Python identifier DescontoCondicionado
    __DescontoCondicionado = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DescontoCondicionado"),
        "DescontoCondicionado",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresDeclaracaoServico_httpwww_betha_com_bre_nota_contribuinte_wsDescontoCondicionado",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 426, 3
        ),
    )

    DescontoCondicionado = property(
        __DescontoCondicionado.value, __DescontoCondicionado.set, None, None
    )

    _ElementMap.update(
        {
            __ValorServicos.name(): __ValorServicos,
            __ValorDeducoes.name(): __ValorDeducoes,
            __ValorPis.name(): __ValorPis,
            __ValorCofins.name(): __ValorCofins,
            __ValorInss.name(): __ValorInss,
            __ValorIr.name(): __ValorIr,
            __ValorCsll.name(): __ValorCsll,
            __OutrasRetencoes.name(): __OutrasRetencoes,
            __ValorIss.name(): __ValorIss,
            __Aliquota.name(): __Aliquota,
            __DescontoIncondicionado.name(): __DescontoIncondicionado,
            __DescontoCondicionado.name(): __DescontoCondicionado,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcValoresDeclaracaoServico = tcValoresDeclaracaoServico
Namespace.addCategoryObject("typeBinding", "tcValoresDeclaracaoServico", tcValoresDeclaracaoServico)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcValoresNfse with content type ELEMENT_ONLY
class tcValoresNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcValoresNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcValoresNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 431, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}BaseCalculo uses Python identifier BaseCalculo
    __BaseCalculo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "BaseCalculo"),
        "BaseCalculo",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresNfse_httpwww_betha_com_bre_nota_contribuinte_wsBaseCalculo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 433, 3
        ),
    )

    BaseCalculo = property(__BaseCalculo.value, __BaseCalculo.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Aliquota uses Python identifier Aliquota
    __Aliquota = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Aliquota"),
        "Aliquota",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresNfse_httpwww_betha_com_bre_nota_contribuinte_wsAliquota",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 435, 3
        ),
    )

    Aliquota = property(__Aliquota.value, __Aliquota.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorIss uses Python identifier ValorIss
    __ValorIss = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorIss"),
        "ValorIss",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresNfse_httpwww_betha_com_bre_nota_contribuinte_wsValorIss",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 437, 3
        ),
    )

    ValorIss = property(__ValorIss.value, __ValorIss.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorLiquidoNfse uses Python identifier ValorLiquidoNfse
    __ValorLiquidoNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorLiquidoNfse"),
        "ValorLiquidoNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcValoresNfse_httpwww_betha_com_bre_nota_contribuinte_wsValorLiquidoNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 439, 3
        ),
    )

    ValorLiquidoNfse = property(__ValorLiquidoNfse.value, __ValorLiquidoNfse.set, None, None)

    _ElementMap.update(
        {
            __BaseCalculo.name(): __BaseCalculo,
            __Aliquota.name(): __Aliquota,
            __ValorIss.name(): __ValorIss,
            __ValorLiquidoNfse.name(): __ValorLiquidoNfse,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcValoresNfse = tcValoresNfse
Namespace.addCategoryObject("typeBinding", "tcValoresNfse", tcValoresNfse)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDadosServico with content type ELEMENT_ONLY
class tcDadosServico(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDadosServico with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcDadosServico")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 444, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Valores uses Python identifier Valores
    __Valores = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Valores"),
        "Valores",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsValores",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 446, 3
        ),
    )

    Valores = property(__Valores.value, __Valores.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}IssRetido uses Python identifier IssRetido
    __IssRetido = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IssRetido"),
        "IssRetido",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsIssRetido",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 448, 3
        ),
    )

    IssRetido = property(__IssRetido.value, __IssRetido.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ResponsavelRetencao uses Python identifier ResponsavelRetencao
    __ResponsavelRetencao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ResponsavelRetencao"),
        "ResponsavelRetencao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsResponsavelRetencao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 450, 3
        ),
    )

    ResponsavelRetencao = property(
        __ResponsavelRetencao.value, __ResponsavelRetencao.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ItemListaServico uses Python identifier ItemListaServico
    __ItemListaServico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ItemListaServico"),
        "ItemListaServico",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsItemListaServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 452, 3
        ),
    )

    ItemListaServico = property(__ItemListaServico.value, __ItemListaServico.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoCnae uses Python identifier CodigoCnae
    __CodigoCnae = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoCnae"),
        "CodigoCnae",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsCodigoCnae",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 454, 3
        ),
    )

    CodigoCnae = property(__CodigoCnae.value, __CodigoCnae.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoTributacaoMunicipio uses Python identifier CodigoTributacaoMunicipio
    __CodigoTributacaoMunicipio = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoTributacaoMunicipio"),
        "CodigoTributacaoMunicipio",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsCodigoTributacaoMunicipio",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 456, 3
        ),
    )

    CodigoTributacaoMunicipio = property(
        __CodigoTributacaoMunicipio.value, __CodigoTributacaoMunicipio.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Discriminacao uses Python identifier Discriminacao
    __Discriminacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Discriminacao"),
        "Discriminacao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsDiscriminacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 458, 3
        ),
    )

    Discriminacao = property(__Discriminacao.value, __Discriminacao.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        "CodigoMunicipio",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsCodigoMunicipio",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 460, 3
        ),
    )

    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoPais uses Python identifier CodigoPais
    __CodigoPais = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoPais"),
        "CodigoPais",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsCodigoPais",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 462, 3
        ),
    )

    CodigoPais = property(__CodigoPais.value, __CodigoPais.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ExigibilidadeISS uses Python identifier ExigibilidadeISS
    __ExigibilidadeISS = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ExigibilidadeISS"),
        "ExigibilidadeISS",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsExigibilidadeISS",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 464, 3
        ),
    )

    ExigibilidadeISS = property(__ExigibilidadeISS.value, __ExigibilidadeISS.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}MunicipioIncidencia uses Python identifier MunicipioIncidencia
    __MunicipioIncidencia = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "MunicipioIncidencia"),
        "MunicipioIncidencia",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsMunicipioIncidencia",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 466, 3
        ),
    )

    MunicipioIncidencia = property(
        __MunicipioIncidencia.value, __MunicipioIncidencia.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NumeroProcesso uses Python identifier NumeroProcesso
    __NumeroProcesso = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NumeroProcesso"),
        "NumeroProcesso",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosServico_httpwww_betha_com_bre_nota_contribuinte_wsNumeroProcesso",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 468, 3
        ),
    )

    NumeroProcesso = property(__NumeroProcesso.value, __NumeroProcesso.set, None, None)

    _ElementMap.update(
        {
            __Valores.name(): __Valores,
            __IssRetido.name(): __IssRetido,
            __ResponsavelRetencao.name(): __ResponsavelRetencao,
            __ItemListaServico.name(): __ItemListaServico,
            __CodigoCnae.name(): __CodigoCnae,
            __CodigoTributacaoMunicipio.name(): __CodigoTributacaoMunicipio,
            __Discriminacao.name(): __Discriminacao,
            __CodigoMunicipio.name(): __CodigoMunicipio,
            __CodigoPais.name(): __CodigoPais,
            __ExigibilidadeISS.name(): __ExigibilidadeISS,
            __MunicipioIncidencia.name(): __MunicipioIncidencia,
            __NumeroProcesso.name(): __NumeroProcesso,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcDadosServico = tcDadosServico
Namespace.addCategoryObject("typeBinding", "tcDadosServico", tcDadosServico)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDadosConstrucaoCivil with content type ELEMENT_ONLY
class tcDadosConstrucaoCivil(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDadosConstrucaoCivil with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcDadosConstrucaoCivil")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 474, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoObra uses Python identifier CodigoObra
    __CodigoObra = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoObra"),
        "CodigoObra",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosConstrucaoCivil_httpwww_betha_com_bre_nota_contribuinte_wsCodigoObra",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 476, 3
        ),
    )

    CodigoObra = property(__CodigoObra.value, __CodigoObra.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Art uses Python identifier Art
    __Art = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Art"),
        "Art",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosConstrucaoCivil_httpwww_betha_com_bre_nota_contribuinte_wsArt",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 478, 3
        ),
    )

    Art = property(__Art.value, __Art.set, None, None)

    _ElementMap.update({__CodigoObra.name(): __CodigoObra, __Art.name(): __Art})
    _AttributeMap.update({})


_module_typeBindings.tcDadosConstrucaoCivil = tcDadosConstrucaoCivil
Namespace.addCategoryObject("typeBinding", "tcDadosConstrucaoCivil", tcDadosConstrucaoCivil)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDadosPrestador with content type ELEMENT_ONLY
class tcDadosPrestador(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDadosPrestador with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcDadosPrestador")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 483, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}IdentificacaoPrestador uses Python identifier IdentificacaoPrestador
    __IdentificacaoPrestador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoPrestador"),
        "IdentificacaoPrestador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosPrestador_httpwww_betha_com_bre_nota_contribuinte_wsIdentificacaoPrestador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 485, 3
        ),
    )

    IdentificacaoPrestador = property(
        __IdentificacaoPrestador.value, __IdentificacaoPrestador.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}RazaoSocial uses Python identifier RazaoSocial
    __RazaoSocial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        "RazaoSocial",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosPrestador_httpwww_betha_com_bre_nota_contribuinte_wsRazaoSocial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 487, 3
        ),
    )

    RazaoSocial = property(__RazaoSocial.value, __RazaoSocial.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NomeFantasia uses Python identifier NomeFantasia
    __NomeFantasia = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NomeFantasia"),
        "NomeFantasia",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosPrestador_httpwww_betha_com_bre_nota_contribuinte_wsNomeFantasia",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 489, 3
        ),
    )

    NomeFantasia = property(__NomeFantasia.value, __NomeFantasia.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Endereco uses Python identifier Endereco
    __Endereco = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        "Endereco",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosPrestador_httpwww_betha_com_bre_nota_contribuinte_wsEndereco",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 491, 3
        ),
    )

    Endereco = property(__Endereco.value, __Endereco.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Contato uses Python identifier Contato
    __Contato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Contato"),
        "Contato",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDadosPrestador_httpwww_betha_com_bre_nota_contribuinte_wsContato",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 493, 3
        ),
    )

    Contato = property(__Contato.value, __Contato.set, None, None)

    _ElementMap.update(
        {
            __IdentificacaoPrestador.name(): __IdentificacaoPrestador,
            __RazaoSocial.name(): __RazaoSocial,
            __NomeFantasia.name(): __NomeFantasia,
            __Endereco.name(): __Endereco,
            __Contato.name(): __Contato,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcDadosPrestador = tcDadosPrestador
Namespace.addCategoryObject("typeBinding", "tcDadosPrestador", tcDadosPrestador)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDeclaracaoPrestacaoServico with content type ELEMENT_ONLY
class tcDeclaracaoPrestacaoServico(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcDeclaracaoPrestacaoServico with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcDeclaracaoPrestacaoServico")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 538, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}InfDeclaracaoPrestacaoServico uses Python identifier InfDeclaracaoPrestacaoServico
    __InfDeclaracaoPrestacaoServico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InfDeclaracaoPrestacaoServico"),
        "InfDeclaracaoPrestacaoServico",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsInfDeclaracaoPrestacaoServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 540, 3
        ),
    )

    InfDeclaracaoPrestacaoServico = property(
        __InfDeclaracaoPrestacaoServico.value, __InfDeclaracaoPrestacaoServico.set, None, None
    )

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcDeclaracaoPrestacaoServico_httpwww_w3_org200009xmldsigSignature",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update(
        {
            __InfDeclaracaoPrestacaoServico.name(): __InfDeclaracaoPrestacaoServico,
            __Signature.name(): __Signature,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcDeclaracaoPrestacaoServico = tcDeclaracaoPrestacaoServico
Namespace.addCategoryObject(
    "typeBinding", "tcDeclaracaoPrestacaoServico", tcDeclaracaoPrestacaoServico
)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoNfse with content type ELEMENT_ONLY
class tcIdentificacaoNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcIdentificacaoNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 547, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        "Numero",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoNfse_httpwww_betha_com_bre_nota_contribuinte_wsNumero",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 549, 3
        ),
    )

    Numero = property(__Numero.value, __Numero.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CpfCnpj uses Python identifier CpfCnpj
    __CpfCnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        "CpfCnpj",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoNfse_httpwww_betha_com_bre_nota_contribuinte_wsCpfCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 551, 3
        ),
    )

    CpfCnpj = property(__CpfCnpj.value, __CpfCnpj.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoNfse_httpwww_betha_com_bre_nota_contribuinte_wsInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 553, 3
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        "CodigoMunicipio",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcIdentificacaoNfse_httpwww_betha_com_bre_nota_contribuinte_wsCodigoMunicipio",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 555, 3
        ),
    )

    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    _ElementMap.update(
        {
            __Numero.name(): __Numero,
            __CpfCnpj.name(): __CpfCnpj,
            __InscricaoMunicipal.name(): __InscricaoMunicipal,
            __CodigoMunicipio.name(): __CodigoMunicipio,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoNfse = tcIdentificacaoNfse
Namespace.addCategoryObject("typeBinding", "tcIdentificacaoNfse", tcIdentificacaoNfse)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcPedidoCancelamento with content type ELEMENT_ONLY
class tcPedidoCancelamento(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcPedidoCancelamento with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcPedidoCancelamento")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 605, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}InfPedidoCancelamento uses Python identifier InfPedidoCancelamento
    __InfPedidoCancelamento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InfPedidoCancelamento"),
        "InfPedidoCancelamento",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcPedidoCancelamento_httpwww_betha_com_bre_nota_contribuinte_wsInfPedidoCancelamento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 607, 3
        ),
    )

    InfPedidoCancelamento = property(
        __InfPedidoCancelamento.value, __InfPedidoCancelamento.set, None, None
    )

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcPedidoCancelamento_httpwww_w3_org200009xmldsigSignature",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update(
        {__InfPedidoCancelamento.name(): __InfPedidoCancelamento, __Signature.name(): __Signature}
    )
    _AttributeMap.update({})


_module_typeBindings.tcPedidoCancelamento = tcPedidoCancelamento
Namespace.addCategoryObject("typeBinding", "tcPedidoCancelamento", tcPedidoCancelamento)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcRetCancelamento with content type ELEMENT_ONLY
class tcRetCancelamento(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcRetCancelamento with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcRetCancelamento")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 634, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NfseCancelamento uses Python identifier NfseCancelamento
    __NfseCancelamento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseCancelamento"),
        "NfseCancelamento",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcRetCancelamento_httpwww_betha_com_bre_nota_contribuinte_wsNfseCancelamento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 636, 3
        ),
    )

    NfseCancelamento = property(__NfseCancelamento.value, __NfseCancelamento.set, None, None)

    _ElementMap.update({__NfseCancelamento.name(): __NfseCancelamento})
    _AttributeMap.update({})


_module_typeBindings.tcRetCancelamento = tcRetCancelamento
Namespace.addCategoryObject("typeBinding", "tcRetCancelamento", tcRetCancelamento)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcCompNfse with content type ELEMENT_ONLY
class tcCompNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcCompNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcCompNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 660, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Nfse uses Python identifier Nfse
    __Nfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Nfse"),
        "Nfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcCompNfse_httpwww_betha_com_bre_nota_contribuinte_wsNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 662, 3
        ),
    )

    Nfse = property(__Nfse.value, __Nfse.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NfseCancelamento uses Python identifier NfseCancelamento
    __NfseCancelamento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseCancelamento"),
        "NfseCancelamento",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcCompNfse_httpwww_betha_com_bre_nota_contribuinte_wsNfseCancelamento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 664, 3
        ),
    )

    NfseCancelamento = property(__NfseCancelamento.value, __NfseCancelamento.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NfseSubstituicao uses Python identifier NfseSubstituicao
    __NfseSubstituicao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituicao"),
        "NfseSubstituicao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcCompNfse_httpwww_betha_com_bre_nota_contribuinte_wsNfseSubstituicao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 666, 3
        ),
    )

    NfseSubstituicao = property(__NfseSubstituicao.value, __NfseSubstituicao.set, None, None)

    _ElementMap.update(
        {
            __Nfse.name(): __Nfse,
            __NfseCancelamento.name(): __NfseCancelamento,
            __NfseSubstituicao.name(): __NfseSubstituicao,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcCompNfse = tcCompNfse
Namespace.addCategoryObject("typeBinding", "tcCompNfse", tcCompNfse)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcMensagemRetorno with content type ELEMENT_ONLY
class tcMensagemRetorno(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcMensagemRetorno with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcMensagemRetorno")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 671, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Codigo uses Python identifier Codigo
    __Codigo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Codigo"),
        "Codigo",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcMensagemRetorno_httpwww_betha_com_bre_nota_contribuinte_wsCodigo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 673, 3
        ),
    )

    Codigo = property(__Codigo.value, __Codigo.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Mensagem uses Python identifier Mensagem
    __Mensagem = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Mensagem"),
        "Mensagem",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcMensagemRetorno_httpwww_betha_com_bre_nota_contribuinte_wsMensagem",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 675, 3
        ),
    )

    Mensagem = property(__Mensagem.value, __Mensagem.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Correcao uses Python identifier Correcao
    __Correcao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Correcao"),
        "Correcao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcMensagemRetorno_httpwww_betha_com_bre_nota_contribuinte_wsCorrecao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 677, 3
        ),
    )

    Correcao = property(__Correcao.value, __Correcao.set, None, None)

    _ElementMap.update(
        {__Codigo.name(): __Codigo, __Mensagem.name(): __Mensagem, __Correcao.name(): __Correcao}
    )
    _AttributeMap.update({})


_module_typeBindings.tcMensagemRetorno = tcMensagemRetorno
Namespace.addCategoryObject("typeBinding", "tcMensagemRetorno", tcMensagemRetorno)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcMensagemRetornoLote with content type ELEMENT_ONLY
class tcMensagemRetornoLote(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcMensagemRetornoLote with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcMensagemRetornoLote")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 682, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}IdentificacaoRps uses Python identifier IdentificacaoRps
    __IdentificacaoRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        "IdentificacaoRps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcMensagemRetornoLote_httpwww_betha_com_bre_nota_contribuinte_wsIdentificacaoRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 684, 3
        ),
    )

    IdentificacaoRps = property(__IdentificacaoRps.value, __IdentificacaoRps.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Codigo uses Python identifier Codigo
    __Codigo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Codigo"),
        "Codigo",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcMensagemRetornoLote_httpwww_betha_com_bre_nota_contribuinte_wsCodigo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 686, 3
        ),
    )

    Codigo = property(__Codigo.value, __Codigo.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Mensagem uses Python identifier Mensagem
    __Mensagem = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Mensagem"),
        "Mensagem",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcMensagemRetornoLote_httpwww_betha_com_bre_nota_contribuinte_wsMensagem",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 688, 3
        ),
    )

    Mensagem = property(__Mensagem.value, __Mensagem.set, None, None)

    _ElementMap.update(
        {
            __IdentificacaoRps.name(): __IdentificacaoRps,
            __Codigo.name(): __Codigo,
            __Mensagem.name(): __Mensagem,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcMensagemRetornoLote = tcMensagemRetornoLote
Namespace.addCategoryObject("typeBinding", "tcMensagemRetornoLote", tcMensagemRetornoLote)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 704, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Rps uses Python identifier Rps
    __Rps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Rps"),
        "Rps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_httpwww_betha_com_bre_nota_contribuinte_wsRps",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 706, 6
        ),
    )

    Rps = property(__Rps.value, __Rps.set, None, None)

    _ElementMap.update({__Rps.name(): __Rps})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 718, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}MensagemRetorno uses Python identifier MensagemRetorno
    __MensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno"),
        "MensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON__httpwww_betha_com_bre_nota_contribuinte_wsMensagemRetorno",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 720, 4
        ),
    )

    MensagemRetorno = property(__MensagemRetorno.value, __MensagemRetorno.set, None, None)

    _ElementMap.update({__MensagemRetorno.name(): __MensagemRetorno})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 727, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}MensagemRetorno uses Python identifier MensagemRetorno
    __MensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno"),
        "MensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_2_httpwww_betha_com_bre_nota_contribuinte_wsMensagemRetorno",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 729, 4
        ),
    )

    MensagemRetorno = property(__MensagemRetorno.value, __MensagemRetorno.set, None, None)

    _ElementMap.update({__MensagemRetorno.name(): __MensagemRetorno})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 736, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}MensagemRetorno uses Python identifier MensagemRetorno
    __MensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno"),
        "MensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_3_httpwww_betha_com_bre_nota_contribuinte_wsMensagemRetorno",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 738, 4
        ),
    )

    MensagemRetorno = property(__MensagemRetorno.value, __MensagemRetorno.set, None, None)

    _ElementMap.update({__MensagemRetorno.name(): __MensagemRetorno})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 757, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}LoteRps uses Python identifier LoteRps
    __LoteRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "LoteRps"),
        "LoteRps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_4_httpwww_betha_com_bre_nota_contribuinte_wsLoteRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 759, 4
        ),
    )

    LoteRps = property(__LoteRps.value, __LoteRps.set, None, None)

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_4_httpwww_w3_org200009xmldsigSignature",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({__LoteRps.name(): __LoteRps, __Signature.name(): __Signature})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 767, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_5_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NumeroLote"),
        "NumeroLote",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_5_httpwww_betha_com_bre_nota_contribuinte_wsNumeroLote",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 770, 5
        ),
    )

    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataRecebimento uses Python identifier DataRecebimento
    __DataRecebimento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataRecebimento"),
        "DataRecebimento",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_5_httpwww_betha_com_bre_nota_contribuinte_wsDataRecebimento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 772, 5
        ),
    )

    DataRecebimento = property(__DataRecebimento.value, __DataRecebimento.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Protocolo uses Python identifier Protocolo
    __Protocolo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Protocolo"),
        "Protocolo",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_5_httpwww_betha_com_bre_nota_contribuinte_wsProtocolo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 774, 5
        ),
    )

    Protocolo = property(__Protocolo.value, __Protocolo.set, None, None)

    _ElementMap.update(
        {
            __ListaMensagemRetorno.name(): __ListaMensagemRetorno,
            __NumeroLote.name(): __NumeroLote,
            __DataRecebimento.name(): __DataRecebimento,
            __Protocolo.name(): __Protocolo,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 784, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}LoteRps uses Python identifier LoteRps
    __LoteRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "LoteRps"),
        "LoteRps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_6_httpwww_betha_com_bre_nota_contribuinte_wsLoteRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 786, 4
        ),
    )

    LoteRps = property(__LoteRps.value, __LoteRps.set, None, None)

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_6_httpwww_w3_org200009xmldsigSignature",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({__LoteRps.name(): __LoteRps, __Signature.name(): __Signature})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 795, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetornoLote uses Python identifier ListaMensagemRetornoLote
    __ListaMensagemRetornoLote = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetornoLote"),
        "ListaMensagemRetornoLote",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_7_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetornoLote",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 717, 2
        ),
    )

    ListaMensagemRetornoLote = property(
        __ListaMensagemRetornoLote.value, __ListaMensagemRetornoLote.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_7_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NumeroLote"),
        "NumeroLote",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_7_httpwww_betha_com_bre_nota_contribuinte_wsNumeroLote",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 797, 4
        ),
    )

    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataRecebimento uses Python identifier DataRecebimento
    __DataRecebimento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataRecebimento"),
        "DataRecebimento",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_7_httpwww_betha_com_bre_nota_contribuinte_wsDataRecebimento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 799, 4
        ),
    )

    DataRecebimento = property(__DataRecebimento.value, __DataRecebimento.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Protocolo uses Python identifier Protocolo
    __Protocolo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Protocolo"),
        "Protocolo",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_7_httpwww_betha_com_bre_nota_contribuinte_wsProtocolo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 801, 4
        ),
    )

    Protocolo = property(__Protocolo.value, __Protocolo.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaNfse uses Python identifier ListaNfse
    __ListaNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        "ListaNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_7_httpwww_betha_com_bre_nota_contribuinte_wsListaNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 804, 5
        ),
    )

    ListaNfse = property(__ListaNfse.value, __ListaNfse.set, None, None)

    _ElementMap.update(
        {
            __ListaMensagemRetornoLote.name(): __ListaMensagemRetornoLote,
            __ListaMensagemRetorno.name(): __ListaMensagemRetorno,
            __NumeroLote.name(): __NumeroLote,
            __DataRecebimento.name(): __DataRecebimento,
            __Protocolo.name(): __Protocolo,
            __ListaNfse.name(): __ListaNfse,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 805, 6
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemAlertaRetorno uses Python identifier ListaMensagemAlertaRetorno
    __ListaMensagemAlertaRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno"),
        "ListaMensagemAlertaRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_8_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemAlertaRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 735, 1
        ),
    )

    ListaMensagemAlertaRetorno = property(
        __ListaMensagemAlertaRetorno.value, __ListaMensagemAlertaRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        "CompNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_8_httpwww_betha_com_bre_nota_contribuinte_wsCompNfse",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )

    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    _ElementMap.update(
        {
            __ListaMensagemAlertaRetorno.name(): __ListaMensagemAlertaRetorno,
            __CompNfse.name(): __CompNfse,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 823, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Rps uses Python identifier Rps
    __Rps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Rps"),
        "Rps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_9_httpwww_betha_com_bre_nota_contribuinte_wsRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 825, 4
        ),
    )

    Rps = property(__Rps.value, __Rps.set, None, None)

    _ElementMap.update({__Rps.name(): __Rps})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 831, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_10_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaNfse uses Python identifier ListaNfse
    __ListaNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        "ListaNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_10_httpwww_betha_com_bre_nota_contribuinte_wsListaNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 834, 5
        ),
    )

    ListaNfse = property(__ListaNfse.value, __ListaNfse.set, None, None)

    _ElementMap.update(
        {__ListaMensagemRetorno.name(): __ListaMensagemRetorno, __ListaNfse.name(): __ListaNfse}
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 835, 6
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemAlertaRetorno uses Python identifier ListaMensagemAlertaRetorno
    __ListaMensagemAlertaRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno"),
        "ListaMensagemAlertaRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_11_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemAlertaRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 735, 1
        ),
    )

    ListaMensagemAlertaRetorno = property(
        __ListaMensagemAlertaRetorno.value, __ListaMensagemAlertaRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        "CompNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_11_httpwww_betha_com_bre_nota_contribuinte_wsCompNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )

    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    _ElementMap.update(
        {
            __ListaMensagemAlertaRetorno.name(): __ListaMensagemAlertaRetorno,
            __CompNfse.name(): __CompNfse,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 851, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Pedido uses Python identifier Pedido
    __Pedido = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Pedido"),
        "Pedido",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_12_httpwww_betha_com_bre_nota_contribuinte_wsPedido",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 853, 4
        ),
    )

    Pedido = property(__Pedido.value, __Pedido.set, None, None)

    _ElementMap.update({__Pedido.name(): __Pedido})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 859, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_13_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}RetCancelamento uses Python identifier RetCancelamento
    __RetCancelamento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RetCancelamento"),
        "RetCancelamento",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_13_httpwww_betha_com_bre_nota_contribuinte_wsRetCancelamento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 861, 4
        ),
    )

    RetCancelamento = property(__RetCancelamento.value, __RetCancelamento.set, None, None)

    _ElementMap.update(
        {
            __ListaMensagemRetorno.name(): __ListaMensagemRetorno,
            __RetCancelamento.name(): __RetCancelamento,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 868, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}SubstituicaoNfse uses Python identifier SubstituicaoNfse
    __SubstituicaoNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "SubstituicaoNfse"),
        "SubstituicaoNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_14_httpwww_betha_com_bre_nota_contribuinte_wsSubstituicaoNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 870, 4
        ),
    )

    SubstituicaoNfse = property(__SubstituicaoNfse.value, __SubstituicaoNfse.set, None, None)

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_14_httpwww_w3_org200009xmldsigSignature",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update(
        {__SubstituicaoNfse.name(): __SubstituicaoNfse, __Signature.name(): __Signature}
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 887, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_15_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}RetSubstituicao uses Python identifier RetSubstituicao
    __RetSubstituicao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RetSubstituicao"),
        "RetSubstituicao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_15_httpwww_betha_com_bre_nota_contribuinte_wsRetSubstituicao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 889, 5
        ),
    )

    RetSubstituicao = property(__RetSubstituicao.value, __RetSubstituicao.set, None, None)

    _ElementMap.update(
        {
            __ListaMensagemRetorno.name(): __ListaMensagemRetorno,
            __RetSubstituicao.name(): __RetSubstituicao,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 890, 6
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NfseSubstituida uses Python identifier NfseSubstituida
    __NfseSubstituida = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituida"),
        "NfseSubstituida",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_16_httpwww_betha_com_bre_nota_contribuinte_wsNfseSubstituida",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 892, 8
        ),
    )

    NfseSubstituida = property(__NfseSubstituida.value, __NfseSubstituida.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NfseSubstituidora uses Python identifier NfseSubstituidora
    __NfseSubstituidora = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituidora"),
        "NfseSubstituidora",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_16_httpwww_betha_com_bre_nota_contribuinte_wsNfseSubstituidora",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 901, 8
        ),
    )

    NfseSubstituidora = property(__NfseSubstituidora.value, __NfseSubstituidora.set, None, None)

    _ElementMap.update(
        {
            __NfseSubstituida.name(): __NfseSubstituida,
            __NfseSubstituidora.name(): __NfseSubstituidora,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 893, 9
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemAlertaRetorno uses Python identifier ListaMensagemAlertaRetorno
    __ListaMensagemAlertaRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno"),
        "ListaMensagemAlertaRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_17_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemAlertaRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 735, 1
        ),
    )

    ListaMensagemAlertaRetorno = property(
        __ListaMensagemAlertaRetorno.value, __ListaMensagemAlertaRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        "CompNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_17_httpwww_betha_com_bre_nota_contribuinte_wsCompNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )

    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    _ElementMap.update(
        {
            __ListaMensagemAlertaRetorno.name(): __ListaMensagemAlertaRetorno,
            __CompNfse.name(): __CompNfse,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 902, 9
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        "CompNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_18_httpwww_betha_com_bre_nota_contribuinte_wsCompNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )

    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    _ElementMap.update({__CompNfse.name(): __CompNfse})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 918, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        "Prestador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_19_httpwww_betha_com_bre_nota_contribuinte_wsPrestador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 920, 4
        ),
    )

    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Protocolo uses Python identifier Protocolo
    __Protocolo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Protocolo"),
        "Protocolo",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_19_httpwww_betha_com_bre_nota_contribuinte_wsProtocolo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 922, 4
        ),
    )

    Protocolo = property(__Protocolo.value, __Protocolo.set, None, None)

    _ElementMap.update({__Prestador.name(): __Prestador, __Protocolo.name(): __Protocolo})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 929, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetornoLote uses Python identifier ListaMensagemRetornoLote
    __ListaMensagemRetornoLote = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetornoLote"),
        "ListaMensagemRetornoLote",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_20_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetornoLote",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 717, 2
        ),
    )

    ListaMensagemRetornoLote = property(
        __ListaMensagemRetornoLote.value, __ListaMensagemRetornoLote.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_20_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Situacao uses Python identifier Situacao
    __Situacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Situacao"),
        "Situacao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_20_httpwww_betha_com_bre_nota_contribuinte_wsSituacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 931, 11
        ),
    )

    Situacao = property(__Situacao.value, __Situacao.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaNfse uses Python identifier ListaNfse
    __ListaNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        "ListaNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_20_httpwww_betha_com_bre_nota_contribuinte_wsListaNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 933, 4
        ),
    )

    ListaNfse = property(__ListaNfse.value, __ListaNfse.set, None, None)

    _ElementMap.update(
        {
            __ListaMensagemRetornoLote.name(): __ListaMensagemRetornoLote,
            __ListaMensagemRetorno.name(): __ListaMensagemRetorno,
            __Situacao.name(): __Situacao,
            __ListaNfse.name(): __ListaNfse,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 934, 5
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemAlertaRetorno uses Python identifier ListaMensagemAlertaRetorno
    __ListaMensagemAlertaRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno"),
        "ListaMensagemAlertaRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_21_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemAlertaRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 735, 1
        ),
    )

    ListaMensagemAlertaRetorno = property(
        __ListaMensagemAlertaRetorno.value, __ListaMensagemAlertaRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        "CompNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_21_httpwww_betha_com_bre_nota_contribuinte_wsCompNfse",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )

    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    _ElementMap.update(
        {
            __ListaMensagemAlertaRetorno.name(): __ListaMensagemAlertaRetorno,
            __CompNfse.name(): __CompNfse,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_21 = CTD_ANON_21


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 952, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}IdentificacaoRps uses Python identifier IdentificacaoRps
    __IdentificacaoRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        "IdentificacaoRps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_22_httpwww_betha_com_bre_nota_contribuinte_wsIdentificacaoRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 954, 4
        ),
    )

    IdentificacaoRps = property(__IdentificacaoRps.value, __IdentificacaoRps.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        "Prestador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_22_httpwww_betha_com_bre_nota_contribuinte_wsPrestador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 956, 4
        ),
    )

    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    _ElementMap.update(
        {__IdentificacaoRps.name(): __IdentificacaoRps, __Prestador.name(): __Prestador}
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_22 = CTD_ANON_22


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 963, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_23_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        "CompNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_23_httpwww_betha_com_bre_nota_contribuinte_wsCompNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )

    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    _ElementMap.update(
        {__ListaMensagemRetorno.name(): __ListaMensagemRetorno, __CompNfse.name(): __CompNfse}
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_23 = CTD_ANON_23


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 973, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        "Prestador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_24_httpwww_betha_com_bre_nota_contribuinte_wsPrestador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 975, 4
        ),
    )

    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NumeroNfse uses Python identifier NumeroNfse
    __NumeroNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NumeroNfse"),
        "NumeroNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_24_httpwww_betha_com_bre_nota_contribuinte_wsNumeroNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 977, 4
        ),
    )

    NumeroNfse = property(__NumeroNfse.value, __NumeroNfse.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}PeriodoEmissao uses Python identifier PeriodoEmissao
    __PeriodoEmissao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "PeriodoEmissao"),
        "PeriodoEmissao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_24_httpwww_betha_com_bre_nota_contribuinte_wsPeriodoEmissao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 980, 5
        ),
    )

    PeriodoEmissao = property(__PeriodoEmissao.value, __PeriodoEmissao.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}PeriodoCompetencia uses Python identifier PeriodoCompetencia
    __PeriodoCompetencia = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "PeriodoCompetencia"),
        "PeriodoCompetencia",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_24_httpwww_betha_com_bre_nota_contribuinte_wsPeriodoCompetencia",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 991, 5
        ),
    )

    PeriodoCompetencia = property(__PeriodoCompetencia.value, __PeriodoCompetencia.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Tomador uses Python identifier Tomador
    __Tomador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Tomador"),
        "Tomador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_24_httpwww_betha_com_bre_nota_contribuinte_wsTomador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1003, 4
        ),
    )

    Tomador = property(__Tomador.value, __Tomador.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Intermediario uses Python identifier Intermediario
    __Intermediario = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Intermediario"),
        "Intermediario",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_24_httpwww_betha_com_bre_nota_contribuinte_wsIntermediario",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1005, 4
        ),
    )

    Intermediario = property(__Intermediario.value, __Intermediario.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Pagina uses Python identifier Pagina
    __Pagina = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Pagina"),
        "Pagina",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_24_httpwww_betha_com_bre_nota_contribuinte_wsPagina",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1007, 4
        ),
    )

    Pagina = property(__Pagina.value, __Pagina.set, None, None)

    _ElementMap.update(
        {
            __Prestador.name(): __Prestador,
            __NumeroNfse.name(): __NumeroNfse,
            __PeriodoEmissao.name(): __PeriodoEmissao,
            __PeriodoCompetencia.name(): __PeriodoCompetencia,
            __Tomador.name(): __Tomador,
            __Intermediario.name(): __Intermediario,
            __Pagina.name(): __Pagina,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_24 = CTD_ANON_24


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 982, 6
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataInicial uses Python identifier DataInicial
    __DataInicial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataInicial"),
        "DataInicial",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_25_httpwww_betha_com_bre_nota_contribuinte_wsDataInicial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 984, 8
        ),
    )

    DataInicial = property(__DataInicial.value, __DataInicial.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataFinal uses Python identifier DataFinal
    __DataFinal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataFinal"),
        "DataFinal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_25_httpwww_betha_com_bre_nota_contribuinte_wsDataFinal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 986, 8
        ),
    )

    DataFinal = property(__DataFinal.value, __DataFinal.set, None, None)

    _ElementMap.update({__DataInicial.name(): __DataInicial, __DataFinal.name(): __DataFinal})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_25 = CTD_ANON_25


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 993, 6
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataInicial uses Python identifier DataInicial
    __DataInicial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataInicial"),
        "DataInicial",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_26_httpwww_betha_com_bre_nota_contribuinte_wsDataInicial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 995, 8
        ),
    )

    DataInicial = property(__DataInicial.value, __DataInicial.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataFinal uses Python identifier DataFinal
    __DataFinal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataFinal"),
        "DataFinal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_26_httpwww_betha_com_bre_nota_contribuinte_wsDataFinal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 997, 8
        ),
    )

    DataFinal = property(__DataFinal.value, __DataFinal.set, None, None)

    _ElementMap.update({__DataInicial.name(): __DataInicial, __DataFinal.name(): __DataFinal})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_26 = CTD_ANON_26


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1013, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_27_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaNfse uses Python identifier ListaNfse
    __ListaNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        "ListaNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_27_httpwww_betha_com_bre_nota_contribuinte_wsListaNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1015, 4
        ),
    )

    ListaNfse = property(__ListaNfse.value, __ListaNfse.set, None, None)

    _ElementMap.update(
        {__ListaMensagemRetorno.name(): __ListaMensagemRetorno, __ListaNfse.name(): __ListaNfse}
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_27 = CTD_ANON_27


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1016, 5
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        "CompNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_28_httpwww_betha_com_bre_nota_contribuinte_wsCompNfse",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )

    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ProximaPagina uses Python identifier ProximaPagina
    __ProximaPagina = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ProximaPagina"),
        "ProximaPagina",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_28_httpwww_betha_com_bre_nota_contribuinte_wsProximaPagina",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1019, 7
        ),
    )

    ProximaPagina = property(__ProximaPagina.value, __ProximaPagina.set, None, None)

    _ElementMap.update({__CompNfse.name(): __CompNfse, __ProximaPagina.name(): __ProximaPagina})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_28 = CTD_ANON_28


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1030, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Consulente uses Python identifier Consulente
    __Consulente = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Consulente"),
        "Consulente",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_29_httpwww_betha_com_bre_nota_contribuinte_wsConsulente",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1032, 4
        ),
    )

    Consulente = property(__Consulente.value, __Consulente.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NumeroNfse uses Python identifier NumeroNfse
    __NumeroNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NumeroNfse"),
        "NumeroNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_29_httpwww_betha_com_bre_nota_contribuinte_wsNumeroNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1034, 4
        ),
    )

    NumeroNfse = property(__NumeroNfse.value, __NumeroNfse.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}PeriodoEmissao uses Python identifier PeriodoEmissao
    __PeriodoEmissao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "PeriodoEmissao"),
        "PeriodoEmissao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_29_httpwww_betha_com_bre_nota_contribuinte_wsPeriodoEmissao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1037, 5
        ),
    )

    PeriodoEmissao = property(__PeriodoEmissao.value, __PeriodoEmissao.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}PeriodoCompetencia uses Python identifier PeriodoCompetencia
    __PeriodoCompetencia = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "PeriodoCompetencia"),
        "PeriodoCompetencia",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_29_httpwww_betha_com_bre_nota_contribuinte_wsPeriodoCompetencia",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1048, 5
        ),
    )

    PeriodoCompetencia = property(__PeriodoCompetencia.value, __PeriodoCompetencia.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        "Prestador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_29_httpwww_betha_com_bre_nota_contribuinte_wsPrestador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1060, 4
        ),
    )

    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Tomador uses Python identifier Tomador
    __Tomador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Tomador"),
        "Tomador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_29_httpwww_betha_com_bre_nota_contribuinte_wsTomador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1062, 4
        ),
    )

    Tomador = property(__Tomador.value, __Tomador.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Intermediario uses Python identifier Intermediario
    __Intermediario = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Intermediario"),
        "Intermediario",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_29_httpwww_betha_com_bre_nota_contribuinte_wsIntermediario",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1064, 4
        ),
    )

    Intermediario = property(__Intermediario.value, __Intermediario.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Pagina uses Python identifier Pagina
    __Pagina = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Pagina"),
        "Pagina",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_29_httpwww_betha_com_bre_nota_contribuinte_wsPagina",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1066, 4
        ),
    )

    Pagina = property(__Pagina.value, __Pagina.set, None, None)

    _ElementMap.update(
        {
            __Consulente.name(): __Consulente,
            __NumeroNfse.name(): __NumeroNfse,
            __PeriodoEmissao.name(): __PeriodoEmissao,
            __PeriodoCompetencia.name(): __PeriodoCompetencia,
            __Prestador.name(): __Prestador,
            __Tomador.name(): __Tomador,
            __Intermediario.name(): __Intermediario,
            __Pagina.name(): __Pagina,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_29 = CTD_ANON_29


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1039, 6
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataInicial uses Python identifier DataInicial
    __DataInicial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataInicial"),
        "DataInicial",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_30_httpwww_betha_com_bre_nota_contribuinte_wsDataInicial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1041, 8
        ),
    )

    DataInicial = property(__DataInicial.value, __DataInicial.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataFinal uses Python identifier DataFinal
    __DataFinal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataFinal"),
        "DataFinal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_30_httpwww_betha_com_bre_nota_contribuinte_wsDataFinal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1043, 8
        ),
    )

    DataFinal = property(__DataFinal.value, __DataFinal.set, None, None)

    _ElementMap.update({__DataInicial.name(): __DataInicial, __DataFinal.name(): __DataFinal})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_30 = CTD_ANON_30


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1050, 6
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataInicial uses Python identifier DataInicial
    __DataInicial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataInicial"),
        "DataInicial",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_31_httpwww_betha_com_bre_nota_contribuinte_wsDataInicial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1052, 8
        ),
    )

    DataInicial = property(__DataInicial.value, __DataInicial.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataFinal uses Python identifier DataFinal
    __DataFinal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataFinal"),
        "DataFinal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_31_httpwww_betha_com_bre_nota_contribuinte_wsDataFinal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1054, 8
        ),
    )

    DataFinal = property(__DataFinal.value, __DataFinal.set, None, None)

    _ElementMap.update({__DataInicial.name(): __DataInicial, __DataFinal.name(): __DataFinal})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_31 = CTD_ANON_31


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1072, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_32_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaNfse uses Python identifier ListaNfse
    __ListaNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        "ListaNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_32_httpwww_betha_com_bre_nota_contribuinte_wsListaNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1074, 4
        ),
    )

    ListaNfse = property(__ListaNfse.value, __ListaNfse.set, None, None)

    _ElementMap.update(
        {__ListaMensagemRetorno.name(): __ListaMensagemRetorno, __ListaNfse.name(): __ListaNfse}
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_32 = CTD_ANON_32


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1075, 5
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        "CompNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_33_httpwww_betha_com_bre_nota_contribuinte_wsCompNfse",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )

    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ProximaPagina uses Python identifier ProximaPagina
    __ProximaPagina = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ProximaPagina"),
        "ProximaPagina",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_33_httpwww_betha_com_bre_nota_contribuinte_wsProximaPagina",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1078, 7
        ),
    )

    ProximaPagina = property(__ProximaPagina.value, __ProximaPagina.set, None, None)

    _ElementMap.update({__CompNfse.name(): __CompNfse, __ProximaPagina.name(): __ProximaPagina})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_33 = CTD_ANON_33


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1089, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        "Prestador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_34_httpwww_betha_com_bre_nota_contribuinte_wsPrestador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1091, 4
        ),
    )

    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Faixa uses Python identifier Faixa
    __Faixa = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Faixa"),
        "Faixa",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_34_httpwww_betha_com_bre_nota_contribuinte_wsFaixa",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1093, 4
        ),
    )

    Faixa = property(__Faixa.value, __Faixa.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Pagina uses Python identifier Pagina
    __Pagina = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Pagina"),
        "Pagina",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_34_httpwww_betha_com_bre_nota_contribuinte_wsPagina",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1103, 4
        ),
    )

    Pagina = property(__Pagina.value, __Pagina.set, None, None)

    _ElementMap.update(
        {__Prestador.name(): __Prestador, __Faixa.name(): __Faixa, __Pagina.name(): __Pagina}
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_34 = CTD_ANON_34


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1094, 5
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NumeroNfseInicial uses Python identifier NumeroNfseInicial
    __NumeroNfseInicial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NumeroNfseInicial"),
        "NumeroNfseInicial",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_35_httpwww_betha_com_bre_nota_contribuinte_wsNumeroNfseInicial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1096, 7
        ),
    )

    NumeroNfseInicial = property(__NumeroNfseInicial.value, __NumeroNfseInicial.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NumeroNfseFinal uses Python identifier NumeroNfseFinal
    __NumeroNfseFinal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NumeroNfseFinal"),
        "NumeroNfseFinal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_35_httpwww_betha_com_bre_nota_contribuinte_wsNumeroNfseFinal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1098, 7
        ),
    )

    NumeroNfseFinal = property(__NumeroNfseFinal.value, __NumeroNfseFinal.set, None, None)

    _ElementMap.update(
        {
            __NumeroNfseInicial.name(): __NumeroNfseInicial,
            __NumeroNfseFinal.name(): __NumeroNfseFinal,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_35 = CTD_ANON_35


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1109, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        "ListaMensagemRetorno",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_36_httpwww_betha_com_bre_nota_contribuinte_wsListaMensagemRetorno",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )

    ListaMensagemRetorno = property(
        __ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaNfse uses Python identifier ListaNfse
    __ListaNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        "ListaNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_36_httpwww_betha_com_bre_nota_contribuinte_wsListaNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1111, 4
        ),
    )

    ListaNfse = property(__ListaNfse.value, __ListaNfse.set, None, None)

    _ElementMap.update(
        {__ListaMensagemRetorno.name(): __ListaMensagemRetorno, __ListaNfse.name(): __ListaNfse}
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_36 = CTD_ANON_36


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1112, 5
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        "CompNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_37_httpwww_betha_com_bre_nota_contribuinte_wsCompNfse",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )

    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ProximaPagina uses Python identifier ProximaPagina
    __ProximaPagina = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ProximaPagina"),
        "ProximaPagina",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_37_httpwww_betha_com_bre_nota_contribuinte_wsProximaPagina",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1115, 7
        ),
    )

    ProximaPagina = property(__ProximaPagina.value, __ProximaPagina.set, None, None)

    _ElementMap.update({__CompNfse.name(): __CompNfse, __ProximaPagina.name(): __ProximaPagina})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_37 = CTD_ANON_37


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcInfRps with content type ELEMENT_ONLY
class tcInfRps(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcInfRps with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcInfRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 498, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}IdentificacaoRps uses Python identifier IdentificacaoRps
    __IdentificacaoRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        "IdentificacaoRps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfRps_httpwww_betha_com_bre_nota_contribuinte_wsIdentificacaoRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 500, 3
        ),
    )

    IdentificacaoRps = property(__IdentificacaoRps.value, __IdentificacaoRps.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataEmissao uses Python identifier DataEmissao
    __DataEmissao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataEmissao"),
        "DataEmissao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfRps_httpwww_betha_com_bre_nota_contribuinte_wsDataEmissao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 502, 3
        ),
    )

    DataEmissao = property(__DataEmissao.value, __DataEmissao.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Status"),
        "Status",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfRps_httpwww_betha_com_bre_nota_contribuinte_wsStatus",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 504, 3
        ),
    )

    Status = property(__Status.value, __Status.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}RpsSubstituido uses Python identifier RpsSubstituido
    __RpsSubstituido = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RpsSubstituido"),
        "RpsSubstituido",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfRps_httpwww_betha_com_bre_nota_contribuinte_wsRpsSubstituido",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 506, 3
        ),
    )

    RpsSubstituido = property(__RpsSubstituido.value, __RpsSubstituido.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfRps_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 509, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 509, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update(
        {
            __IdentificacaoRps.name(): __IdentificacaoRps,
            __DataEmissao.name(): __DataEmissao,
            __Status.name(): __Status,
            __RpsSubstituido.name(): __RpsSubstituido,
        }
    )
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcInfRps = tcInfRps
Namespace.addCategoryObject("typeBinding", "tcInfRps", tcInfRps)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcInfDeclaracaoPrestacaoServico with content type ELEMENT_ONLY
class tcInfDeclaracaoPrestacaoServico(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcInfDeclaracaoPrestacaoServico with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcInfDeclaracaoPrestacaoServico")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 512, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Rps uses Python identifier Rps
    __Rps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Rps"),
        "Rps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 514, 3
        ),
    )

    Rps = property(__Rps.value, __Rps.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Competencia uses Python identifier Competencia
    __Competencia = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Competencia"),
        "Competencia",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsCompetencia",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 516, 3
        ),
    )

    Competencia = property(__Competencia.value, __Competencia.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Servico uses Python identifier Servico
    __Servico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Servico"),
        "Servico",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 518, 3
        ),
    )

    Servico = property(__Servico.value, __Servico.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        "Prestador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsPrestador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 520, 3
        ),
    )

    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Tomador uses Python identifier Tomador
    __Tomador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Tomador"),
        "Tomador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsTomador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 522, 3
        ),
    )

    Tomador = property(__Tomador.value, __Tomador.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Intermediario uses Python identifier Intermediario
    __Intermediario = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Intermediario"),
        "Intermediario",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsIntermediario",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 524, 3
        ),
    )

    Intermediario = property(__Intermediario.value, __Intermediario.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ConstrucaoCivil uses Python identifier ConstrucaoCivil
    __ConstrucaoCivil = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ConstrucaoCivil"),
        "ConstrucaoCivil",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsConstrucaoCivil",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 526, 3
        ),
    )

    ConstrucaoCivil = property(__ConstrucaoCivil.value, __ConstrucaoCivil.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}RegimeEspecialTributacao uses Python identifier RegimeEspecialTributacao
    __RegimeEspecialTributacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RegimeEspecialTributacao"),
        "RegimeEspecialTributacao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsRegimeEspecialTributacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 528, 3
        ),
    )

    RegimeEspecialTributacao = property(
        __RegimeEspecialTributacao.value, __RegimeEspecialTributacao.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}OptanteSimplesNacional uses Python identifier OptanteSimplesNacional
    __OptanteSimplesNacional = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "OptanteSimplesNacional"),
        "OptanteSimplesNacional",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsOptanteSimplesNacional",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 530, 3
        ),
    )

    OptanteSimplesNacional = property(
        __OptanteSimplesNacional.value, __OptanteSimplesNacional.set, None, None
    )

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}IncentivoFiscal uses Python identifier IncentivoFiscal
    __IncentivoFiscal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IncentivoFiscal"),
        "IncentivoFiscal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_httpwww_betha_com_bre_nota_contribuinte_wsIncentivoFiscal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 532, 3
        ),
    )

    IncentivoFiscal = property(__IncentivoFiscal.value, __IncentivoFiscal.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfDeclaracaoPrestacaoServico_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 535, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 535, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update(
        {
            __Rps.name(): __Rps,
            __Competencia.name(): __Competencia,
            __Servico.name(): __Servico,
            __Prestador.name(): __Prestador,
            __Tomador.name(): __Tomador,
            __Intermediario.name(): __Intermediario,
            __ConstrucaoCivil.name(): __ConstrucaoCivil,
            __RegimeEspecialTributacao.name(): __RegimeEspecialTributacao,
            __OptanteSimplesNacional.name(): __OptanteSimplesNacional,
            __IncentivoFiscal.name(): __IncentivoFiscal,
        }
    )
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcInfDeclaracaoPrestacaoServico = tcInfDeclaracaoPrestacaoServico
Namespace.addCategoryObject(
    "typeBinding", "tcInfDeclaracaoPrestacaoServico", tcInfDeclaracaoPrestacaoServico
)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcInfNfse with content type ELEMENT_ONLY
class tcInfNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcInfNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcInfNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 560, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        "Numero",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_httpwww_betha_com_bre_nota_contribuinte_wsNumero",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 562, 3
        ),
    )

    Numero = property(__Numero.value, __Numero.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoVerificacao uses Python identifier CodigoVerificacao
    __CodigoVerificacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoVerificacao"),
        "CodigoVerificacao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_httpwww_betha_com_bre_nota_contribuinte_wsCodigoVerificacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 564, 3
        ),
    )

    CodigoVerificacao = property(__CodigoVerificacao.value, __CodigoVerificacao.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataEmissao uses Python identifier DataEmissao
    __DataEmissao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataEmissao"),
        "DataEmissao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_httpwww_betha_com_bre_nota_contribuinte_wsDataEmissao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 566, 3
        ),
    )

    DataEmissao = property(__DataEmissao.value, __DataEmissao.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NfseSubstituida uses Python identifier NfseSubstituida
    __NfseSubstituida = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituida"),
        "NfseSubstituida",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_httpwww_betha_com_bre_nota_contribuinte_wsNfseSubstituida",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 568, 3
        ),
    )

    NfseSubstituida = property(__NfseSubstituida.value, __NfseSubstituida.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}OutrasInformacoes uses Python identifier OutrasInformacoes
    __OutrasInformacoes = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "OutrasInformacoes"),
        "OutrasInformacoes",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_httpwww_betha_com_bre_nota_contribuinte_wsOutrasInformacoes",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 570, 3
        ),
    )

    OutrasInformacoes = property(__OutrasInformacoes.value, __OutrasInformacoes.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValoresNfse uses Python identifier ValoresNfse
    __ValoresNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValoresNfse"),
        "ValoresNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_httpwww_betha_com_bre_nota_contribuinte_wsValoresNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 572, 3
        ),
    )

    ValoresNfse = property(__ValoresNfse.value, __ValoresNfse.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ValorCredito uses Python identifier ValorCredito
    __ValorCredito = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorCredito"),
        "ValorCredito",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_httpwww_betha_com_bre_nota_contribuinte_wsValorCredito",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 574, 3
        ),
    )

    ValorCredito = property(__ValorCredito.value, __ValorCredito.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}PrestadorServico uses Python identifier PrestadorServico
    __PrestadorServico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "PrestadorServico"),
        "PrestadorServico",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_httpwww_betha_com_bre_nota_contribuinte_wsPrestadorServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 576, 3
        ),
    )

    PrestadorServico = property(__PrestadorServico.value, __PrestadorServico.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}OrgaoGerador uses Python identifier OrgaoGerador
    __OrgaoGerador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "OrgaoGerador"),
        "OrgaoGerador",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_httpwww_betha_com_bre_nota_contribuinte_wsOrgaoGerador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 578, 3
        ),
    )

    OrgaoGerador = property(__OrgaoGerador.value, __OrgaoGerador.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DeclaracaoPrestacaoServico uses Python identifier DeclaracaoPrestacaoServico
    __DeclaracaoPrestacaoServico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DeclaracaoPrestacaoServico"),
        "DeclaracaoPrestacaoServico",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_httpwww_betha_com_bre_nota_contribuinte_wsDeclaracaoPrestacaoServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 580, 3
        ),
    )

    DeclaracaoPrestacaoServico = property(
        __DeclaracaoPrestacaoServico.value, __DeclaracaoPrestacaoServico.set, None, None
    )

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfNfse_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 582, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 582, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update(
        {
            __Numero.name(): __Numero,
            __CodigoVerificacao.name(): __CodigoVerificacao,
            __DataEmissao.name(): __DataEmissao,
            __NfseSubstituida.name(): __NfseSubstituida,
            __OutrasInformacoes.name(): __OutrasInformacoes,
            __ValoresNfse.name(): __ValoresNfse,
            __ValorCredito.name(): __ValorCredito,
            __PrestadorServico.name(): __PrestadorServico,
            __OrgaoGerador.name(): __OrgaoGerador,
            __DeclaracaoPrestacaoServico.name(): __DeclaracaoPrestacaoServico,
        }
    )
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcInfNfse = tcInfNfse
Namespace.addCategoryObject("typeBinding", "tcInfNfse", tcInfNfse)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcNfse with content type ELEMENT_ONLY
class tcNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 585, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}InfNfse uses Python identifier InfNfse
    __InfNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InfNfse"),
        "InfNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcNfse_httpwww_betha_com_bre_nota_contribuinte_wsInfNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 587, 3
        ),
    )

    InfNfse = property(__InfNfse.value, __InfNfse.set, None, None)

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcNfse_httpwww_w3_org200009xmldsigSignature",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    # Attribute versao uses Python identifier versao
    __versao = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "versao"),
        "versao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcNfse_versao",
        _module_typeBindings.tsVersao,
        required=True,
    )
    __versao._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 592, 2
    )
    __versao._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 592, 2
    )

    versao = property(__versao.value, __versao.set, None, None)

    _ElementMap.update({__InfNfse.name(): __InfNfse, __Signature.name(): __Signature})
    _AttributeMap.update({__versao.name(): __versao})


_module_typeBindings.tcNfse = tcNfse
Namespace.addCategoryObject("typeBinding", "tcNfse", tcNfse)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcInfPedidoCancelamento with content type ELEMENT_ONLY
class tcInfPedidoCancelamento(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcInfPedidoCancelamento with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcInfPedidoCancelamento")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 595, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}IdentificacaoNfse uses Python identifier IdentificacaoNfse
    __IdentificacaoNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoNfse"),
        "IdentificacaoNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfPedidoCancelamento_httpwww_betha_com_bre_nota_contribuinte_wsIdentificacaoNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 597, 3
        ),
    )

    IdentificacaoNfse = property(__IdentificacaoNfse.value, __IdentificacaoNfse.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CodigoCancelamento uses Python identifier CodigoCancelamento
    __CodigoCancelamento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoCancelamento"),
        "CodigoCancelamento",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfPedidoCancelamento_httpwww_betha_com_bre_nota_contribuinte_wsCodigoCancelamento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 599, 3
        ),
    )

    CodigoCancelamento = property(__CodigoCancelamento.value, __CodigoCancelamento.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfPedidoCancelamento_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 602, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 602, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update(
        {
            __IdentificacaoNfse.name(): __IdentificacaoNfse,
            __CodigoCancelamento.name(): __CodigoCancelamento,
        }
    )
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcInfPedidoCancelamento = tcInfPedidoCancelamento
Namespace.addCategoryObject("typeBinding", "tcInfPedidoCancelamento", tcInfPedidoCancelamento)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcConfirmacaoCancelamento with content type ELEMENT_ONLY
class tcConfirmacaoCancelamento(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcConfirmacaoCancelamento with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcConfirmacaoCancelamento")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 614, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Pedido uses Python identifier Pedido
    __Pedido = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Pedido"),
        "Pedido",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcConfirmacaoCancelamento_httpwww_betha_com_bre_nota_contribuinte_wsPedido",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 616, 3
        ),
    )

    Pedido = property(__Pedido.value, __Pedido.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}DataHora uses Python identifier DataHora
    __DataHora = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataHora"),
        "DataHora",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcConfirmacaoCancelamento_httpwww_betha_com_bre_nota_contribuinte_wsDataHora",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 618, 3
        ),
    )

    DataHora = property(__DataHora.value, __DataHora.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcConfirmacaoCancelamento_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 621, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 621, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({__Pedido.name(): __Pedido, __DataHora.name(): __DataHora})
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcConfirmacaoCancelamento = tcConfirmacaoCancelamento
Namespace.addCategoryObject("typeBinding", "tcConfirmacaoCancelamento", tcConfirmacaoCancelamento)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcCancelamentoNfse with content type ELEMENT_ONLY
class tcCancelamentoNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcCancelamentoNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcCancelamentoNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 624, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Confirmacao uses Python identifier Confirmacao
    __Confirmacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Confirmacao"),
        "Confirmacao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcCancelamentoNfse_httpwww_betha_com_bre_nota_contribuinte_wsConfirmacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 626, 3
        ),
    )

    Confirmacao = property(__Confirmacao.value, __Confirmacao.set, None, None)

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcCancelamentoNfse_httpwww_w3_org200009xmldsigSignature",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    # Attribute versao uses Python identifier versao
    __versao = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "versao"),
        "versao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcCancelamentoNfse_versao",
        _module_typeBindings.tsVersao,
        required=True,
    )
    __versao._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 631, 2
    )
    __versao._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 631, 2
    )

    versao = property(__versao.value, __versao.set, None, None)

    _ElementMap.update({__Confirmacao.name(): __Confirmacao, __Signature.name(): __Signature})
    _AttributeMap.update({__versao.name(): __versao})


_module_typeBindings.tcCancelamentoNfse = tcCancelamentoNfse
Namespace.addCategoryObject("typeBinding", "tcCancelamentoNfse", tcCancelamentoNfse)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcInfSubstituicaoNfse with content type ELEMENT_ONLY
class tcInfSubstituicaoNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcInfSubstituicaoNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcInfSubstituicaoNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 642, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NfseSubstituidora uses Python identifier NfseSubstituidora
    __NfseSubstituidora = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituidora"),
        "NfseSubstituidora",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfSubstituicaoNfse_httpwww_betha_com_bre_nota_contribuinte_wsNfseSubstituidora",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 644, 3
        ),
    )

    NfseSubstituidora = property(__NfseSubstituidora.value, __NfseSubstituidora.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcInfSubstituicaoNfse_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 647, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 647, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({__NfseSubstituidora.name(): __NfseSubstituidora})
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcInfSubstituicaoNfse = tcInfSubstituicaoNfse
Namespace.addCategoryObject("typeBinding", "tcInfSubstituicaoNfse", tcInfSubstituicaoNfse)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcSubstituicaoNfse with content type ELEMENT_ONLY
class tcSubstituicaoNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcSubstituicaoNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcSubstituicaoNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 650, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}SubstituicaoNfse uses Python identifier SubstituicaoNfse
    __SubstituicaoNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "SubstituicaoNfse"),
        "SubstituicaoNfse",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcSubstituicaoNfse_httpwww_betha_com_bre_nota_contribuinte_wsSubstituicaoNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 652, 3
        ),
    )

    SubstituicaoNfse = property(__SubstituicaoNfse.value, __SubstituicaoNfse.set, None, None)

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcSubstituicaoNfse_httpwww_w3_org200009xmldsigSignature",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    # Attribute versao uses Python identifier versao
    __versao = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "versao"),
        "versao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcSubstituicaoNfse_versao",
        _module_typeBindings.tsVersao,
        required=True,
    )
    __versao._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 657, 2
    )
    __versao._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 657, 2
    )

    versao = property(__versao.value, __versao.set, None, None)

    _ElementMap.update(
        {__SubstituicaoNfse.name(): __SubstituicaoNfse, __Signature.name(): __Signature}
    )
    _AttributeMap.update({__versao.name(): __versao})


_module_typeBindings.tcSubstituicaoNfse = tcSubstituicaoNfse
Namespace.addCategoryObject("typeBinding", "tcSubstituicaoNfse", tcSubstituicaoNfse)


# Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcLoteRps with content type ELEMENT_ONLY
class tcLoteRps(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.betha.com.br/e-nota-contribuinte-ws}tcLoteRps with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcLoteRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 693, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NumeroLote"),
        "NumeroLote",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcLoteRps_httpwww_betha_com_bre_nota_contribuinte_wsNumeroLote",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 695, 3
        ),
    )

    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}CpfCnpj uses Python identifier CpfCnpj
    __CpfCnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        "CpfCnpj",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcLoteRps_httpwww_betha_com_bre_nota_contribuinte_wsCpfCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 697, 3
        ),
    )

    CpfCnpj = property(__CpfCnpj.value, __CpfCnpj.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcLoteRps_httpwww_betha_com_bre_nota_contribuinte_wsInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 699, 3
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}QuantidadeRps uses Python identifier QuantidadeRps
    __QuantidadeRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "QuantidadeRps"),
        "QuantidadeRps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcLoteRps_httpwww_betha_com_bre_nota_contribuinte_wsQuantidadeRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 701, 3
        ),
    )

    QuantidadeRps = property(__QuantidadeRps.value, __QuantidadeRps.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}ListaRps uses Python identifier ListaRps
    __ListaRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaRps"),
        "ListaRps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcLoteRps_httpwww_betha_com_bre_nota_contribuinte_wsListaRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 703, 3
        ),
    )

    ListaRps = property(__ListaRps.value, __ListaRps.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcLoteRps_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 713, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 713, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    # Attribute versao uses Python identifier versao
    __versao = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "versao"),
        "versao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_tcLoteRps_versao",
        _module_typeBindings.tsVersao,
        required=True,
    )
    __versao._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 714, 2
    )
    __versao._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 714, 2
    )

    versao = property(__versao.value, __versao.set, None, None)

    _ElementMap.update(
        {
            __NumeroLote.name(): __NumeroLote,
            __CpfCnpj.name(): __CpfCnpj,
            __InscricaoMunicipal.name(): __InscricaoMunicipal,
            __QuantidadeRps.name(): __QuantidadeRps,
            __ListaRps.name(): __ListaRps,
        }
    )
    _AttributeMap.update({__Id.name(): __Id, __versao.name(): __versao})


_module_typeBindings.tcLoteRps = tcLoteRps
Namespace.addCategoryObject("typeBinding", "tcLoteRps", tcLoteRps)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 745, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}versaoDados uses Python identifier versaoDados
    __versaoDados = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "versaoDados"),
        "versaoDados",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_38_httpwww_betha_com_bre_nota_contribuinte_wsversaoDados",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 747, 4
        ),
    )

    versaoDados = property(__versaoDados.value, __versaoDados.set, None, None)

    # Attribute versao uses Python identifier versao
    __versao = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "versao"),
        "versao",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_38_versao",
        _module_typeBindings.tsVersao,
        required=True,
    )
    __versao._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 750, 3
    )
    __versao._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 750, 3
    )

    versao = property(__versao.value, __versao.set, None, None)

    _ElementMap.update({__versaoDados.name(): __versaoDados})
    _AttributeMap.update({__versao.name(): __versao})


_module_typeBindings.CTD_ANON_38 = CTD_ANON_38


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 872, 5
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Pedido uses Python identifier Pedido
    __Pedido = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Pedido"),
        "Pedido",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_39_httpwww_betha_com_bre_nota_contribuinte_wsPedido",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 874, 7
        ),
    )

    Pedido = property(__Pedido.value, __Pedido.set, None, None)

    # Element {http://www.betha.com.br/e-nota-contribuinte-ws}Rps uses Python identifier Rps
    __Rps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Rps"),
        "Rps",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_39_httpwww_betha_com_bre_nota_contribuinte_wsRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 875, 7
        ),
    )

    Rps = property(__Rps.value, __Rps.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_betha_com_bre_nota_contribuinte_ws_CTD_ANON_39_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 877, 6
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 877, 6
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({__Pedido.name(): __Pedido, __Rps.name(): __Rps})
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.CTD_ANON_39 = CTD_ANON_39


ListaMensagemRetornoLote = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetornoLote"),
    CTD_ANON_,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 717, 2
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ListaMensagemRetornoLote.name().localName(), ListaMensagemRetornoLote
)

ListaMensagemRetorno = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
    CTD_ANON_2,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ListaMensagemRetorno.name().localName(), ListaMensagemRetorno
)

ListaMensagemAlertaRetorno = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno"),
    CTD_ANON_3,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 735, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ListaMensagemAlertaRetorno.name().localName(), ListaMensagemAlertaRetorno
)

CompNfse = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
    tcCompNfse,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
    ),
)
Namespace.addCategoryObject("elementBinding", CompNfse.name().localName(), CompNfse)

EnviarLoteRpsEnvio = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "EnviarLoteRpsEnvio"),
    CTD_ANON_4,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 756, 2
    ),
)
Namespace.addCategoryObject(
    "elementBinding", EnviarLoteRpsEnvio.name().localName(), EnviarLoteRpsEnvio
)

EnviarLoteRpsResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "EnviarLoteRpsResposta"),
    CTD_ANON_5,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 766, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", EnviarLoteRpsResposta.name().localName(), EnviarLoteRpsResposta
)

EnviarLoteRpsSincronoEnvio = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "EnviarLoteRpsSincronoEnvio"),
    CTD_ANON_6,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 783, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", EnviarLoteRpsSincronoEnvio.name().localName(), EnviarLoteRpsSincronoEnvio
)

EnviarLoteRpsSincronoResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "EnviarLoteRpsSincronoResposta"),
    CTD_ANON_7,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 794, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding",
    EnviarLoteRpsSincronoResposta.name().localName(),
    EnviarLoteRpsSincronoResposta,
)

GerarNfseEnvio = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "GerarNfseEnvio"),
    CTD_ANON_9,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 822, 1
    ),
)
Namespace.addCategoryObject("elementBinding", GerarNfseEnvio.name().localName(), GerarNfseEnvio)

GerarNfseResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "GerarNfseResposta"),
    CTD_ANON_10,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 830, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", GerarNfseResposta.name().localName(), GerarNfseResposta
)

CancelarNfseEnvio = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "CancelarNfseEnvio"),
    CTD_ANON_12,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 850, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", CancelarNfseEnvio.name().localName(), CancelarNfseEnvio
)

CancelarNfseResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "CancelarNfseResposta"),
    CTD_ANON_13,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 858, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", CancelarNfseResposta.name().localName(), CancelarNfseResposta
)

SubstituirNfseEnvio = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "SubstituirNfseEnvio"),
    CTD_ANON_14,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 867, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", SubstituirNfseEnvio.name().localName(), SubstituirNfseEnvio
)

SubstituirNfseResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "SubstituirNfseResposta"),
    CTD_ANON_15,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 886, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", SubstituirNfseResposta.name().localName(), SubstituirNfseResposta
)

ConsultarLoteRpsEnvio = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarLoteRpsEnvio"),
    CTD_ANON_19,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 917, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ConsultarLoteRpsEnvio.name().localName(), ConsultarLoteRpsEnvio
)

ConsultarLoteRpsResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarLoteRpsResposta"),
    CTD_ANON_20,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 928, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ConsultarLoteRpsResposta.name().localName(), ConsultarLoteRpsResposta
)

ConsultarNfseRpsEnvio = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarNfseRpsEnvio"),
    CTD_ANON_22,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 951, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ConsultarNfseRpsEnvio.name().localName(), ConsultarNfseRpsEnvio
)

ConsultarNfseRpsResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarNfseRpsResposta"),
    CTD_ANON_23,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 962, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ConsultarNfseRpsResposta.name().localName(), ConsultarNfseRpsResposta
)

ConsultarNfseServicoPrestadoEnvio = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarNfseServicoPrestadoEnvio"),
    CTD_ANON_24,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 972, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding",
    ConsultarNfseServicoPrestadoEnvio.name().localName(),
    ConsultarNfseServicoPrestadoEnvio,
)

ConsultarNfseServicoPrestadoResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarNfseServicoPrestadoResposta"),
    CTD_ANON_27,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1012, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding",
    ConsultarNfseServicoPrestadoResposta.name().localName(),
    ConsultarNfseServicoPrestadoResposta,
)

ConsultarNfseServicoTomadoEnvio = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarNfseServicoTomadoEnvio"),
    CTD_ANON_29,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1029, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding",
    ConsultarNfseServicoTomadoEnvio.name().localName(),
    ConsultarNfseServicoTomadoEnvio,
)

ConsultarNfseServicoTomadoResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarNfseServicoTomadoResposta"),
    CTD_ANON_32,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1071, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding",
    ConsultarNfseServicoTomadoResposta.name().localName(),
    ConsultarNfseServicoTomadoResposta,
)

ConsultarNfseFaixaEnvio = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarNfseFaixaEnvio"),
    CTD_ANON_34,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1088, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ConsultarNfseFaixaEnvio.name().localName(), ConsultarNfseFaixaEnvio
)

ConsultarNfseFaixaResposta = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ConsultarNfseFaixaResposta"),
    CTD_ANON_36,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1108, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ConsultarNfseFaixaResposta.name().localName(), ConsultarNfseFaixaResposta
)

cabecalho = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "cabecalho"),
    CTD_ANON_38,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 744, 1
    ),
)
Namespace.addCategoryObject("elementBinding", cabecalho.name().localName(), cabecalho)


tcCpfCnpj._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Cpf"),
        tsCpf,
        scope=tcCpfCnpj,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 291, 3
        ),
    )
)

tcCpfCnpj._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Cnpj"),
        tsCnpj,
        scope=tcCpfCnpj,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 293, 3
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
        tcCpfCnpj._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Cpf")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 291, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcCpfCnpj._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Cnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 293, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcCpfCnpj._Automaton = _BuildAutomaton()


tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        tsEndereco,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 300, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        tsNumeroEndereco,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 302, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Complemento"),
        tsComplementoEndereco,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 304, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Bairro"),
        tsBairro,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 306, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        tsCodigoMunicipioIbge,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 308, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Uf"),
        tsUf,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 310, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoPais"),
        tsCodigoPaisBacen,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 312, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Cep"),
        tsCep,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 314, 3
        ),
    )
)


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 300, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 302, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 304, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 306, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 308, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 310, 3
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 312, 3
        ),
    )
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 314, 3
        ),
    )
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Endereco")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 300, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Numero")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 302, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Complemento")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 304, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Bairro")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 306, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 308, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Uf")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 310, 3
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoPais")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 312, 3
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Cep")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 314, 3
        ),
    )
    st_7 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_7, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


tcEndereco._Automaton = _BuildAutomaton_()


tcContato._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Telefone"),
        tsTelefone,
        scope=tcContato,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 321, 3
        ),
    )
)

tcContato._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Email"),
        tsEmail,
        scope=tcContato,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 323, 3
        ),
    )
)


def _BuildAutomaton_2():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 321, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 323, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcContato._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Telefone")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 321, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        tcContato._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Email")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 323, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


tcContato._Automaton = _BuildAutomaton_2()


tcIdentificacaoOrgaoGerador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        tsCodigoMunicipioIbge,
        scope=tcIdentificacaoOrgaoGerador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 330, 3
        ),
    )
)

tcIdentificacaoOrgaoGerador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Uf"),
        tsUf,
        scope=tcIdentificacaoOrgaoGerador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 332, 3
        ),
    )
)


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoOrgaoGerador._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 330, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoOrgaoGerador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Uf")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 332, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcIdentificacaoOrgaoGerador._Automaton = _BuildAutomaton_3()


tcIdentificacaoRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        tsNumeroRps,
        scope=tcIdentificacaoRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 339, 3
        ),
    )
)

tcIdentificacaoRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Serie"),
        tsSerieRps,
        scope=tcIdentificacaoRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 341, 3
        ),
    )
)

tcIdentificacaoRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Tipo"),
        tsTipoRps,
        scope=tcIdentificacaoRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 343, 3
        ),
    )
)


def _BuildAutomaton_4():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Numero")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 339, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Serie")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 341, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Tipo")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 343, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcIdentificacaoRps._Automaton = _BuildAutomaton_4()


tcIdentificacaoPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        tcCpfCnpj,
        scope=tcIdentificacaoPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 350, 3
        ),
    )
)

tcIdentificacaoPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcIdentificacaoPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 352, 3
        ),
    )
)


def _BuildAutomaton_5():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 350, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 352, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CpfCnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 350, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoPrestador._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 352, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


tcIdentificacaoPrestador._Automaton = _BuildAutomaton_5()


tcIdentificacaoTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        tcCpfCnpj,
        scope=tcIdentificacaoTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 359, 3
        ),
    )
)

tcIdentificacaoTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcIdentificacaoTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 361, 3
        ),
    )
)


def _BuildAutomaton_6():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 359, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 361, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CpfCnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 359, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoTomador._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 361, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


tcIdentificacaoTomador._Automaton = _BuildAutomaton_6()


tcIdentificacaoConsulente._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        tcCpfCnpj,
        scope=tcIdentificacaoConsulente,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 368, 3
        ),
    )
)

tcIdentificacaoConsulente._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcIdentificacaoConsulente,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 370, 3
        ),
    )
)


def _BuildAutomaton_7():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 370, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoConsulente._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CpfCnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 368, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoConsulente._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 370, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcIdentificacaoConsulente._Automaton = _BuildAutomaton_7()


tcIdentificacaoIntermediario._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        tcCpfCnpj,
        scope=tcIdentificacaoIntermediario,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 377, 15
        ),
    )
)

tcIdentificacaoIntermediario._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcIdentificacaoIntermediario,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 378, 14
        ),
    )
)


def _BuildAutomaton_8():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 377, 15
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 378, 14
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoIntermediario._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CpfCnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 377, 15
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoIntermediario._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 378, 14
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


tcIdentificacaoIntermediario._Automaton = _BuildAutomaton_8()


tcDadosTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoTomador"),
        tcIdentificacaoTomador,
        scope=tcDadosTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 384, 3
        ),
    )
)

tcDadosTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        tsRazaoSocial,
        scope=tcDadosTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 386, 3
        ),
    )
)

tcDadosTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        tcEndereco,
        scope=tcDadosTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 388, 3
        ),
    )
)

tcDadosTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Contato"),
        tcContato,
        scope=tcDadosTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 390, 3
        ),
    )
)


def _BuildAutomaton_9():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 384, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 386, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 388, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 390, 3
        ),
    )
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcDadosTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IdentificacaoTomador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 384, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        tcDadosTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "RazaoSocial")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 386, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        tcDadosTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Endereco")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 388, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        tcDadosTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Contato")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 390, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


tcDadosTomador._Automaton = _BuildAutomaton_9()


tcDadosIntermediario._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoIntermediario"),
        tcIdentificacaoIntermediario,
        scope=tcDadosIntermediario,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 397, 12
        ),
    )
)

tcDadosIntermediario._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        tsRazaoSocial,
        scope=tcDadosIntermediario,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 398, 12
        ),
    )
)


def _BuildAutomaton_10():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosIntermediario._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "IdentificacaoIntermediario")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 397, 12
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcDadosIntermediario._UseForTag(pyxb.namespace.ExpandedName(Namespace, "RazaoSocial")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 398, 12
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcDadosIntermediario._Automaton = _BuildAutomaton_10()


tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorServicos"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 404, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorDeducoes"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 406, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorPis"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 408, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorCofins"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 410, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorInss"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 412, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorIr"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 414, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorCsll"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 416, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "OutrasRetencoes"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 418, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorIss"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 420, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Aliquota"),
        tsAliquota,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 422, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DescontoIncondicionado"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 424, 3
        ),
    )
)

tcValoresDeclaracaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DescontoCondicionado"),
        tsValor,
        scope=tcValoresDeclaracaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 426, 3
        ),
    )
)


def _BuildAutomaton_11():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 406, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 408, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 410, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 412, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 414, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 416, 3
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 418, 3
        ),
    )
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 420, 3
        ),
    )
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 422, 3
        ),
    )
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 424, 3
        ),
    )
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 426, 3
        ),
    )
    counters.add(cc_10)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ValorServicos")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 404, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ValorDeducoes")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 406, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorPis")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 408, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ValorCofins")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 410, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorInss")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 412, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorIr")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 414, 3
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorCsll")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 416, 3
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "OutrasRetencoes")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 418, 3
        ),
    )
    st_7 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorIss")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 420, 3
        ),
    )
    st_8 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Aliquota")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 422, 3
        ),
    )
    st_9 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "DescontoIncondicionado")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 424, 3
        ),
    )
    st_10 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValoresDeclaracaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "DescontoCondicionado")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 426, 3
        ),
    )
    st_11 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    transitions.append(fac.Transition(st_8, []))
    transitions.append(fac.Transition(st_9, []))
    transitions.append(fac.Transition(st_10, []))
    transitions.append(fac.Transition(st_11, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_7, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_8, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_10, True)]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcValoresDeclaracaoServico._Automaton = _BuildAutomaton_11()


tcValoresNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "BaseCalculo"),
        tsValor,
        scope=tcValoresNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 433, 3
        ),
    )
)

tcValoresNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Aliquota"),
        tsAliquota,
        scope=tcValoresNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 435, 3
        ),
    )
)

tcValoresNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorIss"),
        tsValor,
        scope=tcValoresNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 437, 3
        ),
    )
)

tcValoresNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorLiquidoNfse"),
        tsValor,
        scope=tcValoresNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 439, 3
        ),
    )
)


def _BuildAutomaton_12():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 433, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 435, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 437, 3
        ),
    )
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcValoresNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "BaseCalculo")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 433, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcValoresNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Aliquota")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 435, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcValoresNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorIss")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 437, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcValoresNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorLiquidoNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 439, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcValoresNfse._Automaton = _BuildAutomaton_12()


tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Valores"),
        tcValoresDeclaracaoServico,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 446, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IssRetido"),
        tsSimNao,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 448, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ResponsavelRetencao"),
        tsResponsavelRetencao,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 450, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ItemListaServico"),
        tsItemListaServico,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 452, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoCnae"),
        tsCodigoCnae,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 454, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoTributacaoMunicipio"),
        tsCodigoTributacao,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 456, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Discriminacao"),
        tsDiscriminacao,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 458, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        tsCodigoMunicipioIbge,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 460, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoPais"),
        tsCodigoPaisBacen,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 462, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ExigibilidadeISS"),
        tsExigibilidadeISS,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 464, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "MunicipioIncidencia"),
        tsCodigoMunicipioIbge,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 466, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NumeroProcesso"),
        tsNumeroProcesso,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 468, 3
        ),
    )
)


def _BuildAutomaton_13():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 450, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 454, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 456, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 462, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 466, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 468, 3
        ),
    )
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Valores")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 446, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IssRetido")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 448, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ResponsavelRetencao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 450, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ItemListaServico")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 452, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoCnae")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 454, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CodigoTributacaoMunicipio")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 456, 3
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Discriminacao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 458, 3
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 460, 3
        ),
    )
    st_7 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoPais")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 462, 3
        ),
    )
    st_8 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ExigibilidadeISS")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 464, 3
        ),
    )
    st_9 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "MunicipioIncidencia")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 466, 3
        ),
    )
    st_10 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NumeroProcesso")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 468, 3
        ),
    )
    st_11 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    transitions.append(fac.Transition(st_6, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, []))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, []))
    transitions.append(fac.Transition(st_9, []))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_3, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, []))
    transitions.append(fac.Transition(st_11, []))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_4, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_5, True)]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcDadosServico._Automaton = _BuildAutomaton_13()


tcDadosConstrucaoCivil._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoObra"),
        tsCodigoObra,
        scope=tcDadosConstrucaoCivil,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 476, 3
        ),
    )
)

tcDadosConstrucaoCivil._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Art"),
        tsArt,
        scope=tcDadosConstrucaoCivil,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 478, 3
        ),
    )
)


def _BuildAutomaton_14():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 476, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosConstrucaoCivil._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoObra")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 476, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcDadosConstrucaoCivil._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Art")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 478, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcDadosConstrucaoCivil._Automaton = _BuildAutomaton_14()


tcDadosPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoPrestador"),
        tcIdentificacaoPrestador,
        scope=tcDadosPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 485, 3
        ),
    )
)

tcDadosPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        tsRazaoSocial,
        scope=tcDadosPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 487, 3
        ),
    )
)

tcDadosPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NomeFantasia"),
        tsNomeFantasia,
        scope=tcDadosPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 489, 3
        ),
    )
)

tcDadosPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        tcEndereco,
        scope=tcDadosPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 491, 3
        ),
    )
)

tcDadosPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Contato"),
        tcContato,
        scope=tcDadosPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 493, 3
        ),
    )
)


def _BuildAutomaton_15():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 489, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 493, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosPrestador._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "IdentificacaoPrestador")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 485, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "RazaoSocial")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 487, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NomeFantasia")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 489, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcDadosPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Endereco")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 491, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        tcDadosPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Contato")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 493, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcDadosPrestador._Automaton = _BuildAutomaton_15()


tcDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InfDeclaracaoPrestacaoServico"),
        tcInfDeclaracaoPrestacaoServico,
        scope=tcDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 540, 3
        ),
    )
)

tcDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=tcDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )
)


def _BuildAutomaton_16():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 542, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "InfDeclaracaoPrestacaoServico")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 540, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 542, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcDeclaracaoPrestacaoServico._Automaton = _BuildAutomaton_16()


tcIdentificacaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        tsNumeroNfse,
        scope=tcIdentificacaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 549, 3
        ),
    )
)

tcIdentificacaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        tcCpfCnpj,
        scope=tcIdentificacaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 551, 3
        ),
    )
)

tcIdentificacaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcIdentificacaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 553, 3
        ),
    )
)

tcIdentificacaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        tsCodigoMunicipioIbge,
        scope=tcIdentificacaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 555, 3
        ),
    )
)


def _BuildAutomaton_17():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 553, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Numero")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 549, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CpfCnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 551, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoNfse._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 553, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 555, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcIdentificacaoNfse._Automaton = _BuildAutomaton_17()


tcPedidoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InfPedidoCancelamento"),
        tcInfPedidoCancelamento,
        scope=tcPedidoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 607, 3
        ),
    )
)

tcPedidoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=tcPedidoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )
)


def _BuildAutomaton_18():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 609, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcPedidoCancelamento._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "InfPedidoCancelamento")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 607, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcPedidoCancelamento._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 609, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcPedidoCancelamento._Automaton = _BuildAutomaton_18()


tcRetCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseCancelamento"),
        tcCancelamentoNfse,
        scope=tcRetCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 636, 3
        ),
    )
)


def _BuildAutomaton_19():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcRetCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NfseCancelamento")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 636, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcRetCancelamento._Automaton = _BuildAutomaton_19()


tcCompNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Nfse"),
        tcNfse,
        scope=tcCompNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 662, 3
        ),
    )
)

tcCompNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseCancelamento"),
        tcCancelamentoNfse,
        scope=tcCompNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 664, 3
        ),
    )
)

tcCompNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituicao"),
        tcSubstituicaoNfse,
        scope=tcCompNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 666, 3
        ),
    )
)


def _BuildAutomaton_20():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 664, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 666, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcCompNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Nfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 662, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcCompNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NfseCancelamento")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 664, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        tcCompNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NfseSubstituicao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 666, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcCompNfse._Automaton = _BuildAutomaton_20()


tcMensagemRetorno._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Codigo"),
        tsCodigoMensagemAlerta,
        scope=tcMensagemRetorno,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 673, 3
        ),
    )
)

tcMensagemRetorno._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Mensagem"),
        tsDescricaoMensagemAlerta,
        scope=tcMensagemRetorno,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 675, 3
        ),
    )
)

tcMensagemRetorno._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Correcao"),
        tsDescricaoMensagemAlerta,
        scope=tcMensagemRetorno,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 677, 3
        ),
    )
)


def _BuildAutomaton_21():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 677, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcMensagemRetorno._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Codigo")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 673, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcMensagemRetorno._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Mensagem")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 675, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcMensagemRetorno._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Correcao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 677, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcMensagemRetorno._Automaton = _BuildAutomaton_21()


tcMensagemRetornoLote._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        tcIdentificacaoRps,
        scope=tcMensagemRetornoLote,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 684, 3
        ),
    )
)

tcMensagemRetornoLote._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Codigo"),
        tsCodigoMensagemAlerta,
        scope=tcMensagemRetornoLote,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 686, 3
        ),
    )
)

tcMensagemRetornoLote._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Mensagem"),
        tsDescricaoMensagemAlerta,
        scope=tcMensagemRetornoLote,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 688, 3
        ),
    )
)


def _BuildAutomaton_22():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcMensagemRetornoLote._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 684, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcMensagemRetornoLote._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Codigo")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 686, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcMensagemRetornoLote._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Mensagem")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 688, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcMensagemRetornoLote._Automaton = _BuildAutomaton_22()


CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Rps"),
        tcDeclaracaoPrestacaoServico,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 706, 6
        ),
    )
)


def _BuildAutomaton_23():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Rps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 706, 6
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, []))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON._Automaton = _BuildAutomaton_23()


CTD_ANON_._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno"),
        tcMensagemRetornoLote,
        scope=CTD_ANON_,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 720, 4
        ),
    )
)


def _BuildAutomaton_24():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 720, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, []))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_._Automaton = _BuildAutomaton_24()


CTD_ANON_2._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno"),
        tcMensagemRetorno,
        scope=CTD_ANON_2,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 729, 4
        ),
    )
)


def _BuildAutomaton_25():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 729, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, []))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_2._Automaton = _BuildAutomaton_25()


CTD_ANON_3._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno"),
        tcMensagemRetorno,
        scope=CTD_ANON_3,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 738, 4
        ),
    )
)


def _BuildAutomaton_26():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 738, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, []))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_3._Automaton = _BuildAutomaton_26()


CTD_ANON_4._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "LoteRps"),
        tcLoteRps,
        scope=CTD_ANON_4,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 759, 4
        ),
    )
)

CTD_ANON_4._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=CTD_ANON_4,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )
)


def _BuildAutomaton_27():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 760, 4
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, "LoteRps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 759, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 760, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_4._Automaton = _BuildAutomaton_27()


CTD_ANON_5._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        CTD_ANON_2,
        scope=CTD_ANON_5,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )
)

CTD_ANON_5._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NumeroLote"),
        tsNumeroLote,
        scope=CTD_ANON_5,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 770, 5
        ),
    )
)

CTD_ANON_5._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataRecebimento"),
        pyxb.binding.datatypes.dateTime,
        scope=CTD_ANON_5,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 772, 5
        ),
    )
)

CTD_ANON_5._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Protocolo"),
        tsNumeroProtocolo,
        scope=CTD_ANON_5,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 774, 5
        ),
    )
)


def _BuildAutomaton_28():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NumeroLote")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 770, 5
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataRecebimento")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 772, 5
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Protocolo")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 774, 5
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 777, 4
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_5._Automaton = _BuildAutomaton_28()


CTD_ANON_6._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "LoteRps"),
        tcLoteRps,
        scope=CTD_ANON_6,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 786, 4
        ),
    )
)

CTD_ANON_6._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=CTD_ANON_6,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )
)


def _BuildAutomaton_29():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 787, 4
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, "LoteRps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 786, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 787, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_6._Automaton = _BuildAutomaton_29()


CTD_ANON_7._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetornoLote"),
        CTD_ANON_,
        scope=CTD_ANON_7,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 717, 2
        ),
    )
)

CTD_ANON_7._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        CTD_ANON_2,
        scope=CTD_ANON_7,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )
)

CTD_ANON_7._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NumeroLote"),
        tsNumeroLote,
        scope=CTD_ANON_7,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 797, 4
        ),
    )
)

CTD_ANON_7._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataRecebimento"),
        pyxb.binding.datatypes.dateTime,
        scope=CTD_ANON_7,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 799, 4
        ),
    )
)

CTD_ANON_7._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Protocolo"),
        tsNumeroProtocolo,
        scope=CTD_ANON_7,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 801, 4
        ),
    )
)

CTD_ANON_7._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        CTD_ANON_8,
        scope=CTD_ANON_7,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 804, 5
        ),
    )
)


def _BuildAutomaton_30():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 797, 4
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 799, 4
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 801, 4
        ),
    )
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NumeroLote")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 797, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataRecebimento")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 799, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Protocolo")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 801, 4
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 804, 5
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 813, 5
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetornoLote")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 815, 5
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_7._Automaton = _BuildAutomaton_30()


CTD_ANON_8._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno"),
        CTD_ANON_3,
        scope=CTD_ANON_8,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 735, 1
        ),
    )
)

CTD_ANON_8._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        tcCompNfse,
        scope=CTD_ANON_8,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )
)


def _BuildAutomaton_31():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 809, 8
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CompNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 807, 8
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 809, 8
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, []))
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_8._Automaton = _BuildAutomaton_31()


CTD_ANON_9._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Rps"),
        tcDeclaracaoPrestacaoServico,
        scope=CTD_ANON_9,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 825, 4
        ),
    )
)


def _BuildAutomaton_32():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Rps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 825, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_9._Automaton = _BuildAutomaton_32()


CTD_ANON_10._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        CTD_ANON_2,
        scope=CTD_ANON_10,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )
)

CTD_ANON_10._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        CTD_ANON_11,
        scope=CTD_ANON_10,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 834, 5
        ),
    )
)


def _BuildAutomaton_33():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 834, 5
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 843, 5
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_10._Automaton = _BuildAutomaton_33()


CTD_ANON_11._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno"),
        CTD_ANON_3,
        scope=CTD_ANON_11,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 735, 1
        ),
    )
)

CTD_ANON_11._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        tcCompNfse,
        scope=CTD_ANON_11,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )
)


def _BuildAutomaton_34():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 839, 8
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CompNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 837, 8
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_11._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 839, 8
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_11._Automaton = _BuildAutomaton_34()


CTD_ANON_12._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Pedido"),
        tcPedidoCancelamento,
        scope=CTD_ANON_12,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 853, 4
        ),
    )
)


def _BuildAutomaton_35():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Pedido")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 853, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_12._Automaton = _BuildAutomaton_35()


CTD_ANON_13._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        CTD_ANON_2,
        scope=CTD_ANON_13,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )
)

CTD_ANON_13._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RetCancelamento"),
        tcRetCancelamento,
        scope=CTD_ANON_13,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 861, 4
        ),
    )
)


def _BuildAutomaton_36():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, "RetCancelamento")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 861, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 862, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_13._Automaton = _BuildAutomaton_36()


CTD_ANON_14._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "SubstituicaoNfse"),
        CTD_ANON_39,
        scope=CTD_ANON_14,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 870, 4
        ),
    )
)

CTD_ANON_14._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=CTD_ANON_14,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )
)


def _BuildAutomaton_37():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 880, 4
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, "SubstituicaoNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 870, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 880, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_14._Automaton = _BuildAutomaton_37()


CTD_ANON_15._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        CTD_ANON_2,
        scope=CTD_ANON_15,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )
)

CTD_ANON_15._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RetSubstituicao"),
        CTD_ANON_16,
        scope=CTD_ANON_15,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 889, 5
        ),
    )
)


def _BuildAutomaton_38():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, "RetSubstituicao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 889, 5
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 912, 5
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_15._Automaton = _BuildAutomaton_38()


CTD_ANON_16._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituida"),
        CTD_ANON_17,
        scope=CTD_ANON_16,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 892, 8
        ),
    )
)

CTD_ANON_16._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituidora"),
        CTD_ANON_18,
        scope=CTD_ANON_16,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 901, 8
        ),
    )
)


def _BuildAutomaton_39():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NfseSubstituida")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 892, 8
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NfseSubstituidora")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 901, 8
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_16._Automaton = _BuildAutomaton_39()


CTD_ANON_17._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno"),
        CTD_ANON_3,
        scope=CTD_ANON_17,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 735, 1
        ),
    )
)

CTD_ANON_17._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        tcCompNfse,
        scope=CTD_ANON_17,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )
)


def _BuildAutomaton_40():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 897, 11
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CompNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 895, 11
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_17._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 897, 11
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_17._Automaton = _BuildAutomaton_40()


CTD_ANON_18._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        tcCompNfse,
        scope=CTD_ANON_18,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )
)


def _BuildAutomaton_41():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CompNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 904, 11
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_18._Automaton = _BuildAutomaton_41()


CTD_ANON_19._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        tcIdentificacaoPrestador,
        scope=CTD_ANON_19,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 920, 4
        ),
    )
)

CTD_ANON_19._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Protocolo"),
        tsNumeroProtocolo,
        scope=CTD_ANON_19,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 922, 4
        ),
    )
)


def _BuildAutomaton_42():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Prestador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 920, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Protocolo")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 922, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_19._Automaton = _BuildAutomaton_42()


CTD_ANON_20._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetornoLote"),
        CTD_ANON_,
        scope=CTD_ANON_20,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 717, 2
        ),
    )
)

CTD_ANON_20._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        CTD_ANON_2,
        scope=CTD_ANON_20,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )
)

CTD_ANON_20._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Situacao"),
        tsSituacaoLoteRps,
        scope=CTD_ANON_20,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 931, 11
        ),
    )
)

CTD_ANON_20._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        CTD_ANON_21,
        scope=CTD_ANON_20,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 933, 4
        ),
    )
)


def _BuildAutomaton_43():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Situacao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 931, 11
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 933, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 942, 4
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetornoLote")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 944, 4
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_20._Automaton = _BuildAutomaton_43()


CTD_ANON_21._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno"),
        CTD_ANON_3,
        scope=CTD_ANON_21,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 735, 1
        ),
    )
)

CTD_ANON_21._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        tcCompNfse,
        scope=CTD_ANON_21,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )
)


def _BuildAutomaton_44():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=1,
        max=50,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 936, 7
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 938, 7
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CompNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 936, 7
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_21._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ListaMensagemAlertaRetorno")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 938, 7
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_21._Automaton = _BuildAutomaton_44()


CTD_ANON_22._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        tcIdentificacaoRps,
        scope=CTD_ANON_22,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 954, 4
        ),
    )
)

CTD_ANON_22._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        tcIdentificacaoPrestador,
        scope=CTD_ANON_22,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 956, 4
        ),
    )
)


def _BuildAutomaton_45():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 954, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Prestador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 956, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_22._Automaton = _BuildAutomaton_45()


CTD_ANON_23._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        CTD_ANON_2,
        scope=CTD_ANON_23,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )
)

CTD_ANON_23._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        tcCompNfse,
        scope=CTD_ANON_23,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )
)


def _BuildAutomaton_46():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CompNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 965, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 966, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_23._Automaton = _BuildAutomaton_46()


CTD_ANON_24._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        tcIdentificacaoPrestador,
        scope=CTD_ANON_24,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 975, 4
        ),
    )
)

CTD_ANON_24._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NumeroNfse"),
        tsNumeroNfse,
        scope=CTD_ANON_24,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 977, 4
        ),
    )
)

CTD_ANON_24._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "PeriodoEmissao"),
        CTD_ANON_25,
        scope=CTD_ANON_24,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 980, 5
        ),
    )
)

CTD_ANON_24._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "PeriodoCompetencia"),
        CTD_ANON_26,
        scope=CTD_ANON_24,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 991, 5
        ),
    )
)

CTD_ANON_24._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Tomador"),
        tcIdentificacaoTomador,
        scope=CTD_ANON_24,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1003, 4
        ),
    )
)

CTD_ANON_24._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Intermediario"),
        tcIdentificacaoIntermediario,
        scope=CTD_ANON_24,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1005, 4
        ),
    )
)

CTD_ANON_24._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Pagina"),
        tsPagina,
        scope=CTD_ANON_24,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1007, 4
        ),
    )
)


def _BuildAutomaton_47():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 977, 4
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 980, 5
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 991, 5
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1003, 4
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1005, 4
        ),
    )
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Prestador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 975, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NumeroNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 977, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, "PeriodoEmissao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 980, 5
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, "PeriodoCompetencia")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 991, 5
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Tomador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1003, 4
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Intermediario")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1005, 4
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Pagina")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1007, 4
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    transitions.append(fac.Transition(st_6, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_24._Automaton = _BuildAutomaton_47()


CTD_ANON_25._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataInicial"),
        pyxb.binding.datatypes.date,
        scope=CTD_ANON_25,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 984, 8
        ),
    )
)

CTD_ANON_25._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataFinal"),
        pyxb.binding.datatypes.date,
        scope=CTD_ANON_25,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 986, 8
        ),
    )
)


def _BuildAutomaton_48():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataInicial")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 984, 8
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataFinal")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 986, 8
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_25._Automaton = _BuildAutomaton_48()


CTD_ANON_26._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataInicial"),
        pyxb.binding.datatypes.date,
        scope=CTD_ANON_26,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 995, 8
        ),
    )
)

CTD_ANON_26._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataFinal"),
        pyxb.binding.datatypes.date,
        scope=CTD_ANON_26,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 997, 8
        ),
    )
)


def _BuildAutomaton_49():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataInicial")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 995, 8
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataFinal")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 997, 8
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_26._Automaton = _BuildAutomaton_49()


CTD_ANON_27._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        CTD_ANON_2,
        scope=CTD_ANON_27,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )
)

CTD_ANON_27._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        CTD_ANON_28,
        scope=CTD_ANON_27,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1015, 4
        ),
    )
)


def _BuildAutomaton_50():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1015, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1023, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_27._Automaton = _BuildAutomaton_50()


CTD_ANON_28._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        tcCompNfse,
        scope=CTD_ANON_28,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )
)

CTD_ANON_28._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ProximaPagina"),
        tsPagina,
        scope=CTD_ANON_28,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1019, 7
        ),
    )
)


def _BuildAutomaton_51():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=1,
        max=50,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1018, 7
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1019, 7
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CompNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1018, 7
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ProximaPagina")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1019, 7
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_28._Automaton = _BuildAutomaton_51()


CTD_ANON_29._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Consulente"),
        tcIdentificacaoConsulente,
        scope=CTD_ANON_29,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1032, 4
        ),
    )
)

CTD_ANON_29._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NumeroNfse"),
        tsNumeroNfse,
        scope=CTD_ANON_29,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1034, 4
        ),
    )
)

CTD_ANON_29._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "PeriodoEmissao"),
        CTD_ANON_30,
        scope=CTD_ANON_29,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1037, 5
        ),
    )
)

CTD_ANON_29._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "PeriodoCompetencia"),
        CTD_ANON_31,
        scope=CTD_ANON_29,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1048, 5
        ),
    )
)

CTD_ANON_29._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        tcIdentificacaoPrestador,
        scope=CTD_ANON_29,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1060, 4
        ),
    )
)

CTD_ANON_29._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Tomador"),
        tcIdentificacaoTomador,
        scope=CTD_ANON_29,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1062, 4
        ),
    )
)

CTD_ANON_29._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Intermediario"),
        tcIdentificacaoIntermediario,
        scope=CTD_ANON_29,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1064, 4
        ),
    )
)

CTD_ANON_29._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Pagina"),
        tsPagina,
        scope=CTD_ANON_29,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1066, 4
        ),
    )
)


def _BuildAutomaton_52():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1034, 4
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1037, 5
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1048, 5
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1060, 4
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1062, 4
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1064, 4
        ),
    )
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Consulente")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1032, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NumeroNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1034, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, "PeriodoEmissao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1037, 5
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, "PeriodoCompetencia")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1048, 5
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Prestador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1060, 4
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Tomador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1062, 4
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Intermediario")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1064, 4
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Pagina")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1066, 4
        ),
    )
    st_7 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_29._Automaton = _BuildAutomaton_52()


CTD_ANON_30._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataInicial"),
        pyxb.binding.datatypes.date,
        scope=CTD_ANON_30,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1041, 8
        ),
    )
)

CTD_ANON_30._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataFinal"),
        pyxb.binding.datatypes.date,
        scope=CTD_ANON_30,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1043, 8
        ),
    )
)


def _BuildAutomaton_53():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataInicial")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1041, 8
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataFinal")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1043, 8
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_30._Automaton = _BuildAutomaton_53()


CTD_ANON_31._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataInicial"),
        pyxb.binding.datatypes.date,
        scope=CTD_ANON_31,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1052, 8
        ),
    )
)

CTD_ANON_31._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataFinal"),
        pyxb.binding.datatypes.date,
        scope=CTD_ANON_31,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1054, 8
        ),
    )
)


def _BuildAutomaton_54():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataInicial")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1052, 8
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataFinal")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1054, 8
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_31._Automaton = _BuildAutomaton_54()


CTD_ANON_32._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        CTD_ANON_2,
        scope=CTD_ANON_32,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )
)

CTD_ANON_32._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        CTD_ANON_33,
        scope=CTD_ANON_32,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1074, 4
        ),
    )
)


def _BuildAutomaton_55():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1074, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1082, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_32._Automaton = _BuildAutomaton_55()


CTD_ANON_33._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        tcCompNfse,
        scope=CTD_ANON_33,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )
)

CTD_ANON_33._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ProximaPagina"),
        tsPagina,
        scope=CTD_ANON_33,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1078, 7
        ),
    )
)


def _BuildAutomaton_56():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=1,
        max=50,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1077, 7
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1078, 7
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CompNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1077, 7
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ProximaPagina")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1078, 7
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_33._Automaton = _BuildAutomaton_56()


CTD_ANON_34._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        tcIdentificacaoPrestador,
        scope=CTD_ANON_34,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1091, 4
        ),
    )
)

CTD_ANON_34._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Faixa"),
        CTD_ANON_35,
        scope=CTD_ANON_34,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1093, 4
        ),
    )
)

CTD_ANON_34._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Pagina"),
        tsPagina,
        scope=CTD_ANON_34,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1103, 4
        ),
    )
)


def _BuildAutomaton_57():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Prestador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1091, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Faixa")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1093, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Pagina")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1103, 4
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_34._Automaton = _BuildAutomaton_57()


CTD_ANON_35._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NumeroNfseInicial"),
        tsNumeroNfse,
        scope=CTD_ANON_35,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1096, 7
        ),
    )
)

CTD_ANON_35._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NumeroNfseFinal"),
        tsNumeroNfse,
        scope=CTD_ANON_35,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1098, 7
        ),
    )
)


def _BuildAutomaton_58():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1098, 7
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NumeroNfseInicial")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1096, 7
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NumeroNfseFinal")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1098, 7
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_35._Automaton = _BuildAutomaton_58()


CTD_ANON_36._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
        CTD_ANON_2,
        scope=CTD_ANON_36,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 726, 1
        ),
    )
)

CTD_ANON_36._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaNfse"),
        CTD_ANON_37,
        scope=CTD_ANON_36,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1111, 4
        ),
    )
)


def _BuildAutomaton_59():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1111, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1119, 4
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_36._Automaton = _BuildAutomaton_59()


CTD_ANON_37._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompNfse"),
        tcCompNfse,
        scope=CTD_ANON_37,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 754, 1
        ),
    )
)

CTD_ANON_37._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ProximaPagina"),
        tsPagina,
        scope=CTD_ANON_37,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1115, 7
        ),
    )
)


def _BuildAutomaton_60():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=1,
        max=50,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1114, 7
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1115, 7
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CompNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1114, 7
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ProximaPagina")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 1115, 7
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_37._Automaton = _BuildAutomaton_60()


tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        tcIdentificacaoRps,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 500, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataEmissao"),
        pyxb.binding.datatypes.date,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 502, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Status"),
        tsStatusRps,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 504, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RpsSubstituido"),
        tcIdentificacaoRps,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 506, 3
        ),
    )
)


def _BuildAutomaton_61():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 506, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 500, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataEmissao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 502, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Status")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 504, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "RpsSubstituido")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 506, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcInfRps._Automaton = _BuildAutomaton_61()


tcInfDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Rps"),
        tcInfRps,
        scope=tcInfDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 514, 3
        ),
    )
)

tcInfDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Competencia"),
        pyxb.binding.datatypes.date,
        scope=tcInfDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 516, 3
        ),
    )
)

tcInfDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Servico"),
        tcDadosServico,
        scope=tcInfDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 518, 3
        ),
    )
)

tcInfDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        tcIdentificacaoPrestador,
        scope=tcInfDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 520, 3
        ),
    )
)

tcInfDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Tomador"),
        tcDadosTomador,
        scope=tcInfDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 522, 3
        ),
    )
)

tcInfDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Intermediario"),
        tcDadosIntermediario,
        scope=tcInfDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 524, 3
        ),
    )
)

tcInfDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ConstrucaoCivil"),
        tcDadosConstrucaoCivil,
        scope=tcInfDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 526, 3
        ),
    )
)

tcInfDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RegimeEspecialTributacao"),
        tsRegimeEspecialTributacao,
        scope=tcInfDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 528, 3
        ),
    )
)

tcInfDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "OptanteSimplesNacional"),
        tsSimNao,
        scope=tcInfDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 530, 3
        ),
    )
)

tcInfDeclaracaoPrestacaoServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IncentivoFiscal"),
        tsSimNao,
        scope=tcInfDeclaracaoPrestacaoServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 532, 3
        ),
    )
)


def _BuildAutomaton_62():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 514, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 522, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 524, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 526, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 528, 3
        ),
    )
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfDeclaracaoPrestacaoServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Rps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 514, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Competencia")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 516, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Servico")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 518, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Prestador")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 520, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Tomador")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 522, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Intermediario")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 524, 3
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ConstrucaoCivil")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 526, 3
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "RegimeEspecialTributacao")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 528, 3
        ),
    )
    st_7 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "OptanteSimplesNacional")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 530, 3
        ),
    )
    st_8 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcInfDeclaracaoPrestacaoServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "IncentivoFiscal")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 532, 3
        ),
    )
    st_9 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    transitions.append(fac.Transition(st_8, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_1, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_2, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_4, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, []))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcInfDeclaracaoPrestacaoServico._Automaton = _BuildAutomaton_62()


tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        tsNumeroNfse,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 562, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoVerificacao"),
        tsCodigoVerificacao,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 564, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataEmissao"),
        pyxb.binding.datatypes.dateTime,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 566, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituida"),
        tsNumeroNfse,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 568, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "OutrasInformacoes"),
        tsOutrasInformacoes,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 570, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValoresNfse"),
        tcValoresNfse,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 572, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorCredito"),
        tsValor,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 574, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "PrestadorServico"),
        tcDadosPrestador,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 576, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "OrgaoGerador"),
        tcIdentificacaoOrgaoGerador,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 578, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DeclaracaoPrestacaoServico"),
        tcDeclaracaoPrestacaoServico,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 580, 3
        ),
    )
)


def _BuildAutomaton_63():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 568, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 570, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 574, 3
        ),
    )
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Numero")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 562, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoVerificacao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 564, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataEmissao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 566, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NfseSubstituida")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 568, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "OutrasInformacoes")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 570, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValoresNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 572, 3
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorCredito")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 574, 3
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "PrestadorServico")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 576, 3
        ),
    )
    st_7 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "OrgaoGerador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 578, 3
        ),
    )
    st_8 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DeclaracaoPrestacaoServico")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 580, 3
        ),
    )
    st_9 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, []))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, []))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcInfNfse._Automaton = _BuildAutomaton_63()


tcNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InfNfse"),
        tcInfNfse,
        scope=tcNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 587, 3
        ),
    )
)

tcNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=tcNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )
)


def _BuildAutomaton_64():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 589, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "InfNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 587, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcNfse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 589, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcNfse._Automaton = _BuildAutomaton_64()


tcInfPedidoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoNfse"),
        tcIdentificacaoNfse,
        scope=tcInfPedidoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 597, 3
        ),
    )
)

tcInfPedidoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoCancelamento"),
        tsCodigoCancelamentoNfse,
        scope=tcInfPedidoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 599, 3
        ),
    )
)


def _BuildAutomaton_65():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 599, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcInfPedidoCancelamento._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "IdentificacaoNfse")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 597, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcInfPedidoCancelamento._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CodigoCancelamento")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 599, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcInfPedidoCancelamento._Automaton = _BuildAutomaton_65()


tcConfirmacaoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Pedido"),
        tcPedidoCancelamento,
        scope=tcConfirmacaoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 616, 3
        ),
    )
)

tcConfirmacaoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataHora"),
        pyxb.binding.datatypes.dateTime,
        scope=tcConfirmacaoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 618, 3
        ),
    )
)


def _BuildAutomaton_66():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcConfirmacaoCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Pedido")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 616, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcConfirmacaoCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataHora")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 618, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcConfirmacaoCancelamento._Automaton = _BuildAutomaton_66()


tcCancelamentoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Confirmacao"),
        tcConfirmacaoCancelamento,
        scope=tcCancelamentoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 626, 3
        ),
    )
)

tcCancelamentoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=tcCancelamentoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )
)


def _BuildAutomaton_67():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 628, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcCancelamentoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Confirmacao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 626, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcCancelamentoNfse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 628, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcCancelamentoNfse._Automaton = _BuildAutomaton_67()


tcInfSubstituicaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituidora"),
        tsNumeroNfse,
        scope=tcInfSubstituicaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 644, 3
        ),
    )
)


def _BuildAutomaton_68():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcInfSubstituicaoNfse._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "NfseSubstituidora")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 644, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcInfSubstituicaoNfse._Automaton = _BuildAutomaton_68()


tcSubstituicaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "SubstituicaoNfse"),
        tcInfSubstituicaoNfse,
        scope=tcSubstituicaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 652, 3
        ),
    )
)

tcSubstituicaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=tcSubstituicaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/xmldsig-core-schema20020212.xsd", 41, 0
        ),
    )
)


def _BuildAutomaton_69():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=2,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 654, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcSubstituicaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "SubstituicaoNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 652, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcSubstituicaoNfse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 654, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcSubstituicaoNfse._Automaton = _BuildAutomaton_69()


tcLoteRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NumeroLote"),
        tsNumeroLote,
        scope=tcLoteRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 695, 3
        ),
    )
)

tcLoteRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        tcCpfCnpj,
        scope=tcLoteRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 697, 3
        ),
    )
)

tcLoteRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcLoteRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 699, 3
        ),
    )
)

tcLoteRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "QuantidadeRps"),
        tsQuantidadeRps,
        scope=tcLoteRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 701, 3
        ),
    )
)

tcLoteRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaRps"),
        CTD_ANON,
        scope=tcLoteRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 703, 3
        ),
    )
)


def _BuildAutomaton_70():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 699, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NumeroLote")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 695, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CpfCnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 697, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 699, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "QuantidadeRps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 701, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ListaRps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 703, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcLoteRps._Automaton = _BuildAutomaton_70()


CTD_ANON_38._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "versaoDados"),
        tsVersao,
        scope=CTD_ANON_38,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 747, 4
        ),
    )
)


def _BuildAutomaton_71():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, "versaoDados")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 747, 4
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_38._Automaton = _BuildAutomaton_71()


CTD_ANON_39._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Pedido"),
        tcPedidoCancelamento,
        scope=CTD_ANON_39,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 874, 7
        ),
    )
)

CTD_ANON_39._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Rps"),
        tcDeclaracaoPrestacaoServico,
        scope=CTD_ANON_39,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 875, 7
        ),
    )
)


def _BuildAutomaton_72():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Pedido")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 874, 7
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Rps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Betha/nfse_v202.xsd", 875, 7
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_39._Automaton = _BuildAutomaton_72()
