# Hospital Operations Helpdesk

> **Administrative routing with an explicit safety boundary: operations help, not diagnosis.**

The historical healthcare/hospital project ideas risk becoming misleading if a small software demo is described as clinical AI. This repository therefore focuses on a safer, useful administrative slice: appointments, billing, records, facilities, missing identifiers, and urgent-language escalation.

## Implemented
- appointment/billing/records/facilities routing
- patient/reference requirement for sensitive admin requests
- unknown-category abstention
- high-risk emergency phrase escalation
- structured ROUTE/ASK/ESCALATE responses
- unit tests

## Run
```bash
python -m unittest discover -s tests -v
python hospital_ops_helpdesk.py
```

## Repository map
- `hospital_ops_helpdesk.py` — core implementation
- `tests/` — deterministic tests
- `examples/` — example request
- `docs/architecture.md` — architecture
- `docs/research-agenda.md` — experiments and research lineage
- `STATUS.md` — exact claims boundary
- `CITATION.cff` — citation metadata

## Pipeline
**request → emergency screen → admin category → required identifier → administrative route / ask / emergency escalate**

## Research lineage
This is the conservative operations core derived from older Hospital Information System and 'Medilux' healthcare-command-center discussions. Clinical claims are intentionally excluded.

## Evaluation direction
Use synthetic administrative requests with paraphrases, missing references, and clearly urgent language. Track routing coverage and unsafe administrative handling of emergency cases.

## Maturity
**Research prototype.** This project does not diagnose, interpret tests, recommend treatment, rank clinicians, triage clinical severity, or replace qualified medical/emergency professionals.
