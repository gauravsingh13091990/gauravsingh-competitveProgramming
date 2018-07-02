import unittest


def find_rotation_point(words):
    no = len(words)-1
    lini = 0
    while no >= lini:
        
        midd = int (lini + (no - lini)/2)
        
        if words[midd-1] >= words[no] and words[midd] <= words[no]:
            return midd
            
        elif words[midd] > words[no]:
            lini = midd+1
            
        else:
            no = midd-1
            
    return -1

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)