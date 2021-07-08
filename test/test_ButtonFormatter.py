#!/usr/bin/env python3
# unit testing ButtonFormatter.py

import os
import sys
import unittest
#sys.path.append(os.path.realpath(__file__ + '/../code/usr/share/toonsite'))
sys.path.append(os.path.realpath(__file__ + '/../../site/cgi-bin'))
#sys.path.append('test/stubs')
#sys.path.append('./stubs')
#print(sys.path)
from ButtonFormatter    import ButtonFormatter

class TestAdd_ButtonFormatter(unittest.TestCase):
    # test ButtonFormatter
    def test_ButtonFormatter(self):
        """testing ButtonFormatter"""
        BFm     = ButtonFormatter()
        #print()
        #print(BFm)
        control     = ''
        self.assertEqual(control, repr(BFm))
        
        control     = '<button id="test" disabled>TEST</button>'
        result      = BFm.setButton('test', 'TEST')
        #print(result)
        self.assertEqual(control, result)

# main function
if __name__ == '__main__':
    print("\n\nunit testing ButtonFormatter.py...\n\n")
    unittest.main()
