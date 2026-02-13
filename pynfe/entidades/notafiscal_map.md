# Source Map: `notafiscal.py` (1253 lines)

Entity models for NF-e/NFC-e invoices and related objects (products, taxes, payments, transport, etc.).

## Classes Overview

| Class | Lines | Purpose |
|-------|-------|---------|
| `NotaFiscal` | 14-572 | Main invoice entity |
| `NotaFiscalReferenciada` | 575-603 | Referenced invoice |
| `NotaFiscalProduto` | 606-1019 | Product/service item with all tax fields |
| `NotaFiscalDeclaracaoImportacao` | 1022-1067 | Import declaration |
| `NotaFiscalDeclaracaoImportacaoAdicao` | 1070-1082 | Import declaration addition |
| `NotaFiscalTransporteVolume` | 1084-1113 | Transport volume |
| `NotaFiscalTransporteVolumeLacre` | 1116-1118 | Volume seal |
| `NotaFiscalCobrancaDuplicata` | 1121-1129 | Billing duplicate |
| `NotaFiscalObservacaoContribuinte` | 1132-1137 | Taxpayer note |
| `NotaFiscalProcessoReferenciado` | 1140-1150 | Referenced process |
| `NotaFiscalEntregaRetirada` | 1153-1190 | Delivery/withdrawal address |
| `NotaFiscalServico` | 1192-1220 | NFS-e service invoice |
| `NotaFiscalResponsavelTecnico` | 1223-1229 | Technical responsible (NT2018/003) |
| `AutorizadosBaixarXML` | 1232-1233 | Authorized XML downloaders |
| `NotaFiscalPagamentos` | 1236-1253 | Payment details |

---

## `NotaFiscal` — Lines 14-572

### Field Groups
| Section | Lines | Fields |
|---------|-------|--------|
| Deprecated fields | 16-23 | `tipo_pagamento` deprecated |
| Invoice identity | 25-127 | status, codigo_numerico, modelo, serie, numero_nf, data_emissao, natureza_operacao, tipo_documento, processo_emissao, tipo_impressao_danfe, forma_emissao, finalidade_emissao, cliente_final, indicador_presencial, indicador_intermediador, indicador_destino, uf, municipio |
| Read-only fields | 128-144 | digest_value, valor_total_nota, valor_icms_nota, valor_icms_st_nota, protocolo, data |
| Relationships | 146-173 | notas_fiscais_referenciadas, emitente, destinatario_remetente, entrega, retirada, autorizados_baixar_xml, produtos_e_servicos |
| ICMS totals | 175-303 | totais_icms_base_calculo, totais_icms_total, totais_icms_desonerado, totais_icms_st_*, totais_icms_total_*, totais_fcp_*, totais_icms_inter_*, totais_icms_*_mono_* |
| Transport | 305-361 | transporte_modalidade_frete, transporte_transportadora, transporte_retencao_icms_*, transporte_veiculo_*, transporte_reboque_*, transporte_volumes |
| Billing | 363-378 | fatura_numero, fatura_valor_original, fatura_valor_desconto, fatura_valor_liquido, duplicatas |
| Additional info | 380-397 | informacoes_adicionais_*, observacoes_contribuinte, processos_referenciados, pagamentos, valor_troco |

### Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `__init__()` | 399-410 | Initialize all list fields |
| `adicionar_pagamento()` | 415-419 | Add payment |
| `adicionar_autorizados_baixar_xml()` | 421-424 | Add authorized XML downloader |
| `adicionar_nota_fiscal_referenciada()` | 426-430 | Add referenced invoice |
| `adicionar_produto_servico()` | 432-484 | **Add product** — also accumulates all ICMS/tax totals |
| `adicionar_transporte_volume()` | 486-490 | Add transport volume |
| `adicionar_duplicata()` | 492-496 | Add billing duplicate |
| `adicionar_observacao_contribuinte()` | 498-502 | Add taxpayer note |
| `adicionar_processo_referenciado()` | 504-508 | Add referenced process |
| `adicionar_responsavel_tecnico()` | 510-514 | Add technical responsible |
| `_codigo_numerico_aleatorio()` | 516-519 | Generate random 8-digit code |
| `_dv_codigo_numerico()` | 521-543 | Calculate check digit (mod 11) |
| `identificador_unico` (property) | 545-572 | Build 44-char NF-e access key |

---

## `NotaFiscalProduto` — Lines 606-1019

### Field Groups
| Section | Lines | Fields |
|---------|-------|--------|
| Product data | 612-686 | codigo, descricao, ean, ncm, cfop, unidade_comercial, quantidade_comercial, valor_unitario_comercial, unidade_tributavel, cbenef, quantidade_tributavel, valor_unitario_tributavel, ean_tributavel, total_frete, total_seguro, desconto, outras_despesas_acessorias, valor_total_bruto, numero_pedido, numero_item |
| Fuel data | 688-733 | cProdANP, descANP, pGLP, pGNn, pGNi, vPart, UFCons, comb_codif, comb_q_temp, comb_n_bico, comb_n_bomba, comb_n_tanque, comb_v_enc_ini, comb_v_enc_fin, comb_p_bio |
| ICMS fields | 735-826 | icms_modalidade, icms_origem, icms_modalidade_determinacao_bc, icms_percentual_reducao_bc, icms_valor_base_calculo, icms_aliquota, icms_valor, icms_desonerado, icms_motivo_desoneracao, icms_st_*, fcp_*, icms_inter_*, icms_st_ret_*, icms_*_mono_* |
| IPI fields | 828-877 | ipi_situacao_tributaria, ipi_classe_enquadramento, ipi_codigo_enquadramento, ipi_valor_base_calculo, ipi_aliquota, ipi_valor_ipi, pdevol, ipi_valor_ipi_dev |
| PIS fields | 879-923 | pis_modalidade (via pis_situacao_tributaria), pis_valor_base_calculo, pis_aliquota_percentual, pis_aliquota_reais, pis_valor, pis_st_* |
| COFINS fields | 925-969 | cofins_modalidade, cofins_valor_base_calculo, cofins_aliquota_percentual, cofins_aliquota_reais, cofins_valor, cofins_st_* |
| ISSQN fields | 971-990 | issqn_valor_base_calculo, issqn_aliquota, issqn_lista_servico, issqn_uf, issqn_municipio, issqn_valor |
| Import tax fields | 992-1003 | imposto_importacao_valor_base_calculo, imposto_importacao_valor_despesas_aduaneiras, imposto_importacao_valor_iof, imposto_importacao_valor |
| Additional info | 1005-1019 | informacoes_adicionais, declaracoes_importacao |

---

## Supporting Entities (Lines 1022-1253)

Small entity classes for nested data — see class table above for line ranges. All extend `Entidade` base class and use kwargs initialization.
