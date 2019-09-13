#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:34:27 2019

@author: tcm410
"""
import os

path = os.getcwd()

print(path)

import datetime
help(datetime)

isoyear = datetime.date(2019, 9, 11).isoformat()
print(isoyear)

print(datetime.date(2019, 9, 11).isoformat())

import string as s
numbers = s.digits
print(numbers)


from string import digits
print(list(digits))

import string
print(string.ascii_uppercase)

import string as s
print(list(s.digits))

import math
angle = math.degrees(math.pi/2) 
print(angle)

