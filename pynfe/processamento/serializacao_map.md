# Source Map: `serializacao.py` (2740 lines)

XML serialization of NF-e, NFC-e, NFS-e and MDF-e documents into SEFAZ-compliant XML format.

## Classes Overview

| Class | Lines | Purpose |
|-------|-------|---------|
| `Serializacao` | 30-63 | Abstract base class (not instantiable directly) |
| `SerializacaoXML` | 66-1829 | Main NF-e/NFC-e XML serialization |
| `SerializacaoQrcode` | 2070-2174 | NFC-e QR Code generation |
| `SerializacaoNfse` | 2177-2243 | NFS-e serialization (Betha/Ginfes) |
| `SerializacaoQrcodeMDFe` | 2246-2269 | MDF-e QR Code generation |
| `SerializacaoMDFe` | 2272-2740 | MDF-e XML serialization |

---

## `Serializacao` (base class) — Lines 30-63

Abstract base for all serializers. Stores `_fonte_dados`, `_ambiente` (1=prod, 2=homolog), `_contingencia`, `_so_cpf`.

## `SerializacaoXML` — Lines 66-1829

### Exported Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `exportar()` | 71-97 | Main entry: exports NF-e XML from data source |
| `serializar_evento()` | 1831-1863 | Serializes NF-e events (cancellation, correction letter) |
| `serializar_evento_mdfe()` | 1865-1957 | Serializes MDF-e events (cancel, close, add driver, add DF-e, payment) |

### Internal Serializers (NF-e)
| Method | Lines | Purpose |
|--------|-------|---------|
| `_serializar_emitente()` | 105-146 | Issuer data (CNPJ/CPF, address, IE, CRT) |
| `_serializar_cliente()` | 148-200 | Customer/destination data (document, address, IE indicator) |
| `_serializar_transportadora()` | 202-228 | Carrier data |
| `_serializar_entrega_retirada()` | 230-255 | Delivery/withdrawal address |
| `_serializar_autorizados_baixar_xml()` | 257-270 | Authorized XML downloaders |
| `_serializar_produto_servico()` | 272-459 | **Product/service item** (prod data, fuel, taxes dispatch) |
| `_serializar_responsavel_tecnico()` | 1347-1359 | Technical responsible (NT2018/003) |
| `_serializar_nota_fiscal()` | 1423-1829 | **Main NF-e assembly** (ide, emit, dest, items, totals, transport, billing, payment, additional info) |

### Tax Serializers (within `SerializacaoXML`)
| Method | Lines | Purpose |
|--------|-------|---------|
| `_serializar_imposto_icms()` | 461-1078 | **ICMS tax** — all CST/CSOSN modalities |
| `_serializar_imposto_ipi()` | 1080-1118 | IPI tax |
| `_serializar_imposto_pis()` | 1120-1192 | PIS tax |
| `_serializar_imposto_cofins()` | 1194-1269 | COFINS tax |
| `_serializar_imposto_importacao()` | 1271-1293 | Import tax (II) |
| `_serializar_imposto_ibscbs()` | 1295-1322 | Reforma Tributaria — impostoMisto wrapper (CBS + IBS + IS) |
| `_serializar_cbs()` | 1324-1339 | CBS (Contribuicao sobre Bens e Servicos) |
| `_serializar_ibs()` | 1341-1361 | IBS (Imposto sobre Bens e Servicos) |
| `_serializar_is()` | 1363-1378 | IS (Imposto Seletivo) |
| `_serializar_declaracao_importacao()` | 1380-1430 | Import declaration (DI) |

