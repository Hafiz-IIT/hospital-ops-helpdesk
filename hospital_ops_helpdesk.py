from __future__ import annotations

from dataclasses import dataclass


EMERGENCY_PHRASES = (
    "can't breathe",
    "cannot breathe",
    "unconscious",
    "severe chest pain",
    "heavy bleeding",
    "stroke symptoms",
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
    message = request.message.lower()
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
