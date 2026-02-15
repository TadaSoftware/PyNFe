# Source Map: `comunicacao.py` (1348 lines)

SEFAZ webservice communication for NF-e, NFC-e, NFS-e, MDF-e and CT-e.

## Classes Overview

| Class | Lines | Purpose |
|-------|-------|---------|
| `Comunicacao` | 31-47 | Abstract base class |
| `ComunicacaoSefaz` | 50-612 | NF-e/NFC-e SEFAZ communication |
| `ComunicacaoNfse` | 615-845 | NFS-e municipal communication (Betha/Ginfes) |
| `ComunicacaoMDFe` | 848-1119 | MDF-e SEFAZ communication |
| `ComunicacaoCTe` | 1121-1348 | CT-e SEFAZ communication |

---

## `Comunicacao` (base) — Lines 31-47

Stores `uf`, `certificado`, `certificado_senha`, `_ambiente` (1=prod, 2=homolog).

## `ComunicacaoSefaz` — Lines 50-612

### Public Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `autorizacao()` | 56-130 | Send NF-e for authorization (sync/async) |
| `consulta_recibo()` | 132-155 | Query batch processing result |
| `consulta_nota()` | 157-175 | Query NF-e status by access key |
| `consulta_distribuicao()` | 177-231 | DF-e distribution query (distNSU, consNSU, consChNFe) |
| `consulta_cadastro()` | 233-292 | Taxpayer registration query |
| `evento()` | 294-320 | Send NF-e events (cancel, correction letter) |
| `status_servico()` | 322-335 | Check SEFAZ server status |
| `inutilizacao()` | 337-410 | Number range invalidation |

### Internal Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `_get_url_an()` | 412-424 | Get national environment URL (AN) |
| `_get_url()` | 426-551 | **URL resolver** — routes to correct SEFAZ by UF, model, environment, contingency |
| `_construir_xml_soap()` | 553-570 | Build SOAP XML envelope |
| `_post_header()` | 572-581 | HTTP headers (PE requires SOAPAction) |
| `_post()` | 583-612 | Execute HTTPS POST with A1 certificate |

### URL Routing Detail (`_get_url`)
| Section | Lines | States |
|---------|-------|--------|
| Contingency SVRS | 429-462 | AM, BA, CE, GO, MA, MS, MT, PE, PR |
| Contingency SVAN | 463-476 | AC, AL, AP, DF, ES, MG, PA, PB, PI, RJ, RN, RO, RR, RS, SC, SE, SP, TO |
| Own webservices | 480-501 | PR, MS, SP, AM, CE, BA, GO, MG, MT, PE, RS |
| SVRS states | 504-533 | AC, AL, AP, DF, ES, PB, PI, RJ, RN, RO, RR, SC, SE, TO, PA |
| SVAN (MA only) | 536-548 | MA |

---

## `ComunicacaoNfse` — Lines 615-845

### Public Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `autorizacao()` | 635-644 | Generate NFS-e (Betha only) |
| `enviar_lote()` | 646-655 | Send batch (Ginfes only) |
| `consultar()` | 657-666 | Query NFS-e (Ginfes only) |
| `consultar_rps()` | 668-678 | Query by RPS (Betha + Ginfes) |
| `consultar_faixa()` | 680-687 | Query range (Betha only) |
| `consultar_lote()` | 689-698 | Query batch (Ginfes only) |
| `consultar_situacao_lote()` | 700-707 | Query batch status (Ginfes only) |
| `cancelar()` | 709-722 | Cancel NFS-e (Betha + Ginfes) |

### Internal Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `_cabecalho()` / `_cabecalho2()` | 724-762 | WSDL request header XML |
| `_cabecalho_ginfes()` | 764-768 | Ginfes-specific header via XSD |
| `_get_url()` | 770-780 | URL resolver for NFS-e |
| `_post()` | 782-804 | HTTP (no cert) WSDL communication |
| `_post_https()` | 806-845 | HTTPS (with cert) WSDL communication |

---

## `ComunicacaoMDFe` — Lines 848-1119

### Public Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `autorizacao()` | 874-956 | Send MDF-e for authorization (sync/async) |
| `status_servico()` | 958-965 | Check MDF-e server status |
| `consulta()` | 967-976 | Query MDF-e by access key |
| `consulta_nao_encerrados()` | 978-990 | Query non-closed MDF-e |
| `consulta_recibo()` | 992-1000 | Query batch processing result |
| `evento()` | 1002-1017 | Send MDF-e events (cancel, close, add driver, add DF-e, payment) |

### Internal Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `_construir_xml_soap()` | 1019-1044 | Build SOAP XML with header |
| `_post_header()` | 1046-1061 | HTTP headers |
| `_post()` | 1063-1099 | Execute HTTPS POST with cert |
| `_cabecalho_soap()` | 1101-1107 | SOAP header with cUF and versaoDados |
| `_get_url()` | 1109-1118 | URL resolver (SVRS only) |

---

## `ComunicacaoCTe` — Lines 1121-1348

### Public Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `status_servico()` | 1136-1147 | Check CT-e server status |
| `consulta_distribuicao()` | 1149-1200 | CT-e distribution query |
| `consulta()` | 1202-1211 | Query CT-e by access key |

### Internal Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `_get_url_an()` | 1213-1219 | National environment URL |
| `_cabecalho_soap()` | 1221-1227 | SOAP header |
| `_get_url()` | 1229-1281 | **URL resolver** — own (MT, MS, MG, PR, RS, SP), SVRS, SVSP |
| `_construir_xml_soap()` | 1283-1304 | Build SOAP XML envelope |
| `_post_header()` | 1306-1313 | HTTP headers |
| `_post()` | 1315-1348 | Execute HTTPS POST with cert |
