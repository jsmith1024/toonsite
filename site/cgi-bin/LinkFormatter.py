##  @file    LinkFormatter.py
#   @brief   Format and accumulate a group of buttons.
#   @authors joe smith

from HTMLSegmentFormatter   import HTMLSegmentFormatter

#import fileinput
#import json
#import cgi
#import cgitb
#cgitb.enable()

##  @class  LinkFormatter
#   @brief  Format and accumulate a group of buttons.
class LinkFormatter(HTMLSegmentFormatter):

    ##  setLink
    #   @brief      Format and append a button.
    #   @param      url         (str)           address (fqdn + path)
    #   @param      name        (str)           link label
    #   @param      fields      (dict)          request fields
    #   @returns    (str)                       link string
    def setLink(self, url, name, fields = False):
        #print("here")
        data            = '<a href=\"' + url
        if fields:
            data       += '?'
            for key in fields.keys():
                data   += key + '=' + fields[key] + '&'
            data        = data[:-1]
        data           += '\">' + name + '</a>'
        #print(data)
        return data
