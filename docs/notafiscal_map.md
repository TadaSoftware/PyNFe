# Source Map: `notafiscal.py` (1303 lines)

Entity models for NF-e/NFC-e invoices and related objects (products, taxes, payments, transport, etc.).

## Classes Overview

| Class | Lines | Purpose |
|-------|-------|---------|
| `NotaFiscal` | 14-593 | Main invoice entity |
| `NotaFiscalReferenciada` | 595-624 | Referenced invoice |
| `NotaFiscalProduto` | 626-1071 | Product/service item with all tax fields |
| `NotaFiscalDeclaracaoImportacao` | 1073-1119 | Import declaration |
| `NotaFiscalDeclaracaoImportacaoAdicao` | 1121-1133 | Import declaration addition |
| `NotaFiscalTransporteVolume` | 1135-1164 | Transport volume |
| `NotaFiscalTransporteVolumeLacre` | 1167-1169 | Volume seal |
| `NotaFiscalCobrancaDuplicata` | 1172-1180 | Billing duplicate |
| `NotaFiscalObservacaoContribuinte` | 1183-1188 | Taxpayer note |
| `NotaFiscalProcessoReferenciado` | 1191-1201 | Referenced process |
| `NotaFiscalEntregaRetirada` | 1204-1240 | Delivery/withdrawal address |
| `NotaFiscalServico` | 1243-1271 | NFS-e service invoice |
| `NotaFiscalResponsavelTecnico` | 1274-1280 | Technical responsible (NT2018/003) |
| `AutorizadosBaixarXML` | 1283-1284 | Authorized XML downloaders |
| `NotaFiscalPagamentos` | 1287-1303 | Payment details |

---

## `NotaFiscal` — Lines 14-593

### Field Groups
| Section | Lines | Fields |
|---------|-------|--------|
| Deprecated fields | 16-23 | `tipo_pagamento` deprecated |
| Invoice identity | 25-127 | status, codigo_numerico, modelo, serie, numero_nf, data_emissao, natureza_operacao, tipo_documento, processo_emissao, tipo_impressao_danfe, forma_emissao, finalidade_emissao, cliente_final, indicador_presencial, indicador_intermediador, indicador_destino, uf, municipio |
| Read-only fields | 128-144 | digest_value, valor_total_nota, valor_icms_nota, valor_icms_st_nota, protocolo, data |
| Relationships | 146-173 | notas_fiscais_referenciadas, emitente, destinatario_remetente, entrega, retirada, autorizados_baixar_xml, produtos_e_servicos |
| ICMS totals | 175-303 | totais_icms_base_calculo, totais_icms_total, totais_icms_desonerado, totais_icms_st_*, totais_icms_total_*, totais_fcp_*, totais_icms_inter_*, totais_icms_*_mono_* |
| **Reforma Tributaria totals** | 305-314 | totais_vbc_ibscbs, totais_ibs_uf, totais_ibs_mun, totais_ibs, totais_cbs, totais_is, **municipio_fato_gerador_ibs** — IVA Dual totals + Group B field (EC 132/2023) |
| Transport | 317-372 | transporte_modalidade_frete, transporte_transportadora, transporte_retencao_icms_*, transporte_veiculo_*, transporte_reboque_*, transporte_volumes |
| Billing | 374-389 | fatura_numero, fatura_valor_original, fatura_valor_desconto, fatura_valor_liquido, duplicatas |
| Additional info | 391-408 | informacoes_adicionais_*, observacoes_contribuinte, processos_referenciados, pagamentos, valor_troco |

