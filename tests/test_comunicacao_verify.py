from unittest import mock

import pytest

from pynfe.processamento.comunicacao import ComunicacaoCTe, ComunicacaoMDFe, ComunicacaoSefaz
from pynfe.utils import etree


@pytest.mark.parametrize("cls", [ComunicacaoSefaz, ComunicacaoMDFe, ComunicacaoCTe])
def test_verify_default_preserves_legacy_behavior(cls):
    assert cls("SP", "cert.pfx", "x").verify is False


@pytest.mark.parametrize("cls", [ComunicacaoSefaz, ComunicacaoMDFe, ComunicacaoCTe])
def test_verify_is_configurable(cls):
    assert (
        cls("SP", "cert.pfx", "x", verify="/etc/ssl/icp-brasil.pem").verify
        == "/etc/ssl/icp-brasil.pem"
    )
    assert cls("SP", "cert.pfx", "x", verify=True).verify is True


@pytest.mark.parametrize("cls", [ComunicacaoSefaz, ComunicacaoMDFe, ComunicacaoCTe])
@pytest.mark.parametrize("verify", [False, True, "/etc/ssl/icp-brasil.pem"])
def test_post_forwards_verify_to_requests(cls, verify):
    con = cls("SP", "./tests/certificado.pfx", b"123456", verify=verify)
    with mock.patch("pynfe.processamento.comunicacao.requests.post") as post:
        con._post("https://sefaz.example/ws", etree.Element("NFe"))
    assert post.call_args.kwargs["verify"] == verify
