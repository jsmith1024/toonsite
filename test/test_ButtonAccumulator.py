#!/usr/bin/env python3
# unit testing DivUpdateFormatter.py

import os
import sys
import unittest
#sys.path.append(os.path.realpath(__file__ + '/../code/usr/share/toonsite'))
sys.path.append(os.path.realpath(__file__ + '/../../site/cgi-bin'))
#sys.path.append('test/stubs')
#sys.path.append('./stubs')
#print(sys.path)
from ButtonAccumulator  import ButtonAccumulator

class TestAdd_ButtonAccumulator(unittest.TestCase):
    # test ButtonAccumulator
    def test_ButtonAccumulator(self):
        """testing ButtonAccumulator"""
        BAc     = ButtonAccumulator(test = True)
        print()
        print(BAc)

# main function
if __name__ == '__main__':
    print("\n\nunit testing CenterDisplay.py...\n\n")
    unittest.main()
