#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text='', endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

dots  = []
folds = []
parseDots = True

inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    if parseDots:
        dotRe = re.match('(\d*),(\d*)', line)
        if not dotRe:
            parseDots = False
            continue
        dots.append((int(dotRe.group(1)), int(dotRe.group(2))))
    else:
        foldRe = re.match('fold along (.)=(\d*)', line)
        folds.append((foldRe.group(1), int(foldRe.group(2))))


inputFile.close()


def printDots(dots):
    maxX = 0
    maxY = 0
    for d in dots:
        if d[0] > maxX: maxX = d[0]
        if d[1] > maxY: maxY = d[1]

    grid = []
    for i in range(0,maxY+1):
        grid.append(['.']*(maxX+1))

    for d in dots:
        grid[d[1]][d[0]] = '#'

    for g in grid:
        print("".join(g))



print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:

    newDots = {}
    for d in dots:
        newDots[d] = True

    if dbgEn:
        printDots(dots)
        print("--------------------")

    numFolds = 1
    for f in range(0,numFolds):

        fold  = folds[f]
        fDir  = fold[0]
        fLine = fold[1]
        nextNewDots = {}
        for d in newDots:
            if fDir == 'y':
                if d[1] < fLine:
                    nextNewDots[d] = True
                else:
                    nextNewDots[(d[0], fLine - (d[1] - fLine))] = True
    
            if fDir == 'x':
                if d[0] < fLine:
                    nextNewDots[d] = True
                else:
                    foldedX = fLine - (d[0] - fLine)
                    nextNewDots[(foldedX, d[1])] = True

        newDots = nextNewDots

        if dbgEn:
            printDots(newDots.keys())
            print("--------------------")


    print(f'Result = {len(newDots.keys())}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    newDots = {}
    for d in dots:
        newDots[d] = True

    numFolds = 1
    for f in range(0,len(folds)):

        fold  = folds[f]
        fDir  = fold[0]
        fLine = fold[1]
        nextNewDots = {}
        for d in newDots:
            if fDir == 'y':
                if d[1] < fLine:
                    nextNewDots[d] = True
                else:
                    nextNewDots[(d[0], fLine - (d[1] - fLine))] = True
    
            if fDir == 'x':
                if d[0] < fLine:
                    nextNewDots[d] = True
                else:
                    foldedX = fLine - (d[0] - fLine)
                    nextNewDots[(foldedX, d[1])] = True

        newDots = nextNewDots

    printDots(newDots.keys())


