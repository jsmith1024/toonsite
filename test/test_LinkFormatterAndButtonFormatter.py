#!/usr/bin/env python3
# unit testing LinkFormatter and ButtonFormatter

import os
import sys
import unittest
#sys.path.append(os.path.realpath(__file__ + '/../code/usr/share/toonsite'))
sys.path.append(os.path.realpath(__file__ + '/../../site/cgi-bin'))
#sys.path.append('test/stubs')
#sys.path.append('./stubs')
#print(sys.path)
from LinkFormatter      import LinkFormatter
from ButtonFormatter    import ButtonFormatter

class TestAdd_LinkAndButton(unittest.TestCase):
    # test LinkFormatter and ButtonFormatter
    def test_LinkFormatterAndButtonFormatter(self):
        """testing LinkFormatter and ButtonFormatter"""
        BFm     = ButtonFormatter()
        LFm     = LinkFormatter()
        #print()
        control     = '<a href="http://localhost:8000/cgi-bin/index.py?title=TEST&index=2&action=next"><button id="next" disabled>Next</button></a>'
        url         = 'http://localhost:8000/cgi-bin/index.py'
        name        = BFm.setButton('next', 'Next')
        fields      = {'title': 'TEST', 'index': '2', 'action': 'next'}
        result      = LFm.setLink(url, name, fields)
        #print(result)
        self.assertEqual(control, result)

# main function
if __name__ == '__main__':
    print("\n\nunit testing LinkAndButton...\n\n")
    unittest.main()
