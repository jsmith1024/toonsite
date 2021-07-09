##  @file    LinkFormatter.py
#   @brief   Format and accumulate a group of buttons.
#   @authors joe smith

from HTMLSegmentFormatter   import HTMLSegmentFormatter

from copy                   import deepcopy

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
        # merge default and local fields
        if not super()._getAllSegments() == {}:
            temp_fields = deepcopy(fields)
            fields      = deepcopy(super()._getAllSegments())
            for key in temp_fields.keys():
                fields[key] = temp_fields[key]
        #print(str(fields))
        
        # Format link.
        data            = '<a href=\"' + url
        if fields:
            data       += '?'
            for key in fields.keys():
                data   += key + '=' + fields[key] + '&'
            data        = data[:-1]
        data           += '\">' + name + '</a>'
        #print(data)
        return data
