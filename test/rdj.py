#!/usr/bin/env python3

# jsonfile validation tool

#import json

#with open('site/TEST.json', 'r') as myfile:
    #data=myfile.read()

#print(data)

#obj = json.loads(data)

#print(obj["meta"]["title"])
#print(obj["episodes"][1]["number"])

base    = '<a href="http://localhost:8000/cgi-bin/index.py?title=' + 'TITLE' + '&index=' + '11' + '&action='
data    = '<h1 id="title">Coming Soon...</h1>'
data   += base + 'about><button     id=about    disabled>About</button> </a>\n'
data   += "</br>\n"
data   += base + 'first><button     id=first    disabled>First</button> </a>\n'
data   += base + 'previous><button  id=previous disabled>Prev</button>  </a>\n'
data   += base + 'reload><button    id=reload   disabled>Ret</button>   </a>\n'
data   += base + 'next><button      id=next     disabled>Next</button>  </a>\n'
data   += base + 'last><button      id=last     disabled>Last</button>  </a>\n'
print('<script>document.getElementById("controls").innerHTML = ' + data + ';</script>')
