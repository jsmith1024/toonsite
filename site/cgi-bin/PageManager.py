##  @file    PageManager.py
#   @brief   Python CGI script to present a simple website.
#   @authors joe smith

import fileinput

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
        filename            = "index.txt"
        with fileinput.input(files=(filename)) as f:
            for line in f:
                print(line)
    
    ##  run
    #   @brief  Page run loo, which handles events.
    def run(self):
        #while(true):
            ## catch event
            # seperate theread(s) ???
            # if detect action: ???
            #action  = ???
            #output  = self.__Model.setAction(action)
            #content = self.__View.setOut(output)
            #self.__setDiv("data", content)
            #self.__update()
            #self.__setDiv()
        pass
    
    ##  update
    #   @brief  updates page
    def __update(self):
        pass

    def __setDiv(self, div, data):
        print("here")
        script  = "<script>document.getElementById(\"" + div + "\").innerHTML = \"" + data + "\";</script>"
        print(script)

if __name__ == "__main__":
    Page = PageManager()
