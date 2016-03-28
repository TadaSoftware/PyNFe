Documentação PyNFE!
=============================

Contents:

.. toctree::
   :maxdepth: 2


Visão Geral
-----------

Biblioteca de interface com o webservice de Nota Fiscal Eletronica,
(NF-e/NFC-e) da SEFAZ, oficializada pelo Ministerio da Fazendo do
Governo do Brasil.
Desenvolvido e testado com Python 3 no GNU/Linux.

A NF-e visa substituir as notas fiscais séries 1 e 1A.
A NFC-e visa substituir as notas fiscais modelo 2 e
cupom fiscal emitido por ECF.


Dependências
------------

- Java 8u51
  - para a geração da DANFE
- lxml
  - biblioteca de leitura e gravação de arquivos XML, de alta performance e fácil de implementar.
- xmlsec1 e openssl
  - assinatura e validação do XML
- requests
  - biblioteca para a comunicação com os webservices da SEFAZ

Referências
-----------

- Site oficial da Nota Fiscal eletrônica
  - http://www.nfe.fazenda.gov.br/portal/

- lxml
  - http://lxml.de/

- Tutorial de lxml
   - http://codespeak.net/lxml/tutorial.html

- requests
  - http://docs.python-requests.org/en/latest/
  - https://github.com/kennethreitz/requests
  - https://pypi.python.org/pypi/requests

- Exemplos de arquivos XML
  - http://www.javac.com.br/jc/downloads.javac?cat=3

- Schemas para validação dos arquivos
  - http://www.nfe.fazenda.gov.br/portal/schemas.aspx

- Validao de XML via XSD no lxml
   - http://codespeak.net/lxml/validation.html#xmlschema

- Lista de codigos para campo EX TIPI
   - http://www.fisconet.com.br/ipi/tipi/04.htm

- Certificado para testes
   - http://nf-eletronica.com/blog/?p=133

- Instalação::

   pip3 install --user https://github.com/leotada/PyNFe/archive/master.zip

- Instalação opcional para NFS-e::

    pip3 install --user -r https://github.com/leotada/PyNFe/raw/master/requirements-nfse.txt

Exemplos de uso
---------------
Consulta Status::

   from pynfe.processamento.comunicacao import ComunicacaoSefaz

   certificado = "/home/user/certificado.pfx"
   senha = 'senha'
   uf = 'pr'
   homologacao = True

   con = ComunicacaoSefaz(uf, certificado, senha, homologacao)
   xml = con.status_servico('nfe')
   print (xml.text)

Consulta Notas Emitidas para um CNPJ (apenas NF-e e no RS)::


   from pynfe.processamento.comunicacao import ComunicacaoSefaz

   certificado = "/home/user/certificado.pfx"
   senha = 'senha'
   uf = 'rs'
   homologacao = True

   con = ComunicacaoSefaz(uf, certificado, senha, homologacao)
   # informar cnpj que deseja consultar (String) e nsu (inteiro) (por default se não informar nsu ele assumirá o valor 0, retornando as dos últimos 15 dias)
   xml = con.consulta_notas_cnpj(cnpj='cnpj_somente_numeros', nsu=0)

   print (xml.text)
