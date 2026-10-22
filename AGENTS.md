# AGENTS.md — PyNFe

Brazilian electronic fiscal document library for NF-e, NFC-e, NFS-e, MDF-e, CT-e, and SEFAZ communication. `AGENTS.md` is the sole canonical instruction source; client settings may load it but must not copy its policies.

## Bootstrap and Git identity

- Resolve the repository with `git rev-parse --show-toplevel`. For shared Nuvel resources, prefer a validated `NUVEL_WORKSPACE_ROOT`; otherwise derive candidates from the common Git directory/original checkout and accept only a directory containing `.claude/workflows/issue-orchestrator.js`. Never assume `../docs` works from a detached worktree.
- Commit with the machine's global Git identity exactly as configured. Never set or override `user.name`, `user.email`, signing settings, author/committer environment variables, or `.git/config`. Derive branch prefixes and paths; never hardcode a developer identity or home path.
- Preserve user changes. Use focused branches and squash PR merges. Verify official SEFAZ/provider specifications before changing external fiscal contracts.

## Navigation gate

Before reading a mapped source file longer than 200 lines, read its map in `docs/` and then open only the relevant source range. The maps cover `serializacao.py`, `comunicacao.py`, `autorizador_nfse.py`, `notafiscal.py`, `manifesto.py`, `evento.py`, `flags.py`, `webservices.py`, and `utils/__init__.py`; use [`docs/README.md`](docs/README.md) to select one.

## Commands and full checks

Use Python 3.9+ in an isolated environment.

```bash
python -m pip install --upgrade pip
python -m pip install build -e . -r requirements.txt -r requirements-dev.txt -r requirements-nfse.txt
pytest -v
ruff check .
ruff format --check .
python -m build
git diff --check
```

`requirements-dev.txt` pins Ruff 0.12.5, matching the existing Poetry minimum; use that environment so lint results are reproducible.

A focused `pytest tests/<file>.py` is useful during development but never replaces the full suite. Project metadata requires Python 3.9+, and CI tests every supported minor from 3.9 through 3.13; do not claim support outside that declared range or weaken it to accommodate an obsolete runner. Pushes and PRs run format, lint, and tests across the CI matrix. Every push also builds distributions; publishing occurs only for tags. Do not create a tag or publish without explicit authorization.

## Architecture and invariants

- `pynfe/entidades/` contains fiscal domain entities; `pynfe/processamento/` owns signing, serialization, communication, and validation; `pynfe/utils/` contains flags, endpoint tables, XML helpers, and generated NFS-e bindings; `pynfe/data/` holds schemas and reference data.
- Never manually edit generated PyXB bindings under `pynfe/utils/nfse/`. Treat XSDs and reference tables as controlled fiscal inputs; change them only with verified source material.
- SEFAZ XML order, namespaces, decimal formatting, optional element rules, endpoint/environment selection, and signature/certificate handling are protocol contracts. Preserve them and add fixture-based tests for changed output.
- Extend existing entities, flags, serializers, and communication paths before creating parallel models or pipelines. Keep public APIs backward-compatible unless a breaking release is explicitly authorized.
- Tests must exercise real entity serialization/validation state. Do not mock core entity or XML behavior merely to simulate fiscal success or failure.
- Read [`docs/reforma_tributaria.md`](docs/reforma_tributaria.md) before changing IBS/CBS or tax-reform fields.

## Dependencies

Core dependencies include `lxml`, `signxml`, `cryptography`/`pyopenssl`, and `requests`; NFS-e additionally uses `suds-community` and `PyXB-X`. Do not casually broaden supported Python/dependency ranges because certificate and generated-binding compatibility is sensitive.

Language: anything not customer-visible (docs, rules, prompts, code comments, commits, PRs) is written in English; only customer-facing copy stays PT-BR.
