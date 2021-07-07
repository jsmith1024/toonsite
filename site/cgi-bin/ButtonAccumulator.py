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

    ##  addLink
    #   @brief      Format and append a button.
    #   @param      button_id   (str)           button id
    #   @param      button_name (str)           button name
    #   @param      button_act  (str)           button action
    #   @param      end_row     (bool)          end of row              default = False
    #   @param      end_line    (bool)          break line after entry  default = False
    #   @param      beg_line    (bool)          break line before entry default = False
    def addLink(self, button_id, button_name, button_act, end_row = False, end_line = False, beg_line):
        #print("here")
        ID              = button_id
        name            = button_name
        action          = button_act
        data            = '<a href="http://localhost:8000/cgi-bin/index.py'
        if fields:
            data       += '?'
            for key in fields.keys():
                data   += key + '=' + value + '&'
        data            = data[:-2]
        data           += '\">' + name + '</a>\n'
        super._setResults(data)
        
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
        
        ############################################################################################################
    
    ##  addButton
    #   @brief      Format a link.
    #   @param      button_id   (str)           button id
    #   @param      button_name (str)           button name
    #   @returns    (str)                       formatted button
    def @addButton(self, button_id, button_name, button_act):
        #print("here")
        data        = '<button id=' + button_id + '  disabled>' + button_name + '</button> </a>\n'
        #print(data)
        return data
    
    ##  addLine
    #   @brief      Append a line.
    def addLine():
        #print("here")
        data        = super().getResults()
        data       += "<hr>\n"
        super._setResults(data)
