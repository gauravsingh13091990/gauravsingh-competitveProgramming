import unittest


def Word(lis, initials, last):
    l = initials + (last-initials)/2
    for i in range (initials,l):
        (lis[i], lis[initials+last-i-1] ) = (lis[initials+last-i-1], lis[i])
    return lis
def reverse_words(mesg):

    # Decode the message by reversing the words
    le = len(mesg)
    mesg = Word(mesg,0,le)
    i=0
    while(i<le):
        initials = i
        while(i<le and mesg[i]!=' '):
            i+=1
        last = i
        mesg = Word(mesg,initials,last)
        i+=1
    return mesg

    


















# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)