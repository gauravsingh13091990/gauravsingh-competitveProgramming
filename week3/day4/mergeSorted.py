import unittest


import unittest


def merge_lists(mlist, alist):

	# Combine the sorted lists into one large sorted list
	sorte = []
	i1 = 0
	i2 = 0

	while(True):
		if(len(sorte)==len(mlist)+len(alist)):
			break
		if i1==len(mlist):
			for i in alist[i2:]:
				sorte.append(i)
		elif i2==len(alist):
			for i in mlist[i1:]:
				sorte.append(i)
		else:
			if(mlist[i1]<=alist[i2]):
				sorte.append(mlist[i1])
				i1 = i1+1
			else:
				sorte.append(alist[i2])
				i2 = i2+1
		# print(sorted_array)
	return sorte

















# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)