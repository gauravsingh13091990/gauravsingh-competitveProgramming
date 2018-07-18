import unittest


def get_permutations(string):

    # Generate all permutations of the input string
    ans = []
    li = len(string)

    if(li==0 or li==1):

        return set([string])

    for j in range (li):

        newstr= string[0:j]+string[j+1:li]
        
        newli = get_permutations(newstr)
        for y in newli:
            ans.append(string[j]+y)
    return set(ans)

    


















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)