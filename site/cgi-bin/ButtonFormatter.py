##  @file    ButtonFormatter.py
#   @brief   Format and accumulate a group of buttons.
#   @authors joe smith

from HTMLSegmentFormatter   import HTMLSegmentFormatter

##  @class  ButtonFormatter
#   @brief  Format a button.
class ButtonFormatter(HTMLSegmentFormatter):

    ##  setButton
    #   @brief      Format a link.
    #   @param      button_id   (str)           button id
    #   @param      button_name (str)           button name
    #   @returns    (str)                       formatted button
    def setButton(self, button_id, button_name):
        #print("here")
        data        = '<button id=\"' + button_id + '\" disabled>' + button_name + '</button>'
        #print(data)
        return data
