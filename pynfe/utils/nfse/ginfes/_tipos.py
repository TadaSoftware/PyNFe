# flake8: noqa
# pynfe/utils/nfse/ginfes/_tipos.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:13a1074f1cd8519d51c94b3829c0b2dd82c01391
# Generated 2025-04-06 00:00:53.122662 by PyXB version 1.2.6 using Python 3.12.9.final.0
# Namespace http://www.ginfes.com.br/tipos_v03.xsd [xmlns:tipos]

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
    "urn:uuid:9559ba2f-ca50-4313-910d-fe9d437f0e44"
)

# Version of PyXB used to generate the bindings
_PyXBVersion = "1.2.6"

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
from pynfe.utils.nfse.ginfes import _dsig as _ImportedBinding__dsig
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    "http://www.ginfes.com.br/tipos_v03.xsd", create_if_missing=True
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsNumeroNfse
class tsNumeroNfse(pyxb.binding.datatypes.nonNegativeInteger):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 4, 1
    )
    _Documentation = None


tsNumeroNfse._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(15)
)
tsNumeroNfse._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsNumeroNfse._InitializeFacetMap(tsNumeroNfse._CF_totalDigits, tsNumeroNfse._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsNumeroNfse", tsNumeroNfse)
_module_typeBindings.tsNumeroNfse = tsNumeroNfse


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsCodigoVerificacao
class tsCodigoVerificacao(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoVerificacao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 10, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsStatusRps
class tsStatusRps(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsStatusRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 17, 1
    )
    _Documentation = None


tsStatusRps._CF_pattern = pyxb.binding.facets.CF_pattern()
tsStatusRps._CF_pattern.addPattern(pattern="1|2")
tsStatusRps._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsStatusRps._InitializeFacetMap(tsStatusRps._CF_pattern, tsStatusRps._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsStatusRps", tsStatusRps)
_module_typeBindings.tsStatusRps = tsStatusRps


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsStatusNfse
class tsStatusNfse(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsStatusNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 23, 1
    )
    _Documentation = None


tsStatusNfse._CF_pattern = pyxb.binding.facets.CF_pattern()
tsStatusNfse._CF_pattern.addPattern(pattern="1|2")
tsStatusNfse._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsStatusNfse._InitializeFacetMap(tsStatusNfse._CF_pattern, tsStatusNfse._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsStatusNfse", tsStatusNfse)
_module_typeBindings.tsStatusNfse = tsStatusNfse


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsNaturezaOperacao
class tsNaturezaOperacao(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNaturezaOperacao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 29, 1
    )
    _Documentation = None


tsNaturezaOperacao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsNaturezaOperacao._CF_pattern.addPattern(pattern="1|2|3|4|5|6")
tsNaturezaOperacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsNaturezaOperacao._InitializeFacetMap(
    tsNaturezaOperacao._CF_pattern, tsNaturezaOperacao._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsNaturezaOperacao", tsNaturezaOperacao)
_module_typeBindings.tsNaturezaOperacao = tsNaturezaOperacao


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsRegimeEspecialTributacao
class tsRegimeEspecialTributacao(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsRegimeEspecialTributacao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 35, 1
    )
    _Documentation = None


tsRegimeEspecialTributacao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsRegimeEspecialTributacao._CF_pattern.addPattern(pattern="1|2|3|4|5|6")
tsRegimeEspecialTributacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsRegimeEspecialTributacao._InitializeFacetMap(
    tsRegimeEspecialTributacao._CF_pattern, tsRegimeEspecialTributacao._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsRegimeEspecialTributacao", tsRegimeEspecialTributacao)
_module_typeBindings.tsRegimeEspecialTributacao = tsRegimeEspecialTributacao


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsSimNao
class tsSimNao(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsSimNao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 41, 1
    )
    _Documentation = None


tsSimNao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsSimNao._CF_pattern.addPattern(pattern="1|2")
tsSimNao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsSimNao._InitializeFacetMap(tsSimNao._CF_pattern, tsSimNao._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsSimNao", tsSimNao)
_module_typeBindings.tsSimNao = tsSimNao


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsNumeroRps
class tsNumeroRps(pyxb.binding.datatypes.nonNegativeInteger):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 47, 1
    )
    _Documentation = None


tsNumeroRps._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(15)
)
tsNumeroRps._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsNumeroRps._InitializeFacetMap(tsNumeroRps._CF_totalDigits, tsNumeroRps._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsNumeroRps", tsNumeroRps)
_module_typeBindings.tsNumeroRps = tsNumeroRps


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsSerieRps
class tsSerieRps(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsSerieRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 53, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsTipoRps
class tsTipoRps(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsTipoRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 60, 1
    )
    _Documentation = None


tsTipoRps._CF_pattern = pyxb.binding.facets.CF_pattern()
tsTipoRps._CF_pattern.addPattern(pattern="1|2|3")
tsTipoRps._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsTipoRps._InitializeFacetMap(tsTipoRps._CF_pattern, tsTipoRps._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsTipoRps", tsTipoRps)
_module_typeBindings.tsTipoRps = tsTipoRps


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsOutrasInformacoes
class tsOutrasInformacoes(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsOutrasInformacoes")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 66, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsValor
class tsValor(pyxb.binding.datatypes.decimal):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsValor")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 73, 1
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
tsValor._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsValor._InitializeFacetMap(
    tsValor._CF_fractionDigits,
    tsValor._CF_minInclusive,
    tsValor._CF_totalDigits,
    tsValor._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsValor", tsValor)
_module_typeBindings.tsValor = tsValor


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsItemListaServico
class tsItemListaServico(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsItemListaServico")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 81, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsCodigoCnae
class tsCodigoCnae(pyxb.binding.datatypes.int):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoCnae")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 88, 1
    )
    _Documentation = None


tsCodigoCnae._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(7)
)
tsCodigoCnae._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCodigoCnae._InitializeFacetMap(tsCodigoCnae._CF_totalDigits, tsCodigoCnae._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsCodigoCnae", tsCodigoCnae)
_module_typeBindings.tsCodigoCnae = tsCodigoCnae


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsCodigoTributacao
class tsCodigoTributacao(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoTributacao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 94, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsAliquota
class tsAliquota(pyxb.binding.datatypes.decimal):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsAliquota")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 101, 1
    )
    _Documentation = None


tsAliquota._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(
    value=pyxb.binding.datatypes.nonNegativeInteger(4)
)
tsAliquota._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(
    value=pyxb.binding.datatypes.decimal("0.0"), value_datatype=tsAliquota
)
tsAliquota._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(5)
)
tsAliquota._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsAliquota._InitializeFacetMap(
    tsAliquota._CF_fractionDigits,
    tsAliquota._CF_minInclusive,
    tsAliquota._CF_totalDigits,
    tsAliquota._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsAliquota", tsAliquota)
_module_typeBindings.tsAliquota = tsAliquota


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsDiscriminacao
class tsDiscriminacao(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsDiscriminacao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 109, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsCodigoMunicipioIbge
class tsCodigoMunicipioIbge(pyxb.binding.datatypes.int):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoMunicipioIbge")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 116, 1
    )
    _Documentation = None


tsCodigoMunicipioIbge._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(7)
)
tsCodigoMunicipioIbge._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCodigoMunicipioIbge._InitializeFacetMap(
    tsCodigoMunicipioIbge._CF_totalDigits, tsCodigoMunicipioIbge._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsCodigoMunicipioIbge", tsCodigoMunicipioIbge)
_module_typeBindings.tsCodigoMunicipioIbge = tsCodigoMunicipioIbge


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsInscricaoMunicipal
class tsInscricaoMunicipal(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsInscricaoMunicipal")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 122, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsRazaoSocial
class tsRazaoSocial(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsRazaoSocial")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 129, 1
    )
    _Documentation = None


tsRazaoSocial._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(115)
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsNomeFantasia
class tsNomeFantasia(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNomeFantasia")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 136, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsCnpj
class tsCnpj(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCnpj")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 143, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsEndereco
class tsEndereco(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsEndereco")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 149, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsNumeroEndereco
class tsNumeroEndereco(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroEndereco")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 156, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsComplementoEndereco
class tsComplementoEndereco(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsComplementoEndereco")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 163, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsBairro
class tsBairro(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsBairro")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 170, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsUf
class tsUf(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsUf")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 177, 1
    )
    _Documentation = None


tsUf._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tsUf._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsUf._InitializeFacetMap(tsUf._CF_length, tsUf._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsUf", tsUf)
_module_typeBindings.tsUf = tsUf


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsCep
class tsCep(pyxb.binding.datatypes.int):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCep")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 183, 1
    )
    _Documentation = None


tsCep._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(8)
)
tsCep._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCep._InitializeFacetMap(tsCep._CF_totalDigits, tsCep._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsCep", tsCep)
_module_typeBindings.tsCep = tsCep


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsEmail
class tsEmail(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsEmail")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 189, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsTelefone
class tsTelefone(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsTelefone")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 196, 1
    )
    _Documentation = None


tsTelefone._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(11)
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsCpf
class tsCpf(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCpf")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 203, 1
    )
    _Documentation = None


tsCpf._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(11)
)
tsCpf._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCpf._InitializeFacetMap(tsCpf._CF_length, tsCpf._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsCpf", tsCpf)
_module_typeBindings.tsCpf = tsCpf


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsIndicacaoCpfCnpj
class tsIndicacaoCpfCnpj(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsIndicacaoCpfCnpj")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 209, 1
    )
    _Documentation = None


tsIndicacaoCpfCnpj._CF_pattern = pyxb.binding.facets.CF_pattern()
tsIndicacaoCpfCnpj._CF_pattern.addPattern(pattern="1|2|3")
tsIndicacaoCpfCnpj._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsIndicacaoCpfCnpj._InitializeFacetMap(
    tsIndicacaoCpfCnpj._CF_pattern, tsIndicacaoCpfCnpj._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsIndicacaoCpfCnpj", tsIndicacaoCpfCnpj)
_module_typeBindings.tsIndicacaoCpfCnpj = tsIndicacaoCpfCnpj


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsCodigoObra
class tsCodigoObra(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoObra")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 215, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsArt
class tsArt(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsArt")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 222, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsNumeroLote
class tsNumeroLote(pyxb.binding.datatypes.nonNegativeInteger):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroLote")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 229, 1
    )
    _Documentation = None


tsNumeroLote._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(15)
)
tsNumeroLote._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsNumeroLote._InitializeFacetMap(tsNumeroLote._CF_totalDigits, tsNumeroLote._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsNumeroLote", tsNumeroLote)
_module_typeBindings.tsNumeroLote = tsNumeroLote


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsNumeroProtocolo
class tsNumeroProtocolo(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsNumeroProtocolo")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 235, 1
    )
    _Documentation = None


tsNumeroProtocolo._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(50)
)
tsNumeroProtocolo._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsNumeroProtocolo._InitializeFacetMap(
    tsNumeroProtocolo._CF_maxLength, tsNumeroProtocolo._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsNumeroProtocolo", tsNumeroProtocolo)
_module_typeBindings.tsNumeroProtocolo = tsNumeroProtocolo


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsSituacaoLoteRps
class tsSituacaoLoteRps(pyxb.binding.datatypes.byte):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsSituacaoLoteRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 241, 1
    )
    _Documentation = None


tsSituacaoLoteRps._CF_pattern = pyxb.binding.facets.CF_pattern()
tsSituacaoLoteRps._CF_pattern.addPattern(pattern="1|2|3|4")
tsSituacaoLoteRps._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsSituacaoLoteRps._InitializeFacetMap(
    tsSituacaoLoteRps._CF_pattern, tsSituacaoLoteRps._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "tsSituacaoLoteRps", tsSituacaoLoteRps)
_module_typeBindings.tsSituacaoLoteRps = tsSituacaoLoteRps


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsQuantidadeRps
class tsQuantidadeRps(pyxb.binding.datatypes.int):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsQuantidadeRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 247, 1
    )
    _Documentation = None


tsQuantidadeRps._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(
    value=pyxb.binding.datatypes.positiveInteger(4)
)
tsQuantidadeRps._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsQuantidadeRps._InitializeFacetMap(tsQuantidadeRps._CF_totalDigits, tsQuantidadeRps._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsQuantidadeRps", tsQuantidadeRps)
_module_typeBindings.tsQuantidadeRps = tsQuantidadeRps


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsCodigoMensagemAlerta
class tsCodigoMensagemAlerta(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoMensagemAlerta")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 253, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsDescricaoMensagemAlerta
class tsDescricaoMensagemAlerta(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsDescricaoMensagemAlerta")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 260, 1
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


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsCodigoCancelamentoNfse
class tsCodigoCancelamentoNfse(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsCodigoCancelamentoNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 267, 1
    )
    _Documentation = None


tsCodigoCancelamentoNfse._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(4)
)
tsCodigoCancelamentoNfse._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
tsCodigoCancelamentoNfse._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsCodigoCancelamentoNfse._InitializeFacetMap(
    tsCodigoCancelamentoNfse._CF_maxLength,
    tsCodigoCancelamentoNfse._CF_minLength,
    tsCodigoCancelamentoNfse._CF_whiteSpace,
)
Namespace.addCategoryObject("typeBinding", "tsCodigoCancelamentoNfse", tsCodigoCancelamentoNfse)
_module_typeBindings.tsCodigoCancelamentoNfse = tsCodigoCancelamentoNfse


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsIdTag
class tsIdTag(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsIdTag")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 274, 1
    )
    _Documentation = None


tsIdTag._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(255)
)
tsIdTag._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsIdTag._InitializeFacetMap(tsIdTag._CF_maxLength, tsIdTag._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsIdTag", tsIdTag)
_module_typeBindings.tsIdTag = tsIdTag


# Atomic simple type: {http://www.ginfes.com.br/tipos_v03.xsd}tsVersao
class tsVersao(pyxb.binding.datatypes.token):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tsVersao")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 280, 1
    )
    _Documentation = None


tsVersao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsVersao._CF_pattern.addPattern(pattern="[0-9]{1,4}")
tsVersao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
tsVersao._InitializeFacetMap(tsVersao._CF_pattern, tsVersao._CF_whiteSpace)
Namespace.addCategoryObject("typeBinding", "tsVersao", tsVersao)
_module_typeBindings.tsVersao = tsVersao


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcCpfCnpj with content type ELEMENT_ONLY
class tcCpfCnpj(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcCpfCnpj with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcCpfCnpj")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 287, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Cpf uses Python identifier Cpf
    __Cpf = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Cpf"),
        "Cpf",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcCpfCnpj_httpwww_ginfes_com_brtipos_v03_xsdCpf",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 289, 3
        ),
    )

    Cpf = property(__Cpf.value, __Cpf.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Cnpj uses Python identifier Cnpj
    __Cnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Cnpj"),
        "Cnpj",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcCpfCnpj_httpwww_ginfes_com_brtipos_v03_xsdCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 290, 3
        ),
    )

    Cnpj = property(__Cnpj.value, __Cnpj.set, None, None)

    _ElementMap.update({__Cpf.name(): __Cpf, __Cnpj.name(): __Cnpj})
    _AttributeMap.update({})


_module_typeBindings.tcCpfCnpj = tcCpfCnpj
Namespace.addCategoryObject("typeBinding", "tcCpfCnpj", tcCpfCnpj)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcEndereco with content type ELEMENT_ONLY
class tcEndereco(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcEndereco with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcEndereco")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 293, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Endereco uses Python identifier Endereco
    __Endereco = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        "Endereco",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcEndereco_httpwww_ginfes_com_brtipos_v03_xsdEndereco",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 295, 3
        ),
    )

    Endereco = property(__Endereco.value, __Endereco.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        "Numero",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcEndereco_httpwww_ginfes_com_brtipos_v03_xsdNumero",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 296, 3
        ),
    )

    Numero = property(__Numero.value, __Numero.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Complemento uses Python identifier Complemento
    __Complemento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Complemento"),
        "Complemento",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcEndereco_httpwww_ginfes_com_brtipos_v03_xsdComplemento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 297, 3
        ),
    )

    Complemento = property(__Complemento.value, __Complemento.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Bairro uses Python identifier Bairro
    __Bairro = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Bairro"),
        "Bairro",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcEndereco_httpwww_ginfes_com_brtipos_v03_xsdBairro",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 298, 3
        ),
    )

    Bairro = property(__Bairro.value, __Bairro.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        "CodigoMunicipio",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcEndereco_httpwww_ginfes_com_brtipos_v03_xsdCodigoMunicipio",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 299, 3
        ),
    )

    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Uf uses Python identifier Uf
    __Uf = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Uf"),
        "Uf",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcEndereco_httpwww_ginfes_com_brtipos_v03_xsdUf",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 300, 3
        ),
    )

    Uf = property(__Uf.value, __Uf.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Cep uses Python identifier Cep
    __Cep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Cep"),
        "Cep",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcEndereco_httpwww_ginfes_com_brtipos_v03_xsdCep",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 301, 3
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
            __Cep.name(): __Cep,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcEndereco = tcEndereco
Namespace.addCategoryObject("typeBinding", "tcEndereco", tcEndereco)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcContato with content type ELEMENT_ONLY
class tcContato(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcContato with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcContato")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 304, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Telefone uses Python identifier Telefone
    __Telefone = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Telefone"),
        "Telefone",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcContato_httpwww_ginfes_com_brtipos_v03_xsdTelefone",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 306, 3
        ),
    )

    Telefone = property(__Telefone.value, __Telefone.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Email uses Python identifier Email
    __Email = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Email"),
        "Email",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcContato_httpwww_ginfes_com_brtipos_v03_xsdEmail",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 307, 3
        ),
    )

    Email = property(__Email.value, __Email.set, None, None)

    _ElementMap.update({__Telefone.name(): __Telefone, __Email.name(): __Email})
    _AttributeMap.update({})


_module_typeBindings.tcContato = tcContato
Namespace.addCategoryObject("typeBinding", "tcContato", tcContato)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoOrgaoGerador with content type ELEMENT_ONLY
class tcIdentificacaoOrgaoGerador(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoOrgaoGerador with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoOrgaoGerador")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 310, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        "CodigoMunicipio",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoOrgaoGerador_httpwww_ginfes_com_brtipos_v03_xsdCodigoMunicipio",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 312, 3
        ),
    )

    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Uf uses Python identifier Uf
    __Uf = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Uf"),
        "Uf",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoOrgaoGerador_httpwww_ginfes_com_brtipos_v03_xsdUf",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 313, 3
        ),
    )

    Uf = property(__Uf.value, __Uf.set, None, None)

    _ElementMap.update({__CodigoMunicipio.name(): __CodigoMunicipio, __Uf.name(): __Uf})
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoOrgaoGerador = tcIdentificacaoOrgaoGerador
Namespace.addCategoryObject(
    "typeBinding", "tcIdentificacaoOrgaoGerador", tcIdentificacaoOrgaoGerador
)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoRps with content type ELEMENT_ONLY
class tcIdentificacaoRps(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoRps with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 316, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        "Numero",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoRps_httpwww_ginfes_com_brtipos_v03_xsdNumero",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 318, 3
        ),
    )

    Numero = property(__Numero.value, __Numero.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Serie uses Python identifier Serie
    __Serie = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Serie"),
        "Serie",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoRps_httpwww_ginfes_com_brtipos_v03_xsdSerie",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 319, 3
        ),
    )

    Serie = property(__Serie.value, __Serie.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Tipo uses Python identifier Tipo
    __Tipo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Tipo"),
        "Tipo",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoRps_httpwww_ginfes_com_brtipos_v03_xsdTipo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 320, 3
        ),
    )

    Tipo = property(__Tipo.value, __Tipo.set, None, None)

    _ElementMap.update({__Numero.name(): __Numero, __Serie.name(): __Serie, __Tipo.name(): __Tipo})
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoRps = tcIdentificacaoRps
Namespace.addCategoryObject("typeBinding", "tcIdentificacaoRps", tcIdentificacaoRps)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoPrestador with content type ELEMENT_ONLY
class tcIdentificacaoPrestador(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoPrestador with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoPrestador")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 323, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Cnpj uses Python identifier Cnpj
    __Cnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Cnpj"),
        "Cnpj",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoPrestador_httpwww_ginfes_com_brtipos_v03_xsdCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 325, 3
        ),
    )

    Cnpj = property(__Cnpj.value, __Cnpj.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoPrestador_httpwww_ginfes_com_brtipos_v03_xsdInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 326, 3
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    _ElementMap.update({__Cnpj.name(): __Cnpj, __InscricaoMunicipal.name(): __InscricaoMunicipal})
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoPrestador = tcIdentificacaoPrestador
Namespace.addCategoryObject("typeBinding", "tcIdentificacaoPrestador", tcIdentificacaoPrestador)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoTomador with content type ELEMENT_ONLY
class tcIdentificacaoTomador(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoTomador with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoTomador")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 329, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CpfCnpj uses Python identifier CpfCnpj
    __CpfCnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        "CpfCnpj",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoTomador_httpwww_ginfes_com_brtipos_v03_xsdCpfCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 331, 3
        ),
    )

    CpfCnpj = property(__CpfCnpj.value, __CpfCnpj.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoTomador_httpwww_ginfes_com_brtipos_v03_xsdInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 332, 3
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    _ElementMap.update(
        {__CpfCnpj.name(): __CpfCnpj, __InscricaoMunicipal.name(): __InscricaoMunicipal}
    )
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoTomador = tcIdentificacaoTomador
Namespace.addCategoryObject("typeBinding", "tcIdentificacaoTomador", tcIdentificacaoTomador)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcDadosTomador with content type ELEMENT_ONLY
class tcDadosTomador(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcDadosTomador with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcDadosTomador")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 335, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IdentificacaoTomador uses Python identifier IdentificacaoTomador
    __IdentificacaoTomador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoTomador"),
        "IdentificacaoTomador",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosTomador_httpwww_ginfes_com_brtipos_v03_xsdIdentificacaoTomador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 337, 3
        ),
    )

    IdentificacaoTomador = property(
        __IdentificacaoTomador.value, __IdentificacaoTomador.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}RazaoSocial uses Python identifier RazaoSocial
    __RazaoSocial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        "RazaoSocial",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosTomador_httpwww_ginfes_com_brtipos_v03_xsdRazaoSocial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 338, 3
        ),
    )

    RazaoSocial = property(__RazaoSocial.value, __RazaoSocial.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Endereco uses Python identifier Endereco
    __Endereco = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        "Endereco",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosTomador_httpwww_ginfes_com_brtipos_v03_xsdEndereco",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 339, 3
        ),
    )

    Endereco = property(__Endereco.value, __Endereco.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Contato uses Python identifier Contato
    __Contato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Contato"),
        "Contato",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosTomador_httpwww_ginfes_com_brtipos_v03_xsdContato",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 340, 3
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


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoIntermediarioServico with content type ELEMENT_ONLY
class tcIdentificacaoIntermediarioServico(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoIntermediarioServico with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoIntermediarioServico")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 343, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}RazaoSocial uses Python identifier RazaoSocial
    __RazaoSocial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        "RazaoSocial",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoIntermediarioServico_httpwww_ginfes_com_brtipos_v03_xsdRazaoSocial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 345, 3
        ),
    )

    RazaoSocial = property(__RazaoSocial.value, __RazaoSocial.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CpfCnpj uses Python identifier CpfCnpj
    __CpfCnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        "CpfCnpj",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoIntermediarioServico_httpwww_ginfes_com_brtipos_v03_xsdCpfCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 346, 3
        ),
    )

    CpfCnpj = property(__CpfCnpj.value, __CpfCnpj.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoIntermediarioServico_httpwww_ginfes_com_brtipos_v03_xsdInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 347, 3
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    _ElementMap.update(
        {
            __RazaoSocial.name(): __RazaoSocial,
            __CpfCnpj.name(): __CpfCnpj,
            __InscricaoMunicipal.name(): __InscricaoMunicipal,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoIntermediarioServico = tcIdentificacaoIntermediarioServico
Namespace.addCategoryObject(
    "typeBinding", "tcIdentificacaoIntermediarioServico", tcIdentificacaoIntermediarioServico
)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcValores with content type ELEMENT_ONLY
class tcValores(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcValores with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcValores")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 350, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorServicos uses Python identifier ValorServicos
    __ValorServicos = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorServicos"),
        "ValorServicos",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdValorServicos",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 352, 3
        ),
    )

    ValorServicos = property(__ValorServicos.value, __ValorServicos.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorDeducoes uses Python identifier ValorDeducoes
    __ValorDeducoes = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorDeducoes"),
        "ValorDeducoes",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdValorDeducoes",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 353, 3
        ),
    )

    ValorDeducoes = property(__ValorDeducoes.value, __ValorDeducoes.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorPis uses Python identifier ValorPis
    __ValorPis = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorPis"),
        "ValorPis",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdValorPis",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 354, 3
        ),
    )

    ValorPis = property(__ValorPis.value, __ValorPis.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorCofins uses Python identifier ValorCofins
    __ValorCofins = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorCofins"),
        "ValorCofins",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdValorCofins",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 355, 3
        ),
    )

    ValorCofins = property(__ValorCofins.value, __ValorCofins.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorInss uses Python identifier ValorInss
    __ValorInss = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorInss"),
        "ValorInss",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdValorInss",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 356, 3
        ),
    )

    ValorInss = property(__ValorInss.value, __ValorInss.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorIr uses Python identifier ValorIr
    __ValorIr = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorIr"),
        "ValorIr",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdValorIr",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 357, 3
        ),
    )

    ValorIr = property(__ValorIr.value, __ValorIr.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorCsll uses Python identifier ValorCsll
    __ValorCsll = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorCsll"),
        "ValorCsll",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdValorCsll",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 358, 3
        ),
    )

    ValorCsll = property(__ValorCsll.value, __ValorCsll.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IssRetido uses Python identifier IssRetido
    __IssRetido = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IssRetido"),
        "IssRetido",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdIssRetido",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 359, 3
        ),
    )

    IssRetido = property(__IssRetido.value, __IssRetido.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorIss uses Python identifier ValorIss
    __ValorIss = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorIss"),
        "ValorIss",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdValorIss",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 360, 3
        ),
    )

    ValorIss = property(__ValorIss.value, __ValorIss.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorIssRetido uses Python identifier ValorIssRetido
    __ValorIssRetido = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorIssRetido"),
        "ValorIssRetido",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdValorIssRetido",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 361, 3
        ),
    )

    ValorIssRetido = property(__ValorIssRetido.value, __ValorIssRetido.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}OutrasRetencoes uses Python identifier OutrasRetencoes
    __OutrasRetencoes = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "OutrasRetencoes"),
        "OutrasRetencoes",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdOutrasRetencoes",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 362, 3
        ),
    )

    OutrasRetencoes = property(__OutrasRetencoes.value, __OutrasRetencoes.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}BaseCalculo uses Python identifier BaseCalculo
    __BaseCalculo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "BaseCalculo"),
        "BaseCalculo",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdBaseCalculo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 363, 3
        ),
    )

    BaseCalculo = property(__BaseCalculo.value, __BaseCalculo.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Aliquota uses Python identifier Aliquota
    __Aliquota = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Aliquota"),
        "Aliquota",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdAliquota",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 364, 3
        ),
    )

    Aliquota = property(__Aliquota.value, __Aliquota.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorLiquidoNfse uses Python identifier ValorLiquidoNfse
    __ValorLiquidoNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorLiquidoNfse"),
        "ValorLiquidoNfse",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdValorLiquidoNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 365, 3
        ),
    )

    ValorLiquidoNfse = property(__ValorLiquidoNfse.value, __ValorLiquidoNfse.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}DescontoIncondicionado uses Python identifier DescontoIncondicionado
    __DescontoIncondicionado = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DescontoIncondicionado"),
        "DescontoIncondicionado",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdDescontoIncondicionado",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 366, 3
        ),
    )

    DescontoIncondicionado = property(
        __DescontoIncondicionado.value, __DescontoIncondicionado.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}DescontoCondicionado uses Python identifier DescontoCondicionado
    __DescontoCondicionado = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DescontoCondicionado"),
        "DescontoCondicionado",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcValores_httpwww_ginfes_com_brtipos_v03_xsdDescontoCondicionado",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 367, 3
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
            __IssRetido.name(): __IssRetido,
            __ValorIss.name(): __ValorIss,
            __ValorIssRetido.name(): __ValorIssRetido,
            __OutrasRetencoes.name(): __OutrasRetencoes,
            __BaseCalculo.name(): __BaseCalculo,
            __Aliquota.name(): __Aliquota,
            __ValorLiquidoNfse.name(): __ValorLiquidoNfse,
            __DescontoIncondicionado.name(): __DescontoIncondicionado,
            __DescontoCondicionado.name(): __DescontoCondicionado,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcValores = tcValores
