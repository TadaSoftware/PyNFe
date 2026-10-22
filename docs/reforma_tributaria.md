# Tax Reform (Reforma Tributaria) - IBS/CBS (NT 2025.002-RTC)

Support for the Brazilian Dual VAT (IVA Dual) per Constitutional Amendment 132/2023, Complementary Law 214/2025 and Technical Note NT 2025.002-RTC.

## Context

The Tax Reform gradually replaces five taxes with a Dual VAT model:

| Tax | Type | Replaces | Jurisdiction | Start |
|---------|------|-----------|-------------|--------|
| **CBS** (Contribuicao sobre Bens e Servicos) | Federal | PIS, COFINS | Union | 2026 (test 0.9%) |
| **IBS** (Imposto sobre Bens e Servicos) | Subnational | ICMS, ISS | States + Municipalities | 2026 (test 0.1% UF) |
| **IS** (Imposto Seletivo) | Extrafiscal | IPI (partial) | Union | **2027** |

> **IBS is split into two parts**: IBS-UF (state) and IBS-Mun (municipal), reported separately in the XML.

### Transition schedule

- **2026**: Test phase — CBS 0.9%, IBS-UF 0.1%, IBS-Mun 0%. Mandatory for CRT=3.
- **2027**: CBS at full rate. IS takes effect. Split Payment starts.
- **2029-2032**: Gradual reduction of ICMS/ISS, proportional increase of IBS.
- **2033**: Full extinction of ICMS, ISS, PIS, COFINS and IPI.

During the transition, the legacy taxes (ICMS, PIS, COFINS) **coexist** with the new ones (IBS, CBS) in the same NF-e.

## Implementation scope

The implementation covers:

- Grupo `<IBSCBS>` as a direct child of `<imposto>` (no `<impostoMisto>` wrapper)
- 3-digit CSTs per NT 2025.002-RTC (e.g. "000", "010", "222")
- `cClassTrib` (6-digit tax classification code)
- IBS split into `gIBSUF` and `gIBSMun`
- Shared tax base (`vBC`) for IBS and CBS
- Totals in `<IBSCBSTot>`, separate from `<ICMSTot>`
- `cMunFGIBS` in the header (Group B)
- `vNF` **does NOT include** IBS/CBS (forbidden in 2025-2026)
- `finNFe=5` (Debit Note) and `finNFe=6` (Credit Note)
- Entity fields for IS (Selective Tax) — **stored but not serialized** until the schema supports it (2027)
- Single-phase taxation (`gIBSCBSMono`) for CST 620 — fuels and other products under the IBS/CBS single-phase regime

**Does not include** (yet): Split Payment, cashback, assisted assessment events, Group VB (item total), Group VC (DF-e referencing), Group BB (payment anticipation), per-item deferral (`gDif`), per-item tax refund (`gDevTrib`), per-item rate reduction (`gRed`), credit reversal (`gEstornoCred`), per-item presumed credit (`gCredPresOper`, `gCredPresIBSZFM`).

### Single-phase taxation — `gIBSCBSMono`

For products with CST 620 (fuels, etc.) the group emitted inside `<IBSCBS>` is `<gIBSCBSMono>` instead of `<gIBSCBS>`. Per the official schema (`DFeTiposBasicos_v1.00.xsd`, type `TMonofasia`), the five single-phase fields live under the mandatory `<gMonoPadrao>` wrapper, in the order defined by the schema. In addition, `<vTotIBSMonoItem>` and `<vTotCBSMonoItem>` are SIBLINGS of `<gMonoPadrao>` (NOT children) and both are MANDATORY per schema (no `minOccurs=0`):

```xml
<gIBSCBSMono>
  <gMonoPadrao>
    <qBCMono>18.0000</qBCMono>
    <adRemIBS>0.1000</adRemIBS>
    <adRemCBS>0.0000</adRemCBS>
    <vIBSMono>1.80</vIBSMono>
    <vCBSMono>0.00</vCBSMono>
  </gMonoPadrao>
  <vTotIBSMonoItem>1.80</vTotIBSMonoItem>
  <vTotCBSMonoItem>0.00</vTotCBSMonoItem>
</gIBSCBSMono>
```

