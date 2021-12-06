#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = True
def dbgPrint(text):
    if dbgEn:
        print(text)

fishAgesChar = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    fishAgesChar = line.strip().split(',')
inputFile.close()

fishAges = []
for c in fishAgesChar:
    fishAges.append(int(c))


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    fishAgesP1 = list(fishAges)
    for i in range(0,80):
        fishAgesNext = []
        for fish in fishAgesP1:
            if fish == 0: 
                fishAgesNext.append(6)
                fishAgesNext.append(8)
            else:
                fishAgesNext.append(fish-1)

        fishAgesP1 = fishAgesNext

    print(f'Result = {len(fishAgesP1)}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
# This does the same thing as part 1, just faster because no new arrays
doPart2 = True
if doPart2:
    fishOfAge = [0]*9
    for f in fishAges:
        fishOfAge[f] += 1

    for i in range(0,256):
        fishOfAgeNext = [0]*9

        fishOfAgeNext[0] = fishOfAge[1]
        fishOfAgeNext[1] = fishOfAge[2]
        fishOfAgeNext[2] = fishOfAge[3]
        fishOfAgeNext[3] = fishOfAge[4]
        fishOfAgeNext[4] = fishOfAge[5]
        fishOfAgeNext[5] = fishOfAge[6]
        fishOfAgeNext[6] = fishOfAge[7] + fishOfAge[0]
        fishOfAgeNext[7] = fishOfAge[8]
        fishOfAgeNext[8] = fishOfAge[0]

        fishOfAge = fishOfAgeNext

    print(f'Result = {sum(fishOfAge)}')