Namespace.addCategoryObject("typeBinding", "tcValores", tcValores)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcDadosServico with content type ELEMENT_ONLY
class tcDadosServico(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcDadosServico with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcDadosServico")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 370, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Valores uses Python identifier Valores
    __Valores = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Valores"),
        "Valores",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosServico_httpwww_ginfes_com_brtipos_v03_xsdValores",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 372, 3
        ),
    )

    Valores = property(__Valores.value, __Valores.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ItemListaServico uses Python identifier ItemListaServico
    __ItemListaServico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ItemListaServico"),
        "ItemListaServico",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosServico_httpwww_ginfes_com_brtipos_v03_xsdItemListaServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 373, 3
        ),
    )

    ItemListaServico = property(__ItemListaServico.value, __ItemListaServico.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CodigoCnae uses Python identifier CodigoCnae
    __CodigoCnae = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoCnae"),
        "CodigoCnae",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosServico_httpwww_ginfes_com_brtipos_v03_xsdCodigoCnae",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 374, 3
        ),
    )

    CodigoCnae = property(__CodigoCnae.value, __CodigoCnae.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CodigoTributacaoMunicipio uses Python identifier CodigoTributacaoMunicipio
    __CodigoTributacaoMunicipio = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoTributacaoMunicipio"),
        "CodigoTributacaoMunicipio",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosServico_httpwww_ginfes_com_brtipos_v03_xsdCodigoTributacaoMunicipio",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 375, 3
        ),
    )

    CodigoTributacaoMunicipio = property(
        __CodigoTributacaoMunicipio.value, __CodigoTributacaoMunicipio.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Discriminacao uses Python identifier Discriminacao
    __Discriminacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Discriminacao"),
        "Discriminacao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosServico_httpwww_ginfes_com_brtipos_v03_xsdDiscriminacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 376, 3
        ),
    )

    Discriminacao = property(__Discriminacao.value, __Discriminacao.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        "CodigoMunicipio",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosServico_httpwww_ginfes_com_brtipos_v03_xsdCodigoMunicipio",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 377, 3
        ),
    )

    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    _ElementMap.update(
        {
            __Valores.name(): __Valores,
            __ItemListaServico.name(): __ItemListaServico,
            __CodigoCnae.name(): __CodigoCnae,
            __CodigoTributacaoMunicipio.name(): __CodigoTributacaoMunicipio,
            __Discriminacao.name(): __Discriminacao,
            __CodigoMunicipio.name(): __CodigoMunicipio,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcDadosServico = tcDadosServico
Namespace.addCategoryObject("typeBinding", "tcDadosServico", tcDadosServico)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcDadosConstrucaoCivil with content type ELEMENT_ONLY
class tcDadosConstrucaoCivil(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcDadosConstrucaoCivil with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcDadosConstrucaoCivil")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 380, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CodigoObra uses Python identifier CodigoObra
    __CodigoObra = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoObra"),
        "CodigoObra",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosConstrucaoCivil_httpwww_ginfes_com_brtipos_v03_xsdCodigoObra",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 382, 3
        ),
    )

    CodigoObra = property(__CodigoObra.value, __CodigoObra.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Art uses Python identifier Art
    __Art = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Art"),
        "Art",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosConstrucaoCivil_httpwww_ginfes_com_brtipos_v03_xsdArt",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 383, 3
        ),
    )

    Art = property(__Art.value, __Art.set, None, None)

    _ElementMap.update({__CodigoObra.name(): __CodigoObra, __Art.name(): __Art})
    _AttributeMap.update({})


