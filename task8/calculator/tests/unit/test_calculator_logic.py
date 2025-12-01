# tests/unit/test_calculator_logic.py
import unittest
from src.calculator_cli import perform_calculation # Assuming perform_calculation is in src/calculator_cli.py

class TestPerformCalculation(unittest.TestCase):
    def test_addition(self):
        self.assertAlmostEqual(perform_calculation(1, 5, 3), 8.0)
        self.assertAlmostEqual(perform_calculation(1, -5, 3), -2.0)
        self.assertAlmostEqual(perform_calculation(1, 0, 0), 0.0)

    def test_subtractiom(self):
        self.assertAlmostEqual(perform_calculation(2, 10, 4), 6.0)
        self.assertAlmostEqual(perform_calculation(2, 4, 10), -6.0)
        self.assertAlmostEqual(perform_calculation(2, 0, 0), 0.0)

    def test_multiplication(self):
        self.assertAlmostEqual(perform_calculation(3, 2, 5), 10.0)
        self.assertAlmostEqual(perform_calculation(3, -2, 5), -10.0)
        self.assertAlmostEqual(perform_calculation(3, 0, 5), 0.0)

    def test_division(self):
        self.assertAlmostEqual(perform_calculation(4, 10, 2), 5.0)
        self.assertAlmostEqual(perform_calculation(4, -10, 2), -5.0)
        self.assertAlmostEqual(perform_calculation(4, 10, -2), -5.0)
        self.assertAlmostEqual(perform_calculation(4, 0, 5), 0.0)

    def test_division_by_zero(self):
        # perform_calculation returns None for division by zero
        self.assertIsNone(perform_calculation(4, 10, 0))
        self.assertIsNone(perform_calculation(4, 0, 0))

if __name__ == '__main__':
    unittest.main()
