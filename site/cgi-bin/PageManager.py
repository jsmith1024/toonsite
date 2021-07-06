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
    #   @param  Model       (Model)         Model class
    #   @param  View        (View)          View class
    #   @param  Controller  (Controller)    Controller class
    def __init__(self): # ,Model, View, Controller):
        #self.__Model        = Model
        #self.__View         = View
        #self.__Controller   = Controller
        form                = cgi.FieldStorage()
        if form.getfirst('title'):
            self.__title    = form.getfirst('title')
        else:
            self.__title    = "TEST"
        if form.getfirst('index'):
            self.__index    = int(form.getfirst('index'))
        else:
            self.__index    = 0
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
        print("<script>document.getElementById(\"title\").innerHTML     = \"" + self.__series["meta"]["title"] + "\";</script>")
    
    ##  run
    #   @brief  Page run loo, which handles events.
    def run(self):
        print("<script>document.getElementById(\"about\").disabled      = false;</script>")
        print("<script>document.getElementById(\"title\").innerHTML     = series[\"meta\"][\"title\"];</script>")
        print("<script>document.getElementById(\"first\").disabled      = false;</script>")
        print("<script>document.getElementById(\"previous\").disabled   = (episode.index <= 1);</script>")
        print("<script>document.getElementById(\"reload\").disabled     = false;</script>")
        print("<script>document.getElementById(\"next\").disabled       = episode.index >= (length - 1);</script>")
        print("<script>document.getElementById(\"last\").disabled       = false;</script>")
        
        episode = self.__series["episodes"][1]
        data    = "Episode #" + episode["number"]
        data   += "<h1>" + episode["story"] + " - Part" + episode["part"] + "</h1>"
        data   += "<img src=\"" + self.__title + "/episodes/" + self.__title + "_" + episode["number"] + ".jpg\">"
        data   += "<p>" + episode["notes"] + "</p>"
        print(data)
        #self.__setDiv("data", data)
        
        length              = len(self.__series["episodes"])
        if  (self.__action == "about") or (self.__action == "reload"):
            self.__setDiv("data", data)
        elif self.__action == "first":
            self.__index    = 0
            self.__setDiv("data", data)
        # Add previous and next.
        elif self.__action == "last":
            self.__index    = length - 1
            self.__setDiv("data", data)
        else:
            raise ValueError("Invalid request.")
        pass
    
    ##  update
    #   @brief  updates page
    def __update(self):
        pass

    def __setDiv(self, div, data):
        #print("here")
        script  = "<script>document.getElementById(\"" + div + "\").innerHTML = \"" + data + "\";</script>"
        print(script)

if __name__ == "__main__":
    Page = PageManager()
