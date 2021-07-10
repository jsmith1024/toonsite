##  @file    TextBoxFormatter.py
#   @brief   Format text inputs within a form.
#   @authors joe smith

from HTMLSegmentFormatter   import HTMLSegmentFormatter

#from copy                   import deepcopy

##  @class  TextBoxFormatter
#   @brief  Format and accumulate a group of buttons.
class TextBoxFormatter(HTMLSegmentFormatter):

    ##  setForm
    #   @brief      Format a form.
    #   @param      boxes       (list)          formatted text boxes
    #   @param      vertical    (bool)          Add new line between boxes? default = False
    #   @param      sub_vert    (bool)          Add new line before submit? default = False
    #   @returns    (str)                       form string
    def setForm(self, boxes, vertical = False, sub_vert = False):
        data            = '\t\t\t' +'<form>\n'
        for i in range(len(boxes)):
            if vertical and (i != 0):
                data   += '</p>'
            data       += boxes[i]
        if sub_vert:
            data       += '</p>'
        data           += '\t\t\t\t' + '<input type="submit" value="submit">\n'
        data           += '\t\t\t' +'</form>\n'
        #print(data)
        return data

    ##  setTextBox
    #   @brief      Format a text box.
    #   @param      box_id      (str)           text box id
    #   @param      box_label   (str)           text box label              default = False
    #   @param      box_name    (str)           text box name               default = False
    #   @returns    (str)                       text box string
    def setTextBox(self, box_id, box_label = False, box_name = False):
        if not box_label:
            box_label   = box_id.capitalize()
        if not box_name:
            box_name    = box_label.lower()
        #data            = '\t\t\t\t' + '<label for="' + box_id + '">' + box_label + '</label><br>\n'
        data            = '\t\t\t\t' + '<input type="text" id="' + box_id + '" value="' + box_label + '">\n'
        #print(data)
        return data
