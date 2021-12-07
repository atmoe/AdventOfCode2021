#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = True
def dbgPrint(text):
    if dbgEn:
        print(text)

locationsChar = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    locationsChar = line.strip().split(',')
inputFile.close()

locations = []
maxLoc = 0
minLoc = 100000000
for l in locationsChar:
    lInt = int(l)
    locations.append(lInt)
    if lInt > maxLoc:
        maxLoc = lInt

    if lInt < minLoc:
        minLoc = lInt

print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:

    minFuel = 1000000000
    for i in range(minLoc, maxLoc+1):
        total = 0
        for l in locations:
            total += abs(i - l)

        if total < minFuel:
            minFuel = total

    print(f'Result = {minFuel}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:

    minFuel = 1000000000
    for i in range(minLoc, maxLoc+1):
        total = 0
        for l in locations:
            diff = abs(i - l)
            total += int(diff * (diff + 1) / 2)

        if total < minFuel:
            minFuel = total

    print(f'Result = {minFuel}')

