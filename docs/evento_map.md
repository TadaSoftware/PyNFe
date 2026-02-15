# Source Map: `evento.py` (237 lines)

Event entity models for NF-e and MDF-e lifecycle operations.

## Classes Overview

| Class | Lines | Purpose |
|-------|-------|---------|
| `Evento` | 11-46 | Base event class |
| `EventoCancelarNota` | 49-60 | NF-e cancellation (tp_evento=110111) |
| `EventoCartaCorrecao` | 63-90 | NF-e correction letter (tp_evento=110110) |
| `EventoManifestacaoDest` | 93-130 | Recipient manifestation (confirm/unknown/not performed/unaware) |
| `EventoOperacaoNaoRealizada` | ~132-145 | Operation not performed |
| `EventoCancelarMDFe` | ~147-160 | MDF-e cancellation |
| `EventoEncerrarMDFe` | ~162-180 | MDF-e closure |
| `EventoIncluirCondutorMDFe` | ~182-195 | Add driver to MDF-e |
| `EventoIncluirDFeMDFe` | ~197-215 | Add DF-e to MDF-e |
| `EventoPagamentoMDFe` | ~217-237 | MDF-e operation payment |

## `Evento` (base) — Lines 11-46

Fields: `id`, `orgao`, `cnpj`, `chave`, `data_emissao`, `uf`, `tp_evento`, `n_seq_evento`, `descricao`.

Property `identificador` builds: `"ID" + tp_evento + chave + n_seq_evento(2 digits)`.

## Key Event Types

| Class | tp_evento | descricao |
|-------|-----------|-----------|
| `EventoCancelarNota` | 110111 | "Cancelamento" |
| `EventoCartaCorrecao` | 110110 | "Carta de Correcao" |
| `EventoManifestacaoDest` | 210200-210240 | Various manifestation types |
| `EventoOperacaoNaoRealizada` | 110112 | "Operacao nao Realizada" |
| `EventoCancelarMDFe` | 110111 | "Cancelamento" (MDF-e) |
| `EventoEncerrarMDFe` | 110112 | "Encerramento" |
| `EventoIncluirCondutorMDFe` | 110114 | "Inclusão Condutor" |
| `EventoIncluirDFeMDFe` | 110115 | "Inclusao DF-e" |
| `EventoPagamentoMDFe` | 110116 | "Pagamento Operacao MDF-e" |