| Field | Type | Description |
|-------|------|-----------|
| `qBCMono` | TDec1104RTC | Quantity taxed on the single-phase base |
| `adRemIBS` | TDec_0302_04RTC | IBS ad rem rate (BRL amount per unit) |
| `adRemCBS` | TDec_0302_04RTC | CBS ad rem rate (BRL amount per unit) |
| `vIBSMono` | TDec1302RTC | Single-phase IBS amount |
| `vCBSMono` | TDec1302RTC | Single-phase CBS amount |
| `vTotIBSMonoItem` | TDec1302RTC | Item single-phase IBS total (sibling of `gMonoPadrao`) |
| `vTotCBSMonoItem` | TDec1302RTC | Item single-phase CBS total (sibling of `gMonoPadrao`) |

Attributes on the `NotaFiscalProduto` entity: `ibscbs_q_bc_mono`, `ibscbs_ad_rem_ibs`, `ibscbs_v_ibs_mono`, `ibscbs_ad_rem_cbs`, `ibscbs_v_cbs_mono`, `ibscbs_v_tot_ibs_mono_item`, `ibscbs_v_tot_cbs_mono_item`.

For single-line items (no withholding / prior withholding / deferral), `vTotIBSMonoItem == vIBSMono` and `vTotCBSMonoItem == vCBSMono`. When the caller does not provide the attributes, the serializer emits `0.00` (safe default during the 2026 Load Test with zeroed ad rem rates).

During the 2026 Load Test SEFAZ has not published the ad rem rates yet, so the values may be zero — the `gIBSCBSMono` group is still emitted correctly.

## Available CSTs

### IBS and CBS — 3-digit CST (they share the same table)

```python
from pynfe.utils.flags import IBS_CBS_TIPOS_TRIBUTACAO
```

| CST | Description |
|-----|-----------|
| 000 | Full taxation |
| 010 | Taxation at a reduced rate |
| 100 | Taxation with suspension |
| 110 | Immunity — export |
| 200 | Taxation with deferral |
| 222 | Exemption |
| 300 | Non-incidence |
| 400 | Taxation by substitution |
| 410 | Taxation at zero rate |
| 510 | Full taxation — specific regime |
| 600 | Single-phase taxation — standard incidence |
| 620 | Single-phase taxation — other operations |
| 800 | Presumed credit |
| 810 | Presumed credit — ZFM |
| 900 | Other |

### IS (Imposto Seletivo, Selective Tax) — 2-digit CSTIS

```python
from pynfe.utils.flags import IS_TIPOS_TRIBUTACAO
```

| CSTIS | Description |
|-------|-----------|
| 01 | Fully taxed |
| 02 | Taxed with reduction |
| 03 | Exemption |
| 04 | Immunity |
| 05 | Suspension |
| 06 | Deferral |
| 90 | Other |

> **IS is not serialized in the XML in 2026.** The SEFAZ schema (PL 010b) includes the `TIS` type with tags `CSTIS`, `cClassTribIS`, `vBCIS`, `pIS`, `vIS`, but serialization is disabled until 2027. The entity fields are ready and will be enabled when needed.

## How to use

### Example: product with IBSCBS (full taxation, CST 000)

