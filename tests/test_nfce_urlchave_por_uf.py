#!/usr/bin/env python
# *-* encoding: utf8 *-*
"""Pins the ``<urlChave>`` of every UF that can emit NFC-e.

``<qrCode>`` and ``<urlChave>`` are different fields with different official registries.
GO rejects 878 ("Endereco do site da UF da Consulta por chave de acesso diverge do
previsto") when the QR Code address is emitted as ``urlChave`` - which is what PyNFe did
for GO until DEV-2468, because IT 2025.003 only ever defined the QR Code URL.

Reference values come from the ACBr registry
(``ACBrNFeServicos.ini``, ``URL-ConsultaNFCe_2.00`` of ``[NFCe_<UF>_P]`` / ``[NFCe_<UF>_H]``),
cross-checked against the ENCAT listing for GO. The corrupted/outdated UFs left untouched in
this round are inventoried in
``docs/issues/followup-dev-2468-urlchave-ufs-sem-loja.md`` of the workspace repo, and pinned
here as exact sets so a NEW corruption fails the suite and fixing an old one forces the list
to shrink.
"""

import unittest

from lxml import etree

from pynfe.processamento.serializacao import SerializacaoQrcode
from pynfe.utils.flags import CODIGOS_ESTADOS, NAMESPACE_NFE, NAMESPACE_SIG
from pynfe.utils.webservices import NFCE, url_consulta_chave

TP_AMB_PRODUCAO = "1"
TP_AMB_HOMOLOGACAO = "2"

# UFs corrigidas nesta rodada: valor verbatim do registro, por ambiente.
CORRIGIDAS = {
    "GO": {
        TP_AMB_PRODUCAO: "http://www.sefaz.go.gov.br/nfce/consulta",
        TP_AMB_HOMOLOGACAO: (
            "http://www.nfce.go.gov.br/post/ver/214413/consulta-nfc-e-homologacao"
        ),
    },
    "BA": {
        TP_AMB_PRODUCAO: "http://www.sefaz.ba.gov.br/nfce/consulta",
        TP_AMB_HOMOLOGACAO: "http://hinternet.sefaz.ba.gov.br/nfce/consulta",
    },
    "PR": {
        TP_AMB_PRODUCAO: "http://www.fazenda.pr.gov.br/nfce/consulta",
        TP_AMB_HOMOLOGACAO: "http://www.fazenda.pr.gov.br/nfce/consulta",
    },
}

# UFs que ja batiam com o registro e nao podem mudar um byte. RJ carrega a maior parte da
# frota, entao e a nao-regressao mais importante do arquivo.
NAO_REGRESSAO = {
    "RJ": {
        TP_AMB_PRODUCAO: "www.fazenda.rj.gov.br/nfce/consulta",
        TP_AMB_HOMOLOGACAO: "www.fazenda.rj.gov.br/nfce/consulta",
    },
    "AC": {
        TP_AMB_PRODUCAO: "http://www.sefaznet.ac.gov.br/nfce/consulta",
        TP_AMB_HOMOLOGACAO: "http://hml.sefaznet.ac.gov.br/nfce/consulta",
    },
    "DF": {
        TP_AMB_PRODUCAO: "www.fazenda.df.gov.br/nfce/consulta",
        TP_AMB_HOMOLOGACAO: "www.fazenda.df.gov.br/nfce/consulta",
    },
    "PE": {
        TP_AMB_PRODUCAO: "http://nfce.sefaz.pe.gov.br/nfce/consulta",
        TP_AMB_HOMOLOGACAO: "http://nfcehomolog.sefaz.pe.gov.br/nfce/consulta",
    },
    "SC": {
        TP_AMB_PRODUCAO: "https://sat.sef.sc.gov.br/nfce/consulta",
        TP_AMB_HOMOLOGACAO: "https://hom.sat.sef.sc.gov.br/nfce/consulta",
    },
}

# UFs sem endereco de consulta cadastrado: nao emitem NFC-e por este fork.
UFS_SEM_URLCHAVE = frozenset({"AL", "MA", "MT", "PB", "PI", "RN", "TO"})

# Divergencias conhecidas e deliberadamente NAO corrigidas (sem loja para validar).
# "http" repetido = prefixo de host concatenado sobre uma URL que ja tinha esquema.
UFS_URLCHAVE_COM_ESQUEMA_DUPLICADO = frozenset({"AP", "MS"})
# ".www." no meio do host = prefixo de host concatenado sobre um hostname completo.
UFS_URLCHAVE_COM_HOST_DUPLICADO = frozenset({"ES"})
# UFs em que o registro oficial usa o MESMO endereco para consulta e QR Code (SC: o proprio
# ACBr registra sat.sef.sc.gov.br/nfce/consulta nos dois) ou em que o valor legado ainda
# aponta para o leitor de QR (RS, pendente de correcao).
UFS_URLCHAVE_IGUAL_AO_QRCODE = frozenset({"RS", "SC"})

UFS_EMISSORAS = sorted(set(NFCE) - {"SVRS"} - UFS_SEM_URLCHAVE)


