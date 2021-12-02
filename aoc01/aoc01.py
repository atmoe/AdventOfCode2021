#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

entries = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    entries.append(int(line))

inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")

increases = 0
for i in range(len(entries) - 1):
    if entries[i] < entries[i+1]:
        increases += 1
    
print(increases)

print("------------------")
print("---- PART 2 ------")
print("------------------")

increases = 0
for i in range(len(entries) - 3):
    if entries[i] < entries[i+3]:
        increases += 1
    
print(increases)


