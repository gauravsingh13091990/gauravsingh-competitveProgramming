import unittest


def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    li=[]
    if(len(int_list)<2):
        raise Exception('invalid input')
    else:
        mul=1
        m=0
        count=0
        for i in range(len(int_list)):
            if(int_list[i]!=0):
                mul=mul*int_list[i]
            if(int_list[i]==0):
                count +=1
            m= mul
        
        for j in range(len(int_list)):
            if(count<1):
                li.append(m//(int_list[j]))
                m=mul
            elif( count==1):
                if(int_list[j]!=0):
                    li.append(0)
                else:
                    li.append(m)
            else:
                li.append(0)
        return li




















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)