# Source Map: `serializacao.py` (2771 lines)

XML serialization of NF-e, NFC-e, NFS-e and MDF-e documents into SEFAZ-compliant XML format.

## Classes Overview

| Class | Lines | Purpose |
|-------|-------|---------|
| `Serializacao` | 30-63 | Abstract base class (not instantiable directly) |
| `SerializacaoXML` | 66-1860 | Main NF-e/NFC-e XML serialization |
| `SerializacaoQrcode` | 2102-2206 | NFC-e QR Code generation |
| `SerializacaoNfse` | 2209-2275 | NFS-e serialization (Betha/Ginfes) |
| `SerializacaoQrcodeMDFe` | 2278-2301 | MDF-e QR Code generation |
| `SerializacaoMDFe` | 2304-2771 | MDF-e XML serialization |

---

## `Serializacao` (base class) — Lines 30-63

Abstract base for all serializers. Stores `_fonte_dados`, `_ambiente` (1=prod, 2=homolog), `_contingencia`, `_so_cpf`.

## `SerializacaoXML` — Lines 66-1860

### Exported Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `exportar()` | 71-97 | Main entry: exports NF-e XML from data source |
| `serializar_evento()` | ~1862 | Serializes NF-e events (cancellation, correction letter) |
| `serializar_evento_mdfe()` | ~1896 | Serializes MDF-e events (cancel, close, add driver, add DF-e, payment) |

### Internal Serializers (NF-e)
| Method | Lines | Purpose |
|--------|-------|---------|
| `_serializar_emitente()` | 105-146 | Issuer data (CNPJ/CPF, address, IE, CRT) |
| `_serializar_cliente()` | 148-200 | Customer/destination data (document, address, IE indicator) |
| `_serializar_transportadora()` | 202-228 | Carrier data |
| `_serializar_entrega_retirada()` | 230-255 | Delivery/withdrawal address |
| `_serializar_autorizados_baixar_xml()` | 257-270 | Authorized XML downloaders |
| `_serializar_produto_servico()` | 272-467 | **Product/service item** (prod data, fuel, taxes dispatch incl. IBSCBS) |
| `_serializar_responsavel_tecnico()` | 1440-1452 | Technical responsible (NT2018/003) |
| `_serializar_nota_fiscal()` | 1516-1860 | **Main NF-e assembly** (ide w/ cMunFGIBS, emit, dest, items, totals incl. IBSCBSTot, transport, billing, payment, additional info) |

### Tax Serializers (within `SerializacaoXML`)
| Method | Lines | Purpose |
|--------|-------|---------|
| `_serializar_imposto_icms()` | 469-1086 | **ICMS tax** — all CST/CSOSN modalities |
| `_serializar_imposto_ipi()` | 1088-1126 | IPI tax |
| `_serializar_imposto_pis()` | 1128-1200 | PIS tax |
| `_serializar_imposto_cofins()` | 1202-1277 | COFINS tax |
| `_serializar_imposto_importacao()` | 1279-1301 | Import tax (II) |
| `_serializar_imposto_ibscbs()` | 1310-1328 | **Reforma Tributaria** — dispatches IBSCBS + IS serialization |
| `_serializar_ibscbs()` | 1330-1369 | IBSCBS (IBS + CBS) — `<IBSCBS>` as direct child of `<imposto>` |
| `_serializar_is()` | 1371-1386 | IS (Imposto Seletivo) — ready but not called until 2027 |
| `_serializar_declaracao_importacao()` | 1388-1438 | Import declaration (DI) |

### ICMS Modalities Detail (within `_serializar_imposto_icms`)
| CST/CSOSN | Lines | Description |
|-----------|-------|-------------|
| 00 | 473-497 | Fully taxed |
| 02 | 499-512 | Monophasic on fuels |
| 10 | 515-576 | Taxed + ICMS ST |
| 15 | 579-608 | Monophasic + retention on fuels |
| 20 | 611-650 | Reduced base |
| 30 | 653-693 | Exempt + ICMS ST |
| 40/41/50 | 696-707 | Exempt / Not taxed / Suspended |
| 51 | 710-727 | Deferral |
| 53 | 730-752 | Monophasic deferred on fuels |
| 60/ST | 755-778 | Previously charged by ST |
| 61 | 781-793 | Monophasic previously charged on fuels |
| 70 | 796-863 | Reduced base + ICMS ST |
| 90 | 866-938 | Other |
| 101 | 943-952 | Simples Nacional with credit |
| 102/103/300/400 | 959-962 | Simples Nacional without credit |
| 201/202/203 | 967-1012 | Simples Nacional + ICMS ST |
| 500 | 1015-1018 | SN previously charged by ST |
| 900 | 1021-1083 | SN Other |