_module_typeBindings.tcDadosConstrucaoCivil = tcDadosConstrucaoCivil
Namespace.addCategoryObject("typeBinding", "tcDadosConstrucaoCivil", tcDadosConstrucaoCivil)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcDadosPrestador with content type ELEMENT_ONLY
class tcDadosPrestador(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcDadosPrestador with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcDadosPrestador")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 386, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IdentificacaoPrestador uses Python identifier IdentificacaoPrestador
    __IdentificacaoPrestador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoPrestador"),
        "IdentificacaoPrestador",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosPrestador_httpwww_ginfes_com_brtipos_v03_xsdIdentificacaoPrestador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 388, 3
        ),
    )

    IdentificacaoPrestador = property(
        __IdentificacaoPrestador.value, __IdentificacaoPrestador.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}RazaoSocial uses Python identifier RazaoSocial
    __RazaoSocial = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        "RazaoSocial",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosPrestador_httpwww_ginfes_com_brtipos_v03_xsdRazaoSocial",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 389, 3
        ),
    )

    RazaoSocial = property(__RazaoSocial.value, __RazaoSocial.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}NomeFantasia uses Python identifier NomeFantasia
    __NomeFantasia = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NomeFantasia"),
        "NomeFantasia",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosPrestador_httpwww_ginfes_com_brtipos_v03_xsdNomeFantasia",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 390, 3
        ),
    )

    NomeFantasia = property(__NomeFantasia.value, __NomeFantasia.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Endereco uses Python identifier Endereco
    __Endereco = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        "Endereco",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosPrestador_httpwww_ginfes_com_brtipos_v03_xsdEndereco",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 391, 3
        ),
    )

    Endereco = property(__Endereco.value, __Endereco.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Contato uses Python identifier Contato
    __Contato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Contato"),
        "Contato",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcDadosPrestador_httpwww_ginfes_com_brtipos_v03_xsdContato",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 392, 3
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


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcRps with content type ELEMENT_ONLY
class tcRps(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcRps with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 413, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}InfRps uses Python identifier InfRps
    __InfRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InfRps"),
        "InfRps",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcRps_httpwww_ginfes_com_brtipos_v03_xsdInfRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 415, 3
        ),
    )

    InfRps = property(__InfRps.value, __InfRps.set, None, None)

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcRps_httpwww_w3_org200009xmldsigSignature",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd",
            41,
            0,
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({__InfRps.name(): __InfRps, __Signature.name(): __Signature})
    _AttributeMap.update({})


