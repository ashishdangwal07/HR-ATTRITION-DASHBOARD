import os
import unittest

from analysis import load_dataset, compute_summary


class AnalysisTests(unittest.TestCase):
    def setUp(self):
        self.data_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "WA_Fn-UseC_-HR-Employee-Attrition.csv",
        )

    def test_summary_returns_expected_structure(self):
        rows = load_dataset(self.data_path)
        summary = compute_summary(rows)

        self.assertEqual(summary["total_employees"], 1470)
        self.assertGreater(summary["attrition_rate"], 0)
        self.assertIn("Sales", summary["department_attrition"])
        self.assertIn("Research & Development", summary["department_attrition"])
        self.assertGreater(
            summary["department_attrition"]["Sales"],
            summary["department_attrition"]["Research & Development"],
        )
        self.assertTrue(
            any(role == "Sales Representative" for role, _ in summary["top_roles"])
        )


if __name__ == "__main__":
    unittest.main()
