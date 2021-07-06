#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

def setDiv(div, data):
    #print("here")
    script  = "<script>document.getElementById(\"" + div + "\").innerHTML = \"" + data + "\";</script>"
    print(script)

#def doThis(resource):
    #print("here: " + resource)
    #script  = "http://localhost:8000/cgi-bin/index.py&" + resource
    #print(script)

print("Content-Type: text/html\n\n")
print("<html>")
print("\t<!DOCTYPE html>")
print("\t<head>")
print('\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
print("\t\t<title>TOONS!</title>")
print("\t\t<Content-Type: text/html>")
print("\t</head>")
print("\t<body>")
print("""
        <div id="controls">
            <h1 id="title">Coming Soon...</h1>
            <a href="http://localhost:8000/cgi-bin/index.py?action=about"><button>About</button></a>
            </br>
            <button type="button" class="nav" id="first"    disabled>First</button>
            <button type="button" class="nav" id="previous" disabled>Prev</button>
            <button type="button" class="nav" id="reload"   onclick="reload()"              disabled>Ret</button>
            <button type="button" class="nav" id="next"     disabled>Next</button>
            <button type="button" class="nav" id="last"     disabled>Last</button>
        </div>		
        <hr>
        <div class="data" id="meta">
            Initial meta.
        </div>
        <div class="data" id="view">
            Initial view.
        </div>
    """)
form = cgi.FieldStorage()
print("form:")
print(form)
user = form.getfirst("user", "").upper()    # This way it's safe.
for item in form.getlist("item"):
    print(item)
print("keys:")
print(form.keys())
print("EOF")
print(form.getfirst('action'))
print('<script>document.getElementById("view").innerHTML = "hello";</script>')
setDiv("view", "HELLO")
print("\t</body>")
print("</html>")
setDiv("view", "YAY!!")

###############################################
## Using PageManager class to replace above: ##
###############################################

#from ToonModel      import ToonModelv
#from ToonView       import ToonView
#from ToonController import ToonController
#from PageManager    import PageManager

#Page    = PageManager(ToonModel(), ToonView(), ToonController())
#Page.run()