_module_typeBindings.tcRps = tcRps
Namespace.addCategoryObject("typeBinding", "tcRps", tcRps)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoNfse with content type ELEMENT_ONLY
class tcIdentificacaoNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcIdentificacaoNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcIdentificacaoNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 419, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        "Numero",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoNfse_httpwww_ginfes_com_brtipos_v03_xsdNumero",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 421, 3
        ),
    )

    Numero = property(__Numero.value, __Numero.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Cnpj uses Python identifier Cnpj
    __Cnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Cnpj"),
        "Cnpj",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoNfse_httpwww_ginfes_com_brtipos_v03_xsdCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 422, 3
        ),
    )

    Cnpj = property(__Cnpj.value, __Cnpj.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoNfse_httpwww_ginfes_com_brtipos_v03_xsdInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 423, 3
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        "CodigoMunicipio",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcIdentificacaoNfse_httpwww_ginfes_com_brtipos_v03_xsdCodigoMunicipio",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 424, 3
        ),
    )

    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    _ElementMap.update(
        {
            __Numero.name(): __Numero,
            __Cnpj.name(): __Cnpj,
            __InscricaoMunicipal.name(): __InscricaoMunicipal,
            __CodigoMunicipio.name(): __CodigoMunicipio,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.tcIdentificacaoNfse = tcIdentificacaoNfse
Namespace.addCategoryObject("typeBinding", "tcIdentificacaoNfse", tcIdentificacaoNfse)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcNfse with content type ELEMENT_ONLY
class tcNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 451, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}InfNfse uses Python identifier InfNfse
    __InfNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InfNfse"),
        "InfNfse",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcNfse_httpwww_ginfes_com_brtipos_v03_xsdInfNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 453, 3
        ),
    )

    InfNfse = property(__InfNfse.value, __InfNfse.set, None, None)

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcNfse_httpwww_w3_org200009xmldsigSignature",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd",
            41,
            0,
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({__InfNfse.name(): __InfNfse, __Signature.name(): __Signature})
    _AttributeMap.update({})


_module_typeBindings.tcNfse = tcNfse
Namespace.addCategoryObject("typeBinding", "tcNfse", tcNfse)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcPedidoCancelamento with content type ELEMENT_ONLY
class tcPedidoCancelamento(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcPedidoCancelamento with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcPedidoCancelamento")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 464, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}InfPedidoCancelamento uses Python identifier InfPedidoCancelamento
    __InfPedidoCancelamento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InfPedidoCancelamento"),
        "InfPedidoCancelamento",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcPedidoCancelamento_httpwww_ginfes_com_brtipos_v03_xsdInfPedidoCancelamento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 466, 3
        ),
    )

    InfPedidoCancelamento = property(
        __InfPedidoCancelamento.value, __InfPedidoCancelamento.set, None, None
    )

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcPedidoCancelamento_httpwww_w3_org200009xmldsigSignature",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd",
            41,
            0,
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update(
        {__InfPedidoCancelamento.name(): __InfPedidoCancelamento, __Signature.name(): __Signature}
    )
    _AttributeMap.update({})


_module_typeBindings.tcPedidoCancelamento = tcPedidoCancelamento
Namespace.addCategoryObject("typeBinding", "tcPedidoCancelamento", tcPedidoCancelamento)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcInfConfirmacaoCancelamento with content type ELEMENT_ONLY
class tcInfConfirmacaoCancelamento(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcInfConfirmacaoCancelamento with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcInfConfirmacaoCancelamento")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 470, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Sucesso uses Python identifier Sucesso
    __Sucesso = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Sucesso"),
        "Sucesso",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfConfirmacaoCancelamento_httpwww_ginfes_com_brtipos_v03_xsdSucesso",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 472, 3
        ),
    )

    Sucesso = property(__Sucesso.value, __Sucesso.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}DataHora uses Python identifier DataHora
    __DataHora = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataHora"),
        "DataHora",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfConfirmacaoCancelamento_httpwww_ginfes_com_brtipos_v03_xsdDataHora",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 473, 3
        ),
    )

    DataHora = property(__DataHora.value, __DataHora.set, None, None)

    _ElementMap.update({__Sucesso.name(): __Sucesso, __DataHora.name(): __DataHora})
    _AttributeMap.update({})


_module_typeBindings.tcInfConfirmacaoCancelamento = tcInfConfirmacaoCancelamento
Namespace.addCategoryObject(
    "typeBinding", "tcInfConfirmacaoCancelamento", tcInfConfirmacaoCancelamento
)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcCancelamentoNfse with content type ELEMENT_ONLY
class tcCancelamentoNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcCancelamentoNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcCancelamentoNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 483, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Confirmacao uses Python identifier Confirmacao
    __Confirmacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Confirmacao"),
        "Confirmacao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcCancelamentoNfse_httpwww_ginfes_com_brtipos_v03_xsdConfirmacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 485, 3
        ),
    )

    Confirmacao = property(__Confirmacao.value, __Confirmacao.set, None, None)

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcCancelamentoNfse_httpwww_w3_org200009xmldsigSignature",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd",
            41,
            0,
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({__Confirmacao.name(): __Confirmacao, __Signature.name(): __Signature})
    _AttributeMap.update({})


_module_typeBindings.tcCancelamentoNfse = tcCancelamentoNfse
Namespace.addCategoryObject("typeBinding", "tcCancelamentoNfse", tcCancelamentoNfse)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcSubstituicaoNfse with content type ELEMENT_ONLY
class tcSubstituicaoNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcSubstituicaoNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcSubstituicaoNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 495, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}SubstituicaoNfse uses Python identifier SubstituicaoNfse
    __SubstituicaoNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "SubstituicaoNfse"),
        "SubstituicaoNfse",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcSubstituicaoNfse_httpwww_ginfes_com_brtipos_v03_xsdSubstituicaoNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 497, 3
        ),
    )

    SubstituicaoNfse = property(__SubstituicaoNfse.value, __SubstituicaoNfse.set, None, None)

    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        "Signature",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcSubstituicaoNfse_httpwww_w3_org200009xmldsigSignature",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd",
            41,
            0,
        ),
    )

    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update(
        {__SubstituicaoNfse.name(): __SubstituicaoNfse, __Signature.name(): __Signature}
    )
    _AttributeMap.update({})


_module_typeBindings.tcSubstituicaoNfse = tcSubstituicaoNfse
Namespace.addCategoryObject("typeBinding", "tcSubstituicaoNfse", tcSubstituicaoNfse)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcCompNfse with content type ELEMENT_ONLY
class tcCompNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcCompNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcCompNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 501, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Nfse uses Python identifier Nfse
    __Nfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Nfse"),
        "Nfse",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcCompNfse_httpwww_ginfes_com_brtipos_v03_xsdNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 503, 3
        ),
    )

    Nfse = property(__Nfse.value, __Nfse.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}NfseCancelamento uses Python identifier NfseCancelamento
    __NfseCancelamento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseCancelamento"),
        "NfseCancelamento",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcCompNfse_httpwww_ginfes_com_brtipos_v03_xsdNfseCancelamento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 504, 3
        ),
    )

    NfseCancelamento = property(__NfseCancelamento.value, __NfseCancelamento.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}NfseSubstituicao uses Python identifier NfseSubstituicao
    __NfseSubstituicao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituicao"),
        "NfseSubstituicao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcCompNfse_httpwww_ginfes_com_brtipos_v03_xsdNfseSubstituicao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 505, 3
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 509, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}MensagemRetorno uses Python identifier MensagemRetorno
    __MensagemRetorno = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno"),
        "MensagemRetorno",
        "__httpwww_ginfes_com_brtipos_v03_xsd_CTD_ANON_httpwww_ginfes_com_brtipos_v03_xsdMensagemRetorno",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 511, 4
        ),
    )

    MensagemRetorno = property(__MensagemRetorno.value, __MensagemRetorno.set, None, None)

    _ElementMap.update({__MensagemRetorno.name(): __MensagemRetorno})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcMensagemRetorno with content type ELEMENT_ONLY
