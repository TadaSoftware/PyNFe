## PyNFe

![status](https://img.shields.io/badge/status-stable-green.svg) ![pyversions](https://img.shields.io/badge/Python-3.6%2B-blue.svg) [![license](https://img.shields.io/github/license/TadaSoftware/PyNFe)](https://github.com/TadaSoftware/PyNFe/blob/master/LICENCE)


Biblioteca de interface com os webservices de Nota Fiscal Eletrônica (NF-e) e Nota Fiscal de Consumidor Eletrônica (NFC-e) da SEFAZ e Receita Federal do Brasil e Nota Fiscal de Serviço Eletrônica (NFS-e) para Prefeituras.

- A NF-e visa substituir as notas fiscais séries 1 e 1A.
- A NFC-e visa substituir as notas fiscais modelo 2 e cupom fiscal emitido por ECF.
- NFS-e padrão Abrasf para autorizadores Ginfes e Betha.

Atualizado para a versão 4.00 NF-e/NFC-e
Suporte a Python >=3.6


Dependências
------------

- lxml
  - Biblioteca de leitura e gravação de arquivos XML, de alta performance e fácil de implementar.
- signxml
  - Assinatura e validação do XML
- pyopenssl
  - Biblioteca para manuseio do certificado digital
- requests
  - Biblioteca para a comunicação com os webservices da SEFAZ
- suds-jurko (*apenas para NFS-e)
  - Biblioteca para a comunicação com os webservices via wsdl
- pyxb (*apenas para NFS-e)
  - Biblioteca para geração de bindings a partir de XML Schema(xsd)

Referências
-----------

- Site oficial da Nota Fiscal Eletrônica
  - http://www.nfe.fazenda.gov.br/

- lxml
  - http://lxml.de/

- requests
  - http://docs.python-requests.org/en/latest/
  - https://github.com/psf/requests
  - https://pypi.python.org/pypi/requests

- Schemas para validação dos arquivos
  - http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/fwLvLUSmU8=

- Validador de XML
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
print(xml.text)
```

Documentação
-----------
- https://github.com/TadaSoftware/PyNFe/wiki
- http://pynfe.readthedocs.org/pt/latest/


Suporte
-----------
Se tiver qualquer problema or sugestão abra uma issue [aqui](https://github.com/TadaSoftware/PyNFe/issues) ou inicie uma discussão sobre um assunto [aqui](https://github.com/TadaSoftware/PyNFe/discussions).


Licença
-----------
[Licença](LICENSE)
