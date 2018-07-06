import unittest


def get_closing_paren(sen, opening_p_i):

    # Find the position of the matching closing parenthesis
    n = len(sen)
    
    arr = []
    
    ind= 0
    for i in range(n):
        if sen[i] == "(":
            if i == opening_p_i:
                
                arr.append(sen[i])
                
                ind = len(arr)
            else:
                arr.append(sen[i])
        elif sen[i] == ")":
            
            if len(arr) == ind:
                
                return i
            else:
                
                arr.pop()
    if 1:
        
        raise ValueError("exception occur")

    
class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)