import unittest


class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    

    L1 = []
    L2 = []
    def enqueue(self, it):
        self.L1.append(it)
    def dequeue(self):
        if(len(self.L2)==0):
            while len(self.L1)>0:
                self.L2.append(self.L1.pop())
        return self.L2.pop()


















# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)