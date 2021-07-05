#!/usr/bin/env python3

import cgi

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
            <button type="button" class="nav" id="about"    onclick="updateToAbout()"       disabled>About</button>
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

print("\t</body>")
print("</html>")
