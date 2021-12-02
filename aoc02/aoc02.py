#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

entries = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    entries.append(line.rstrip('\n').split(" "))
inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")
horiz = 0
depth = 0

for e in entries:
    if e[0] == 'forward':
        horiz += int(e[1])
    if e[0] == 'down':
        depth += int(e[1])
    if e[0] == 'up':
        depth -= int(e[1])

print(f'{horiz}, {depth} = {horiz*depth}')

print("------------------")
print("---- PART 2 ------")
print("------------------")


horiz = 0
depth = 0
aim = 0

for e in entries:
    if e[0] == 'forward':
        horiz += int(e[1])
        depth += aim * int(e[1])
    if e[0] == 'down':
        aim += int(e[1])
    if e[0] == 'up':
        aim -= int(e[1])

print(f'{horiz}, {depth} = {horiz*depth}')

