#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:02:34 2019

@author: tcm410
"""

values = []
values.append(1)
values.append(3)
values.append(5)

print('first time:', values)
values=values[1:3]  #slice function

print('second time:', values)

print('string to list:', list('tin'))
print('list to string:', ''.join(['g','o','l','d']))

element = 'helium'
print(element[0:-1])

element = 'fluorine' #lookup stride in manual
print(element[::2]) #https://docs.python.org/3/library/stdtypes.html#typesseq
print(element[::-1])

#letters = list('gold')
#result = sorted(letters)
#print(letters, result)

#letters = list('gold')
#print(letters.sort(gold)) #lookup in manual
#print(letters, result)

old = list('gold')
new = old
new[0] = 'D'                  #item 0 of new replaced by D
print(new, old)

old = list('gold')
new = old[:]                 #a copy is returned iterable[:] https://docs.python.org/3/library/stdtypes.html?highlight=slice%20assignment
new[0] = 'D'
print(new, old)

