# Source Map: `flags.py` (681 lines)

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
| NF-e enumerations | 184-248 | Document types, emission processes, DANFE types, payment forms, emission forms, **emission purposes (incl. finNFe 5/6)**, referenced types, specific products, environments |
| IPI types | 250-270 | `IPI_TIPOS_TRIBUTACAO` and `IPI_TIPOS_CALCULO` |
| PIS types | 272-407 | `PIS_TIPOS_TRIBUTACAO` — all CST codes (01-99) |
| COFINS types | 411-548 | `COFINS_TIPOS_TRIBUTACAO` — all CST codes (01-99) |
| Reforma Tributaria | 550-582 | `IBS_CBS_TIPOS_TRIBUTACAO` (15 CSTs, 3-digit) and `IS_TIPOS_TRIBUTACAO` (7 CSTs, 2-digit) — IVA Dual (EC 132/2023) |
| Freight modalities | 584-591 | `MODALIDADES_FRETE` (0-9) |
| Process origins | 593-599 | `ORIGENS_PROCESSO` |
| State codes | 601-633 | `CODIGOS_ESTADOS` — UF to IBGE code mapping |
| Card brands | 635-664 | `BANDEIRA_CARTAO` (01-99) |
| Payment methods | 666-681 | `FORMAS_PAGAMENTO` (01-99) |

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
