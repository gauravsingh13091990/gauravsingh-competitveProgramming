import unittest


class NodeT(object):

    # Implement a trie and use it to efficiently store strings
    def __init__(self):
        self.child = [None]*30
        self.istheend = False
 
class Trie(object):
    def __init__(self):
        self.root = self.ValidateNode()
 
    def ValidateNode(self):
        return NodeT()
 
    def charToI(self,c):
        return ord(c)-ord('a')
    def add_word(self,k):
        if self.search(k):
            return False
        else:
            wl = self.root
            length = len(k)
            for level in range(length):
                index = self.charToI(k[level])
                if not wl.child[index]:
                    wl.child[index] = self.ValidateNode()
                wl = wl.child[index]
            wl.istheend = True
            return True
            
    def search(self, k):
        wl = self.root
        length = len(k)
        for level in range(length):
            index = self.charToI(k[level])
            if not wl.child[index]:
                return False
            wl = wl.child[index] 
        return wl != None and wl.istheend
    
















# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)