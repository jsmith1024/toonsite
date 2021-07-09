#!/usr/bin/env python3
# unit testing LinkFormatter.py

import os
import sys
import unittest
#sys.path.append(os.path.realpath(__file__ + '/../code/usr/share/toonsite'))
sys.path.append(os.path.realpath(__file__ + '/../../site/cgi-bin'))
#sys.path.append('test/stubs')
#sys.path.append('./stubs')
#print(sys.path)
from LinkFormatter      import LinkFormatter

class TestAdd_LinkFormatter(unittest.TestCase):
    # test LinkFormatter
    def test_LinkFormatter(self):
        """testing LinkFormatter"""
        LFm     = LinkFormatter()
        #print()
        #print(LFm)
        control     = ''
        self.assertEqual(control, repr(LFm))
        
        control     = '<a href="http://localhost:8000/cgi-bin/index.py">TEST</a>'
        url         = 'http://localhost:8000/cgi-bin/index.py'
        name        = 'TEST'
        result      = LFm.setLink(url, name)
        #print(result)
        self.assertEqual(control, result)
        
        control     = '<a href="http://localhost:8000/cgi-bin/index.py?title=TEST&index=2&action=next">TEST</a>'
        url         = 'http://localhost:8000/cgi-bin/index.py'
        name        = 'TEST'
        fields      = {'title': 'TEST', 'index': '2', 'action': 'next'}
        result      = LFm.setLink(url, name, fields)
        #print(result)
        self.assertEqual(control, result)

# main function
if __name__ == '__main__':
    print("\n\nunit testing LinkFormatter.py...\n\n")
    unittest.main()
