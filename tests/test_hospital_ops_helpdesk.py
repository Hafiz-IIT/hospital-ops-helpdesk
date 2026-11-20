import unittest
from hospital_ops_helpdesk import HelpRequest, route

class HospitalHelpdeskTests(unittest.TestCase):
    def test_appointment_routes_to_scheduling(self):
        result = route(HelpRequest("appointment", "reschedule"))
        self.assertEqual(result["route"], "scheduling")
        self.assertEqual(result["status"], "ROUTE")
    def test_records_need_reference(self):
        self.assertEqual(route(HelpRequest("records", "need a copy"))["status"], "ASK")
    def test_emergency_language_escalates(self):
        result = route(HelpRequest("appointment", "patient is unconscious"))
        self.assertEqual(result["status"], "ESCALATE")
        self.assertEqual(result["route"], "emergency")
    def test_empty_and_non_string_messages_rejected(self):
        for message in (" ", None, 7):
            with self.subTest(message=message), self.assertRaises(ValueError):
                HelpRequest("appointment", message)
    def test_patient_reference_must_be_nonempty(self):
        with self.assertRaises(ValueError):
            HelpRequest("records", "need a copy", " ")
    def test_unknown_category_asks(self):
        self.assertEqual(route(HelpRequest("unknown", "help"))["status"], "ASK")
if __name__ == "__main__": unittest.main()
