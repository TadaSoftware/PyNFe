# Reforma Tributaria - IBS/CBS/IS (EC 132/2023)

Suporte ao IVA Dual brasileiro introduzido pela Emenda Constitucional 132/2023.

## Contexto

A Reforma Tributaria brasileira substitui gradualmente cinco tributos por tres novos impostos:

| Imposto | Tipo | Substitui | Competencia |
|---------|------|-----------|-------------|
| **CBS** (Contribuicao sobre Bens e Servicos) | Federal | PIS, COFINS | Uniao |
| **IBS** (Imposto sobre Bens e Servicos) | Subnacional | ICMS, ISS | Estados + Municipios |
| **IS** (Imposto Seletivo) | Extrafiscal | IPI (parcial) | Uniao |

### Cronograma de transicao

- **2026**: Fase de testes (aliquotas reduzidas CBS 0.9%, IBS 0.1%)
- **2027-2028**: CBS integral, IBS em transicao
- **2029-2032**: Reducao gradual de ICMS/ISS
- **2033**: Extincao completa de ICMS/ISS

Durante a transicao, os impostos legados (ICMS, PIS, COFINS) **coexistem** com os novos (IBS, CBS, IS) na mesma NF-e.

## Escopo da implementacao

A implementacao atual cobre a **infraestrutura XML basica**:

- Campos de entidade (produto e nota fiscal)
- Serializacao XML (grupo `<impostoMisto>` contendo `<CBS>`, `<IBS>`, `<IS>`)
- Acumulacao de totais
- CSTs (Codigos de Situacao Tributaria) para IBS, CBS e IS

**Nao inclui** (ainda): Split Payment, cashback, helpers de calculo da transicao, validacao XSD (schemas oficiais ainda nao publicados pela SEFAZ).

## CSTs disponiveis

### IBS e CBS (compartilham a mesma tabela)

```python
from pynfe.utils.flags import IBS_CBS_TIPOS_TRIBUTACAO
```

| CST | Descricao |
|-----|-----------|
| 01 | Tributada Integralmente |
| 02 | Tributada com Reducao (Cesta Basica/Saude) |
| 03 | Isencao |
| 04 | Imunidade |
| 05 | Suspensao |
| 51 | Diferimento |
| 70 | Monofasica (Combustiveis) |

### IS (Imposto Seletivo)

```python
from pynfe.utils.flags import IS_TIPOS_TRIBUTACAO
```

| CST | Descricao |
|-----|-----------|
| 01 | Tributada Integralmente |
| 02 | Tributada com Reducao |
| 03 | Isencao |
| 04 | Imunidade |
| 05 | Suspensao |

## Como usar

### Exemplo basico: produto com CBS + IBS + IS

```python
from decimal import Decimal

nota_fiscal.adicionar_produto_servico(
    # ... campos obrigatorios do produto (codigo, descricao, ncm, cfop, etc.)
    codigo="001",
    descricao="Produto exemplo",
    ncm="99999999",
    ean="SEM GTIN",
    cfop="5102",
    unidade_comercial="UN",
    quantidade_comercial=Decimal("10"),
    valor_unitario_comercial=Decimal("100.00"),
    valor_total_bruto=Decimal("1000.00"),
    unidade_tributavel="UN",
    quantidade_tributavel=Decimal("10"),
    valor_unitario_tributavel=Decimal("100.00"),
    ean_tributavel="SEM GTIN",
    ind_total=1,

    # ... impostos legados (ICMS, PIS, COFINS) continuam obrigatorios
    icms_modalidade="00",
    icms_origem=0,
    icms_csosn="",
    pis_modalidade="99",
    cofins_modalidade="99",
    pis_valor=Decimal("0.00"),
    cofins_valor=Decimal("0.00"),

    # CBS - Contribuicao sobre Bens e Servicos (Federal)
    cbs_situacao_tributaria="01",              # CST 01 = Tributada integralmente
    cbs_valor_base_calculo=Decimal("1000.00"),
    cbs_aliquota=Decimal("8.8000"),            # 4 casas decimais
    cbs_valor=Decimal("88.00"),

    # IBS - Imposto sobre Bens e Servicos (Estadual/Municipal)
    ibs_situacao_tributaria="01",
    ibs_valor_base_calculo=Decimal("1000.00"),
    ibs_aliquota=Decimal("17.7000"),
    ibs_valor=Decimal("177.00"),
    ibs_codigo_municipio_destino="4118402",    # Codigo IBGE do municipio destino

    # IS - Imposto Seletivo (opcional, apenas para produtos sujeitos)
    is_situacao_tributaria="01",
    is_valor_base_calculo=Decimal("1000.00"),
    is_aliquota=Decimal("1.0000"),
    is_valor=Decimal("10.00"),
)
```

### Exemplo: produto isento (CBS + IBS com CST 03)

