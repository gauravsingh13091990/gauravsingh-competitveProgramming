import unittest


def is_single_riffle(h1, h2, deck):

    Ind1 = 0
    Ind2 = 0
    Ind1Max = len(h1) - 1
    Ind2Max = len(h2) - 1
    for c in deck:
        if (Ind1 <= Ind1Max and c== h1[Ind1]):
            Ind1+= 1
        elif (Ind2 <= Ind2Max and c == h2[Ind2]):
            Ind2 += 1
        else:
            return False
    return True


    






class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)