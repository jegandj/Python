# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:28:26 2021

@author: DaviesJones
"""
import csv

name = input("Database file: ")
name2 = input("Sequences file: ")
#Create data structures for csv files

#Open and read files. Ignore first row
#Database should look like this {Name,[3,3,3]}
csv_file = open(name, "r")

strands = []
database = {}
for ind,row in enumerate(csv_file):
    if ind == 0:
        strands = [strand for strand in row.strip().split(',')][1:]
    else:
        current_row = row.strip().split(',')
        database[current_row[0]] = [int (x) for x in current_row[1:]]

s =  open(name2, "r").read()

final_strands = []
for strand in strands:
    i = 0
    max_s = 0
    current_max = 0
    while i < len(s):
        current_window = s[i:i+len(strand)]
        if current_window == strand:
            current_max += 1
            i += len(strand)
            max_s = max(max_s, current_max)
        else:
            current_max = 0
            i += 1
    final_strands.append(max_s)

for name,data in database.items():
    if data == final_strands:
        print(name)
        break
        print("No match")
        