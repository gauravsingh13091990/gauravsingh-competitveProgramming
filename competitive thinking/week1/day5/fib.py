import unittest


def fib(n):
    firstTerm = 0
    SecondTerm = 1
    
    if n == 0:
        return firstTerm
    elif n == 1:
        return SecondTerm
    elif n < 0:
        raise ValueError("Invalid Input")
    else:
        for k in range(2,n+1):
            nextT = firstTerm + SecondTerm
            firstTerm = SecondTerm
            SecondTerm = nextT
        return SecondTerm
class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)