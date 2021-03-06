import unittest
import json
from calculator import Calculator

def myfun(str):
    return 'hello ' + str

class CalculatorTest(unittest.TestCase):
    
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

    def test_list(self):
        calc = Calculator()
        arr = calc.list(8);
        print(arr);

    def test_map(self):
        calc = Calculator()
        arr = calc.map();
        print(arr);

    def test_atributo(self):
        calc = Calculator()
        calc.increase(10);
        calc.increase(15);
        print('atributo '+str(calc.atributo));

    def test_func(self):
        print(myfun(' volpe'))

def main():
    unittest.main()

if __name__ == '__main__':
    main()