```python
from decimal import Decimal

nota_fiscal.adicionar_produto_servico(
    # ... mandatory product fields ...
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

    # ... legacy taxes (ICMS, PIS, COFINS) are still mandatory ...
    icms_modalidade="00",
    icms_origem=0,
    icms_csosn="",
    pis_modalidade="99",
    cofins_modalidade="99",
    pis_valor=Decimal("0.00"),
    cofins_valor=Decimal("0.00"),

    # IBSCBS — Group UB
    ibscbs_cst="000",                           # 3-digit CST
    ibscbs_c_class_trib="000001",               # 6-digit cClassTrib
    ibscbs_vbc=Decimal("1000.00"),              # Shared IBS+CBS tax base
    ibscbs_p_ibs_uf=Decimal("0.1000"),          # IBS UF rate (4 decimals)
    ibscbs_v_ibs_uf=Decimal("1.00"),            # IBS UF amount
    ibscbs_p_ibs_mun=Decimal("0.0000"),         # Municipal IBS rate
    ibscbs_v_ibs_mun=Decimal("0.00"),           # Municipal IBS amount
    ibscbs_v_ibs=Decimal("1.00"),               # Total IBS amount (UF + Mun)
    ibscbs_p_cbs=Decimal("0.9000"),             # CBS rate (4 decimals)
    ibscbs_v_cbs=Decimal("9.00"),               # CBS amount

    # IS — stored on the entity but NOT serialized in the XML (2026)
    # is_cst_selec="01",
    # is_c_class_trib="010001",
    # is_vbc=Decimal("1000.00"),
    # is_aliquota=Decimal("1.0000"),
    # is_valor=Decimal("10.00"),
)
```

### Example: exempt product (CST 222)

```python
nota_fiscal.adicionar_produto_servico(
    # ... product fields ...

    # Exempt IBSCBS — only CST and cClassTrib, no amounts
    ibscbs_cst="222",
    ibscbs_c_class_trib="000002",
)
```

### Example: without the tax reform (backward compatibility)

If no `ibscbs_*` field is provided, the `<IBSCBS>` group **is not emitted** in the XML. This guarantees full compatibility with NF-e that do not need the new taxes.

```python
# Product without reform fields = XML identical to before
nota_fiscal.adicionar_produto_servico(
    # ... only legacy fields (ICMS, PIS, COFINS) ...
)
```

### cMunFGIBS in the header

```python
nota_fiscal = NotaFiscal(
    # ... other fields ...
    municipio_fato_gerador_ibs="4118402",  # IBGE code — generates <cMunFGIBS> in <ide>
)
```

## Available fields

### Product fields (`adicionar_produto_servico`)

#### IBSCBS (Group UB)

| Field | Type | Description |
|-------|------|-----------|
| `ibscbs_cst` | `str` | 3-digit CST (e.g. "000", "222") |
| `ibscbs_c_class_trib` | `str` | 6-digit cClassTrib (tax classification) |
| `ibscbs_vbc` | `Decimal` | Shared IBS + CBS tax base |
| `ibscbs_p_ibs_uf` | `Decimal` | State IBS rate (4 decimal places) |
| `ibscbs_v_ibs_uf` | `Decimal` | State IBS amount |
| `ibscbs_p_ibs_mun` | `Decimal` | Municipal IBS rate (4 decimal places) |
| `ibscbs_v_ibs_mun` | `Decimal` | Municipal IBS amount |
| `ibscbs_v_ibs` | `Decimal` | Total IBS amount (UF + Mun) |
| `ibscbs_p_cbs` | `Decimal` | CBS rate (4 decimal places) |
| `ibscbs_v_cbs` | `Decimal` | CBS amount |

#### IS (Selective Tax) — stored, not serialized in 2026

| Field | XML Tag | Description |
|-------|---------|-----------|
| `is_cst_selec` | `CSTIS` | 2-digit CSTIS (e.g. "01", "02") |
| `is_c_class_trib` | `cClassTribIS` | 6-digit cClassTribIS |
| `is_vbc` | `vBCIS` | IS tax base |
| `is_aliquota` | `pIS` | IS rate (4 decimal places) |
| `is_valor` | `vIS` | IS amount |

### Invoice totals (accumulated automatically)

