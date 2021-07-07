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
from DivUpdateFormatter import DivUpdateFormatter

class TestAdd_DivUpdateFormatter(unittest.TestCase):
    # test DivUpdateFormatter
    def test_DivUpdateFormatter(self):
        """testing DivUpdateFormatter"""
        segments    = {"div": "data"}
        DUF     = DivUpdateFormatter(segments)
        #print()
        #print(DUF)
        data    = "<h1>hello world</h1>"
        control = '<script>document.getElementById("data").innerHTML = "<h1>hello world</h1>";</script>'
        DUF.setDiv(data)
        result  = DUF.getResults()
        #print(result)
        self.assertEqual(control, result)
        
        control = '<script>document.getElementById("title").innerHTML = "<h1>hello world</h1>";</script>'
        DUF.setDiv(data, "title")
        result  = DUF.getResults()
        #print(result)
        self.assertEqual(control, result)
        
        control = '<script>document.getElementById("controls").innerHTML = "<h1>hello world</h1>";</script>'
        DUF.setDiv(data, "controls")
        result  = DUF.getResults()
        #print(result)
        self.assertEqual(control, result)

# main function
if __name__ == '__main__':
    print("\n\nunit testing DivUpdateFormatter.py...\n\n")
    unittest.main()
