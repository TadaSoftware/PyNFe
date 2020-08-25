
Atualizado para a versão 4.00 NF-e/NFC-e
-----------

Visão Geral
-----------

Biblioteca de interface com o webservice de Nota Fiscal Eletronica,
(NF-e/NFC-e/NFS-e) da SEFAZ, oficializada pelo Ministerio da Fazendo do
Governo do Brasil.  
Desenvolvido e testado com Python 3.6 no GNU/Linux.

A NF-e visa substituir as notas fiscais séries 1 e 1A.  
A NFC-e visa substituir as notas fiscais modelo 2 e
cupom fiscal emitido por ECF.  
NFS-e padrão Abrasf para autorizadores Ginfes e Betha.


Dependências
------------

- lxml
  - biblioteca de leitura e gravação de arquivos XML, de alta
    performance e fácil de implementar.
- signxml
  - assinatura e validação do XML
- pyopenssl
  - biblioteca para manuseio do certificado digital
- requests
  - biblioteca para a comunicação com os webservices da SEFAZ
- suds-jurko (*apenas para NFS-e)
  - biblioteca para a comunicação com os webservices via wsdl
- pyxb (*apenas para NFS-e)
  - biblioteca para geração de bindings a partir de XML Schema(xsd)

Referências
-----------

- Site oficial da Nota Fiscal eletrônica
  - http://www.nfe.fazenda.gov.br/

- lxml
  - http://lxml.de/

- requests
  - http://docs.python-requests.org/en/latest/
  - https://github.com/kennethreitz/requests
  - https://pypi.python.org/pypi/requests

- Schemas para validação dos arquivos
  - http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/fwLvLUSmU8=

- Validador de xml
  - https://www.sefaz.rs.gov.br/NFE/NFE-VAL.aspx

- Validador de assinaturas
  - https://www.receita.fazenda.gov.br/Aplicacoes/SSL/ATBHE/Assinadoc/ValidadorAssinaturas.app/valida.aspx

Instalação
-----------

```sh
pip3 install --user https://github.com/TadaSoftware/PyNFe/archive/master.zip
```

Opcional para NFS-e:

```sh
pip3 install --user -r https://github.com/TadaSoftware/PyNFe/raw/master/requirements-nfse.txt
```

Exemplos de uso
-----------
  - Consulta Status

```python
from pynfe.processamento.comunicacao import ComunicacaoSefaz

certificado = "/home/user/certificado.pfx"
senha = 'senha'
uf = 'pr'
homologacao = True

con = ComunicacaoSefaz(uf, certificado, senha, homologacao)
xml = con.status_servico('nfe')
print (xml.text)
```

Documentação
-----------
- https://github.com/leotada/PyNFe/wiki
- http://pynfe.readthedocs.org/pt/latest/
