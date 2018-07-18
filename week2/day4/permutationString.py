import unittest


def has_palindrome_permutation(string):

    
    l = len(string)
    dic = {}
    for i in range (l):
        n = dic.setdefault(string[i], 0)
        dic[string[i]]=n+1
        
    if (l%2==0):
        for j in dic.keys():
            if (dic[j]%2!=0):
                return False
    else:
        flag = False
        for z in dic.keys():
            if (dic[z]%2!=0):
                if(flag == True):
                    return False
                else:
                    flag = True
    return True

    

















# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)