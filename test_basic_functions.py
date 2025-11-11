import unittest
from basic_functions import *

class TestBasicFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(7), 7)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)

    def test_triangle(self):
        self.assertEqual(triangle(0), [])
        self.assertEqual(triangle(1), ["*"])
        self.assertEqual(triangle(2), ["*", "***"])
        self.assertEqual(triangle(3), ["*", "***", "*****"])
        self.assertEqual(triangle(4), ["*", "***", "*****", "*******"])

    def test_return_list_stats(self):
        self.assertEqual(return_list_stats([1, 2, 3, 4, 5]), {
            "unique_numbers": {1, 2, 3, 4, 5},
            "min": 1,
            "max": 5,
            "average": 3.0,
            "even_pairs": [],
            "odd_pairs": [(0, 1), (1, 2), (2, 3), (3, 4)],
            "even_numbers": (2, 4),
            "odd_numbers": (1, 3, 5),
            "number_of_even_numbers": 2,
            "number_of_odd_numbers": 3
        })
        self.assertEqual(return_list_stats([1, 2, 3, 4, 5, 6]), {
            "unique_numbers": {1, 2, 3, 4, 5, 6},
            "min": 1,
            "max": 6,
            "average": 3.5,
            "even_pairs": [],
            "odd_pairs": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)],
            "even_numbers": (2, 4, 6),
            "odd_numbers": (1, 3, 5),
            "number_of_even_numbers": 3,
            "number_of_odd_numbers": 3
        })
        self.assertEqual(return_list_stats([6, 2, 3, 5, 9, 4, 1, 11]), {
            "unique_numbers": {6, 2, 3, 5, 9, 4, 1, 11},
            "min": 1,
            "max": 11,
            "average": 5.1,
            "even_pairs": [(0, 1), (2, 3), (3, 4), (6, 7)],
            "odd_pairs": [(1, 2), (4, 5), (5, 6)],
            "even_numbers": (6, 2, 4),
            "odd_numbers": (3, 5, 9, 1, 11),
            "number_of_even_numbers": 3,
            "number_of_odd_numbers": 5
        })

    def test_n_0(self):
            # Test for n = 0 (base case)
            self.assertEqual(pascal_triangle(0), [1])

    def test_n_3(self):
        # Test for n = 3
        self.assertEqual(pascal_triangle(3), [1, 3, 3, 1])

    def test_n_5(self):
        # Test for n = 5
        self.assertEqual(pascal_triangle(5), [1, 5, 10, 10, 5, 1])

    def test_n_negative(self):
        # Test for a negative value of n
        with self.assertRaises(ValueError):
            pascal_triangle(-1)

    def test_n_large(self):
        # Test for a large value of n
        self.assertEqual(pascal_triangle(20), [1, 20, 190, 1140, 4845, 15504, 38760, 77520, 125970, 167960, 184756, 167960, 125970, 77520, 38760, 15504, 4845, 1140, 190, 20, 1])
