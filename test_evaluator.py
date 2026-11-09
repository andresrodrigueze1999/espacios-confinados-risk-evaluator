import unittest
from src.evaluator import ConfinedSpaceEvaluator

class TestConfinedSpaceEvaluator(unittest.TestCase):

    def test_safe_atmosphere(self):
        evaluator = ConfinedSpaceEvaluator(o2_percentage=20.9, h2s_ppm=0, co_ppm=0, lel_percentage=0)
        res = evaluator.evaluate_atmosphere()
        self.assertIn("Grado C", res["grado_clasificacion"])
        self.assertFalse(res["monitoreo_continuo"])

    def test_grade_a_low_o2(self):
        evaluator = ConfinedSpaceEvaluator(o2_percentage=18.5, h2s_ppm=0, co_ppm=0, lel_percentage=0)
        res = evaluator.evaluate_atmosphere()
        self.assertIn("Grado A", res["grado_clasificacion"])
        self.assertTrue(res["monitoreo_continuo"])

    def test_grade_a_high_toxic_gas(self):
        evaluator = ConfinedSpaceEvaluator(o2_percentage=20.9, h2s_ppm=15.0, co_ppm=0, lel_percentage=0)
        res = evaluator.evaluate_atmosphere()
        self.assertIn("Grado A", res["grado_clasificacion"])

if __name__ == "__main__":
    unittest.main()
