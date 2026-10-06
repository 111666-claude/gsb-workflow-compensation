import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from saga import core


def steps(*ids):
    return [{"id": i} for i in ids]


class SagaTest(unittest.TestCase):
    def test_all_steps_succeed_and_no_failure(self):
        out = core.run(steps("s1", "s2"), None, "t1", [], core.Counter())
        self.assertEqual(out["done"], ["s1", "s2"])

    def test_first_step_fails(self):
        out = core.run(steps("s1", "s2"), "s1", "t1", [], core.Counter())
        self.assertEqual(out["done"], [])

    def test_stop_at_failure(self):
        out = core.run(steps("s1", "s2", "s3"), "s2", "t1", [], core.Counter())
        self.assertEqual(out["done"], ["s1"])

    def test_empty_workflow(self):
        out = core.run([], None, "t1", [], core.Counter())
        self.assertEqual(out["done"], [])

    def test_ledger_records_tx(self):
        ledger = []
        core.run(steps("s1"), None, "t9", ledger, core.Counter())
        self.assertEqual(ledger, ["t9"])


if __name__ == "__main__":
    unittest.main()
