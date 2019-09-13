#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:37:38 2019

@author: tcm410
"""

print(type(3.4))  #float

number = 3.25 + 4
print(type(number))  #float

num_students = 600
num_per_class = 42


num_class = num_students//num_per_class
remainder = num_students % num_per_class

print(num_students, num_per_class)
print(num_class, remainder)

print("fractional string to int:", int(float("3.4"))) # only one step at a time first string to float and then float to int