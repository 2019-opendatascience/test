#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:13:22 2019

@author: tcm410
"""

original = "tin"
result = ""
for char in original:
    
    result = char + result # appending chars in reverse order

print(result)

print("tin"[::-1])