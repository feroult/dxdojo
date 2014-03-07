import unittest
import json
from calculator import Calculator
 
class CalculatorTest(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

    def test_list(self):
        calc = Calculator()
        arr = calc.list(8);
        print(json.dumps(arr));

    def test_map(self):
        calc = Calculator()
        arr = calc.map();
        print(json.dumps(arr));

def main():
    unittest.main()

if __name__ == '__main__':
    main()