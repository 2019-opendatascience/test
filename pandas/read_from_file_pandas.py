#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:23:00 2019

@author: tcm410
"""

import pandas as pd

df_SN7577 = pd.read_csv("data/SN7577.tab", sep='\t')

df_SN7577.head()

for name in df_SN7577.columns:
    print(name)
    