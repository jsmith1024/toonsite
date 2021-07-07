#!/usr/bin/env python3
# unit testing HTMLSegmentFormatter.py

import os
import sys
import unittest
#sys.path.append(os.path.realpath(__file__ + '/../../code/usr/share/toonsite'))
sys.path.append(os.path.realpath(__file__ + '/../../site/cgi-bin'))
#sys.path.append('test/stubs')
#sys.path.append('./stubs')
# print(sys.path)
from HTMLSegmentFormatter      import HTMLSegmentFormatter

class TestAdd_HTMLSegmentFormatter(unittest.TestCase):
    # test HTMLSegmentFormatter
    def test_HTMLSegmentFormatter(self):
        """testing HTMLSegmentFormatter"""
        segments    = {"test": "data"}
        HSF         = HTMLSegmentFormatter(segments)
        #print()
        #print(HSF)
        control     = ''
        self.assertEqual(control, repr(HSF))
        result      = HSF.getResults()
        #print(result)
        self.assertEqual(control, result)
        control     = segments['test']
        result      = HSF._getSegments('test')
        #print(result)
        self.assertEqual(control, result)

# main function
if __name__ == '__main__':
    print("\n\nunit testing HTMLSegmentFormatter.py...\n\n")
    unittest.main()
