#!/usr/bin/env python3
# unit testing TextBoxFormatter.py

import os
import sys
import unittest
#sys.path.append(os.path.realpath(__file__ + '/../code/usr/share/toonsite'))
sys.path.append(os.path.realpath(__file__ + '/../../site/cgi-bin'))
#sys.path.append('test/stubs')
#sys.path.append('./stubs')
#print(sys.path)
from TextBoxFormatter   import TextBoxFormatter

class TestAdd_TextBoxFormatter(unittest.TestCase):
    # test TextBoxFormatter
    def test_TextBoxFormatter(self):
        """testing TextBoxFormatter"""
        TBF     = TextBoxFormatter()
        print()
        print(TBF)
        control     = ''
        self.assertEqual(control, repr(TBF))
        
        boxes       = []
        
        box_id      = 'id'
        control     = '\t\t\t\t' + '<label for="' + box_id + '">' + box_id.capitalize() + '</label><br>\n'
        control    += '\t\t\t\t' + '<input type="text" id="' + box_id + '">\n'
        result      = TBF.setTextBox(box_id)
        #print(result)
        self.assertEqual(control,   result)
        boxes.append(result)
        
        control     = '\t\t\t' + '<form>\n'
        control    += boxes[0]
        control1    = '\t\t\t\t' + '<input type="submit" value="submit">\n'
        control1   += '\t\t\t' +'</form>\n'
        result      = TBF.setForm(boxes)
        #print(result)
        self.assertEqual(control + control1,    result)
        
        box_id      = 'id'
        box_label   = 'ID'
        controlA    = '\t\t\t\t' + '<label for="' + box_id + '">' + box_id.upper() + '</label><br>\n'
        controlA   += '\t\t\t\t' + '<input type="text" id="' + box_id + '">\n'
        result      = TBF.setTextBox(box_id, box_label)
        #print(result)
        self.assertEqual(controlA,  result)
        boxes.append(result)
        
        control2    = control
        control2   += controlA
        control2   += control1
        result      = TBF.setForm(boxes)
        #print('=========================')
        #print(control2)
        #print('=========================')
        #print(result)
        #print('=========================')
        self.assertEqual(control2, result)

# main function
if __name__ == '__main__':
    print("\n\nunit testing TextBoxFormatter.py...\n\n")
    unittest.main()
