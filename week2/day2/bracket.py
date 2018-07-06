import unittest


def is_valid(code):
    indi = 0
    n = len(code)
    s = []
    
    for i in range(n):
        if code[i] == "[" or code[i] == "{" or code[i] == "(":
            s.append(code[i])
        elif len(s) == 0:
            return False
        elif code[i] == ")" and s[-1] == "(":
            s.pop()
        elif code[i] == "}" and s[-1] == "{":
            s.pop()
        elif code[i] == "]" and s[-1] == "[":
            s.pop()
        else:
            return False
    if len(s) != 0:
        return False
    else:
        return True

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)