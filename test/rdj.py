#!/usr/bin/env python3

# jsonfile validation tool

import json

with open('site/TEST.json', 'r') as myfile:
    data=myfile.read()

print(data)

obj = json.loads(data)

print(obj["meta"]["title"])
print(obj["episodes"][1]["number"])
