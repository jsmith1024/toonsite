##  @file    HTMLSegmentFormatter.py
#   @brief   Formats HTML segments for CGI scripts.
#   @authors joe smith

#import fileinput
#import json
#import cgi
#import cgitb
#cgitb.enable()

##  @class  HTMLSegmentFormatter
#   @brief  Stores basic format parameters and results.
class HTMLSegmentFormatter():

    ##  constuctor
    #   @brief      Aggregate MVC and display page.
    #   @param      segments    (dict)          code segments
    def __init__(self, segments = {}):
        self.__segments     = segments
        self.__results      = ''            # output string
    
    ##  repr
    #   @brief      string representation
    def __repr__(self):
        #print(self.__results)
        return self.__results
    
    ##  getSegments
    #   @brief      Format HTML/JavaScript segments.
    #   @returns    (str)           string to format
    def _getSegments(self, key):
        return self.__segments[key]
    
    ##  getResults
    #   @brief      Format HTML/JavaScript segments.
    #   @returns    (str)           formatted string
    def getResults(self):
        return self.__results
    
    ##  setResults
    #   @brief      Format HTML/JavaScript segments.
    #   @param      data        (str)           string to format
    def _setResults(self, results):
        self.__results      = results
