##  @file    PageManager.py
#   @brief   Python CGI script to present a simple website.
#   @authors joe smith

import fileinput
import json
import cgi
import cgitb
cgitb.enable()

##  @class  PageManager
#   @brief  Manage a simple CGI page.
class PageManager():

    ##  constuctor
    #   @brief  Aggregate MVC and display page.
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
        filename            = "cgi-bin/index.txt"
        
        with fileinput.input(files=(filename)) as f:
            for line in f:
                print(line)
        with open(self.__title + '/'+ self.__title + '.json', 'r') as myfile:
            data=myfile.read()
        self.__series       = json.loads(data)
        print("<script>document.getElementById(\"title_bar\").innerHTML = \"" + self.__series["meta"]["title"] + "\";</script>")
        
        if not form.getfirst('index'):
            self.__index    = len(self.__series["episodes"]) - 1
        
        base        = '<a href="http://localhost:8000/cgi-bin/index.py?title=' + self.__title + '&index='
        index       = str(self.__index)
        data        = base + index + '&action=about\">      <button id="about"      disabled>About</button> </a>\n'
        data       += "</br>\n"
        index       = str(1)
        data       += base + index +  '&action=first\">      <button id="first"      disabled>First</button> </a>\n'
        index       = str(self.__index - 1)
        data       += base + index +  '&action=previous\">   <button id="previous"   disabled>Prev</button>  </a>\n'
        index       = str(self.__index)
        data       += base + index +  '&action=reload\">     <button id="reload"     disabled>Ret</button>   </a>\n'
        index       = str(self.__index + 1)
        data       += base + index +  '&action=next\">       <button id="next"       disabled>Next</button>  </a>\n'
        index       = str(len(self.__series["episodes"]) - 1)
        data       += base + index +  '&action=last\">       <button id="last"       disabled>Last</button>  </a>\n'
        print(data)
        #print("<script>document.getElementById(\"controls\").innerHTML  = \"" + data + "\";</script>")
        print("<hr>")
        print("<script>document.getElementById(\"title\").innerHTML     = \"<h1>" + self.__series["meta"]["title"] + "</h1>\";</script>")
    
    ##  run
    #   @brief  Page run loo, which handles events.
    def run(self):
        print('<script>document.getElementById("about").disabled      = false;</script>')
        print('<script>document.getElementById("title").innerHTML     = ' + self.__series["meta"]["title"] + ';</script>')
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
        
        #print("index: " + str(self.__index))
        episode = self.__series["episodes"][self.__index]
        data    = "Episode #" + episode["number"]
        data   += "<h1>" + episode["story"] + " - Part" + episode["part"] + "</h1>"
        data   += "<img src=\"../" + self.__title + "/episodes/" + self.__title + "_" + episode["number"] + ".jpg\">"
        data   += "<p>" + episode["notes"] + "</p>"
        #self.__setDiv("view", data)
        
        length              = len(self.__series["episodes"])
        if  (self.__action == "about"):
            data            = self.__series["meta"]["about"]
        elif self.__action == "first":
            self.__index    = 0
        # Add previous.
        # Add next.
        elif self.__action == "last":
            self.__index    = len(self.__series["episodes"]) - 1
        else:
            #raise ValueError("Invalid request.")
            pass
        print(data)
        #self.__setDiv("view", data)
    
    ##  setDiv
    #   @brief  updates page
    def __setDiv(self, div, data):
        #print("here")
        script  = "<script>document.getElementById(\"" + div + "\").innerHTML = \"" + data + "\";</script>"
        print(script)
