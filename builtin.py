#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:53:18 2019

@author: tcm410
"""

# word = 'blah'
word = "blah"
#first min of blahblahblur and aaah is stored = aaah 
#then aaah and ping is compaired letter by letter
word = max(min(word * 2, 'aaah '), 'ping')
print(word)

rich = "gold"
poor = "tin"
print(max(rich, poor))
print(max(len(rich), len(poor)))

start = "word"
start[len(start)- 1]