class tcMensagemRetorno(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcMensagemRetorno with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcMensagemRetorno")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 515, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Codigo uses Python identifier Codigo
    __Codigo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Codigo"),
        "Codigo",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcMensagemRetorno_httpwww_ginfes_com_brtipos_v03_xsdCodigo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 517, 3
        ),
    )

    Codigo = property(__Codigo.value, __Codigo.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Mensagem uses Python identifier Mensagem
    __Mensagem = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Mensagem"),
        "Mensagem",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcMensagemRetorno_httpwww_ginfes_com_brtipos_v03_xsdMensagem",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 518, 3
        ),
    )

    Mensagem = property(__Mensagem.value, __Mensagem.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Correcao uses Python identifier Correcao
    __Correcao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Correcao"),
        "Correcao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcMensagemRetorno_httpwww_ginfes_com_brtipos_v03_xsdCorrecao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 519, 3
        ),
    )

    Correcao = property(__Correcao.value, __Correcao.set, None, None)

    _ElementMap.update(
        {__Codigo.name(): __Codigo, __Mensagem.name(): __Mensagem, __Correcao.name(): __Correcao}
    )
    _AttributeMap.update({})


_module_typeBindings.tcMensagemRetorno = tcMensagemRetorno
Namespace.addCategoryObject("typeBinding", "tcMensagemRetorno", tcMensagemRetorno)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcMensagemRetornoLote with content type ELEMENT_ONLY
class tcMensagemRetornoLote(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcMensagemRetornoLote with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcMensagemRetornoLote")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 522, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IdentificacaoRps uses Python identifier IdentificacaoRps
    __IdentificacaoRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        "IdentificacaoRps",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcMensagemRetornoLote_httpwww_ginfes_com_brtipos_v03_xsdIdentificacaoRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 524, 3
        ),
    )

    IdentificacaoRps = property(__IdentificacaoRps.value, __IdentificacaoRps.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Codigo uses Python identifier Codigo
    __Codigo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Codigo"),
        "Codigo",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcMensagemRetornoLote_httpwww_ginfes_com_brtipos_v03_xsdCodigo",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 525, 3
        ),
    )

    Codigo = property(__Codigo.value, __Codigo.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Mensagem uses Python identifier Mensagem
    __Mensagem = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Mensagem"),
        "Mensagem",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcMensagemRetornoLote_httpwww_ginfes_com_brtipos_v03_xsdMensagem",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 526, 3
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
class CTD_ANON_(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 536, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Rps uses Python identifier Rps
    __Rps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Rps"),
        "Rps",
        "__httpwww_ginfes_com_brtipos_v03_xsd_CTD_ANON__httpwww_ginfes_com_brtipos_v03_xsdRps",
        True,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 538, 6
        ),
    )

    Rps = property(__Rps.value, __Rps.set, None, None)

    _ElementMap.update({__Rps.name(): __Rps})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcInfRps with content type ELEMENT_ONLY
