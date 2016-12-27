#coding:utf-8
import json
# Reading data back
with open('t1.json', 'r') as f:
    data = json.load(f)
    for d in data:
        #print d['name'],d['place'],d['intro']
        print d['name']