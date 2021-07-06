##  @file    ToonController.py
#   @brief   Controls page response.
#   @authors joe smith

##  @class  ToonController
#   @brief  Controls page response.
class ToonController():

    ##  constuctor
    #   @brief  
    def __init__(self):
        self.__length   = 0
        self.__index    = self.__length
    
    ##  setLength
    #   @brief  Sets the number of episodes.
    #   @param  length      (int)           length of series['episodes']
    def setLength(self, length):
        self.__length   = length
    
    ##  setAction
    #   @brief  Sets the request.
    #   @param  action      (str)           requested action
    def setAction(self, action):
        if  (action == "about") or (action == "reload"):
            self.__action   = action
        elif action == "first":
            self.__index    = 0
            self.__action   = str(index)
        # Add previous, next, and last.
        else:
            raise ValueError("Invalid request.")
    
    ##  update
    #   @brief  updates page
    #def __update(self):
        #pass

    #def __setDiv(self, div, data):
        #print("here")
        #script  = "<script>document.getElementById(\"" + div + "\").innerHTML = \"" + data + "\";</script>"
        #print(script)
