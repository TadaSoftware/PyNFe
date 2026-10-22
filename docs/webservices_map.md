# Source Map: `webservices.py` (684 lines)

SEFAZ webservice endpoint URLs organized by document type, state, and environment.

## Sections

| Section | Lines | Variable | Purpose |
|---------|-------|----------|---------|
| Host roles + `qrCode` vs `urlChave` | 1-44 | — | Module docstring: which key family each consumer may read |
| NFC-e endpoints | 49-363 | `NFCE` | NFC-e webservice URLs, QR Code URLs and consultation URLs by state |
| `qrcode_host` helper | 366-384 | — | Consultation-portal host prefix for `<qrCode>` |
| `url_consulta_chave` helper | 392-406 | — | Complete `<urlChave>` URL, never concatenated |
| NF-e endpoints | 412-583 | `NFE` | NF-e webservice URLs by state |
| NFS-e endpoints | 586-611 | `NFSE` | NFS-e URLs (Betha, Ginfes) |
| MDF-e endpoints | 614-628 | `MDFE` | MDF-e URLs (SVRS only) |
| CT-e endpoints | 630-684 | `CTE` | CT-e URLs by state |

## URL Structure

Each state/virtual environment entry contains:
- `STATUS` — Service status check endpoint
- `AUTORIZACAO` — Authorization endpoint
- `RECIBO` — Receipt query endpoint
- `CHAVE` — Access key query endpoint
- `INUTILIZACAO` — Number invalidation endpoint
- `EVENTOS` — Event reception endpoint
- `CADASTRO` — Registration query endpoint (some states)
- `HTTPS` — Production base URL prefix of the AUTHORIZER (webservices; read only by
  `ComunicacaoSefaz._get_url`)
- `HOMOLOGACAO` — Homologation base URL prefix of the AUTHORIZER
- `QR_HOST` / `QR_HOST_HOMOLOGACAO` — Base URL prefix of the CONSULTATION portal, used for
  `<qrCode>`/`<urlChave>` (read only by `qrcode_host`); falls back to `HTTPS`/`HOMOLOGACAO`
  for UFs that serve both roles from the same host
- `QR` — QR Code path (NFC-e only; `QR_HOMOLOGACAO` where the path differs per environment)
- `URL` — Legacy consultation path (NFC-e only), still read by `url_consulta_chave` as a
  fallback for UFs that declare no `CONSULTA_CHAVE`
- `CONSULTA_CHAVE` / `CONSULTA_CHAVE_HOMOLOGACAO` — COMPLETE, verbatim `<urlChave>` from the
  official registry (`URL-ConsultaNFCe_2.00` in ACBr / the ENCAT listing). Returned as-is: no
  host prefix is ever concatenated onto it. Declare this for any UF you add or fix

The two host families must never be shared: a UF such as GO answers webservice POSTs sent to
its consultation host with a load-balancer redirect and HTML, so the invoice never receives a
SEFAZ verdict and the failure surfaces as a transport/XML-parse error, not a rejeicao.

`<qrCode>` and `<urlChave>` are likewise separate registries, each with its own entry in the
official listing, so one is never a safe substitute for the other: GO rejects 878 when
`urlChave` carries the QR Code address. Equality is not by itself the defect — the registry
does list the same address for both fields in a few UFs (SC today) — so always compare against
the registry entry for the field you are changing, never against the sibling field. `urlChave`
values live in `CONSULTA_CHAVE*`; `qrCode` is built from `QR*` over `qrcode_host`. The exact set
of UFs where the two addresses coincide is pinned in `tests/test_nfce_urlchave_por_uf.py`.

## State/Virtual Environment Groups

### NFC-e (`NFCE`) — Lines 49-363
| Key | Lines | Description |
|-----|-------|-------------|
| Individual states | 50-350 | RO, AC, AM, RR, PA, AP, TO, MA, PI, CE, RN, PB, PE, AL, SE, BA, MG, ES, RJ, SP, PR, SC, RS, MS, MT, GO, DF |
| `SVRS` | 352-362 | Virtual SEFAZ RS (fallback for states without own NFC-e) |

### NF-e (`NFE`) — Lines 412-583
| Key | Lines | Description |
|-----|-------|-------------|
| `AN` | 414-421 | National environment (events, distribution) |
| Individual states | 422-541 | AM, MA, PE, BA, MG, SP, PR, RS, MS, MT, GO |
| `SVAN` | 542-552 | Virtual SEFAZ AN (MA for NF-e) |
| `SVRS` | 553-563 | Virtual SEFAZ RS (most states) |
| `SVC-AN` | 564-572 | Contingency AN |
| `SVC-RS` | 573-582 | Contingency RS |

### NFS-e (`NFSE`) — Lines 586-611
| Key | Lines | Description |
|-----|-------|-------------|
| `BETHA` | 588-598 | Betha provider (HTTP WSDL) |
| `GINFES` | 600-610 | Ginfes provider (HTTPS WSDL) |

### MDF-e (`MDFE`) — Lines 614-628
Only `SVRS` (616-627) — single authorizer for all states.

### CT-e (`CTE`) — Lines 630-684
| Key | Lines | Description |
|-----|-------|-------------|
| `AN` | 631-635 | National environment (distribution) |
| Individual states | 636-671 | MT, MS, MG, PR, RS, SP |
| `SVRS` | 672-677 | Virtual SEFAZ RS |
| `SVSP` | 678-683 | Virtual SEFAZ SP (AP, PE, RR) |

## Helpers

| Function | Lines | Purpose |
|----------|-------|---------|
| `qrcode_host(uf, producao=True)` | 366-384 | Consultation-portal host prefix for `<qrCode>`, with fallback to the webservice host |
| `url_consulta_chave(uf, producao=True)` | 392-406 | Complete `<urlChave>` URL from `CONSULTA_CHAVE*`, falling back to the legacy `URL` path (which it prefixes with `qrcode_host`) |
