##  @file    DivUpdateFormatter.py
#   @brief   Format HTML/JavaScript segments.
#   @authors joe smith

from HTMLSegmentFormatter   import HTMLSegmentFormatter

#import fileinput
#import json
#import cgi
#import cgitb
#cgitb.enable()

##  @class  DivUpdateFormatter
#   @brief  Format HTML/JavaScript segments.
class DivUpdateFormatter(HTMLSegmentFormatter):

    ##  setDiv
    #   @brief      Format HTML/JavaScript segments.
    #   @param      data        (str)           string to format
    #   @param      div_id      (str)           id of div to format     default = False
    def setDiv(self, data, div_id = False):
        #print("here")
        if div_id:
            div = div_id
        else:
            div = super()._getSegments('div')
        script  = "<script>document.getElementById(\"" + div + "\").innerHTML = \"" + data + "\";</script>"
        #print(script)
        super()._setResults(script)
