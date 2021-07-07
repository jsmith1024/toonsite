##  @file    ButtonAcumulator.py
#   @brief   Format and accumulate a group of buttons.
#   @authors joe smith

from HTMLSegmentFormatter   import HTMLSegmentFormatter

#import fileinput
#import json
#import cgi
#import cgitb
#cgitb.enable()

##  @class  ButtonAcumulator
#   @brief  Format and accumulate a group of buttons.
class ButtonAcumulator(HTMLSegmentFormatter):

    ##  addButton
    #   @brief      Format and append a button.
    #   @param      button_id   (str)           button id
    #   @param      button_name (str)           button name
    #   @param      button_act  (str)           button action
    #   @param      end_row     (bool)          end of row              default = False
    #   @param      end_line    (bool)          break line after entry  default = False
    #   @param      beg_line    (bool)          break line before entry default = False
    def setDiv(self, button_id, button_name, button_act, end_row = False, end_line = False, beg_line):
        #print("here")
        ID          = button_id
        name        = button_name
        action      = button_act
        if beg_line:
            data   += "<hr>\n"
        #base        = '<a href="http://localhost:8000/cgi-bin/index.py?title=' + self.__title + '&index='
        base        = super()._getSegments('div')
        #data        = base + index + '&action=about\">         <button id="about"     disabled>About</button> </a>\n'
        data        = base + action + '&action=' + name + '\">  <button id=' + ID + '  disabled>About</button> </a>\n'
        if end_row:
            data   += "</br>\n"
        if end_line:
            data   += "<hr>\n"
        print(data)
        
        ############################################################################################################
        
        #index       = str(1)
        #data       += base + index +  '&action=first\">      <button id="first"      disabled>First</button> </a>\n'
        #index       = str(self.__index - 1)
        #data       += base + index +  '&action=previous\">   <button id="previous"   disabled>Prev</button>  </a>\n'
        #index       = str(self.__index)
        #data       += base + index +  '&action=reload\">     <button id="reload"     disabled>Ret</button>   </a>\n'
        #index       = str(self.__index + 1)
        #data       += base + index +  '&action=next\">       <button id="next"       disabled>Next</button>  </a>\n'
        #index       = str(len(self.__series["episodes"]) - 1)
        #data       += base + index +  '&action=last\">       <button id="last"       disabled>Last</button>  </a>\n'
        
        #print(data)
        #print("<hr>")
