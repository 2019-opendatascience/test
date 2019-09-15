#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:40:25 2019

@author: tcm410
"""

import requests
import pandas as pd

#from pandas.io.json import json_normalize 
payload={'resource_id' : 'b3eeb0ff-c8a8-4824-99d6-e0a3747c8b0d'}
r = requests.get('http://portal.opendata.dk/api/3/action/datastore_search', params=payload)
r.status_code

content = r.json()

def flatten_json(y):
    out = {}
 
    def flatten(x, name=''):
     if type(x) is dict:
          for a in x:
               flatten(x[a], name + a + '')
     elif type(x) is list:
              i = 0
              for a in x:
                 flatten(a, name + str(i) + '')
                 i += 1
     else:
          out[name[:-1]] = x
              
    flatten(y)
    return out

flat = flatten_json(content)

df = pd.io.json.json_normalize(flat)


























#df = pd.io.json.json_normalize(content["result"])

#df.dtypes
#df.records[0]


