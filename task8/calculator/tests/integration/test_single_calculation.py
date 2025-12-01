# tests/integration/test_single_calculation.py
import unittest
from unittest.mock import patch
import io
import sys
import re # Import re module for regex
from src.calculator_cli import main # Import the main function

class TestSingleCalculation(unittest.TestCase):
    """
    Integration tests for a single calculation flow.
    Simulates user input and captures output to verify behavior.
    """

    def setUp(self):
        """Set up for each test case."""
        # Patch sys.stdout to capture print statements
        self.held_output = io.StringIO()
        self.stdout_patch = patch('sys.stdout', new=self.held_output)
        self.stdout_patch.start()
        # Patch sys.exit to prevent the program from actually exiting during tests
        self.exit_patch = patch('sys.exit')
        self.exit_patch.start()

    def tearDown(self):
        """Clean up after each test case."""
        self.stdout_patch.stop()
        self.exit_patch.stop()

    def strip_ansi_codes(self, s):
        """Strips ANSI escape codes from a string."""
        return re.sub(r'\x1b\[[0-9;]*m', '', s)

    def simulate_input_and_run_main(self, input_values):
        """
        Helper to simulate input and run the main calculator logic.
        Args:
            input_values (list): A list of strings representing user inputs.
        """
        with patch('builtins.input', side_effect=input_values):
            main()
            
    def test_single_addition(self):
        # Simulate input: 1 (add), 10, 5, n (exit)
        self.simulate_input_and_run_main(['1', '10', '5', 'n'])
        output = self.strip_ansi_codes(self.held_output.getvalue())
        # Assert key parts of the output
        self.assertIn("Welcome to the Basic Calculator!", output)
        self.assertIn("Please choose an operation:", output)
        # self.assertIn("Enter your choice (1-5):", output) # This prompt is not captured by mocked input
        # self.assertIn("Enter the first number:", output) # This prompt is not captured by mocked input
        # self.assertIn("Enter the second number:", output) # This prompt is not captured by mocked input
        self.assertIn("10.0 + 5.0 = 15.0", output)
        # self.assertIn("Do you want to do another calculation? (y/n):", output) # This prompt is not captured by mocked input
        self.assertIn("Thank you for using the Basic Calculator!", output)

    def test_single_subtraction(self):
        # Simulate input: 2 (subtract), 20, 8, n (exit)
        self.simulate_input_and_run_main(['2', '20', '8', 'n'])
        output = self.strip_ansi_codes(self.held_output.getvalue())
        self.assertIn("20.0 - 8.0 = 12.0", output)

    def test_single_multiplication(self):
        # Simulate input: 3 (multiply), 7, 6, n (exit)
        self.simulate_input_and_run_main(['3', '7', '6', 'n'])
        output = self.strip_ansi_codes(self.held_output.getvalue())
        self.assertIn("7.0 x 6.0 = 42.0", output)

    def test_single_division(self):
        # Simulate input: 4 (divide), 100, 4, n (exit)
        self.simulate_input_and_run_main(['4', '100', '4', 'n'])
        output = self.strip_ansi_codes(self.held_output.getvalue())
        self.assertIn("100.0 / 4.0 = 25.0", output)
    
    def test_invalid_menu_choice(self):
        # Simulate input: invalid (6), valid (1), 10, 5, n
        self.simulate_input_and_run_main(['6', '1', '10', '5', 'n'])
        output = self.strip_ansi_codes(self.held_output.getvalue())
        self.assertIn("Please choose only 1, 2, 3, 4 or 5! 😵", output)
        self.assertIn("10.0 + 5.0 = 15.0", output)
    
    def test_invalid_first_number(self):
        # Simulate input: 1, invalid (abc), valid (10), 5, n
        self.simulate_input_and_run_main(['1', 'abc', '10', '5', 'n'])
        output = self.strip_ansi_codes(self.held_output.getvalue())
        self.assertIn("Oops! That's not a valid number. Please try again 😊", output)
        self.assertIn("10.0 + 5.0 = 15.0", output)

    def test_invalid_second_number(self):
        # Simulate input: 1, 10, invalid (xyz), valid (5), n
        self.simulate_input_and_run_main(['1', '10', 'xyz', '5', 'n'])
        output = self.strip_ansi_codes(self.held_output.getvalue())
        self.assertIn("Oops! That's not a valid number. Please try again 😊", output)
        self.assertIn("10.0 + 5.0 = 15.0", output)

if __name__ == '__main__':
    unittest.main()
