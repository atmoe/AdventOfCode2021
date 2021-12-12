#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text, endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

class Octopus:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.e = energy
        self.flashed = False

    # returns true if needs to flash
    def incrEnergy(self):
        if self.flashed:
            return False

        self.e += 1
        if self.e > 9:
            return True
        else:
            return False
   
    def flash(self):
        self.e = 0
        self.flashed = True

    def newTurn(self):
        self.flashed = False

octopiOrig = []
inputFile = open(sys.argv[1], "r")
x = 0
y = 0
for line in inputFile.readlines():
    row = []
    x=0
    for o in line.strip():
        row.append(Octopus(x,y,int(o)))
        x+=1

    octopiOrig.append(row)
    y+=1

inputFile.close()

gridW = len(octopiOrig[0])
gridH = len(octopiOrig)
print(f'{gridW}x{gridH}')

def printOctopi(octopi):
    for rows in octopi:
        for y in rows:
            dbgPrint(y.e, '')
        dbgPrint("")


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:

    numFlashes = 0
    octopi = copy.deepcopy(octopiOrig)
    printOctopi(octopi)
    numSteps = 100
    for i in range(1, numSteps+1):
        dbgPrint(f'--- Step {i} ---')

        needsFlash = []

        # increment everyone first
        for rows in octopi:
            for o in rows:
                flash = o.incrEnergy()
                if flash:
                    needsFlash.append(o)

        while len(needsFlash) > 0:
            nxtNeedsFlash = []

            for o in needsFlash:
                o.flash()
                numFlashes+=1
                incrOctopiCoords = []
                incrOctopiCoords.append((o.x-1, o.y-1))
                incrOctopiCoords.append((o.x-1, o.y))
                incrOctopiCoords.append((o.x-1, o.y+1))
                incrOctopiCoords.append((o.x,   o.y-1))
                incrOctopiCoords.append((o.x,   o.y+1))
                incrOctopiCoords.append((o.x+1, o.y-1))
                incrOctopiCoords.append((o.x+1, o.y))
                incrOctopiCoords.append((o.x+1, o.y+1))

                for io in incrOctopiCoords:
                    x = io[0]
                    y = io[1]
                    if x < 0 or x >= gridW:
                        continue
                    if y < 0 or y >= gridH:
                        continue

                    flash = octopi[y][x].incrEnergy()
                    if flash and octopi[y][x] not in nxtNeedsFlash and octopi[y][x] not in needsFlash:
                        nxtNeedsFlash.append(octopi[y][x])

            needsFlash = nxtNeedsFlash


        for row in octopi:
            for o in row:
                o.newTurn()
        printOctopi(octopi)
    print(f'Result = {numFlashes}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:

    octopi = copy.deepcopy(octopiOrig)
    printOctopi(octopi)
    step = 1
    allFlashed = False
    while not allFlashed:
        dbgPrint(f'--- Step {i} ---')

        needsFlash = []

        # increment everyone first
        for rows in octopi:
            for o in rows:
                flash = o.incrEnergy()
                if flash:
                    needsFlash.append(o)

        while len(needsFlash) > 0:
            nxtNeedsFlash = []

            for o in needsFlash:
                o.flash()
                incrOctopiCoords = []
                incrOctopiCoords.append((o.x-1, o.y-1))
                incrOctopiCoords.append((o.x-1, o.y))
                incrOctopiCoords.append((o.x-1, o.y+1))
                incrOctopiCoords.append((o.x,   o.y-1))
                incrOctopiCoords.append((o.x,   o.y+1))
                incrOctopiCoords.append((o.x+1, o.y-1))
                incrOctopiCoords.append((o.x+1, o.y))
                incrOctopiCoords.append((o.x+1, o.y+1))

                for io in incrOctopiCoords:
                    x = io[0]
                    y = io[1]
                    if x < 0 or x >= gridW:
                        continue
                    if y < 0 or y >= gridH:
                        continue

                    flash = octopi[y][x].incrEnergy()
                    if flash and octopi[y][x] not in nxtNeedsFlash and octopi[y][x] not in needsFlash:
                        nxtNeedsFlash.append(octopi[y][x])

            needsFlash = nxtNeedsFlash


        allFlashed = True
        for row in octopi:
            for o in row:
                if not o.flashed:
                    allFlashed = False

                o.newTurn()

        printOctopi(octopi)

        if allFlashed:
            print(f'Result = {step}')
            break

        step+=1




