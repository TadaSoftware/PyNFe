# Source Map: `autorizador_nfse.py` (538 lines)

NFS-e authorization and serialization for Betha and Ginfes providers.

## Classes Overview

| Class | Lines | Purpose |
|-------|-------|---------|
| `InterfaceAutorizador` | 5-11 | Abstract interface (consultar_rps, cancelar) |
| `SerializacaoBetha` | 14-200 | Betha NFS-e XML generation using PyXB bindings |
| `SerializacaoGinfes` | ~202-538 | Ginfes NFS-e XML generation using PyXB bindings |

## `SerializacaoBetha` — Lines 14-200

### Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `__init__()` | 15-18 | Import Betha NFS-e v2.02 schema |
| `gerar()` | 20-94 | Generate NFS-e XML (service, provider, customer, RPS) |
| `consultar_rps()` | 96-130 | Query NFS-e by RPS |
| `consultar_faixa()` | ~132-160 | Query NFS-e by range |
| `cancelar()` | ~162-200 | Cancel NFS-e |

## `SerializacaoGinfes` — Lines ~202-538

### Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `__init__()` | ~202-210 | Import Ginfes schema modules |
| `cabecalho()` | ~212-220 | Generate XML header |
| `serializar_lote_assincrono()` | ~222-310 | Serialize async batch (RPS list) |
| `consultar_nfse()` | ~312-360 | Query NFS-e by provider/period |
| `consultar_lote()` | ~362-390 | Query batch by number |
| `consultar_rps()` | ~392-420 | Query NFS-e by RPS |
| `consultar_situacao_lote()` | ~422-450 | Query batch status |
| `cancelar()` / `cancelar_v2()` | ~452-538 | Cancel NFS-e (v2 and v3) |