| Field | XML path in `IBSCBSTot` | Description |
|-------|-------------------------|-----------|
| `totais_vbc_ibscbs` | `vBCIBSCBS` | Sum of `ibscbs_vbc` across all products |
| `totais_ibs_uf` | `gIBS/gIBSUF/vIBSUF` | Sum of `ibscbs_v_ibs_uf` across all products |
| `totais_ibs_mun` | `gIBS/gIBSMun/vIBSMun` | Sum of `ibscbs_v_ibs_mun` across all products |
| `totais_ibs` | `gIBS/vIBS` | Sum of `ibscbs_v_ibs` across all products |
| `totais_cbs` | `gCBS/vCBS` | Sum of `ibscbs_v_cbs` across all products |
| `totais_is` | *(not emitted)* | Sum of `is_valor` — accumulated internally, not in the XML |

Totals are accumulated automatically when calling `adicionar_produto_servico()`.

> **IMPORTANT**: IBS/CBS/IS **are NOT added** to `vNF` (forbidden in 2025-2026 per NT 2025.002-RTC).

### Header field

| Field | XML Tag | Description |
|-------|---------|-----------|
| `municipio_fato_gerador_ibs` | `cMunFGIBS` | IBGE code of the municipality of the IBS taxable event (7 digits) |

## Generated XML structure

### Item — inside `<det><imposto>`

The `<IBSCBS>` group is added as a direct child of `<imposto>`, after `<COFINS>`:

```xml
<det nItem="1">
  <prod>...</prod>
  <imposto>
    <ICMS>...</ICMS>
    <PIS>...</PIS>
    <COFINS>...</COFINS>
    <IBSCBS>
      <CST>000</CST>
      <cClassTrib>000001</cClassTrib>
      <gIBSCBS>
        <vBC>1000.00</vBC>
        <gIBSUF>
          <pIBSUF>0.1000</pIBSUF>
          <vIBSUF>1.00</vIBSUF>
        </gIBSUF>
        <gIBSMun>
          <pIBSMun>0.0000</pIBSMun>
          <vIBSMun>0.00</vIBSMun>
        </gIBSMun>
        <vIBS>1.00</vIBS>
        <gCBS>
          <pCBS>0.9000</pCBS>
          <vCBS>9.00</vCBS>
        </gCBS>
      </gIBSCBS>
    </IBSCBS>
  </imposto>
</det>
```

For non-taxed CSTs (e.g. 222 — exemption):

```xml
<IBSCBS>
  <CST>222</CST>
  <cClassTrib>000002</cClassTrib>
</IBSCBS>
```

### Totals — Group W03 (`<IBSCBSTot>`)

The totals live in a group **separate** from `<ICMSTot>`, as a sibling inside `<total>`. The XSD type is `TIBSCBSMonoTot` (defined in `DFeTiposBasicos_v1.00.xsd`).

