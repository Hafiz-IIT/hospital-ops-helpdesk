# Hospital Operations Helpdesk

> Administrative hospital-helpdesk router for appointments, billing, records and facilities with explicit emergency escalation.

## Status
**Reproducible prototype** with executable code, tests, CI, architecture, evaluation and roadmap documentation.

## Problem
Hospital front desks receive mixed administrative and urgent messages. An administrative tool must route routine requests while refusing to perform clinical reasoning and escalating obvious emergencies.

## Architecture
Help request → emergency-language guard → admin category validation → reference/identity requirement → ROUTE / ASK / ESCALATE.

## Run
```bash
python -m unittest discover -s tests -v
python hospital_ops_helpdesk.py
```

## Implemented
- Administrative categories
- Emergency phrase guard
- Appointment/billing/records/facilities routing
- Reference requirement for sensitive admin requests
- ASK/ROUTE/ESCALATE outcomes
- Tests and CI

## Research lineage
- *Digital Twins for Healthcare and Wellness Applications*
- *AI-Powered Early Warning Systems for Public Health*
- *Human-Centered AI Design for Inclusive Digital Platforms*

## Evaluation
Tests verify administrative routing, reference requirements and emergency escalation.

## Limitations
- Administrative only
- No diagnosis or treatment
- No medical-record integration
- Keyword emergency guard is not a clinical triage system

## License
MIT.

## Extended implementation

- `admin_queue.py` queues routine administrative requests while keeping emergency escalations outside the routine queue.
