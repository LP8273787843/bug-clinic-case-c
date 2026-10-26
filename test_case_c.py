import unittest

from case_c import average_grade


class TestAverageGrade(unittest.TestCase):

    # Normal: the instructor's example - fails on the original code (15.0)
    def test_1_normal_four_scores(self):
        self.assertEqual(average_grade([80, 70, 90, 60]), 75.0)

    # Normal: non-whole average - fails on the original code (33.33)
    def test_2_normal_non_integer_average(self):
        self.assertAlmostEqual(average_grade([90, 85, 100]), 91.6667, places=4)

    # Boundary: a single score is its own average
    def test_3_boundary_single_score(self):
        self.assertEqual(average_grade([88]), 88.0)

    # Boundary: all equal - the bug is invisible here
    def test_4_boundary_all_equal(self):
        self.assertEqual(average_grade([75, 75, 75, 75]), 75.0)

    # Edge: empty list gives a clear error - original raised ZeroDivisionError
    def test_5_edge_empty_list(self):
        with self.assertRaises(ValueError):
            average_grade([])

    # Edge: min and max scores; 0 counts as a real score
    def test_6_edge_min_and_max(self):
        self.assertEqual(average_grade([0, 100]), 50.0)

    # Edge: last score is the outlier - fails on the original code (0.0)
    def test_7_edge_last_score_differs(self):
        self.assertEqual(average_grade([100, 100, 100, 0]), 75.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
