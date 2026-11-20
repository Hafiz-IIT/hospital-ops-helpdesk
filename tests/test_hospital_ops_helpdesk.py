import unittest

from hospital_ops_helpdesk import HelpRequest, route


class HospitalHelpdeskTests(unittest.TestCase):
    def test_appointment_routes_to_scheduling(self):
        result = route(HelpRequest("appointment", "reschedule"))
        self.assertEqual(result["route"], "scheduling")
        self.assertEqual(result["status"], "ROUTE")

    def test_records_need_reference(self):
        result = route(HelpRequest("records", "need a copy"))
        self.assertEqual(result["status"], "ASK")

    def test_emergency_language_escalates(self):
        result = route(HelpRequest("appointment", "patient is unconscious"))
        self.assertEqual(result["status"], "ESCALATE")
        self.assertEqual(result["route"], "emergency")
        self.assertIn("not clinical triage", result["message"])

    def test_additional_possible_emergency_phrases_escalate(self):
        for message in ("sudden face drooping", "shortness of breath", "possible overdose"):
            with self.subTest(message=message):
                self.assertEqual(route(HelpRequest("billing", message))["status"], "ESCALATE")

    def test_invalid_request_fields_are_rejected(self):
        for args in (("", "message"), ("billing", " "), ("billing", "message", " ")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                HelpRequest(*args)

    def test_oversized_message_rejected(self):
        with self.assertRaises(ValueError):
            HelpRequest("billing", "x" * 4001)

    def test_empty_message_requests_clarification(self):
        self.assertEqual(route(HelpRequest("appointment", "   "))["status"], "ASK")


if __name__ == "__main__":
    unittest.main()
