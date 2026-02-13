# Source Map: `flags.py` (645 lines)

Constants, namespaces, tax code enumerations, and state codes used throughout PyNFe.

## Sections

| Section | Lines | Purpose |
|---------|-------|---------|
| Namespaces | 1-24 | XML namespaces for NF-e, NFS-e, MDF-e, CT-e, SOAP, signatures |
| XSD paths | 26-39 | Paths to XML Schema files |
| ICMS types | 42-84 | `ICMS_TIPOS_TRIBUTACAO` — all CST/CSOSN codes |
| ICMS origins | 86-123 | `ICMS_ORIGENS` — product origin codes (0-8) |
| ICMS modalities | 125-140 | `ICMS_MODALIDADES` and `ICMS_ST_MODALIDADES` |
| ICMS exemption reasons | 142-161 | `ICMS_MOTIVO_DESONERACAO` |
| NF-e status | 163-182 | `NF_STATUS` and `MDFE_STATUS` tuples |
| NF-e enumerations | 184-246 | Document types, emission processes, DANFE types, payment forms, emission forms, emission purposes, referenced types, specific products, environments |
| IPI types | 248-268 | `IPI_TIPOS_TRIBUTACAO` and `IPI_TIPOS_CALCULO` |
| PIS types | 270-407 | `PIS_TIPOS_TRIBUTACAO` — all CST codes (01-99) |
| COFINS types | 409-546 | `COFINS_TIPOS_TRIBUTACAO` — all CST codes (01-99) |
| Freight modalities | 548-555 | `MODALIDADES_FRETE` (0-9) |
| Process origins | 557-563 | `ORIGENS_PROCESSO` |
| State codes | 565-597 | `CODIGOS_ESTADOS` — UF to IBGE code mapping |
| Card brands | 599-628 | `BANDEIRA_CARTAO` (01-99) |
| Payment methods | 630-645 | `FORMAS_PAGAMENTO` (01-99) |

## Key Constants

| Constant | Value | Used For |
|----------|-------|----------|
| `NAMESPACE_NFE` | `http://www.portalfiscal.inf.br/nfe` | NF-e XML |
| `NAMESPACE_MDFE` | `http://www.portalfiscal.inf.br/mdfe` | MDF-e XML |
| `NAMESPACE_CTE` | `http://www.portalfiscal.inf.br/cte` | CT-e XML |
| `VERSAO_PADRAO` | `4.00` | NF-e version |
| `VERSAO_MDFE` | `3.00` | MDF-e version |
| `VERSAO_CTE` | `3.00` | CT-e version |
| `VERSAO_QRCODE` | `2` | QR Code version |
| `CODIGO_BRASIL` | `1058` | Country code for Brazil |
