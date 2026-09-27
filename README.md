# Hospital Operations Helpdesk

An **administrative** hospital-helpdesk routing prototype.

## Implemented
- routing for appointments, billing, records and facilities
- missing-information checks
- emergency-language escalation
- audit-friendly structured responses
- deterministic tests

## Safety boundary
This project does **not** diagnose, recommend treatment, rank clinicians, interpret tests, or replace emergency/clinical staff. If clearly urgent language is detected, it returns an emergency escalation instruction rather than attempting medical reasoning.

## Run
```bash
python -m unittest discover -s tests -v
python hospital_ops_helpdesk.py
```
