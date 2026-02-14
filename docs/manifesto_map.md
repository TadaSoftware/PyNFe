# Source Map: `manifesto.py` (447 lines)

Entity models for MDF-e (Manifesto de Documentos Fiscais Eletrônicos).

## Classes Overview

| Class | Lines | Purpose |
|-------|-------|---------|
| `Manifesto` | 12-200 | Main MDF-e entity |
| `ManifestoEmitente` | ~203-230 | MDF-e issuer |
| `ManifestoMunicipioCarrega` | ~232-240 | Loading municipality |
| `ManifestoPercurso` | ~242-248 | Route waypoint (UF) |
| `ManifestoModalRodoviario` | ~250-290 | Road transport modal |
| `ManifestoCIOT` | ~292-300 | CIOT (toll system) |
| `ManifestoPedagio` | ~302-315 | Toll information |
| `ManifestoContratante` | ~317-330 | Contractor info |
| `ManifestoVeiculoTracao` | ~332-360 | Traction vehicle |
| `ManifestoVeiculoReboque` | ~362-385 | Trailer vehicle |
| `ManifestoProprietario` | ~387-400 | Vehicle owner |
| `ManifestoCondutor` | ~402-410 | Driver |
| `ManifestoDocumentos` | ~412-425 | Linked documents (NF-e/CT-e) |
| `ManifestoSeguradora` | ~427-440 | Insurance |
| `ManifestoTotais` | ~442-447 | Totals (weight, cargo value) |

## `Manifesto` — Lines 12-200

### Field Groups
| Section | Lines | Fields |
|---------|-------|--------|
| Identity | 12-68 | uf, tipo_emitente, tipo_transportador, modelo (58), serie, numero_mdfe, codigo_numerico_aleatorio, modal, data_emissao, forma_emissao, processo_emissao, UFIni, UFFim |
| Read-only | 65-72 | digest_value, protocolo, data |
| Relationships | 74-110 | municipio_carrega, percurso, dhIniViagem, emitente, modal_rodoviario, documentos, seguradora, produto, totais, lacres, responsavel_tecnico |
| Additional info | ~112-120 | informacoes_adicionais_interesse_fisco, informacoes_complementares_interesse_contribuinte |

### Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `__init__()` | ~122-140 | Initialize all list fields |
| `adicionar_*()` | ~142-185 | Add municipio_carrega, percurso, emitente, modal_rodoviario, documento, seguradora, produto, totais, lacre, responsavel_tecnico |
| `_codigo_numerico_aleatorio()` | ~187-190 | Generate random 8-digit code |
| `_dv_codigo_numerico()` | ~192-200 | Calculate check digit (mod 11) |
| `identificador_unico` (property) | ~200+ | Build 44-char MDF-e access key |
