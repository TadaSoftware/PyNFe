# Source Map: `pynfe/utils/__init__.py` (253 lines)

Utility functions for municipality/country lookups, XML signing, and helpers.

## Functions

| Function | Lines | Purpose |
|----------|-------|---------|
| `so_numeros()` | 22-29 | Extract only digits from string |
| `obter_pais_por_codigo()` | 33-41 | Get country name by code (default: 1058=Brasil) |
| `normalizar_municipio()` | 64-68 | Normalize municipality name (remove accents, uppercase) |
| `carregar_arquivo_municipios()` | 72-98 | Load IBGE municipality file for a given UF |
| `carregar_arquivo_pais()` | ~100-120 | Load country code file |
| `obter_municipio_por_codigo()` | ~122-140 | Get municipality name by IBGE code + UF |
| `obter_codigo_por_municipio()` | ~142-170 | Get IBGE code by municipality name + UF |
| `obter_municipio_e_codigo()` | ~172-190 | Get both municipality name and code |
| `assinar_com_a1()` | ~192-230 | Sign XML using A1 digital certificate |
| `validar_xml()` | ~232-253 | Validate XML against XSD schema |

## Constants

| Constant | Lines | Purpose |
|----------|-------|---------|
| `CAMINHO_DATA` | 44 | Path to `pynfe/data/` directory |
| `CAMINHO_MUNICIPIOS` | 45 | Path to `pynfe/data/MunIBGE/` |
| `CARACTERS_ACENTUADOS` | 46-60 | Accent character translation table |
