#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = True
def dbgPrint(text):
    if dbgEn:
        print(text)

def lineIsHoriz(line):
    return line[1] == line[3]

def lineIsVert(line):
    return line[0] == line[2]

lines = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    lineRe = re.match('^(\d+),(\d+) -> (\d+),(\d+)', line)
    lines.append([int(lineRe.group(1)), int(lineRe.group(2)), int(lineRe.group(3)), int(lineRe.group(4))])
inputFile.close()


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    locations = {}
    for l in lines:
        if lineIsHoriz(l):
            if l[0] < l[2]:
                s = l[0]
                e = l[2]
            else:
                s = l[2]
                e = l[0]

            for x in range(s, e+1):
                key = f'{l[1]} {x}'
                if not key in locations:
                    locations[key] = 1
                else:
                    locations[key] += 1

        elif lineIsVert(l):
            if l[1] < l[3]:
                s = l[1]
                e = l[3]
            else:
                s = l[3]
                e = l[1]

            for y in range(s, e+1):
                key = f'{y} {l[0]}'
                if not key in locations:
                    locations[key] = 1
                else:
                    locations[key] += 1

    overlaps = 0
    for k in locations:
        if locations[k] > 1:
            overlaps += 1

    print(f'Overlaps = {overlaps}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    locations = {}
    for l in lines:
        if lineIsHoriz(l):
            if l[0] < l[2]:
                s = l[0]
                e = l[2]
            else:
                s = l[2]
                e = l[0]

            for x in range(s, e+1):
                key = f'{l[1]} {x}'
                if not key in locations:
                    locations[key] = 1
                else:
                    locations[key] += 1

        elif lineIsVert(l):
            if l[1] < l[3]:
                s = l[1]
                e = l[3]
            else:
                s = l[3]
                e = l[1]

            for y in range(s, e+1):
                key = f'{y} {l[0]}'
                if not key in locations:
                    locations[key] = 1
                else:
                    locations[key] += 1
        else: # diagonal
            if l[0] < l[2]:
                s   = l[0]
                e   = l[2]
                y_s = l[1]
                if l[1] < l[3]:
                    y_dir = 1
                else:
                    y_dir = -1


            else:
                s   = l[2]
                e   = l[0]
                y_s = l[3]
                if l[3] < l[1]:
                    y_dir = 1
                else:
                    y_dir = -1

            steps = 0
            for x in range(s, e+1):
                key = f'{y_s+steps*y_dir} {x}'
                if not key in locations:
                    locations[key] = 1
                else:
                    locations[key] += 1

                steps+=1

    overlaps = 0
    for k in locations:
        if locations[k] > 1:
            overlaps += 1

    print(f'Overlaps = {overlaps}')

    quit()

