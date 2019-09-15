#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:39:33 2019

@author: tcm410
"""
import requests
import pandas as pd

#from pandas.io.json import json_normalize 
payload={ 'api-key': '20bda977-fd31-44d8-b894-c88e1d0b0a94'}
r = requests.get('https://content.guardianapis.com/search?q=debates', params=payload)
r.status_code


content = r.json()


# content = r.json()
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

with open('out.json', 'w') as f:
    f.write(str(flat))
    
    
#r.json()
#content = r.json()
#df = pd.io.json.json_normalize(flat)
#df
#print(type(df))
#df.shape
#df.dtypes
#df['response.results'].describe()
#test = df["response.results"]
#results = pd.io.json.json_normalize(test)


import requests
import pandas as pd

#from pandas.io.json import json_normalize 
payload={ 'api-key': '20bda977-fd31-44d8-b894-c88e1d0b0a94'}
r = requests.get('https://content.guardianapis.com/search?q=debates', params=payload)
r.status_code


content = r.json()

print(content)