### ICMS Modalities Detail (within `_serializar_imposto_icms`)
| CST/CSOSN | Lines | Description |
|-----------|-------|-------------|
| 00 | 465-489 | Fully taxed |
| 02 | 491-504 | Monophasic on fuels |
| 10 | 507-568 | Taxed + ICMS ST |
| 15 | 571-600 | Monophasic + retention on fuels |
| 20 | 603-642 | Reduced base |
| 30 | 645-685 | Exempt + ICMS ST |
| 40/41/50 | 688-699 | Exempt / Not taxed / Suspended |
| 51 | 702-719 | Deferral |
| 53 | 722-744 | Monophasic deferred on fuels |
| 60/ST | 747-770 | Previously charged by ST |
| 61 | 773-785 | Monophasic previously charged on fuels |
| 70 | 788-855 | Reduced base + ICMS ST |
| 90 | 858-930 | Other |
| 101 | 935-944 | Simples Nacional with credit |
| 102/103/300/400 | 951-954 | Simples Nacional without credit |
| 201/202/203 | 959-1004 | Simples Nacional + ICMS ST |
| 500 | 1007-1010 | SN previously charged by ST |
| 900 | 1013-1075 | SN Other |

### Payment Serializers
| Method | Lines | Purpose |
|--------|-------|---------|
| `_serializar_pagamentos_antigo_deprecado()` | 1361-1390 | Legacy payment (deprecated) |
| `_serializar_pagamentos()` | 1392-1421 | Current payment serialization |

### NF-e Assembly Detail (`_serializar_nota_fiscal`)
| Section | Lines | XML tags |
|---------|-------|----------|
| IDE (identification) | 1436-1499 | `<ide>` cUF, cNF, natOp, mod, serie, nNF, dhEmi, tpNF, etc. |
| Referenced NF-e | 1501-1537 | `<NFref>` refNFe, refNF, refNFP, refCTe |
| Contingency | 1539-1547 | dhCont, xJust |
| Emitter | 1549-1550 | `<emit>` |
| Customer | 1552-1564 | `<dest>` |
| Withdrawal/Delivery | 1566-1583 | `<retirada>`, `<entrega>` |
| Authorized XML | 1586-1587 | `<autXML>` |
| Items | 1589-1596 | `<det>` with nItem |
| Totals | 1598-1691 | `<total><ICMSTot>` all tax totals |
| Transport | 1693-1747 | `<transp>` modFrete, carrier, vehicle, volumes |
| Billing | 1748-1774 | `<cobr>` fat, dup |
| Payment | 1776-1801 | `<pag>` detPag |
| Additional info | 1803-1816 | `<infAdic>` |
| Technical responsible | 1818-1824 | `<infRespTec>` |

---

## `SerializacaoQrcode` — Lines 1960-2064

Generates NFC-e QR Code URL. Handles online/offline modes and state-specific URL patterns (SP, BA, MG, etc.).

## `SerializacaoNfse` — Lines 2067-2133

Delegates to Betha or Ginfes serializers. Methods: `gerar`, `gerar_lote`, `consultar_nfse`, `consultar_lote`, `consultar_rps`, `consultar_situacao_lote`, `cancelar`.

## `SerializacaoQrcodeMDFe` — Lines 2136-2159

Generates MDF-e QR Code URL using SVRS endpoint.

## `SerializacaoMDFe` — Lines 2162-2630

### Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `exportar()` | 2167-2193 | Main entry: exports MDF-e XML |
| `_serializar_emitente()` | 2201-2233 | MDF-e issuer (CPF/CNPJ, IE, address) |
| `_serializar_municipio_carrega()` | 2235-2245 | Loading municipality |
| `_serializar_percurso()` | 2247-2254 | Route (UF waypoints) |
| `_serializar_modal_rodoviario()` | 2256-2415 | **Road modal** (ANTT, CIOT, tolls, contractors, traction vehicle, trailer) |
| `_serializar_documentos()` | 2417-2441 | Linked documents (NF-e or CT-e) |
| `_serializar_seguradora()` | 2443-2463 | Insurance info |
| `_serializar_produto()` | 2465-2475 | Predominant product |
| `_serializar_totais()` | 2477-2497 | Totals (weight, qty) |
| `_serializar_lacres()` | 2499-2506 | Seals |
| `_serializar_responsavel_tecnico()` | 2508-2520 | Technical responsible |
| `_serializar_manifesto()` | 2522-2629 | **Main MDF-e assembly** (ide, emit, modal, doc, seg, prod, tot, lacres, infAdic, infRespTec) |
