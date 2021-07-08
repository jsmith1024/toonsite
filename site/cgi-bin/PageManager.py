##  @file    PageManager.py
#   @brief   Python CGI script to present a simple website.
#   @authors joe smith

from ButtonFormatter    import ButtonFormatter
from LinkFormatter      import LinkFormatter
from DivUpdateFormatter import DivUpdateFormatter

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
        if form.getfirst('index'):
            self.__index    = int(form.getfirst('index'))
        if form.getfirst('action'):
            self.__action   = form.getfirst('action')
        else:
            self.__action   = 'last'
        self.__filename     = "cgi-bin/index.txt"
        
        div     = {'div': 'view'}
        self.__DUF          = DivUpdateFormatter(div)
        
        if not form.getfirst('index'):
            self.__index    = len(self.__series["episodes"]) - 1
        
        with open(self.__title + '/'+ self.__title + '.json', 'r') as myfile:
            data=myfile.read()
        self.__series       = json.loads(data)

    ##  printBody
    #   @brief  Print outline of page.
    def printBody(self):
        with fileinput.input(files=(self.__filename)) as f:
            for line in f:
                print(line[:-1])

    ##  printTitleBar
    #   @brief  Set title in web browser bar.
    def printTitleBar(self):
        print('<title>' + self.__series["meta"]["title"] + '</title>')
        
    ##  printTitle
    #   @brief  Print title of page.
    def printTitle(self):
        print('<h1>' + self.__series["meta"]["title"] + '</h1>')
        
    ##  printButtons
    #   @brief  Print contol buttons on  page.
    def printButtons(self):
        data        = ''
        LFm         = LinkFormatter({'title': 'TEST'})
        BFm         = ButtonFormatter()
        
        # Format each button.
        action      = 'about'
        index       = str(self.__index)
        fields      = {'index': index, 'action': action}
        url         = 'http://localhost:8000/cgi-bin/index.py'
        name        = BFm.setButton(action, action.capitalize())
        data       += LFm.setLink(url, name, fields)
        data       += "</p>\n"
        
        action      = 'first'
        index       = str(1)
        fields      = {'index': index, 'action': action}
        url         = 'http://localhost:8000/cgi-bin/index.py'
        name        = BFm.setButton(action, action.capitalize())
        data       += LFm.setLink(url, name, fields)
        
        action      = 'previous'
        index       = str(self.__index - 1)
        fields      = {'index': index, 'action': action}
        url         = 'http://localhost:8000/cgi-bin/index.py'
        name        = BFm.setButton(action, action.capitalize()[:-4])
        data       += LFm.setLink(url, name, fields)
        
        action      = 'reload'
        index       = str(self.__index)
        fields      = {'index': index, 'action': action}
        url         = 'http://localhost:8000/cgi-bin/index.py'
        name        = BFm.setButton(action, action.capitalize())
        data       += LFm.setLink(url, name, fields)
        
        action      = 'next'
        index       = str(self.__index + 1)
        fields      = {'index': index, 'action': action}
        url         = 'http://localhost:8000/cgi-bin/index.py'
        name        = BFm.setButton(action, action.capitalize())
        data       += LFm.setLink(url, name, fields)
        
        action      = 'last'
        index       = str(len(self.__series["episodes"]) - 1)
        fields      = {'index': index, 'action': action}
        url         = 'http://localhost:8000/cgi-bin/index.py'
        name        = BFm.setButton(action, action.capitalize())
        data       += LFm.setLink(url, name, fields)
        print(data)
        
        # Set each button's status.
        print('<script>document.getElementById("about").disabled      = false;</script>')
        print('<script>document.getElementById("first").disabled      = false;</script>')
        if self.__index <= 1:
            disabled = "true"
        else:
            disabled = "false"
        print('<script>document.getElementById("previous").disabled   = ' + disabled + ';</script>')
        print('<script>document.getElementById("reload").disabled     = false;</script>')
        if self.__index >= len(self.__series["episodes"]) - 1:
            disabled = "true"
        else:
            disabled = "false"
        print('<script>document.getElementById("next").disabled       = ' + disabled + ';</script>')
        print('<script>document.getElementById("last").disabled       = false;</script>')
        
    ##  printLine
    #   @brief  Print a separation line on page.
    def printLine(self):
        print('<hr>')
        
    ##  printContent
    #   @brief  Print contents on page.
    def printContent(self):
        if  (self.__action == "about"):
            data            = self.__series["meta"]["about"]
        else:
            episode = self.__series["episodes"][self.__index]
            data    = "Episode #" + episode["number"]
            data   += "<h1>" + episode["story"] + " - Part" + episode["part"] + "</h1>"
            data   += "<img src=\"../" + self.__title + "/episodes/" + self.__title + "_" + episode["number"] + ".jpg\">"
            data   += "<p>" + episode["notes"] + "</p>"
        print(data)
