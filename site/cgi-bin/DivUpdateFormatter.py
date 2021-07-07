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
    def setDiv(self, data):
        #print("here")
        script  = "<script>document.getElementById(\"" + super()._getSegments('div') + "\").innerHTML = \"" + data + "\";</script>"
        #print(script)
        super()._setResults(script)