```xml
<total>
  <ICMSTot>
    <!-- existing totals (ICMS, PIS, COFINS, etc.) -->
    <vNF>1250.00</vNF>  <!-- does NOT include IBS/CBS/IS -->
  </ICMSTot>
  <IBSCBSTot>
    <vBCIBSCBS>1000.00</vBCIBSCBS>       <!-- Total BC (mandatory, first child) -->
    <gIBS>                                 <!-- IBS totals (optional) -->
      <gIBSUF>
        <vDif>0.00</vDif>                 <!-- Total IBS UF deferral -->
        <vDevTrib>0.00</vDevTrib>          <!-- Total IBS UF tax refund -->
        <vIBSUF>1.00</vIBSUF>             <!-- Total state IBS -->
      </gIBSUF>
      <gIBSMun>
        <vDif>0.00</vDif>
        <vDevTrib>0.00</vDevTrib>
        <vIBSMun>0.50</vIBSMun>           <!-- Total municipal IBS -->
      </gIBSMun>
      <vIBS>1.50</vIBS>                   <!-- Total IBS (UF + Mun) -->
      <vCredPres>0.00</vCredPres>          <!-- Total IBS presumed credit -->
      <vCredPresCondSus>0.00</vCredPresCondSus>
    </gIBS>
    <gCBS>                                 <!-- CBS totals (optional) -->
      <vDif>0.00</vDif>
      <vDevTrib>0.00</vDevTrib>
      <vCBS>9.00</vCBS>                   <!-- Total CBS -->
      <vCredPres>0.00</vCredPres>
      <vCredPresCondSus>0.00</vCredPresCondSus>
    </gCBS>
    <gMono>                                <!-- Single-phase totals (DEV-1955) -->
      <vIBSMono>0.00</vIBSMono>            <!-- Total standard single-phase IBS -->
      <vCBSMono>0.00</vCBSMono>            <!-- Total standard single-phase CBS -->
      <vIBSMonoReten>0.00</vIBSMonoReten>  <!-- Total single-phase IBS subject to withholding -->
      <vCBSMonoReten>0.00</vCBSMonoReten>  <!-- Total single-phase CBS subject to withholding -->
      <vIBSMonoRet>0.00</vIBSMonoRet>      <!-- Total single-phase IBS previously withheld -->
      <vCBSMonoRet>0.00</vCBSMonoRet>      <!-- Total single-phase CBS previously withheld -->
    </gMono>
    <!-- gEstornoCred: credit reversal totals (not implemented) -->
  </IBSCBSTot>
</total>
```

> The `gIBS` and `gCBS` subgroups are optional (`minOccurs="0"`) — emitted only when there are amounts. The `vDif`, `vDevTrib`, `vCredPres` and `vCredPresCondSus` fields are mandatory inside each subgroup (emitted as "0.00" when unused).
>
> The `gMono` subgroup is optional, but mandatory whenever any NF-e item carries `<gIBSCBSMono>` (CST 620, etc.). When emitted, **all six children** are mandatory (`vIBSMono`, `vCBSMono`, `vIBSMonoReten`, `vCBSMonoReten`, `vIBSMonoRet`, `vCBSMonoRet`). Omitting `<gMono>` in an NF-e with single-phase items makes SEFAZ reject it with `cStat 1119 - "Total de IBS e CBS nao informado"`. The `Reten`/`Ret` totals are not accumulated at item level yet (PyNFe still only emits `<gMonoPadrao>`), so they will be "0.00" until `<gMonoReten>` / `<gMonoRet>` / `<gMonoDif>` are supported at item level.

### Header — `cMunFGIBS` in `<ide>`

```xml
<ide>
  <!-- ... existing fields ... -->
  <cMunFG>4118402</cMunFG>
  <cMunFGIBS>4118402</cMunFGIBS>
  <tpImp>1</tpImp>
  <!-- ... -->
</ide>
```

## Serialization rules

### Taxed CSTs (emit `gIBSCBS` with amounts)

CSTs: 000, 010, 200, 400, 510, 600, 620, 800, 810, 900

These CSTs generate the full `<gIBSCBS>` subgroup with `vBC`, `gIBSUF`, `gIBSMun`, `vIBS` and `gCBS`.

### Non-taxed CSTs (only CST + cClassTrib)

CSTs: 100, 110, 222, 300, 410

These CSTs generate only `<CST>` and `<cClassTrib>`, without `<gIBSCBS>`.

### Other rules

- **`cClassTrib`**: Emitted when provided (mandatory field in practice)
- **`cMunFGIBS`**: Emitted in `<ide>` only when provided
- **`<IBSCBSTot>`**: Tipo `TIBSCBSMonoTot`. Omitted if all totals are zero AND no item carries `<gIBSCBSMono>`. When emitted, `vBCIBSCBS` is mandatory as the first child; `gIBS`, `gCBS` and `gMono` are optional (but `gMono` is mandatory whenever there are single-phase items)
- **`<IBSCBS>`**: Tipo `TTribNFe`. Omitted entirely if `ibscbs_cst` is not provided
- **IS (`<IS>`)**: Tipo `TIS`. **Not emitted in the XML** — serialization disabled until 2027
- **`<ISTot>`**: Tipo `TISTot`. **Not emitted** — will be a sibling of `<IBSCBSTot>` (before it in the schema)
- **`vNF`**: does NOT include IBS, CBS or IS amounts (forbidden in 2025-2026)