def _nfe(uf, tp_amb):
    cuf = CODIGOS_ESTADOS[uf]
    chave = cuf + "0" * 42
    xml = (
        f'<NFe xmlns="{NAMESPACE_NFE}">'
        f'<infNFe Id="NFe{chave}">'
        f"<ide><cUF>{cuf}</cUF><dhEmi>2025-01-14T12:00:00-03:00</dhEmi>"
        f"<tpAmb>{tp_amb}</tpAmb></ide>"
        f"<dest><CPF>12345678900</CPF></dest>"
        f"<total><ICMSTot><vNF>10.00</vNF></ICMSTot></total>"
        f"</infNFe>"
        f'<Signature xmlns="{NAMESPACE_SIG}"><SignedInfo><Reference>'
        f"<DigestValue>ABCDEF==</DigestValue>"
        f"</Reference></SignedInfo></Signature>"
        f"</NFe>"
    )
    return etree.fromstring(xml.encode())


def _emitir(uf, tp_amb):
    nfe, qrcode = SerializacaoQrcode().gerar_qrcode(
        "000001", "CSC123", _nfe(uf, tp_amb), return_qr=True
    )
    return qrcode, nfe.find("infNFeSupl").find("urlChave").text


class UrlChaveRegistroTestCase(unittest.TestCase):
    def test_ufs_corrigidas_emitem_valor_do_registro(self):
        for uf, ambientes in CORRIGIDAS.items():
            for tp_amb, esperado in ambientes.items():
                with self.subTest(uf=uf, tpAmb=tp_amb):
                    _, url_chave = _emitir(uf, tp_amb)
                    self.assertEqual(url_chave, esperado)

    def test_ufs_ja_corretas_nao_mudam(self):
        for uf, ambientes in NAO_REGRESSAO.items():
            for tp_amb, esperado in ambientes.items():
                with self.subTest(uf=uf, tpAmb=tp_amb):
                    _, url_chave = _emitir(uf, tp_amb)
                    self.assertEqual(url_chave, esperado)

    def test_qrcode_de_go_continua_no_portal_do_it_2025_003(self):
        """A correcao do urlChave nao pode arrastar o qrCode (DEV-2177/IT 2025.003)."""
        qrcode, _ = _emitir("GO", TP_AMB_PRODUCAO)
        self.assertTrue(
            qrcode.startswith("https://nfeweb.sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe?"),
            f"qrCode de GO regrediu: {qrcode}",
        )
        qrcode_hom, _ = _emitir("GO", TP_AMB_HOMOLOGACAO)
        self.assertTrue(
            qrcode_hom.startswith(
                "https://nfewebhomolog.sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe?"
            ),
            f"qrCode de GO em homologacao regrediu: {qrcode_hom}",
        )

    def test_ufs_sem_endereco_de_consulta_nao_emitem(self):
        for uf in sorted(UFS_SEM_URLCHAVE):
            with self.subTest(uf=uf):
                with self.assertRaises(KeyError):
                    url_consulta_chave(uf, producao=True)


class UrlChaveIntegridadeTestCase(unittest.TestCase):
    """Propriedades que valem para a tabela inteira, nao so para as UFs desta rodada."""

    def test_urlchave_nunca_tem_esquema_concatenado(self):
        encontradas = set()
        for uf in UFS_EMISSORAS:
            for tp_amb in (TP_AMB_PRODUCAO, TP_AMB_HOMOLOGACAO):
                _, url_chave = _emitir(uf, tp_amb)
                if url_chave.count("http") > 1:
                    encontradas.add(uf)
        self.assertEqual(
            encontradas,
            set(UFS_URLCHAVE_COM_ESQUEMA_DUPLICADO),
            "conjunto de UFs com esquema duplicado no urlChave mudou; corrija a UF ou "
            "atualize UFS_URLCHAVE_COM_ESQUEMA_DUPLICADO",
        )

    def test_urlchave_nunca_tem_host_concatenado(self):
        encontradas = set()
        for uf in UFS_EMISSORAS:
            for tp_amb in (TP_AMB_PRODUCAO, TP_AMB_HOMOLOGACAO):
                _, url_chave = _emitir(uf, tp_amb)
                host = url_chave.split("://")[-1].split("/")[0]
                if ".www." in host:
                    encontradas.add(uf)
        self.assertEqual(
            encontradas,
            set(UFS_URLCHAVE_COM_HOST_DUPLICADO),
            "conjunto de UFs com host duplicado no urlChave mudou; corrija a UF ou "
            "atualize UFS_URLCHAVE_COM_HOST_DUPLICADO",
        )

    def test_urlchave_nao_e_o_endereco_do_qrcode(self):
        encontradas = set()
        for uf in UFS_EMISSORAS:
            for tp_amb in (TP_AMB_PRODUCAO, TP_AMB_HOMOLOGACAO):
                qrcode, url_chave = _emitir(uf, tp_amb)
                base_qr = qrcode.split("?")[0]
                self.assertNotEqual(qrcode, url_chave, f"{uf}/{tp_amb}")
                if base_qr == url_chave:
                    encontradas.add(uf)
        self.assertEqual(
            encontradas,
            set(UFS_URLCHAVE_IGUAL_AO_QRCODE),
            "conjunto de UFs cujo urlChave repete o endereco do qrCode mudou; foi "
            "exatamente esse defeito que gerou a rejeicao 878 em GO",
        )


if __name__ == "__main__":
    unittest.main()
