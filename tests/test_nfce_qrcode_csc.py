import hashlib
import unittest

from lxml import etree

from pynfe.processamento.serializacao import SerializacaoQrcode
from pynfe.utils.flags import NAMESPACE_NFE, NAMESPACE_SIG, VERSAO_QRCODE
from pynfe.utils.webservices import NFCE

CHAVE = "4" * 44
CSC = "CSC-TEST-SECRET"


def _tag(namespace, name):
    return f"{{{namespace}}}{name}"


def _nota(chave=CHAVE):
    nfe = etree.Element(_tag(NAMESPACE_NFE, "NFe"), nsmap={None: NAMESPACE_NFE})
    inf = etree.SubElement(nfe, _tag(NAMESPACE_NFE, "infNFe"))
    inf.set("Id", "NFe" + chave)
    ide = etree.SubElement(inf, _tag(NAMESPACE_NFE, "ide"))
    etree.SubElement(ide, _tag(NAMESPACE_NFE, "cUF")).text = "41"
    etree.SubElement(ide, _tag(NAMESPACE_NFE, "dhEmi")).text = "2024-01-15T10:00:00-03:00"
    etree.SubElement(ide, _tag(NAMESPACE_NFE, "tpAmb")).text = "1"
    total = etree.SubElement(inf, _tag(NAMESPACE_NFE, "total"))
    icms = etree.SubElement(total, _tag(NAMESPACE_NFE, "ICMSTot"))
    etree.SubElement(icms, _tag(NAMESPACE_NFE, "vNF")).text = "10.00"
    signature = etree.SubElement(nfe, _tag(NAMESPACE_SIG, "Signature"))
    signed = etree.SubElement(signature, _tag(NAMESPACE_SIG, "SignedInfo"))
    reference = etree.SubElement(signed, _tag(NAMESPACE_SIG, "Reference"))
    etree.SubElement(reference, _tag(NAMESPACE_SIG, "DigestValue")).text = "abc="
    return nfe


def _parametro(qrcode):
    return qrcode.split("p=", 1)[1]


class NfceQrCodeCscTest(unittest.TestCase):
    def test_id_do_csc_preserva_zero_significativo(self):
        _, qrcode = SerializacaoQrcode().gerar_qrcode(
            "000100", CSC, _nota(), return_qr=True, online=True
        )
        parametro = _parametro(qrcode)
        campos = parametro.split("|")
        self.assertEqual(campos[3], "100")
        payload = "|".join(campos[:4])
        esperado = hashlib.sha1((payload + CSC).encode()).hexdigest().upper()
        self.assertEqual(campos[4], esperado)
        self.assertTrue(qrcode.startswith(NFCE["PR"]["QR"]))
        self.assertEqual(campos[1], VERSAO_QRCODE)

    def test_id_do_csc_remove_apenas_zeros_a_esquerda(self):
        _, qrcode = SerializacaoQrcode().gerar_qrcode(
            "000001", CSC, _nota(), return_qr=True, online=True
        )
        self.assertEqual(_parametro(qrcode).split("|")[3], "1")


if __name__ == "__main__":
    unittest.main()
