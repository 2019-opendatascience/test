#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:01:49 2019

@author: tcm410
"""

#define and use

#Encapsulation

#forklar import og pandas

import pandas as pd

def min_in_data(filename):
    data = pd.read.csv(filename)
    
    return data.min()

def report(pressure):
    print('pressure is', pressure)
    
report(22.5)


def first_negative(values):
    for v in values:
        if v < 0:
            return v


print(first_negative([1, 3, 5, -1]))

import random
for i in range(10):
    mass=70+20.0*(2.0*random.random()-1.0)
  
    def print_egg_label(mass):      
        if(mass>=85):
            print("jumbo")
        elif(mass>=70):
            print("large")
        elif(mass<70 and mass>=55):
            print("medium")
        else:
            print("small")
    
    print(mass, print_egg_label(mass))
    