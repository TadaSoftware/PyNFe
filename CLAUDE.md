# CLAUDE.md - PyNFe

Brazilian electronic fiscal document library (NF-e, NFC-e, NFS-e, MDF-e, CT-e) for SEFAZ webservice communication.

## Source Map Navigation (MANDATORY)

**Before reading any large file (>200 lines), you MUST first read its `{filename}_map.md` file** in the same directory. The source map contains:
- Section-by-section breakdown with exact line ranges
- Class/method index with purpose descriptions
- Field group documentation

This allows you to navigate directly to the specific line-window you need instead of reading the entire file.

### Available Source Maps

| Source Map | File | Lines | Description |
|------------|------|-------|-------------|
| `pynfe/processamento/serializacao_map.md` | `serializacao.py` | 2630 | XML serialization (NF-e, MDF-e, QR codes) |
| `pynfe/processamento/comunicacao_map.md` | `comunicacao.py` | 1348 | SEFAZ webservice communication |
| `pynfe/processamento/autorizador_nfse_map.md` | `autorizador_nfse.py` | 538 | NFS-e authorization (Betha/Ginfes) |
| `pynfe/entidades/notafiscal_map.md` | `notafiscal.py` | 1253 | Invoice entities and tax fields |
| `pynfe/entidades/manifesto_map.md` | `manifesto.py` | 447 | MDF-e manifest entities |
| `pynfe/entidades/evento_map.md` | `evento.py` | 237 | Event entities (cancel, correction, etc.) |
| `pynfe/utils/flags_map.md` | `flags.py` | 645 | Constants, namespaces, tax codes |
| `pynfe/utils/webservices_map.md` | `webservices.py` | 572 | SEFAZ endpoint URLs by state |
| `pynfe/utils/utils_map.md` | `__init__.py` | 253 | Utility functions (municipality lookup, signing) |

### How to Use Source Maps

1. **Read the `_map.md` file first** to understand the file structure
2. **Identify the line range** you need from the map tables
3. **Read only that section** using `offset` and `limit` parameters
4. Example: To understand ICMS CST 60 serialization, read `serializacao_map.md`, find it's at lines 747-770, then read `serializacao.py` with `offset=747, limit=25`

## Project Structure

```
pynfe/
├── entidades/          # Domain entities (data models)
│   ├── base.py         # Base entity class with kwargs init
│   ├── certificado.py  # A1 certificate handling
│   ├── cliente.py      # Customer entity
│   ├── emitente.py     # Issuer entity
│   ├── evento.py       # Event entities (cancel, correction, MDF-e events)
│   ├── manifesto.py    # MDF-e manifest entity
│   ├── notafiscal.py   # NF-e/NFC-e invoice entity + products + taxes
│   ├── produto.py      # Product entity (standalone)
│   ├── servico.py      # Service entity (NFS-e)
│   └── transportadora.py  # Carrier entity
├── processamento/      # Core processing logic
│   ├── assinatura.py   # XML digital signing with A1 certificates
│   ├── autorizador_nfse.py  # NFS-e serialization (Betha/Ginfes PyXB bindings)
│   ├── comunicacao.py  # SEFAZ SOAP webservice communication
│   ├── serializacao.py # XML serialization (entities → SEFAZ XML)
│   └── validacao.py    # XML schema validation
├── utils/              # Utilities
│   ├── __init__.py     # Municipality lookup, XML signing helpers
│   ├── flags.py        # Constants, namespaces, tax code enumerations
│   ├── webservices.py  # SEFAZ endpoint URLs by state/environment
│   ├── bar_code_128.py # Code 128 barcode generation for DANFE
│   ├── xml_writer.py   # XML element writing helpers
│   └── nfse/           # NFS-e provider-specific PyXB bindings (GENERATED - do not edit)
│       ├── betha/      # Betha provider bindings (13,941+ lines)
│       └── ginfes/     # Ginfes provider bindings (8,028+ lines)
├── data/               # Reference data files
│   ├── IBPT/           # Tax tables by state (CSV)
│   ├── ISSQN/          # Service tax classification
│   ├── MunIBGE/        # Municipality IBGE codes by UF
│   └── XSDs/           # XML Schema definitions (NF-e, NFC-e, NFS-e, MDF-e, CT-e)
tests/                  # Test suite (37 test files)
```

## Key Concepts

- **NF-e** (modelo 55): Standard electronic invoice
- **NFC-e** (modelo 65): Consumer electronic invoice (retail)
- **NFS-e**: Municipal service invoice (Betha/Ginfes providers)
- **MDF-e** (modelo 58): Transport manifest
- **CT-e**: Transport knowledge document (partial support)
- **SEFAZ**: State tax authority webservices
- **Homologacao**: Test environment (`_ambiente=2`)
- **SVRS/SVAN**: Virtual SEFAZ environments for states without own webservices

## Commands

```bash
# Run tests
pytest tests/

# Run specific test
pytest tests/test_nfe_serializacao_geral.py

# Lint
ruff check pynfe/

# Format
ruff format pynfe/
```

## Dependencies

- `lxml` — XML processing
- `signxml` — XML digital signatures
- `cryptography` / `pyopenssl` — Certificate handling
- `requests` — HTTP communication with SEFAZ
- `suds-community` — SOAP client (NFS-e only)
- `PyXB-X` — XML Schema bindings (NFS-e only)

## Important Notes

- Files under `pynfe/utils/nfse/` are **auto-generated** PyXB bindings — do not edit manually
- The `pynfe/data/` directory contains reference data files that should not be modified casually
- Tax code serialization follows strict SEFAZ XML schema ordering — field order matters
- Each Brazilian state has its own SEFAZ endpoint configuration in `webservices.py`
