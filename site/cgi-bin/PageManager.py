##  @file    PageManager.py
#   @brief   Python CGI script to present a simple website.
#   @authors joe smith

from ButtonFormatter    import ButtonFormatter
from LinkFormatter      import LinkFormatter
from TextBoxFormatter   import TextBoxFormatter

import copy
import fileinput
import json
import cgi
import cgitb
cgitb.enable()

##  @class  PageManager
#   @brief  Manage a simple CGI page.
class PageManager():

    ##  constuctor
    #   @brief  Read form request variables.
    def __init__(self):
        form                = cgi.FieldStorage()
        if form.getfirst('title'):
            self.__title    = form.getfirst('title')
        else:
            self.__title    = "TEST"
        if not form.getfirst('index'):
            self.__index    = False
        else:
            try:
                self.__index= int(form.getfirst('index'))
            except:
                self.__index= False
        if form.getfirst('action'):
            self.__action   = form.getfirst('action')
        else:
            self.__action   = 'last'
        self.__filename     = "cgi-bin/index.txt"
        
        with open('TEST' + '/'+ 'TEST' + '.json', 'r') as myfile:
            data=myfile.read()
        self.__series       = json.loads(data)
        
        maximum             = len(self.__series["episodes"]) - 1
        if not self.__index:
            self.__index    = maximum
        if self.__index <= 0:
            self.__index    = 1
        if self.__index > maximum:
            self.__index > maximum
        
        # Hardwire Address  - MORE SECURE
        # Uncomment and set if desired.
        #host                = 'localhost'         # Hoste address or name.
        #port                = '8000'              # Set to False, if none.
        #file_path           = 'cgi-bin/index.py'  # Precise path.
        #self.__url          = 'http://' + host    # DON'T TOUCH!
        #if port:
            #self.__url      = ':' + port          # DON'T TOUCH!
        #self.__url          = '/' + file_path     # DON'T TOUCH!
        
        # Autodetect Address NOT AS SECURE         Best for Testing
        # Comment or delete to not use autodetect
        import os
        self.__url          = copy.deepcopy(os.environ['HTTP_REFERER'].split('?')[0])
        
    ##  printStart
    #   @brief  Print start of page.
    def printStart(self):
        print('Content-Type: text/html\n\n<html>\n\t<!DOCTYPE html>')
        print('\t<head>')
        print('\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
        print('\t\t<Content-Type: text/html>')
        print('\t\t<link rel="stylesheet" href="../toons.css">')
        print('\t\t<link rel="icon" href="http:///favicon.ico">')
        print('\t\t<title>' + self.__series["meta"]["title"] + '</title>')
        print('\t</head>')
        print('\t<body>\n')
        #print(self.__url)
        
    ##  printTitle
    #   @brief  Print title of page.
    def printTitle(self):
        print('\t\t<div id="title">')
        print('\t\t\t<h1>' + self.__series["meta"]["title"] + '</h1>')
        print('\t\t</div>\n')
        
    ##  printButtons
    #   @brief  Print contol buttons on  page.
    def printButtons(self):
        data        = '\t\t<div id="controls">\n'
        LFm         = LinkFormatter({'title': 'TEST'})
        BFm         = ButtonFormatter()
        
        # Format each button.
        url         = self.__url
        #print(url)
        
        action      = 'about'
        index       = str(self.__index)
        fields      = {'index': index, 'action': action}
        name        = BFm.setButton(action, action.capitalize())
        data       += '\t\t\t' + LFm.setLink(url, name, fields) +'\n'
        
        TBF         = TextBoxFormatter()
        data       += TBF.setForm([TBF.setTextBox('typein')])
        
        data       += "\t\t\t</p>\n"
        
        action      = 'first'
        index       = str(1)
        fields      = {'index': index, 'action': action}
        name        = BFm.setButton(action, action.capitalize())
        data       += '\t\t\t' + LFm.setLink(url, name, fields) +'\n'
        
        action      = 'previous'
        index       = str(self.__index - 1)
        fields      = {'index': index, 'action': action}
        name        = BFm.setButton(action, action.capitalize()[:-4])
        data       += '\t\t\t' + LFm.setLink(url, name, fields) +'\n'
        
        action      = 'reload'
        index       = str(self.__index)
        fields      = {'index': index, 'action': action}
        name        = BFm.setButton(action, action.capitalize())
        data       += '\t\t\t' + LFm.setLink(url, name, fields) +'\n'
        
        action      = 'next'
        index       = str(self.__index + 1)
        fields      = {'index': index, 'action': action}
        name        = BFm.setButton(action, action.capitalize())
        data       += '\t\t\t' + LFm.setLink(url, name, fields) +'\n'
        
        action      = 'last'
        index       = str(len(self.__series["episodes"]) - 1)
        fields      = {'index': index, 'action': action}
        name        = BFm.setButton(action, action.capitalize())
        data       += '\t\t\t' + LFm.setLink(url, name, fields) +'\n'
        print(data)
        
        # Set each button's status.
        print('\t\t\t' + '<script>document.getElementById("about").disabled      = false;</script>')
        print('\t\t\t' + '<script>document.getElementById("first").disabled      = false;</script>')
        if self.__index <= 1:
            disabled = "true"
        else:
            disabled = "false"
        print('\t\t\t' + '<script>document.getElementById("previous").disabled   = ' + disabled + ';</script>')
        print('\t\t\t' + '<script>document.getElementById("reload").disabled     = false;</script>')
        if self.__index >= len(self.__series["episodes"]) - 1:
            disabled = "true"
        else:
            disabled = "false"
        print('\t\t\t' + '<script>document.getElementById("next").disabled       = ' + disabled + ';</script>')
        print('\t\t\t' + '<script>document.getElementById("last").disabled       = false;</script>')
        print('\t\t</div>\n')
        
    ##  printLine
    #   @brief  Print a separation line on page.
    def printLine(self):
        print('\t\t<hr>\n')
        
    ##  printContent
    #   @brief  Print contents on page.
    def printContent(self):
        print('\t\t<div id="data">')
        if  (self.__action == "about"):
            data    = '\t\t\t' + self.__series["meta"]["about"]
        else:
            episode = self.__series["episodes"][self.__index]
            data    = '\t\t\t'
            data   += "<p>Episode #" + episode["number"] + "</p>"
            data   += "<h1>" + episode["story"] + " - Part" + episode["part"] + "</h1>"
            data   += "<img src=\"../" + self.__title + "/episodes/" + self.__title + "_" + episode["number"] + ".jpg\">"
            data   += "<p>" + episode["notes"] + "</p>"
        print(data)
        print('\t\t</div>\n')
        
    ##  printFinish
    #   @brief  Print end of page.
    def printFinish(self):
        print('\t</body>')
        print('</html>')