class tcInfRps(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcInfRps with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcInfRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 395, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IdentificacaoRps uses Python identifier IdentificacaoRps
    __IdentificacaoRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        "IdentificacaoRps",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdIdentificacaoRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 397, 3
        ),
    )

    IdentificacaoRps = property(__IdentificacaoRps.value, __IdentificacaoRps.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}DataEmissao uses Python identifier DataEmissao
    __DataEmissao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataEmissao"),
        "DataEmissao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdDataEmissao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 398, 3
        ),
    )

    DataEmissao = property(__DataEmissao.value, __DataEmissao.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}NaturezaOperacao uses Python identifier NaturezaOperacao
    __NaturezaOperacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NaturezaOperacao"),
        "NaturezaOperacao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdNaturezaOperacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 399, 3
        ),
    )

    NaturezaOperacao = property(__NaturezaOperacao.value, __NaturezaOperacao.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}RegimeEspecialTributacao uses Python identifier RegimeEspecialTributacao
    __RegimeEspecialTributacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RegimeEspecialTributacao"),
        "RegimeEspecialTributacao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdRegimeEspecialTributacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 400, 3
        ),
    )

    RegimeEspecialTributacao = property(
        __RegimeEspecialTributacao.value, __RegimeEspecialTributacao.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}OptanteSimplesNacional uses Python identifier OptanteSimplesNacional
    __OptanteSimplesNacional = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "OptanteSimplesNacional"),
        "OptanteSimplesNacional",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdOptanteSimplesNacional",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 401, 3
        ),
    )

    OptanteSimplesNacional = property(
        __OptanteSimplesNacional.value, __OptanteSimplesNacional.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IncentivadorCultural uses Python identifier IncentivadorCultural
    __IncentivadorCultural = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IncentivadorCultural"),
        "IncentivadorCultural",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdIncentivadorCultural",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 402, 3
        ),
    )

    IncentivadorCultural = property(
        __IncentivadorCultural.value, __IncentivadorCultural.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Status"),
        "Status",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdStatus",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 403, 3
        ),
    )

    Status = property(__Status.value, __Status.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}RpsSubstituido uses Python identifier RpsSubstituido
    __RpsSubstituido = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RpsSubstituido"),
        "RpsSubstituido",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdRpsSubstituido",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 404, 3
        ),
    )

    RpsSubstituido = property(__RpsSubstituido.value, __RpsSubstituido.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Servico uses Python identifier Servico
    __Servico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Servico"),
        "Servico",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 405, 3
        ),
    )

    Servico = property(__Servico.value, __Servico.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        "Prestador",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdPrestador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 406, 3
        ),
    )

    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Tomador uses Python identifier Tomador
    __Tomador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Tomador"),
        "Tomador",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdTomador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 407, 3
        ),
    )

    Tomador = property(__Tomador.value, __Tomador.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IntermediarioServico uses Python identifier IntermediarioServico
    __IntermediarioServico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IntermediarioServico"),
        "IntermediarioServico",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdIntermediarioServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 408, 3
        ),
    )

    IntermediarioServico = property(
        __IntermediarioServico.value, __IntermediarioServico.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ConstrucaoCivil uses Python identifier ConstrucaoCivil
    __ConstrucaoCivil = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ConstrucaoCivil"),
        "ConstrucaoCivil",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_httpwww_ginfes_com_brtipos_v03_xsdConstrucaoCivil",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 409, 3
        ),
    )

    ConstrucaoCivil = property(__ConstrucaoCivil.value, __ConstrucaoCivil.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfRps_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 411, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 411, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update(
        {
            __IdentificacaoRps.name(): __IdentificacaoRps,
            __DataEmissao.name(): __DataEmissao,
            __NaturezaOperacao.name(): __NaturezaOperacao,
            __RegimeEspecialTributacao.name(): __RegimeEspecialTributacao,
            __OptanteSimplesNacional.name(): __OptanteSimplesNacional,
            __IncentivadorCultural.name(): __IncentivadorCultural,
            __Status.name(): __Status,
            __RpsSubstituido.name(): __RpsSubstituido,
            __Servico.name(): __Servico,
            __Prestador.name(): __Prestador,
            __Tomador.name(): __Tomador,
            __IntermediarioServico.name(): __IntermediarioServico,
            __ConstrucaoCivil.name(): __ConstrucaoCivil,
        }
    )
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcInfRps = tcInfRps
Namespace.addCategoryObject("typeBinding", "tcInfRps", tcInfRps)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcInfNfse with content type ELEMENT_ONLY
class tcInfNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcInfNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcInfNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 427, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        "Numero",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdNumero",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 429, 3
        ),
    )

    Numero = property(__Numero.value, __Numero.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CodigoVerificacao uses Python identifier CodigoVerificacao
    __CodigoVerificacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoVerificacao"),
        "CodigoVerificacao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdCodigoVerificacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 430, 3
        ),
    )

    CodigoVerificacao = property(__CodigoVerificacao.value, __CodigoVerificacao.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}DataEmissao uses Python identifier DataEmissao
    __DataEmissao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataEmissao"),
        "DataEmissao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdDataEmissao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 431, 3
        ),
    )

    DataEmissao = property(__DataEmissao.value, __DataEmissao.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IdentificacaoRps uses Python identifier IdentificacaoRps
    __IdentificacaoRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        "IdentificacaoRps",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdIdentificacaoRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 432, 3
        ),
    )

    IdentificacaoRps = property(__IdentificacaoRps.value, __IdentificacaoRps.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}DataEmissaoRps uses Python identifier DataEmissaoRps
    __DataEmissaoRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataEmissaoRps"),
        "DataEmissaoRps",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdDataEmissaoRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 433, 3
        ),
    )

    DataEmissaoRps = property(__DataEmissaoRps.value, __DataEmissaoRps.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}NaturezaOperacao uses Python identifier NaturezaOperacao
    __NaturezaOperacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NaturezaOperacao"),
        "NaturezaOperacao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdNaturezaOperacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 434, 3
        ),
    )

    NaturezaOperacao = property(__NaturezaOperacao.value, __NaturezaOperacao.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}RegimeEspecialTributacao uses Python identifier RegimeEspecialTributacao
    __RegimeEspecialTributacao = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "RegimeEspecialTributacao"),
        "RegimeEspecialTributacao",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdRegimeEspecialTributacao",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 435, 3
        ),
    )

    RegimeEspecialTributacao = property(
        __RegimeEspecialTributacao.value, __RegimeEspecialTributacao.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}OptanteSimplesNacional uses Python identifier OptanteSimplesNacional
    __OptanteSimplesNacional = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "OptanteSimplesNacional"),
        "OptanteSimplesNacional",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdOptanteSimplesNacional",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 436, 3
        ),
    )

    OptanteSimplesNacional = property(
        __OptanteSimplesNacional.value, __OptanteSimplesNacional.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IncentivadorCultural uses Python identifier IncentivadorCultural
    __IncentivadorCultural = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IncentivadorCultural"),
        "IncentivadorCultural",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdIncentivadorCultural",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 437, 3
        ),
    )

    IncentivadorCultural = property(
        __IncentivadorCultural.value, __IncentivadorCultural.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Competencia uses Python identifier Competencia
    __Competencia = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Competencia"),
        "Competencia",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdCompetencia",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 438, 3
        ),
    )

    Competencia = property(__Competencia.value, __Competencia.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}NfseSubstituida uses Python identifier NfseSubstituida
    __NfseSubstituida = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituida"),
        "NfseSubstituida",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdNfseSubstituida",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 439, 3
        ),
    )

    NfseSubstituida = property(__NfseSubstituida.value, __NfseSubstituida.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}OutrasInformacoes uses Python identifier OutrasInformacoes
    __OutrasInformacoes = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "OutrasInformacoes"),
        "OutrasInformacoes",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdOutrasInformacoes",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 440, 3
        ),
    )

    OutrasInformacoes = property(__OutrasInformacoes.value, __OutrasInformacoes.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Servico uses Python identifier Servico
    __Servico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Servico"),
        "Servico",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 441, 3
        ),
    )

    Servico = property(__Servico.value, __Servico.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ValorCredito uses Python identifier ValorCredito
    __ValorCredito = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ValorCredito"),
        "ValorCredito",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdValorCredito",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 442, 3
        ),
    )

    ValorCredito = property(__ValorCredito.value, __ValorCredito.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}PrestadorServico uses Python identifier PrestadorServico
    __PrestadorServico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "PrestadorServico"),
        "PrestadorServico",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdPrestadorServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 443, 3
        ),
    )

    PrestadorServico = property(__PrestadorServico.value, __PrestadorServico.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}TomadorServico uses Python identifier TomadorServico
    __TomadorServico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "TomadorServico"),
        "TomadorServico",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdTomadorServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 444, 3
        ),
    )

    TomadorServico = property(__TomadorServico.value, __TomadorServico.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IntermediarioServico uses Python identifier IntermediarioServico
    __IntermediarioServico = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IntermediarioServico"),
        "IntermediarioServico",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdIntermediarioServico",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 445, 3
        ),
    )

    IntermediarioServico = property(
        __IntermediarioServico.value, __IntermediarioServico.set, None, None
    )

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}OrgaoGerador uses Python identifier OrgaoGerador
    __OrgaoGerador = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "OrgaoGerador"),
        "OrgaoGerador",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdOrgaoGerador",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 446, 3
        ),
    )

    OrgaoGerador = property(__OrgaoGerador.value, __OrgaoGerador.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ConstrucaoCivil uses Python identifier ConstrucaoCivil
    __ConstrucaoCivil = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ConstrucaoCivil"),
        "ConstrucaoCivil",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_httpwww_ginfes_com_brtipos_v03_xsdConstrucaoCivil",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 447, 3
        ),
    )

    ConstrucaoCivil = property(__ConstrucaoCivil.value, __ConstrucaoCivil.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfNfse_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 449, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 449, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update(
        {
            __Numero.name(): __Numero,
            __CodigoVerificacao.name(): __CodigoVerificacao,
            __DataEmissao.name(): __DataEmissao,
            __IdentificacaoRps.name(): __IdentificacaoRps,
            __DataEmissaoRps.name(): __DataEmissaoRps,
            __NaturezaOperacao.name(): __NaturezaOperacao,
            __RegimeEspecialTributacao.name(): __RegimeEspecialTributacao,
            __OptanteSimplesNacional.name(): __OptanteSimplesNacional,
            __IncentivadorCultural.name(): __IncentivadorCultural,
            __Competencia.name(): __Competencia,
            __NfseSubstituida.name(): __NfseSubstituida,
            __OutrasInformacoes.name(): __OutrasInformacoes,
            __Servico.name(): __Servico,
            __ValorCredito.name(): __ValorCredito,
            __PrestadorServico.name(): __PrestadorServico,
            __TomadorServico.name(): __TomadorServico,
            __IntermediarioServico.name(): __IntermediarioServico,
            __OrgaoGerador.name(): __OrgaoGerador,
            __ConstrucaoCivil.name(): __ConstrucaoCivil,
        }
    )
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcInfNfse = tcInfNfse
Namespace.addCategoryObject("typeBinding", "tcInfNfse", tcInfNfse)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcInfPedidoCancelamento with content type ELEMENT_ONLY
class tcInfPedidoCancelamento(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcInfPedidoCancelamento with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcInfPedidoCancelamento")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 457, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}IdentificacaoNfse uses Python identifier IdentificacaoNfse
    __IdentificacaoNfse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoNfse"),
        "IdentificacaoNfse",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfPedidoCancelamento_httpwww_ginfes_com_brtipos_v03_xsdIdentificacaoNfse",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 459, 3
        ),
    )

    IdentificacaoNfse = property(__IdentificacaoNfse.value, __IdentificacaoNfse.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}CodigoCancelamento uses Python identifier CodigoCancelamento
    __CodigoCancelamento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CodigoCancelamento"),
        "CodigoCancelamento",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfPedidoCancelamento_httpwww_ginfes_com_brtipos_v03_xsdCodigoCancelamento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 460, 3
        ),
    )

    CodigoCancelamento = property(__CodigoCancelamento.value, __CodigoCancelamento.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfPedidoCancelamento_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 462, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 462, 2
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


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcConfirmacaoCancelamento with content type ELEMENT_ONLY
class tcConfirmacaoCancelamento(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcConfirmacaoCancelamento with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcConfirmacaoCancelamento")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 476, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Pedido uses Python identifier Pedido
    __Pedido = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Pedido"),
        "Pedido",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcConfirmacaoCancelamento_httpwww_ginfes_com_brtipos_v03_xsdPedido",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 478, 3
        ),
    )

    Pedido = property(__Pedido.value, __Pedido.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}InfConfirmacaoCancelamento uses Python identifier InfConfirmacaoCancelamento
    __InfConfirmacaoCancelamento = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InfConfirmacaoCancelamento"),
        "InfConfirmacaoCancelamento",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcConfirmacaoCancelamento_httpwww_ginfes_com_brtipos_v03_xsdInfConfirmacaoCancelamento",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 479, 3
        ),
    )

    InfConfirmacaoCancelamento = property(
        __InfConfirmacaoCancelamento.value, __InfConfirmacaoCancelamento.set, None, None
    )

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcConfirmacaoCancelamento_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 481, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 481, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update(
        {
            __Pedido.name(): __Pedido,
            __InfConfirmacaoCancelamento.name(): __InfConfirmacaoCancelamento,
        }
    )
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcConfirmacaoCancelamento = tcConfirmacaoCancelamento
Namespace.addCategoryObject("typeBinding", "tcConfirmacaoCancelamento", tcConfirmacaoCancelamento)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcInfSubstituicaoNfse with content type ELEMENT_ONLY
class tcInfSubstituicaoNfse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcInfSubstituicaoNfse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcInfSubstituicaoNfse")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 489, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}NfseSubstituidora uses Python identifier NfseSubstituidora
    __NfseSubstituidora = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituidora"),
        "NfseSubstituidora",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfSubstituicaoNfse_httpwww_ginfes_com_brtipos_v03_xsdNfseSubstituidora",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 491, 3
        ),
    )

    NfseSubstituidora = property(__NfseSubstituidora.value, __NfseSubstituidora.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcInfSubstituicaoNfse_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 493, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 493, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({__NfseSubstituidora.name(): __NfseSubstituidora})
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcInfSubstituicaoNfse = tcInfSubstituicaoNfse
Namespace.addCategoryObject("typeBinding", "tcInfSubstituicaoNfse", tcInfSubstituicaoNfse)


# Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcLoteRps with content type ELEMENT_ONLY
class tcLoteRps(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ginfes.com.br/tipos_v03.xsd}tcLoteRps with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "tcLoteRps")
    _XSDLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 529, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NumeroLote"),
        "NumeroLote",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcLoteRps_httpwww_ginfes_com_brtipos_v03_xsdNumeroLote",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 531, 3
        ),
    )

    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}Cnpj uses Python identifier Cnpj
    __Cnpj = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Cnpj"),
        "Cnpj",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcLoteRps_httpwww_ginfes_com_brtipos_v03_xsdCnpj",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 532, 3
        ),
    )

    Cnpj = property(__Cnpj.value, __Cnpj.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        "InscricaoMunicipal",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcLoteRps_httpwww_ginfes_com_brtipos_v03_xsdInscricaoMunicipal",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 533, 3
        ),
    )

    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}QuantidadeRps uses Python identifier QuantidadeRps
    __QuantidadeRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "QuantidadeRps"),
        "QuantidadeRps",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcLoteRps_httpwww_ginfes_com_brtipos_v03_xsdQuantidadeRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 534, 3
        ),
    )

    QuantidadeRps = property(__QuantidadeRps.value, __QuantidadeRps.set, None, None)

    # Element {http://www.ginfes.com.br/tipos_v03.xsd}ListaRps uses Python identifier ListaRps
    __ListaRps = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ListaRps"),
        "ListaRps",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcLoteRps_httpwww_ginfes_com_brtipos_v03_xsdListaRps",
        False,
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 535, 3
        ),
    )

    ListaRps = property(__ListaRps.value, __ListaRps.set, None, None)

    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "Id"),
        "Id",
        "__httpwww_ginfes_com_brtipos_v03_xsd_tcLoteRps_Id",
        _module_typeBindings.tsIdTag,
    )
    __Id._DeclarationLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 543, 2
    )
    __Id._UseLocation = pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 543, 2
    )

    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update(
        {
            __NumeroLote.name(): __NumeroLote,
            __Cnpj.name(): __Cnpj,
            __InscricaoMunicipal.name(): __InscricaoMunicipal,
            __QuantidadeRps.name(): __QuantidadeRps,
            __ListaRps.name(): __ListaRps,
        }
    )
    _AttributeMap.update({__Id.name(): __Id})


_module_typeBindings.tcLoteRps = tcLoteRps
Namespace.addCategoryObject("typeBinding", "tcLoteRps", tcLoteRps)


ListaMensagemRetorno = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "ListaMensagemRetorno"),
    CTD_ANON,
    location=pyxb.utils.utility.Location(
        "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 508, 1
    ),
)
Namespace.addCategoryObject(
    "elementBinding", ListaMensagemRetorno.name().localName(), ListaMensagemRetorno
)


tcCpfCnpj._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Cpf"),
        tsCpf,
        scope=tcCpfCnpj,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 289, 3
        ),
    )
)

tcCpfCnpj._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Cnpj"),
        tsCnpj,
        scope=tcCpfCnpj,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 290, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 289, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 290, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 295, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        tsNumeroEndereco,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 296, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Complemento"),
        tsComplementoEndereco,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 297, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Bairro"),
        tsBairro,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 298, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        tsCodigoMunicipioIbge,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 299, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Uf"),
        tsUf,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 300, 3
        ),
    )
)

