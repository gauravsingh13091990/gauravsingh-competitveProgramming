import unittest


class TempTracker(object):
    def __init__(self):
        
        self.tempNoCount = 0
        self.minimumTemp =155
        self.total = 0
        self.mean = None
        self.maxFreq = 0
        self.max = -1
        self.mode = None
        self.Temperature=[0]*155

    
    def get_max(self):
        max=self.max
        if max==-1:
            return None
        return max
    def get_min(self):
        minimumTemp=self.minimumTemp
        if minimumTemp==155:
            return None
        return minimumTemp
    def get_mean(self):
        return self.mean
    def get_mode(self):
        return self.mode
    def insert(self, tempe):
        self.Temperature[tempe]+=1
        self.tempNoCount+=1
        if tempe<self.minimumTemp:
            self.minimumTemp=tempe
        if tempe>self.max:
            self.max=tempe
        self.total+=tempe
        self.mean=self.total/float(self.tempNoCount)
        if self.Temperature[tempe]>self.maxFreq:
            self.maxFreq=self.Temperature[tempe]
            self.mode=tempe


















# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)