import unittest

from admin_queue import AdministrativeQueue
from hospital_ops_helpdesk import HelpRequest


class AdministrativeQueueTests(unittest.TestCase):
    def test_routine_request_is_queued(self):
        queue = AdministrativeQueue()
        result = queue.submit(HelpRequest("appointment", "reschedule"))
        self.assertEqual(result["status"], "QUEUED")
        self.assertEqual(len(queue), 1)

    def test_escalated_request_is_not_queued(self):
        queue = AdministrativeQueue()
        result = queue.submit(HelpRequest("appointment", "patient is unconscious"))
        self.assertEqual(result["status"], "ESCALATE")
        self.assertEqual(len(queue), 0)

    def test_records_precede_appointment(self):
        queue = AdministrativeQueue()
        queue.submit(HelpRequest("appointment", "reschedule"))
        queue.submit(HelpRequest("records", "copy request", patient_reference="P1"))
        self.assertEqual(queue.pop_next().request.category, "records")


if __name__ == "__main__":
    unittest.main()
