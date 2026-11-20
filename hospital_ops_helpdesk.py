from __future__ import annotations

from dataclasses import dataclass


EMERGENCY_PHRASES = (
    "can't breathe",
    "cannot breathe",
    "shortness of breath",
    "difficulty breathing",
    "breathing difficulty",
    "unconscious",
    "unresponsive",
    "chest pain",
    "heavy bleeding",
    "stroke symptoms",
    "stroke",
    "seizure",
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


def route(request: HelpRequest) -> dict:
    if not isinstance(request.category, str) or not isinstance(request.message, str):
        raise ValueError("category and message must be strings")
    if not request.message.strip():
        raise ValueError("message must be non-empty")
    message = request.message.casefold()
    if any(phrase in message for phrase in EMERGENCY_PHRASES):
        return {
            "route": "emergency",
            "status": "ESCALATE",
            "message": "Seek immediate emergency assistance from qualified local emergency/clinical services.",
        }

    if request.category not in ROUTES:
        return {
            "route": None,
            "status": "ASK",
            "message": "Select an administrative category: appointment, billing, records, or facilities.",
        }

    if request.category in {"billing", "records"} and (
        not isinstance(request.patient_reference, str) or not request.patient_reference.strip()
    ):
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