## IS (Selective Tax) — prepared for 2027

IS is implemented in the entities but disabled in serialization:

- **Entity** (`NotaFiscalProduto`): fields `is_cst_selec`, `is_c_class_trib`, `is_vbc`, `is_aliquota`, `is_valor` — can be filled in normally
- **Totals** (`NotaFiscal`): `totais_is` is accumulated internally
- **Serialization**: `_serializar_is()` exists and uses the correct schema tags (`CSTIS`, `cClassTribIS`, `vBCIS`, `pIS`, `vIS`) but is not called
- **XML**: emits neither `<IS>` nor `<ISTot>`

When IS serialization is enabled (planned for 2027):
1. Uncomment the call in `_serializar_imposto_ibscbs()`
2. Add `<ISTot>` serialization in `_serializar_nota_fiscal()` (sibling of `<IBSCBSTot>`, before it)
3. Update the tests

## Technical reference

| Resource | Description |
|---------|-----------|
| NT 2025.002-RTC (v1.30+) | Technical Note with changes to the XML layouts |
| PL 010b | XML schema package (`leiauteNFe_v4.00.xsd` + `DFeTiposBasicos_v1.00.xsd`) |
| LC 214/2025 | Complementary Law that regulates the reform |
| [Tabela cClassTrib](https://dfe-portal.svrs.rs.gov.br/DFE/TabelaClassificacaoTributaria) | Official tax classification table (JSON available) |
| [Tabela cCredPres](https://dfe-portal.svrs.rs.gov.br/DFE/TabelaCreditoPresumido) | Presumed credit table |

### Relevant XSD types (DFeTiposBasicos_v1.00.xsd)

| XSD type | XML element | Use |
|----------|-------------|-----|
| `TTribNFe` | `IBSCBS` | Per-item: CST, cClassTrib, choice(gIBSCBS/gIBSCBSMono/...) |
| `TCIBS` | `gIBSCBS` | Per-item: vBC, gIBSUF, gIBSMun, vIBS, gCBS |
| `TIS` | `IS` | Per-item: CSTIS, cClassTribIS, vBCIS, pIS, vIS |
| `TIBSCBSMonoTot` | `IBSCBSTot` | Totals: vBCIBSCBS, gIBS, gCBS, gMono, gEstornoCred |
| `TISTot` | `ISTot` | Totals: vIS |
| `TDif` | `gDif` | Deferral (pDif, vDif) |
| `TDevTrib` | `gDevTrib` | Tax refund (vDevTrib) |
| `TRed` | `gRed` | Rate reduction (pRedAliq, pAliqEfet) |
| `TCredPres` | `gCredPresOper` | Presumed credit (pCredPres, vCredPres/vCredPresCondSus) |

## Important notes

- XML tag names strictly follow the PL 010b XSD types (`DFeTiposBasicos_v1.00.xsd`):
  - Per-item: `TTribNFe` (`IBSCBS`), `TCIBS` (`gIBSCBS`), `TIS` (`IS`)
  - Totals: `TIBSCBSMonoTot` (`IBSCBSTot`), `TISTot` (`ISTot`)
- Computing the amounts (tax base, rate, amount) is the consuming application's job. PyNFe only serializes the provided values.
- During the transition phase (2026-2033), legacy and new taxes coexist in the same XML.
- Test rates for 2026: CBS=0.9%, IBS-UF=0.1%, IBS-Mun=0%.
- Deferral (`vDif`), tax refund (`vDevTrib`) and presumed credit (`vCredPres`, `vCredPresCondSus`) fields are emitted as "0.00" in the totals. Full support for these fields will be added as needed.