tcEndereco._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Cep"),
        tsCep,
        scope=tcEndereco,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 301, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 295, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 296, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 297, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 298, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 299, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 300, 3
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 301, 3
        ),
    )
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Endereco")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 295, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 296, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 297, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 298, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 299, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 300, 3
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Cep")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 301, 3
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_6, True)]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


tcEndereco._Automaton = _BuildAutomaton_()


tcContato._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Telefone"),
        tsTelefone,
        scope=tcContato,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 306, 3
        ),
    )
)

tcContato._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Email"),
        tsEmail,
        scope=tcContato,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 307, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 306, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 307, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcContato._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Telefone")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 306, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 307, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 312, 3
        ),
    )
)

tcIdentificacaoOrgaoGerador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Uf"),
        tsUf,
        scope=tcIdentificacaoOrgaoGerador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 313, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 312, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 313, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 318, 3
        ),
    )
)

tcIdentificacaoRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Serie"),
        tsSerieRps,
        scope=tcIdentificacaoRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 319, 3
        ),
    )
)

tcIdentificacaoRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Tipo"),
        tsTipoRps,
        scope=tcIdentificacaoRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 320, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 318, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 319, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 320, 3
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
        pyxb.namespace.ExpandedName(Namespace, "Cnpj"),
        tsCnpj,
        scope=tcIdentificacaoPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 325, 3
        ),
    )
)

tcIdentificacaoPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcIdentificacaoPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 326, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 326, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Cnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 325, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoPrestador._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 326, 3
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


tcIdentificacaoPrestador._Automaton = _BuildAutomaton_5()


tcIdentificacaoTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        tcCpfCnpj,
        scope=tcIdentificacaoTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 331, 3
        ),
    )
)

tcIdentificacaoTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcIdentificacaoTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 332, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 331, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 332, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CpfCnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 331, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 332, 3
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


tcDadosTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoTomador"),
        tcIdentificacaoTomador,
        scope=tcDadosTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 337, 3
        ),
    )
)

tcDadosTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        tsRazaoSocial,
        scope=tcDadosTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 338, 3
        ),
    )
)

tcDadosTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        tcEndereco,
        scope=tcDadosTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 339, 3
        ),
    )
)

tcDadosTomador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Contato"),
        tcContato,
        scope=tcDadosTomador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 340, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 337, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 338, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 339, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 340, 3
        ),
    )
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcDadosTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IdentificacaoTomador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 337, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 338, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 339, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 340, 3
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


tcDadosTomador._Automaton = _BuildAutomaton_7()


tcIdentificacaoIntermediarioServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        tsRazaoSocial,
        scope=tcIdentificacaoIntermediarioServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 345, 3
        ),
    )
)

tcIdentificacaoIntermediarioServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CpfCnpj"),
        tcCpfCnpj,
        scope=tcIdentificacaoIntermediarioServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 346, 3
        ),
    )
)

tcIdentificacaoIntermediarioServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcIdentificacaoIntermediarioServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 347, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 347, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoIntermediarioServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "RazaoSocial")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 345, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoIntermediarioServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CpfCnpj")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 346, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoIntermediarioServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 347, 3
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


tcIdentificacaoIntermediarioServico._Automaton = _BuildAutomaton_8()


tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorServicos"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 352, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorDeducoes"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 353, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorPis"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 354, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorCofins"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 355, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorInss"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 356, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorIr"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 357, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorCsll"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 358, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IssRetido"),
        tsSimNao,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 359, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorIss"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 360, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorIssRetido"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 361, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "OutrasRetencoes"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 362, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "BaseCalculo"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 363, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Aliquota"),
        tsAliquota,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 364, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorLiquidoNfse"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 365, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DescontoIncondicionado"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 366, 3
        ),
    )
)

tcValores._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DescontoCondicionado"),
        tsValor,
        scope=tcValores,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 367, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 353, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 354, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 355, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 356, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 357, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 358, 3
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 360, 3
        ),
    )
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 361, 3
        ),
    )
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 362, 3
        ),
    )
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 363, 3
        ),
    )
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 364, 3
        ),
    )
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 365, 3
        ),
    )
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 366, 3
        ),
    )
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 367, 3
        ),
    )
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorServicos")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 352, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorDeducoes")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 353, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorPis")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 354, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorCofins")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 355, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorInss")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 356, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorIr")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 357, 3
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorCsll")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 358, 3
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IssRetido")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 359, 3
        ),
    )
    st_7 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorIss")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 360, 3
        ),
    )
    st_8 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorIssRetido")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 361, 3
        ),
    )
    st_9 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "OutrasRetencoes")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 362, 3
        ),
    )
    st_10 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "BaseCalculo")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 363, 3
        ),
    )
    st_11 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Aliquota")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 364, 3
        ),
    )
    st_12 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorLiquidoNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 365, 3
        ),
    )
    st_13 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DescontoIncondicionado")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 366, 3
        ),
    )
    st_14 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(
        tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DescontoCondicionado")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 367, 3
        ),
    )
    st_15 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_15)
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
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
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
    transitions.append(fac.Transition(st_8, []))
    transitions.append(fac.Transition(st_9, []))
    transitions.append(fac.Transition(st_10, []))
    transitions.append(fac.Transition(st_11, []))
    transitions.append(fac.Transition(st_12, []))
    transitions.append(fac.Transition(st_13, []))
    transitions.append(fac.Transition(st_14, []))
    transitions.append(fac.Transition(st_15, []))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_15, [fac.UpdateInstruction(cc_6, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_15, [fac.UpdateInstruction(cc_7, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_15, [fac.UpdateInstruction(cc_8, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_15, [fac.UpdateInstruction(cc_9, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_15, [fac.UpdateInstruction(cc_10, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_15, [fac.UpdateInstruction(cc_11, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_15, [fac.UpdateInstruction(cc_12, False)]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [fac.UpdateInstruction(cc_13, True)]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcValores._Automaton = _BuildAutomaton_9()


tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Valores"),
        tcValores,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 372, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ItemListaServico"),
        tsItemListaServico,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 373, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoCnae"),
        tsCodigoCnae,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 374, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoTributacaoMunicipio"),
        tsCodigoTributacao,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 375, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Discriminacao"),
        tsDiscriminacao,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 376, 3
        ),
    )
)

tcDadosServico._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        tsCodigoMunicipioIbge,
        scope=tcDadosServico,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 377, 3
        ),
    )
)


def _BuildAutomaton_10():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 374, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 375, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Valores")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 372, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ItemListaServico")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 373, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoCnae")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 374, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CodigoTributacaoMunicipio")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 375, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Discriminacao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 376, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 377, 3
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcDadosServico._Automaton = _BuildAutomaton_10()


tcDadosConstrucaoCivil._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoObra"),
        tsCodigoObra,
        scope=tcDadosConstrucaoCivil,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 382, 3
        ),
    )
)

tcDadosConstrucaoCivil._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Art"),
        tsArt,
        scope=tcDadosConstrucaoCivil,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 383, 3
        ),
    )
)


def _BuildAutomaton_11():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcDadosConstrucaoCivil._UseForTag(pyxb.namespace.ExpandedName(Namespace, "CodigoObra")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 382, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 383, 3
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


tcDadosConstrucaoCivil._Automaton = _BuildAutomaton_11()


tcDadosPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoPrestador"),
        tcIdentificacaoPrestador,
        scope=tcDadosPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 388, 3
        ),
    )
)

tcDadosPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RazaoSocial"),
        tsRazaoSocial,
        scope=tcDadosPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 389, 3
        ),
    )
)

tcDadosPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NomeFantasia"),
        tsNomeFantasia,
        scope=tcDadosPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 390, 3
        ),
    )
)

tcDadosPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Endereco"),
        tcEndereco,
        scope=tcDadosPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 391, 3
        ),
    )
)

tcDadosPrestador._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Contato"),
        tcContato,
        scope=tcDadosPrestador,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 392, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 390, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 392, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 388, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 389, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 390, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 391, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 392, 3
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


tcDadosPrestador._Automaton = _BuildAutomaton_12()


tcRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InfRps"),
        tcInfRps,
        scope=tcRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 415, 3
        ),
    )
)

tcRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=tcRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd",
            41,
            0,
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 416, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "InfRps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 415, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        tcRps._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 416, 3
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


tcRps._Automaton = _BuildAutomaton_13()


tcIdentificacaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        tsNumeroNfse,
        scope=tcIdentificacaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 421, 3
        ),
    )
)

tcIdentificacaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Cnpj"),
        tsCnpj,
        scope=tcIdentificacaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 422, 3
        ),
    )
)

tcIdentificacaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcIdentificacaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 423, 3
        ),
    )
)

tcIdentificacaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoMunicipio"),
        tsCodigoMunicipioIbge,
        scope=tcIdentificacaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 424, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 423, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Numero")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 421, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcIdentificacaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Cnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 422, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 423, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 424, 3
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


tcIdentificacaoNfse._Automaton = _BuildAutomaton_14()


tcNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InfNfse"),
        tcInfNfse,
        scope=tcNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 453, 3
        ),
    )
)

tcNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=tcNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd",
            41,
            0,
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
        min=1,
        max=2,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 454, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "InfNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 453, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 454, 3
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


tcNfse._Automaton = _BuildAutomaton_15()


tcPedidoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InfPedidoCancelamento"),
        tcInfPedidoCancelamento,
        scope=tcPedidoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 466, 3
        ),
    )
)

tcPedidoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=tcPedidoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd",
            41,
            0,
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 467, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 466, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 467, 3
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


tcPedidoCancelamento._Automaton = _BuildAutomaton_16()


tcInfConfirmacaoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Sucesso"),
        pyxb.binding.datatypes.boolean,
        scope=tcInfConfirmacaoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 472, 3
        ),
    )
)

tcInfConfirmacaoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataHora"),
        pyxb.binding.datatypes.dateTime,
        scope=tcInfConfirmacaoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 473, 3
        ),
    )
)


def _BuildAutomaton_17():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfConfirmacaoCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Sucesso")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 472, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcInfConfirmacaoCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataHora")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 473, 3
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


tcInfConfirmacaoCancelamento._Automaton = _BuildAutomaton_17()


tcCancelamentoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Confirmacao"),
        tcConfirmacaoCancelamento,
        scope=tcCancelamentoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 485, 3
        ),
    )
)

tcCancelamentoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=tcCancelamentoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd",
            41,
            0,
        ),
    )
)


def _BuildAutomaton_18():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcCancelamentoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Confirmacao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 485, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcCancelamentoNfse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 486, 3
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


tcCancelamentoNfse._Automaton = _BuildAutomaton_18()


tcSubstituicaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "SubstituicaoNfse"),
        tcInfSubstituicaoNfse,
        scope=tcSubstituicaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 497, 3
        ),
    )
)

tcSubstituicaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(_Namespace_dsig, "Signature"),
        _ImportedBinding__dsig.SignatureType,
        scope=tcSubstituicaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/xmldsig-core-schema20020212_v03.xsd",
            41,
            0,
        ),
    )
)


def _BuildAutomaton_19():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=1,
        max=2,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 498, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcSubstituicaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "SubstituicaoNfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 497, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 498, 3
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


tcSubstituicaoNfse._Automaton = _BuildAutomaton_19()


tcCompNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Nfse"),
        tcNfse,
        scope=tcCompNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 503, 3
        ),
    )
)

tcCompNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseCancelamento"),
        tcCancelamentoNfse,
        scope=tcCompNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 504, 3
        ),
    )
)

tcCompNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituicao"),
        tcSubstituicaoNfse,
        scope=tcCompNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 505, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 504, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 505, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcCompNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Nfse")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 503, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 504, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 505, 3
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


CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno"),
        tcMensagemRetorno,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 511, 4
        ),
    )
)


def _BuildAutomaton_21():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, "MensagemRetorno")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 511, 4
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


CTD_ANON._Automaton = _BuildAutomaton_21()


tcMensagemRetorno._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Codigo"),
        tsCodigoMensagemAlerta,
        scope=tcMensagemRetorno,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 517, 3
        ),
    )
)

tcMensagemRetorno._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Mensagem"),
        tsDescricaoMensagemAlerta,
        scope=tcMensagemRetorno,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 518, 3
        ),
    )
)

tcMensagemRetorno._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Correcao"),
        tsDescricaoMensagemAlerta,
        scope=tcMensagemRetorno,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 519, 3
        ),
    )
)


def _BuildAutomaton_22():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 519, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcMensagemRetorno._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Codigo")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 517, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 518, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 519, 3
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


tcMensagemRetorno._Automaton = _BuildAutomaton_22()


tcMensagemRetornoLote._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        tcIdentificacaoRps,
        scope=tcMensagemRetornoLote,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 524, 3
        ),
    )
)

tcMensagemRetornoLote._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Codigo"),
        tsCodigoMensagemAlerta,
        scope=tcMensagemRetornoLote,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 525, 3
        ),
    )
)

tcMensagemRetornoLote._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Mensagem"),
        tsDescricaoMensagemAlerta,
        scope=tcMensagemRetornoLote,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 526, 3
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
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcMensagemRetornoLote._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 524, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 525, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 526, 3
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


tcMensagemRetornoLote._Automaton = _BuildAutomaton_23()


CTD_ANON_._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Rps"),
        tcRps,
        scope=CTD_ANON_,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 538, 6
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
        CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Rps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 538, 6
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


tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        tcIdentificacaoRps,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 397, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataEmissao"),
        pyxb.binding.datatypes.dateTime,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 398, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NaturezaOperacao"),
        tsNaturezaOperacao,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 399, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RegimeEspecialTributacao"),
        tsRegimeEspecialTributacao,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 400, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "OptanteSimplesNacional"),
        tsSimNao,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 401, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IncentivadorCultural"),
        tsSimNao,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 402, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Status"),
        tsStatusRps,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 403, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RpsSubstituido"),
        tcIdentificacaoRps,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 404, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Servico"),
        tcDadosServico,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 405, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Prestador"),
        tcIdentificacaoPrestador,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 406, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Tomador"),
        tcDadosTomador,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 407, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IntermediarioServico"),
        tcIdentificacaoIntermediarioServico,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 408, 3
        ),
    )
)

tcInfRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ConstrucaoCivil"),
        tcDadosConstrucaoCivil,
        scope=tcInfRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 409, 3
        ),
    )
)


def _BuildAutomaton_25():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 400, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 404, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 408, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 409, 3
        ),
    )
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 397, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 398, 3
        ),
    )
    st_1 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NaturezaOperacao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 399, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "RegimeEspecialTributacao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 400, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "OptanteSimplesNacional")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 401, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IncentivadorCultural")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 402, 3
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Status")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 403, 3
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "RpsSubstituido")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 404, 3
        ),
    )
    st_7 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Servico")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 405, 3
        ),
    )
    st_8 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Prestador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 406, 3
        ),
    )
    st_9 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Tomador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 407, 3
        ),
    )
    st_10 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IntermediarioServico")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 408, 3
        ),
    )
    st_11 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ConstrucaoCivil")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 409, 3
        ),
    )
    st_12 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, []))
    transitions.append(fac.Transition(st_8, []))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_1, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, []))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, []))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, []))
    transitions.append(fac.Transition(st_12, []))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_2, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_3, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcInfRps._Automaton = _BuildAutomaton_25()


tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Numero"),
        tsNumeroNfse,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 429, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoVerificacao"),
        tsCodigoVerificacao,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 430, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataEmissao"),
        pyxb.binding.datatypes.dateTime,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 431, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps"),
        tcIdentificacaoRps,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 432, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataEmissaoRps"),
        pyxb.binding.datatypes.date,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 433, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NaturezaOperacao"),
        tsNaturezaOperacao,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 434, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "RegimeEspecialTributacao"),
        tsRegimeEspecialTributacao,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 435, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "OptanteSimplesNacional"),
        tsSimNao,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 436, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IncentivadorCultural"),
        tsSimNao,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 437, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Competencia"),
        pyxb.binding.datatypes.date,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 438, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituida"),
        tsNumeroNfse,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 439, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "OutrasInformacoes"),
        tsOutrasInformacoes,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 440, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Servico"),
        tcDadosServico,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 441, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ValorCredito"),
        tsValor,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 442, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "PrestadorServico"),
        tcDadosPrestador,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 443, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "TomadorServico"),
        tcDadosTomador,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 444, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IntermediarioServico"),
        tcIdentificacaoIntermediarioServico,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 445, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "OrgaoGerador"),
        tcIdentificacaoOrgaoGerador,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 446, 3
        ),
    )
)

tcInfNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ConstrucaoCivil"),
        tcDadosConstrucaoCivil,
        scope=tcInfNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 447, 3
        ),
    )
)


def _BuildAutomaton_26():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 432, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 433, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 435, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 439, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 440, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 442, 3
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 445, 3
        ),
    )
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 447, 3
        ),
    )
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Numero")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 429, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 430, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 431, 3
        ),
    )
    st_2 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IdentificacaoRps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 432, 3
        ),
    )
    st_3 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "DataEmissaoRps")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 433, 3
        ),
    )
    st_4 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NaturezaOperacao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 434, 3
        ),
    )
    st_5 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "RegimeEspecialTributacao")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 435, 3
        ),
    )
    st_6 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "OptanteSimplesNacional")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 436, 3
        ),
    )
    st_7 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IncentivadorCultural")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 437, 3
        ),
    )
    st_8 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Competencia")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 438, 3
        ),
    )
    st_9 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NfseSubstituida")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 439, 3
        ),
    )
    st_10 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "OutrasInformacoes")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 440, 3
        ),
    )
    st_11 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Servico")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 441, 3
        ),
    )
    st_12 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ValorCredito")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 442, 3
        ),
    )
    st_13 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "PrestadorServico")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 443, 3
        ),
    )
    st_14 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "TomadorServico")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 444, 3
        ),
    )
    st_15 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "IntermediarioServico")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 445, 3
        ),
    )
    st_16 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_16)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "OrgaoGerador")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 446, 3
        ),
    )
    st_17 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "ConstrucaoCivil")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 447, 3
        ),
    )
    st_18 = fac.State(
        symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_18)
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
    transitions.append(fac.Transition(st_10, []))
    transitions.append(fac.Transition(st_11, []))
    transitions.append(fac.Transition(st_12, []))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_3, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_4, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, []))
    transitions.append(fac.Transition(st_14, []))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_5, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, []))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, []))
    transitions.append(fac.Transition(st_17, []))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_17, [fac.UpdateInstruction(cc_6, False)]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, []))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [fac.UpdateInstruction(cc_7, True)]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcInfNfse._Automaton = _BuildAutomaton_26()


tcInfPedidoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IdentificacaoNfse"),
        tcIdentificacaoNfse,
        scope=tcInfPedidoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 459, 3
        ),
    )
)

tcInfPedidoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CodigoCancelamento"),
        tsCodigoCancelamentoNfse,
        scope=tcInfPedidoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 460, 3
        ),
    )
)


def _BuildAutomaton_27():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcInfPedidoCancelamento._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "IdentificacaoNfse")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 459, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcInfPedidoCancelamento._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CodigoCancelamento")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 460, 3
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


tcInfPedidoCancelamento._Automaton = _BuildAutomaton_27()


tcConfirmacaoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Pedido"),
        tcPedidoCancelamento,
        scope=tcConfirmacaoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 478, 3
        ),
    )
)

tcConfirmacaoCancelamento._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InfConfirmacaoCancelamento"),
        tcInfConfirmacaoCancelamento,
        scope=tcConfirmacaoCancelamento,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 479, 3
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
        tcConfirmacaoCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Pedido")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 478, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcConfirmacaoCancelamento._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "InfConfirmacaoCancelamento")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 479, 3
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


tcConfirmacaoCancelamento._Automaton = _BuildAutomaton_28()


tcInfSubstituicaoNfse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NfseSubstituidora"),
        tsNumeroNfse,
        scope=tcInfSubstituicaoNfse,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 491, 3
        ),
    )
)


def _BuildAutomaton_29():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        tcInfSubstituicaoNfse._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "NfseSubstituidora")
        ),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 491, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcInfSubstituicaoNfse._Automaton = _BuildAutomaton_29()


tcLoteRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NumeroLote"),
        tsNumeroLote,
        scope=tcLoteRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 531, 3
        ),
    )
)

tcLoteRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Cnpj"),
        tsCnpj,
        scope=tcLoteRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 532, 3
        ),
    )
)

tcLoteRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "InscricaoMunicipal"),
        tsInscricaoMunicipal,
        scope=tcLoteRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 533, 3
        ),
    )
)

tcLoteRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "QuantidadeRps"),
        tsQuantidadeRps,
        scope=tcLoteRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 534, 3
        ),
    )
)

tcLoteRps._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ListaRps"),
        CTD_ANON_,
        scope=tcLoteRps,
        location=pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 535, 3
        ),
    )
)


def _BuildAutomaton_30():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "NumeroLote")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 531, 3
        ),
    )
    st_0 = fac.State(
        symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Cnpj")),
        pyxb.utils.utility.Location(
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 532, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 533, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 534, 3
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
            "/workspaces/PyNFe/pynfe/data/XSDs/NFS-e/Ginfes/tipos_v03.xsd", 535, 3
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


tcLoteRps._Automaton = _BuildAutomaton_30()