### Methods
| Method | Lines | Purpose |
|--------|-------|---------|
| `__init__()` | 410-421 | Initialize all list fields |
| `adicionar_pagamento()` | 426-430 | Add payment |
| `adicionar_autorizados_baixar_xml()` | 432-435 | Add authorized XML downloader |
| `adicionar_nota_fiscal_referenciada()` | 437-441 | Add referenced invoice |
| `adicionar_produto_servico()` | 443-504 | **Add product** — accumulates all ICMS/tax totals + **IBSCBS/IS totals** (vNF excludes IBS/CBS/IS) |
| `adicionar_transporte_volume()` | 506-510 | Add transport volume |
| `adicionar_duplicata()` | 512-516 | Add billing duplicate |
| `adicionar_observacao_contribuinte()` | 518-522 | Add taxpayer note |
| `adicionar_processo_referenciado()` | 524-528 | Add referenced process |
| `adicionar_responsavel_tecnico()` | 530-534 | Add technical responsible |
| `_codigo_numerico_aleatorio()` | 536-539 | Generate random 8-digit code |
| `_dv_codigo_numerico()` | 541-563 | Calculate check digit (mod 11) |
| `identificador_unico` (property) | 565-593 | Build 44-char NF-e access key |

---

## `NotaFiscalProduto` — Lines 626-1071

### Field Groups
| Section | Lines | Fields |
|---------|-------|--------|
| Product data | 632-706 | codigo, descricao, ean, ncm, cfop, unidade_comercial, quantidade_comercial, valor_unitario_comercial, unidade_tributavel, cbenef, quantidade_tributavel, valor_unitario_tributavel, ean_tributavel, total_frete, total_seguro, desconto, outras_despesas_acessorias, valor_total_bruto, numero_pedido, numero_item |
| Fuel data | 708-753 | cProdANP, descANP, pGLP, pGNn, pGNi, vPart, UFCons, comb_codif, comb_q_temp, comb_n_bico, comb_n_bomba, comb_n_tanque, comb_v_enc_ini, comb_v_enc_fin, comb_p_bio |
| ICMS fields | 755-846 | icms_modalidade, icms_origem, icms_modalidade_determinacao_bc, icms_percentual_reducao_bc, icms_valor_base_calculo, icms_aliquota, icms_valor, icms_desonerado, icms_motivo_desoneracao, icms_st_*, fcp_*, icms_inter_*, icms_st_ret_*, icms_*_mono_* |
| IPI fields | 848-897 | ipi_situacao_tributaria, ipi_classe_enquadramento, ipi_codigo_enquadramento, ipi_valor_base_calculo, ipi_aliquota, ipi_valor_ipi, pdevol, ipi_valor_ipi_dev |
| PIS fields | 899-943 | pis_modalidade (via pis_situacao_tributaria), pis_valor_base_calculo, pis_aliquota_percentual, pis_aliquota_reais, pis_valor, pis_st_* |
| COFINS fields | 945-989 | cofins_modalidade, cofins_valor_base_calculo, cofins_aliquota_percentual, cofins_aliquota_reais, cofins_valor, cofins_st_* |
| ISSQN fields | 991-1010 | issqn_valor_base_calculo, issqn_aliquota, issqn_lista_servico, issqn_uf, issqn_municipio, issqn_valor |
| Import tax fields | 1012-1023 | imposto_importacao_valor_base_calculo, imposto_importacao_valor_despesas_aduaneiras, imposto_importacao_valor_iof, imposto_importacao_valor |
| **Reforma Tributaria fields** | 1025-1054 | **IBSCBS**: ibscbs_cst, ibscbs_c_class_trib, ibscbs_vbc, ibscbs_p_ibs_uf, ibscbs_v_ibs_uf, ibscbs_p_ibs_mun, ibscbs_v_ibs_mun, ibscbs_v_ibs, ibscbs_p_cbs, ibscbs_v_cbs; **IS**: is_cst_selec, is_c_class_trib, is_vbc, is_aliquota, is_valor |
| Additional info | 1056-1071 | informacoes_adicionais, declaracoes_importacao |

---

## Supporting Entities (Lines 1073-1303)

Small entity classes for nested data — see class table above for line ranges. All extend `Entidade` base class and use kwargs initialization.
