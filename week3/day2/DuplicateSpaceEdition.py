import unittest


def find_repeat(li):
    first = 1
    last = len(li) - 1

    while first < last:
        mid = first + (last - first)//2
        start, end = first, mid
        startH, endH = mid + 1, last

        num = 0
        enum = end - start + 1
        for item in li:
            if start <= item <= end:
                num += 1

        if num > enum:
            first, last = start, end
        else:
            first, last = startH, endH

    return first




class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)
