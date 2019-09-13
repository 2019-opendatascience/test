#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:17:48 2019

@author: tcm410
"""

total = 0
for char in "tin":
    total = total +1
    
original = "tin"
result = ""
for char in original:
    
    result = char + result # appending chars in reverse order FIFO

print(result)

string = "tin"
print(''.join(reversed(string))) #https://www.journaldev.com/23647/python-reverse-string

print("tin"[::-1])

#"Total length of the strings in the list:
total = 0
for word in ("red", "green", "blue"):
    total = total + len(word)
print(total)

lengths = []
for word in ["red", "green", "blue"]:
        lengths.append(len(word))
print(lengths)

# Concatenate all words: ["red", "green", "blue"] => "redgreenblue"
words = ["red", "green", "blue"]
result = ""
for word in words:
    result = result + word
print(result)

# Create acronym: ["red", "green", "blue"] => "RGB"
# write the whole thing

acronym = ""
for word in ["red", "green", "blue"]:
    acronym = acronym + word[0].upper()
print(acronym)

#indent excercise
sum = 0
data = [1,2,2,5]
cumulative = []
for number in data:
    
    sum += number
    cumulative.append(sum)
    
print(cumulative)

#variable name errors
message = ""                     #message was not defined


for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    
    if (number % 3) == 0:       #change Number to number
        message = message + "a" #change a to string
    else:
        message = message + "b"
print(message)

#identifying item errors

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[3])         #item 4 does not exist numbering bgeins with 0
