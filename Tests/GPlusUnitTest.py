__author__ = 'aferraz'

import unittest
from GPlus import GPlus

class GPlusUnitTest(unittest.TestCase):

    def test_getActivities(self):
        gp = GPlus()

        activities = gp.getContentActivities("aecio")
        print activities


if __name__ == '__main__':
    unittest.main()
