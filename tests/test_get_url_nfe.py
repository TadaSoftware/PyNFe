from pynfe.processamento.comunicacao import ComunicacaoSefaz
from pynfe.utils.flags import NAMESPACE_NFE
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

certificado = "certificado/certificado_mixpel.pfx"
senha = 'lucilene570'
url_prod = None
url_hom = None


class TestGetUrl(unittest.TestCase):

    def dadosPagina(informacoes):
        listaServicos = []
        servicos = []
        contador = 0
        for informacao in informacoes:
            contador  = contador + 1
            servicos.append(informacao.text)
            if contador == 3:
                listaServicos.append(servicos)
                servicos = []
                contador = 0
        return listaServicos

    def filtragemListHom(listaServicos):
        urls = []
        for listaServico in listaServicos:
            if listaServico[1] == "4.00":
                urls.append(listaServico)
        list_estados = ['AM','AM','AM','AM','AM','AM',
                        'BA','BA','BA','BA','BA','BA','BA',
                        'CE','CE','CE','CE','CE','CE',
                        'GO','GO','GO','GO','GO','GO','GO',
                        'MG','MG','MG','MG','MG','MG',
                        'MS','MS','MS','MS','MS','MS','MS',
                        'MT','MT','MT','MT','MT','MT','MT',
                        'PE','PE','PE','PE','PE','PE','PE',
                        'PR','PR','PR','PR','PR','PR','PR',
                        'RS','RS','RS','RS','RS','RS',
                        'SP','SP','SP','SP','SP','SP','SP',
                        'SVAN','SVAN','SVAN','SVAN','SVAN','SVAN',
                        'SVRS','SVRS','SVRS','SVRS','SVRS','SVRS','SVRS',
                        'SVC-AN','SVC-AN','SVC-AN','SVC-AN','SVC-AN',
                        'SVC-RS','SVC-RS','SVC-RS','SVC-RS','SVC-RS',
                        'AN'
                        ]
        urls=[x + [y] for x, y in zip(urls, list_estados)]
        return urls


    def filtragemListProd(listaServicos):
        urlsp = []
        for listaServico in listaServicos:
            if listaServico[1] == "4.00":
                urlsp.append(listaServico)
        list_estados = ['AM','AM','AM','AM','AM','AM',
                        'BA','BA','BA','BA','BA','BA','BA',
                        'CE','CE','CE','CE','CE','CE','CE',
                        'GO','GO','GO','GO','GO','GO','GO',
                        'MG','MG','MG','MG','MG','MG',
                        'MS','MS','MS','MS','MS','MS','MS',
                        'MT','MT','MT','MT','MT','MT','MT',
                        'PE','PE','PE','PE','PE','PE','PE',
                        'PR','PR','PR','PR','PR','PR','PR',
                        'RS','RS','RS','RS','RS','RS','RS',
                        'SP','SP','SP','SP','SP','SP','SP',
                        'SVAN','SVAN','SVAN','SVAN','SVAN','SVAN',
                        'SVRS','SVRS','SVRS','SVRS','SVRS','SVRS','SVRS',
                        'SVC-AN','SVC-AN','SVC-AN','SVC-AN','SVC-AN',
                        'SVC-RS','SVC-RS','SVC-RS','SVC-RS','SVC-RS',
                        'AN'
                        ]
        urlsp=[x + [y] for x, y in zip(urlsp, list_estados)]
        return urlsp

    def nomeEventos(urls):
        for url in urls:
            if url[0] == "NfeInutilizacao":
                url[0] = "INUTILIZACAO"
            if url[0] == "NfeConsultaProtocolo":
                url[0] = "CHAVE"
            if url[0] == "NfeStatusServico":
                url[0] = "STATUS"
            if url[0] == "RecepcaoEvento":
                url[0] = "EVENTOS"
            if url[0] == "NFeAutorizacao":
                url[0] = "AUTORIZACAO"
            if url[0] == "NFeRetAutorizacao":
                url[0] = "RECIBO"
            if url[0] == "NfeConsultaCadastro":
                url[0] = "CADASTRO"
        return urls




    # Pré-Teste para buscar os dados do WebService da Receita em NFe
    @classmethod
    def setUpClass(self):
        # Firefox
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(10)
        # Abre a pagina do WebService da Receita para NFe em Produção
        driver.get("http://www.nfe.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=Wak0FwB7dKs=")
        #busca os elementos da pagina com classe igual a altura21
        informacoes = driver.find_elements_by_class_name('altura21')
        #armazena todos os dados armazenados em informacoes e separa-os em uma list de lists,
        #onde cada uma das lists internas armazena os dados referentes ao nome do evento, a versão do evento e a url do evento
        listaServicos = TestGetUrl.dadosPagina(informacoes)
        #realiza uma filtragem interna nas lists, armazenando apenas as lists da versão 4.00 do webService e adicionando no final de cada list o estado que pertence o serviço
        urlsp = TestGetUrl.filtragemListProd(listaServicos)
        #altera os nomes dos serviços armazenados na list
        urlsp = TestGetUrl.nomeEventos(urls=urlsp)
        global url_prod
        url_prod = urlsp

        # Abre a pagina do WebService da Receita para NFe em Homologação
        driver.get("http://hom.nfe.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=Wak0FwB7dKs=")
        driver.set_page_load_timeout(10)
        #busca os elementos da pagina com classe igual a altura21
        informacoes = driver.find_elements_by_class_name('altura21')
        #armazena todos os dados armazenados em informacoes e separa-os em uma list de lists,
        #onde cada uma das lists internas armazena os dados referentes ao nome do evento, a versão do evento e a url do evento
        listaServicos = TestGetUrl.dadosPagina(informacoes)
        #realiza uma filtragem interna nas lists, armazenando apenas as lists da versão 4.00 do webService e adicionando no final de cada list o estado que pertence o serviço
        urls = TestGetUrl.filtragemListHom(listaServicos)
        #altera os nomes dos serviços armazenados na list
        urls = TestGetUrl.nomeEventos(urls)
        global url_hom
        url_hom = urls
        driver.quit()


    def test_get_url_an(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "an"

        with self.subTest("Erro do WebService em Homologação em AN"):
            for estado in url_hom:
                if estado[3]=="AN":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em AN"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="AN":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1


    def test_get_url_am(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "am"


        with self.subTest("Erro do WebService em Homologação em AM"):
            for estado in url_hom:
                if estado[3]=="AM":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em AM"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="AM":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                test=self.assertEqual(url,list_web_service_prod[s])
                s=s+1


    def test_get_url_ce(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "ce"


        with self.subTest("Erro do WebService em Homologação em CE"):
            for estado in url_hom:
                if estado[3]=="CE":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em CE"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="CE":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1


    def test_get_url_pe(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "pe"


        with self.subTest("Erro do WebService em Homologação em PE"):
            for estado in url_hom:
                if estado[3]=="PE":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em PE"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="PE":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0

            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1


    def test_get_url_ba(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "ba"

        with self.subTest("Erro do WebService em Homologação em BA"):
            for estado in url_hom:
                if estado[3]=="BA":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em BA"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="BA":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1

    def test_get_url_mg(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "mg"


        with self.subTest("Erro do WebService em Homologação em MG"):
            for estado in url_hom:
                if estado[3]=="MG":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em MG"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="MG":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1


    def test_get_url_sp(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "sp"


        with self.subTest("Erro do WebService em Homologação em SP"):
            for estado in url_hom:
                if estado[3]=="SP":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em SP"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="SP":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1


    def test_get_url_pr(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = 'pr'


        with self.subTest("Erro do WebService em Homologação em PR"):
            for estado in url_hom:
                if estado[3]=="PR":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em PR"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="PR":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1


    def test_get_url_rs(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = 'rs'

        with self.subTest("Erro do WebService em Homologação em RS"):
            for estado in url_hom:
                if estado[3]=="RS":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em RS"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="RS":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1



    def test_get_url_mt(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = 'mt'

        with self.subTest("Erro do WebService em Homologação em MT"):
            for estado in url_hom:
                if estado[3]=="MT":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em MT"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="MT":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1



    def test_get_url_go(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "go"

        with self.subTest("Erro do WebService em Homologação em GO"):
            for estado in url_hom:
                if estado[3]=="GO":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em GO"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="GO":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1



    def test_get_url_ms(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = 'ms'

        with self.subTest("Erro do WebService em Homologação em MS"):
            for estado in url_hom:
                if estado[3]=="MS":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em MS"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="MS":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1



    def test_get_url_svan(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = 'SVAN'

        with self.subTest("Erro do WebService em Homologação em SVAN"):
            for estado in url_hom:
                if estado[3]=="SVAN":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em SVAN"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="SVAN":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1



    def test_get_url_svrs(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "svrs"


        with self.subTest("Erro do WebService em Homologação em SVRS"):
            for estado in url_hom:
                if estado[3]=="SVRS":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1


        with self.subTest("Erro do WebService em Produção em SVRS"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="SVRS":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1



    def test_get_url_svc_an(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "svc-an"


        with self.subTest("Erro do WebService em Homologação em SVC-AN"):
            for estado in url_hom:
                if estado[3]=="SVC-AN":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1

        with self.subTest("Erro do WebService em Produção em SVC-AN"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="SVC-AN":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1




    def test_get_url_svc_rs(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "svc-rs"

        with self.subTest("Erro do WebService em Homologação em SVC-RS"):
            for estado in url_hom:
                if estado[3]=="SVC-RS":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1

        with self.subTest("Erro do WebService em Produção em SVC-RS"):
            estado_webservice = []
            for estado in url_prod:
                if estado[3]=="SVC-RS":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfe',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1
