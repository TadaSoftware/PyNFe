import unittest

from pynfe.entidades.notafiscal import NotaFiscalServico
from tests.test_nfse_serializacao import SerializacaoNFSeTest


class SerializacaoNFSeBethaTestCase(unittest.TestCase):
    def test_notafiscal_geral(self):
        nfse = self._get_notafiscal_servico()
        nfse_xml = SerializacaoNFSeTest.serializa_nfse(nfse, 'betha')

        nfse_xml_assinado = SerializacaoNFSeTest.assina_xml(nfse_xml)
        nfse_esperada = self._get_nfse_esperada()

        # Teste do conteúdo das tags do XML
        self.maxDiff = None
        self.assertEqual(nfse_xml_assinado, nfse_esperada)

        # TODO: Testa a validação do XML com os schemas XSD
        # SerializacaoNFSeTest.validacao_com_xsd_do_xml_gerado_sem_processar(
        #     nfse_xml,
        #     nfse_xml_assinado,
        #     'nfse_v202.xsd',
        #     'pynfe/data/XSDs/NFS-e/Betha'
        # )

        SerializacaoNFSeTest.limpa_namespace()

    def _get_notafiscal_servico(self) -> NotaFiscalServico:
        nota_fiscal = SerializacaoNFSeTest.get_notafiscal_servico()
        nota_fiscal.servico.municipio_incidencia = nota_fiscal.servico.codigo_municipio

        return nota_fiscal

    def _get_nfse_esperada(self) -> str:
        return SerializacaoNFSeTest.strip_xml(f"""
            <GerarNfseEnvio xmlns="http://www.betha.com.br/e-nota-contribuinte-ws">
                <Rps>
                    <InfDeclaracaoPrestacaoServico Id="50">
                        <Rps>
                            <IdentificacaoRps>
                                <Numero>50</Numero>
                                <Serie>A1</Serie>
                                <Tipo>1</Tipo>
                            </IdentificacaoRps>
                            <DataEmissao>{SerializacaoNFSeTest.data_hora[:10]}</DataEmissao>
                            <Status>1</Status>
                        </Rps>
                        <Competencia>{SerializacaoNFSeTest.data_hora[:10]}</Competencia>
                        <Servico>
                            <Valores>
                                <ValorServicos>100.0</ValorServicos>
                            </Valores>
                            <IssRetido>1</IssRetido>
                            <ItemListaServico>0101</ItemListaServico>
                            <Discriminacao>Mensalidade</Discriminacao>
                            <CodigoMunicipio>3149309</CodigoMunicipio>
                            <ExigibilidadeISS>1</ExigibilidadeISS>
                            <MunicipioIncidencia>3149309</MunicipioIncidencia>
                        </Servico>
                        <Prestador>
                            <CpfCnpj>
                                <Cnpj>45111111111100</Cnpj>
                            </CpfCnpj>
                            <InscricaoMunicipal>000000</InscricaoMunicipal>
                        </Prestador>
                        <Tomador>
                            <RazaoSocial>NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL</RazaoSocial>
                            <Endereco>
                                <Endereco>Rua tal</Endereco>
                                <Numero>0</Numero>
                                <Bairro>Centro</Bairro>
                                <CodigoMunicipio>123</CodigoMunicipio>
                                <Uf>MG</Uf>
                                <CodigoPais>1058</CodigoPais>
                                <Cep>33257010</Cep>
                            </Endereco>
                        </Tomador>
                        <OptanteSimplesNacional>1</OptanteSimplesNacional>
                        <IncentivoFiscal>2</IncentivoFiscal>
                    </InfDeclaracaoPrestacaoServico>
                </Rps>
                <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
                    <SignedInfo>
                        <CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
                        <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
                        <Reference URI="#50">
                            <Transforms>
                                <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
                                <Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
                            </Transforms>
                            <DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
                            <DigestValue>zKwAgg0wya+wUPDgBq7Uvtv4Q+k=</DigestValue>
                        </Reference>
                    </SignedInfo>
                    <SignatureValue>ak3Ze/cqE4FXmXt0BrUOz7FWOBDH6i2V6ADeF9p8qTBdYCZa5hKFJoQkYpmd8T4lgtn6W4SDDsh0aXvhPn4UXGt5qOulfzBWrlU5+ohldDo60SBZ4gP2DVVtjmGqP0GtdBGp2U+1y75+8brJIUzgGQQxw9fArdlPyB6D6x/GEYo=</SignatureValue>
                    <KeyInfo>
                        <X509Data>
                            <X509Certificate>MIICMTCCAZqgAwIBAgIQfYOsIEVuAJ1FwwcTrY0t1DANBgkqhkiG9w0BAQUFADBX\nMVUwUwYDVQQDHkwAewA1ADkARgAxAEUANAA2ADEALQBEAEQARQA1AC0ANABEADIA\nRgAtAEEAMAAxAEEALQA4ADMAMwAyADIAQQA5AEUAQgA4ADMAOAB9MB4XDTE1MDYx\nNTA1NDc1N1oXDTE2MDYxNDExNDc1N1owVzFVMFMGA1UEAx5MAHsANQA5AEYAMQBF\nADQANgAxAC0ARABEAEUANQAtADQARAAyAEYALQBBADAAMQBBAC0AOAAzADMAMgAy\nAEEAOQBFAEIAOAAzADgAfTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAk41G\nnqXXLaiOC/y0/cA4tbS+NZCqI+x4EsztgDFvPPlHstiVYcLRkni4i93gK9zoC6g0\nmh66HMVzAfE8vRNwW5b7m6nWS1SiHBon7/Mqsw4MIq3SC+J/fTbKpqwyfAuH2YZl\nAiQuQc85fyllAMLh2WrA7JgOLR/5tF3kLtpbHdECAwEAATANBgkqhkiG9w0BAQUF\nAAOBgQArdh+RyT6VxKGsXk1zhHsgwXfToe6GpTF4W8PHI1+T0WIsNForDhvst6nm\nQtgAhuZM9rxpOJuNKc+pM29EixpAiZZiRMCSWEItNyEVdUIi+YnKBcAHd88TwO86\nd126MWQ2O8cu5W1VoDp7hYBYKOnLbYi11/StO+0rzK+oPYAvIw==\n</X509Certificate>
                        </X509Data>
                    </KeyInfo>
                </Signature>
            </GerarNfseEnvio>""")


if __name__ == "__main__":
    unittest.main()
