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
            <GerarNfseEnvio xmlns:ns1="http://www.betha.com.br/e-nota-contribuinte-ws">
                <ns1:Rps>
                    <ns1:InfDeclaracaoPrestacaoServico Id="50">
                        <ns1:Rps>
                            <ns1:IdentificacaoRps>
                                <ns1:Numero>50</ns1:Numero>
                                <ns1:Serie>A1</ns1:Serie>
                                <ns1:Tipo>1</ns1:Tipo>
                            </ns1:IdentificacaoRps>
                            <ns1:DataEmissao>{SerializacaoNFSeTest.data_hora[:10]}</ns1:DataEmissao>
                            <ns1:Status>1</ns1:Status>
                        </ns1:Rps>
                        <ns1:Competencia>{SerializacaoNFSeTest.data_hora[:10]}</ns1:Competencia>
                        <ns1:Servico>
                            <ns1:Valores>
                                <ns1:ValorServicos>100.0</ns1:ValorServicos>
                            </ns1:Valores>
                            <ns1:IssRetido>1</ns1:IssRetido>
                            <ns1:ItemListaServico>0101</ns1:ItemListaServico>
                            <ns1:Discriminacao>Mensalidade</ns1:Discriminacao>
                            <ns1:CodigoMunicipio>3149309</ns1:CodigoMunicipio>
                            <ns1:ExigibilidadeISS>0</ns1:ExigibilidadeISS>
                            <ns1:MunicipioIncidencia>3149309</ns1:MunicipioIncidencia>
                        </ns1:Servico>
                        <ns1:Prestador>
                            <ns1:CpfCnpj>
                                <ns1:Cnpj>99999999999999</ns1:Cnpj>
                            </ns1:CpfCnpj>
                            <ns1:InscricaoMunicipal>000000</ns1:InscricaoMunicipal>
                        </ns1:Prestador>
                        <ns1:Tomador>
                            <ns1:RazaoSocial>NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL</ns1:RazaoSocial>
                            <ns1:Endereco>
                                <ns1:Endereco>Rua tal</ns1:Endereco>
                                <ns1:Numero>0</ns1:Numero>
                                <ns1:Bairro>Centro</ns1:Bairro>
                                <ns1:CodigoMunicipio>123</ns1:CodigoMunicipio>
                                <ns1:Uf>MG</ns1:Uf>
                                <ns1:CodigoPais>1058</ns1:CodigoPais>
                                <ns1:Cep>33257010</ns1:Cep>
                            </ns1:Endereco>
                        </ns1:Tomador>
                        <ns1:OptanteSimplesNacional>1</ns1:OptanteSimplesNacional>
                        <ns1:IncentivoFiscal>2</ns1:IncentivoFiscal>
                    </ns1:InfDeclaracaoPrestacaoServico>
                </ns1:Rps>
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
                            <DigestValue>xzbAflAhVih7JNxmSa2ZJ1rMpzw=</DigestValue>
                        </Reference>
                    </SignedInfo>
                    <SignatureValue>W6Ys1KHIbz9BDtG+ej++ROAkqZTtSgYH2cplorcxxOZ2VJG3KKWnasyLghEIJfcXtss4kjblgdGOf3IJVgaDuub4GyYPkEzCxnGEr1nQXw74rDmGLwZg1vPBUdHsIbcw8wvAoUOW6zfMI5ljr61Rz5CCytBu4IqpUFCQzWguiG8=</SignatureValue>
                    <KeyInfo>
                        <X509Data>
                            <X509Certificate>MIICMTCCAZqgAwIBAgIQfYOsIEVuAJ1FwwcTrY0t1DANBgkqhkiG9w0BAQUFADBXMVUwUwYDVQQDHkwAewA1ADkARgAxAEUANAA2ADEALQBEAEQARQA1AC0ANABEADIARgAtAEEAMAAxAEEALQA4ADMAMwAyADIAQQA5AEUAQgA4ADMAOAB9MB4XDTE1MDYxNTA1NDc1N1oXDTE2MDYxNDExNDc1N1owVzFVMFMGA1UEAx5MAHsANQA5AEYAMQBFADQANgAxAC0ARABEAEUANQAtADQARAAyAEYALQBBADAAMQBBAC0AOAAzADMAMgAyAEEAOQBFAEIAOAAzADgAfTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAk41GnqXXLaiOC/y0/cA4tbS+NZCqI+x4EsztgDFvPPlHstiVYcLRkni4i93gK9zoC6g0mh66HMVzAfE8vRNwW5b7m6nWS1SiHBon7/Mqsw4MIq3SC+J/fTbKpqwyfAuH2YZlAiQuQc85fyllAMLh2WrA7JgOLR/5tF3kLtpbHdECAwEAATANBgkqhkiG9w0BAQUFAAOBgQArdh+RyT6VxKGsXk1zhHsgwXfToe6GpTF4W8PHI1+T0WIsNForDhvst6nmQtgAhuZM9rxpOJuNKc+pM29EixpAiZZiRMCSWEItNyEVdUIi+YnKBcAHd88TwO86d126MWQ2O8cu5W1VoDp7hYBYKOnLbYi11/StO+0rzK+oPYAvIw==</X509Certificate>
                        </X509Data>
                    </KeyInfo>
                </Signature>
            </GerarNfseEnvio>""")


if __name__ == "__main__":
    unittest.main()
