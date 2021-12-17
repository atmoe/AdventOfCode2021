#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text='', endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

inputFile = open(sys.argv[1], "r")
targetRe = re.match('target area: x=(-*\d+)\.\.(-*\d+), y=(-*\d+)\.\.(-*\d+)', inputFile.readline())
tX0 = int(targetRe.group(1))
tX1 = int(targetRe.group(2))
tY0 = int(targetRe.group(3))
tY1 = int(targetRe.group(4))
inputFile.close()

print(f'target = ({tX0},{tY0}) -> ({tX1},{tY1})')


def adjVel(velocity):
    if velocity[0] == 0:
        xVel = 0
    elif velocity[0] < 0:
        xVel = velocity[0] + 1
    elif velocity[0] > 0:
        xVel = velocity[0] - 1

    yVel = velocity[1] - 1
       
    return (xVel, yVel)

def adjPos(p, vel):
    pX = p[0] + vel[0]
    pY = p[1] + vel[1]
    return (pX, pY)

def posInTarget(p):
    if p[0] < tX0 or p[0] > tX1:
        return False
    if p[1] < tY0 or p[1] > tY1:
        return False

    return True

def posLeftTarget(p):
    return p[0] < tX0

def posRightTarget(p):
    return p[0] > tX1

def posBelowTarget(p):
    return p[1] < tY0

def posAboveTarget(p):
    return p[1] > tY1


def fireShot(vel):
    maxY = 0
    pos = (0,0)
    while not posRightTarget(pos) and not posBelowTarget(pos):
        dbgPrint(f'pos = {pos} vel = {vel}')
        pos = adjPos(pos, vel)
        vel = adjVel(vel)

        if pos[1] > maxY:
            maxY = pos[1]

        if posInTarget(pos):
            return maxY

    return -1

# I just guessed at the numbers to iterate
# the guess was based upon a range of hitting the
# target box with one step
numIters = 200
print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    bestY = -1
    for yV in range(0,numIters):
        for xV in range(1,tX1):
            yVal = fireShot((xV, yV))
            if yVal > bestY:
                bestY = yVal

    print(f'Result = {bestY}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    count = 0
    for yV in range(tY0*2,numIters):
        for xV in range(1,tX1+10):
            yVal = fireShot((xV, yV))
            if yVal != -1:
                count+=1

    print(f'Result = {count}')


