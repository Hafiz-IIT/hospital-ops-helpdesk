# Safety and scope boundary

This prototype routes administrative requests and applies a conservative keyword trigger for possible emergency language.

- Emergency phrase matches return ESCALATE and direct the user to local emergency services or qualified clinical staff.
- This is not clinical triage, diagnosis, or a reliable emergency detector. It can miss emergencies and can over-escalate negated, quoted, or hypothetical phrases.
- It must never be used to rule out an emergency or delay contacting emergency services.
- Patient references are caller-supplied strings, not authenticated identifiers. Do not log or publish real patient data.
- The routing queue is an in-memory administrative prototype; it is not a hospital information system.
