# Hospital Operations Helpdesk

<p align="center"><strong>Administrative Routing With an Explicit Safety Boundary</strong><br/><sub>Handle routine operational requests without pretending to perform clinical reasoning.</sub></p>

<p align="center"><img src="https://img.shields.io/badge/status-reproducible%20prototype-blue" alt="Prototype"/> <img src="https://img.shields.io/badge/safety-boundary%20%7C%20admin%20only-red" alt="Administrative only"/></p>

## Question

**How should a hospital helpdesk route administrative requests while preventing obvious emergencies from entering a routine queue?**

```
Request
  ↓
Emergency-language guard
  ├── ESCALATE
  └── Administrative classification
          ↓
       ROUTE / ASK
```

## Try it

```bash
python hospital_ops_helpdesk.py
python -m unittest discover -s tests -v
```

`admin_queue.py` adds a priority queue for routine administrative requests while keeping escalated requests outside it.

## Implemented

- appointment / billing / records / facilities routing
- emergency phrase guard
- reference requirements
- administrative queue
- explicit escalation
- deterministic tests + CI

## Critical boundary

This repository is **not a clinical decision system**. It does not diagnose, triage medically, prescribe, or replace professional care.

Related: [College Ops Copilot Core](https://github.com/Hafiz-IIT/college-ops-copilot-core) · [~haf.s__ OS Core](https://github.com/Hafiz-IIT/hafs-os-core)
