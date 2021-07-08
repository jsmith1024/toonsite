#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

from PageManager    import PageManager

Page    = PageManager()
Page.printStart()
Page.printTitle()
Page.printButtons()
Page.printLine()
Page.printContent()
Page.printFinish()
