from pynfe.processamento.comunicacao import ComunicacaoSefaz
from pynfe.utils.flags import NAMESPACE_NFE
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re

import unittest
certificado = "certificado/certificado_mixpel.pfx"
senha = 'lucilene570'
url_prod = None
url_hom = None



class TestGetUrl(unittest.TestCase):


    def dadosPagina(informacoes):
        tabelaServicos = []
        for informacao in informacoes:
            tabelaServicos.append(informacao.text)
        listaServicos = [s.split('\n') for s in tabelaServicos]
        return listaServicos


    def filtragemListProd(listaServicos):
        linhaServicos = []
        regexp = re.compile('[a-zA-z0-9]+[ ]+[4.00]+[ ]+[a-zA-Z0-9:?//.-]*')
        for servicos in listaServicos:
            for servico in servicos:
                if regexp.match(servico):
                    linhaServicos.append(servico)

        listaServicos = [s.split(' ') for s in linhaServicos]
        list_estados = ["AM","AM","AM","AM","AM","AM",
                        "GO","GO","GO","GO","GO","GO","GO",
                        "MT","MT","MT","MT","MT","MT",
                        "MS","MS","MS","MS","MS","MS","MS",
                        "MG","MG","MG","MG","MG","MG","MG",
                        "PR","PR","PR","PR","PR","PR","PR",
                        "RS","RS","RS","RS","RS","RS",
                        "SVRS","SVRS","SVRS","SVRS","SVRS","SVRS",
                        "SP","SP","SP","SP","SP","SP"
                        ]
        listaServicos=[x + [y] for x, y in zip(listaServicos, list_estados)]
        return listaServicos


    def filtragemListHom(listaServicos):
        linhaServicos = []
        regexp = re.compile('[a-zA-z0-9]+[ ]+[4.00]+[ ]+[a-zA-Z0-9:?//.-]*')
        for servicos in listaServicos:
            for servico in servicos:
                if regexp.match(servico):
                    linhaServicos.append(servico)

        listaServicos = [s.split(' ') for s in linhaServicos]
        list_estados = ["AM","AM","AM","AM","AM","AM",
                        "GO","GO","GO","GO","GO","GO","GO",
                        "MT","MT","MT","MT","MT","MT",
                        "MS","MS","MS","MS","MS","MS","MS",
                        "MG","MG","MG","MG","MG","MG","MG",
                        "PR","PR","PR","PR","PR","PR","PR",
                        "RS","RS","RS","RS","RS","RS",
                        "SVRS","SVRS","SVRS","SVRS","SVRS","SVRS",
                        "SP","SP","SP","SP","SP","SP"
                        ]
        listaServicos=[x + [y] for x, y in zip(listaServicos, list_estados)]
        return listaServicos


    def nomeEventos(listaServicos):
        for listaServico in listaServicos:
            if listaServico[0] == "NfeInutilizacao":
                listaServico[0] = "INUTILIZACAO"
            if listaServico[0] == "NfeConsultaProtocolo":
                listaServico[0] = "CHAVE"
            if listaServico[0] == "NfeStatusServico":
                listaServico[0] = "STATUS"
            if listaServico[0] == "RecepcaoEvento":
                listaServico[0] = "EVENTOS"
            if listaServico[0] == "NFeAutorizacao":
                listaServico[0] = "AUTORIZACAO"
            if listaServico[0] == "NFeRetAutorizacao":
                listaServico[0] = "RECIBO"
            if listaServico[0] == "NfeConsultaCadastro":
                listaServico[0] = "CADASTRO"
        return listaServicos




    @classmethod
    def setUpClass(cls):

        # Firefox
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(10)
        #Abre a pagina do WebService da Receita para NFCe em Produção
        driver.get("http://nfce.encat.org/desenvolvedor/webservices-p/")
        #Busca todas as tables da Pagina
        informacoes = driver.find_elements(By.XPATH,'//table')
        #busca todos os elementos das tabelas do WebService da Receita, e separa-os em elementos de uma list.
        listaServicos = TestGetUrl.dadosPagina(informacoes)
        #Realiza uma filtragem de elementos na List, buscando por expressão regular os elementos da versão 4.00,
        #Adicionando no final de cada list, o estado que pertence o evento correspondente
        listaServicos = TestGetUrl.filtragemListProd(listaServicos)
        #Altera os nomes dos serviços armazenados na list
        listaServicos = TestGetUrl.nomeEventos(listaServicos)

        global url_prod
        url_prod = listaServicos


        #busca todos os elementos das tabelas do WebService da Receita, e separa-os em elementos de uma list.
        driver.get("http://nfce.encat.org/desenvolvedor/webservices-h/")
        #Busca todas as tables da Pagina
        informacoes = driver.find_elements(By.XPATH,'//table')
        #busca todos os elementos das tabelas do WebService da Receita, e separa-os em elementos de uma list.
        listaServicos = TestGetUrl.dadosPagina(informacoes)
        #Realiza uma filtragem de elementos na List, buscando por expressão regular os elementos da versão 4.00,
        #Adicionando no final de cada list, o estado que pertence o evento correspondente
        listaServicos = TestGetUrl.filtragemListHom(listaServicos)
        #Altera os nomes dos serviços armazenados na list
        listaServicos = TestGetUrl.nomeEventos(listaServicos)

        global url_hom
        url_hom = listaServicos


        driver.quit()



    def test_get_url_am(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf="am"

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
                url = con._get_url('nfce',servico)
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
                url = con._get_url('nfce',servico)
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
        uf = 'mg'

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
                url = con._get_url('nfce',servico)
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
                url = con._get_url('nfce',servico)
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
        uf = 'sp'

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
                url = con._get_url('nfce',servico)
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
                url = con._get_url('nfce',servico)
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
                url = con._get_url('nfce',servico)
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
                url = con._get_url('nfce',servico)
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
        uf = "rs"


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
                url = con._get_url('nfce',servico)
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
                url = con._get_url('nfce',servico)
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
        uf = "ms"

        with self.subTest("Erro do WebService em Produção em MS"):
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
                url = con._get_url('nfce',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1

        with self.subTest("Erro do WebService em Homologação em MS"):
            estado_webservice = []
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
                url = con._get_url('nfce',servico)
                self.assertEqual(url,list_web_service_hom[s])
                s=s+1



    def test_get_url_mt(self):
        global url_prod
        global url_hom
        estado_webservice = []
        list_web_service_prod = []
        list_servicos_prod = []
        list_web_service_hom = []
        list_servicos_hom = []
        uf = "mt"

        with self.subTest("Erro do WebService em Produção em MT"):
            for estado in url_prod:
                if estado[3]=="MT":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_prod.append(servico[2])
            for servico in estado_webservice:
                list_servicos_prod.append(servico[0])

            homologacao = True
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_prod:
                url = con._get_url('nfce',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1

        with self.subTest("Erro do WebService em Homologação em MT"):
            estado_webservice = []
            for estado in url_hom:
                if estado[3]=="MT":
                    estado_webservice.append(estado)
            for servico in estado_webservice:
                list_web_service_hom.append(servico[2])
            for servico in estado_webservice:
                list_servicos_hom.append(servico[0])

            homologacao = False
            con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
            s = 0
            for servico in list_servicos_hom:
                url = con._get_url('nfce',servico)
                self.assertEqual(url,list_web_service_hom[s])
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
                url = con._get_url('nfce',servico)
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
                url = con._get_url('nfce',servico)
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
                url = con._get_url('nfce',servico)
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
                url = con._get_url('nfce',servico)
                self.assertEqual(url,list_web_service_prod[s])
                s=s+1
