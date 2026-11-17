from __future__ import annotations

from dataclasses import dataclass
import re


# Conservative keyword triggers only. This list is not a clinical triage model.
EMERGENCY_PHRASES = (
    "can't breathe", "cannot breathe", "difficulty breathing",
    "shortness of breath", "not breathing", "unconscious", "unresponsive",
    "severe chest pain", "chest pain", "heavy bleeding", "bleeding heavily",
    "stroke symptoms", "face drooping", "slurred speech", "sudden weakness",
    "seizure", "anaphylaxis", "severe allergic reaction", "overdose",
    "suicide", "suicidal", "self harm", "self-harm", "blue lips",
)

ROUTES = {
    "appointment": "scheduling",
    "billing": "billing",
    "records": "medical_records",
    "facilities": "facilities",
}


@dataclass(frozen=True)
class HelpRequest:
    category: str
    message: str
    patient_reference: str | None = None

    def __post_init__(self):
        if not isinstance(self.category, str) or not isinstance(self.message, str):
            raise ValueError("category and message must be strings")
        if self.patient_reference is not None and not isinstance(self.patient_reference, str):
            raise ValueError("patient_reference must be a string when supplied")


def route(request: HelpRequest) -> dict:
    message = re.sub(r"\s+", " ", request.message.casefold()).strip()
    if any(phrase in message for phrase in EMERGENCY_PHRASES):
        return {
            "route": "emergency",
            "status": "ESCALATE",
            "message": (
                "Possible emergency language detected. This administrative tool is not clinical triage. "
                "Contact local emergency services or qualified clinical staff immediately; do not wait for this system."
            ),
        }

    if not message:
        return {
            "route": None,
            "status": "ASK",
            "message": "Describe the administrative request so it can be routed to a human team.",
        }

    if request.category not in ROUTES:
        return {
            "route": None,
            "status": "ASK",
            "message": "Select an administrative category: appointment, billing, records, or facilities.",
        }

    if request.category in {"billing", "records"} and not request.patient_reference:
        return {
            "route": ROUTES[request.category],
            "status": "ASK",
            "message": "A patient/reference identifier is required for this administrative request.",
        }

    return {
        "route": ROUTES[request.category],
        "status": "ROUTE",
        "message": "Administrative request routed for human handling.",
    }


if __name__ == "__main__":
    print(route(HelpRequest("appointment", "I need to reschedule my visit.")))
