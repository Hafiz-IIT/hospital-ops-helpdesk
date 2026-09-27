# Architecture

```mermaid
flowchart LR
    N0[request] --> N1
    N1[emergency screen] --> N2
    N2[admin category] --> N3
    N3[required identifier] --> N4
    N4[administrative route / ask / emergency escalate]
```

## Emergency boundary
Known high-risk phrases short-circuit normal administrative routing.

## Category router
Supported requests map only to administrative departments.

## Identifier gate
Billing/records requests require a patient/reference identifier.

## Response
Outputs a structured administrative route or asks for missing information.

## Design principle
In health contexts, make the non-clinical boundary explicit in code and documentation rather than letting a generic assistant drift into diagnosis.
