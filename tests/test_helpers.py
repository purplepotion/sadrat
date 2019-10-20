import sys
sys.path.append('/Users/jarvis/Desktop/CODE/sadrat/')


from scrapers.helpers import Webrequests
import unittest


class TestWebrequests(unittest.TestCase):

    def test_simple_get(self):
        self.obj = Webrequests()
        result = self.obj.simple_get("http://www.medications.com/avelox/27335")
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
