# Source Map: `webservices.py` (572 lines)

SEFAZ webservice endpoint URLs organized by document type, state, and environment.

## Sections

| Section | Lines | Variable | Purpose |
|---------|-------|----------|---------|
| NFC-e endpoints | 8-295 | `NFCE` | NFC-e webservice URLs and QR Code URLs by state |
| NF-e endpoints | 297-471 | `NFE` | NF-e webservice URLs by state |
| NFS-e endpoints | 473-499 | `NFSE` | NFS-e URLs (Betha, Ginfes) |
| MDF-e endpoints | 501-516 | `MDFE` | MDF-e URLs (SVRS only) |
| CT-e endpoints | 518-572 | `CTE` | CT-e URLs by state |

## URL Structure

Each state/virtual environment entry contains:
- `STATUS` — Service status check endpoint
- `AUTORIZACAO` — Authorization endpoint
- `RECIBO` — Receipt query endpoint
- `CHAVE` — Access key query endpoint
- `INUTILIZACAO` — Number invalidation endpoint
- `EVENTOS` — Event reception endpoint
- `CADASTRO` — Registration query endpoint (some states)
- `HTTPS` — Production base URL prefix
- `HOMOLOGACAO` — Homologation base URL prefix
- `QR` — QR Code URL (NFC-e only)
- `URL` — Consultation URL (NFC-e only)

## State/Virtual Environment Groups

### NFC-e (`NFCE`) — Lines 8-295
| Key | Lines | Description |
|-----|-------|-------------|
| Individual states | 9-278 | RO, AC, AM, RR, PA, AP, TO, MA, PI, CE, RN, PB, PE, AL, SE, BA, MG, ES, RJ, SP, PR, SC, RS, MS, MT, GO, DF |
| `SVRS` | 284-294 | Virtual SEFAZ RS (fallback for states without own NFC-e) |

### NF-e (`NFE`) — Lines 297-471
| Key | Lines | Description |
|-----|-------|-------------|
| `AN` | 302-309 | National environment (events, distribution) |
| Individual states | 310-428 | AM, MA, PE, BA, MG, SP, PR, RS, MS, MT, GO |
| `SVAN` | 430-440 | Virtual SEFAZ AN (MA for NF-e) |
| `SVRS` | 441-451 | Virtual SEFAZ RS (most states) |
| `SVC-AN` | 452-460 | Contingency AN |
| `SVC-RS` | 461-470 | Contingency RS |

### NFS-e (`NFSE`) — Lines 473-499
| Key | Lines | Description |
|-----|-------|-------------|
| `BETHA` | 476-486 | Betha provider (HTTP WSDL) |
| `GINFES` | 488-498 | Ginfes provider (HTTPS WSDL) |

### MDF-e (`MDFE`) — Lines 501-516
Only `SVRS` — single authorizer for all states.

### CT-e (`CTE`) — Lines 518-572
| Key | Lines | Description |
|-----|-------|-------------|
| `AN` | 519-523 | National environment (distribution) |
| Individual states | 524-558 | MT, MS, MG, PR, RS, SP |
| `SVRS` | 560-565 | Virtual SEFAZ RS |
| `SVSP` | 566-571 | Virtual SEFAZ SP (AP, PE, RR) |
