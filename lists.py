#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:29:22 2019

@author: tcm410
"""

values = []
values.append(1)
values.append(3)
values.append(5)
print('first time:', values)
#print all from index number to end
values = values[1:3]
print('second time:', values)

values = [1, 2, 3, 4]
print(len(values))

#index 0 er første tegn så pront alt dog ikke sidste tegn
element = 'helium'
print(element[0:-1])



element = 'fluorine'
print(element[0::2])
print(element[::-1])