### Payment Serializers
| Method | Lines | Purpose |
|--------|-------|---------|
| `_serializar_pagamentos_antigo_deprecado()` | 1454-1483 | Legacy payment (deprecated) |
| `_serializar_pagamentos()` | 1485-1514 | Current payment serialization |

### NF-e Assembly Detail (`_serializar_nota_fiscal`)
| Section | Lines | XML tags |
|---------|-------|----------|
| IDE (identification) | 1529-1594 | `<ide>` cUF, cNF, natOp, mod, serie, nNF, dhEmi, tpNF, cMunFG, **cMunFGIBS**, etc. |
| Referenced NF-e | 1596-1632 | `<NFref>` refNFe, refNF, refNFP, refCTe |
| Contingency | 1634-1643 | dhCont, xJust |
| Emitter | 1645 | `<emit>` |
| Customer | 1648-1659 | `<dest>` |
| Withdrawal/Delivery | 1661-1678 | `<retirada>`, `<entrega>` |
| Authorized XML | 1681-1682 | `<autXML>` |
| Items | 1684-1691 | `<det>` with nItem |
| Totals (ICMSTot) | 1693-1786 | `<total><ICMSTot>` all legacy tax totals |
| **Totals (IBSCBSTot)** | 1788-1833 | `<total><IBSCBSTot>` Reforma Tributaria totals (vBCIBSCBS, gIBS, gCBS) |
| Transport | 1835-1878 | `<transp>` modFrete, carrier, vehicle, volumes |
| Billing | ~1880-1900 | `<cobr>` fat, dup |
| Payment | ~1902-1930 | `<pag>` detPag |
| Additional info | ~1932-1945 | `<infAdic>` |
| Technical responsible | ~1947-1953 | `<infRespTec>` |

---

## `SerializacaoQrcode` — Lines 2102-2206

Generates NFC-e QR Code URL. Handles online/offline modes and state-specific URL patterns (SP, BA, MG, etc.).

## `SerializacaoNfse` — Lines 2209-2275

Delegates to Betha or Ginfes serializers. Methods: `gerar`, `gerar_lote`, `consultar_nfse`, `consultar_lote`, `consultar_rps`, `consultar_situacao_lote`, `cancelar`.

## `SerializacaoQrcodeMDFe` — Lines 2278-2301

Generates MDF-e QR Code URL using SVRS endpoint.

## `SerializacaoMDFe` — Lines 2304-2771

### Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `exportar()` | 2309-2335 | Main entry: exports MDF-e XML |
| `_serializar_emitente()` | 2343-2375 | MDF-e issuer (CPF/CNPJ, IE, address) |
| `_serializar_municipio_carrega()` | 2377-2387 | Loading municipality |
| `_serializar_percurso()` | 2389-2396 | Route (UF waypoints) |
| `_serializar_modal_rodoviario()` | 2398-2557 | **Road modal** (ANTT, CIOT, tolls, contractors, traction vehicle, trailer) |
| `_serializar_documentos()` | 2559-2583 | Linked documents (NF-e or CT-e) |
| `_serializar_seguradora()` | 2585-2605 | Insurance info |
| `_serializar_produto()` | 2607-2617 | Predominant product |
| `_serializar_totais()` | 2619-2639 | Totals (weight, qty) |
| `_serializar_lacres()` | 2641-2648 | Seals |
| `_serializar_responsavel_tecnico()` | 2650-2662 | Technical responsible |
| `_serializar_manifesto()` | 2664-2771 | **Main MDF-e assembly** (ide, emit, modal, doc, seg, prod, tot, lacres, infAdic, infRespTec) |