```python
nota_fiscal.adicionar_produto_servico(
    # ... campos do produto ...

    # CBS isenta - apenas o CST, sem valores
    cbs_situacao_tributaria="03",

    # IBS isenta
    ibs_situacao_tributaria="03",

    # IS nao se aplica (nao informar = nao serializado)
)
```

### Exemplo: sem reforma tributaria (compatibilidade retroativa)

Se nenhum campo de IBS/CBS/IS for informado, o grupo `<impostoMisto>` **nao e emitido** no XML. Isso garante compatibilidade total com NF-e que nao precisam dos novos impostos.

```python
# Produto sem campos de reforma tributaria = XML identico ao anterior
nota_fiscal.adicionar_produto_servico(
    # ... apenas campos legados (ICMS, PIS, COFINS) ...
)
```

## Campos disponiveis

### Campos do produto (`adicionar_produto_servico`)

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `cbs_situacao_tributaria` | `str` | CST da CBS (ex: "01", "03") |
| `cbs_valor_base_calculo` | `Decimal` | Base de calculo da CBS |
| `cbs_aliquota` | `Decimal` | Aliquota CBS (4 casas decimais) |
| `cbs_valor` | `Decimal` | Valor da CBS |
| `ibs_situacao_tributaria` | `str` | CST do IBS (ex: "01", "03") |
| `ibs_valor_base_calculo` | `Decimal` | Base de calculo do IBS |
| `ibs_aliquota` | `Decimal` | Aliquota IBS (4 casas decimais) |
| `ibs_valor` | `Decimal` | Valor do IBS |
| `ibs_codigo_municipio_destino` | `str` | Codigo IBGE do municipio destino |
| `is_situacao_tributaria` | `str` | CST do IS (ex: "01", "02") |
| `is_valor_base_calculo` | `Decimal` | Base de calculo do IS |
| `is_aliquota` | `Decimal` | Aliquota IS (4 casas decimais) |
| `is_valor` | `Decimal` | Valor do IS |

### Totais da nota fiscal (acumulados automaticamente)

| Campo | Descricao |
|-------|-----------|
| `totais_cbs` | Soma de `cbs_valor` de todos os produtos |
| `totais_ibs` | Soma de `ibs_valor` de todos os produtos |
| `totais_is` | Soma de `is_valor` de todos os produtos |

Os totais sao acumulados automaticamente ao chamar `adicionar_produto_servico()`. Os valores de IBS, CBS e IS tambem sao somados ao `totais_icms_total_nota` (vNF), pois sao impostos "por fora".

## Estrutura XML gerada

O grupo `<impostoMisto>` e adicionado dentro de `<imposto>`, apos `<COFINS>` e antes de `<impostoDevol>`:

```xml
<det nItem="1">
  <prod>...</prod>
  <imposto>
    <ICMS>...</ICMS>
    <PIS>...</PIS>
    <COFINS>...</COFINS>
    <impostoMisto>
      <CBS>
        <CST>01</CST>
        <vBC>1000.00</vBC>
        <pCBS>8.8000</pCBS>
        <vCBS>88.00</vCBS>
      </CBS>
      <IBS>
        <CST>01</CST>
        <vBC>1000.00</vBC>
        <pIBS>17.7000</pIBS>
        <vIBS>177.00</vIBS>
        <cMunDest>4118402</cMunDest>
      </IBS>
      <IS>
        <CST>01</CST>
        <vBC>1000.00</vBC>
        <pIS>1.0000</pIS>
        <vIS>10.00</vIS>
      </IS>
    </impostoMisto>
  </imposto>
</det>
```

Os totais aparecem dentro de `<ICMSTot>`:

```xml
<total>
  <ICMSTot>
    <!-- ... totais existentes ... -->
    <vNF>1275.00</vNF>
    <vCBS>88.00</vCBS>
    <vIBS>177.00</vIBS>
    <vIS>10.00</vIS>
  </ICMSTot>
</total>
```

## Regras de serializacao

- **CSTs 01, 02, 51**: Serializam `vBC`, aliquota e valor (campos completos)
- **CSTs 03, 04, 05, 70**: Serializam apenas o `CST` (sem valores)
- **IS CSTs 01, 02**: Serializam campos completos; demais apenas `CST`
- **`cMunDest`** (IBS): Serializado apenas quando informado
- **Totais**: Emitidos apenas quando o valor e maior que zero
- **`impostoMisto`**: Omitido completamente se nenhum dos tres impostos for informado

## Notas importantes

- Os nomes das tags XML (`impostoMisto`, `CBS`, `IBS`, `IS`) sao baseados na especificacao preliminar. Podem ser renomeados quando a SEFAZ publicar a Nota Tecnica oficial.
- A validacao XSD e ignorada para os novos grupos, pois os schemas oficiais ainda nao existem.
- Durante a fase de transicao (2026-2032), os impostos legados e os novos coexistem no mesmo XML.
- O calculo dos valores (base de calculo, aliquota, valor) deve ser feito pela aplicacao consumidora. PyNFe apenas serializa os valores informados.
