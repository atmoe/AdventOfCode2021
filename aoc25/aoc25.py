#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text='', endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

grid = []

inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    grid.append(list(line.strip()))
inputFile.close()


gridW = len(grid[0])
gridH = len(grid)


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:

    p1Grid = copy.deepcopy(grid)
    for g in p1Grid:
        print("".join(g))

    row = ['.'] * gridW

    step = 1
    didMove = True
    while didMove:
        didMove = False

        print(f'--- Step {step} ---')


        eastGrid = []
        for i in range(0,gridH):
            eastGrid.append(copy.copy(row))

        southGrid = []
        for i in range(0,gridH):
            southGrid.append(copy.copy(row))

        for y in range(0,gridH):
            for x in range(0,gridW):
                if p1Grid[y][x] == '>':
                    n_x = (x + 1) % gridW
                    if p1Grid[y][n_x] == '.':
                        eastGrid[y][n_x] = '>'
                        didMove = True
                    else:
                        eastGrid[y][x] = '>'
                elif p1Grid[y][x] == 'v':
                    eastGrid[y][x] = 'v'


        for y in range(0,gridH):
            for x in range(0,gridW):
                if eastGrid[y][x] == 'v':
                    n_y = (y + 1) % gridH
                    if eastGrid[n_y][x] == '.':
                        southGrid[n_y][x] = 'v'
                        didMove = True
                    else:
                        southGrid[y][x] = 'v'
                elif eastGrid[y][x] == '>':
                    southGrid[y][x] = '>'
       
        step+=1
        p1Grid = southGrid

        for g in p1Grid:
            print("".join(g))


    print('--- Final ---')
    for g in p1Grid:
        print("".join(g))
    print(f'Result = {1}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:

    print(f'Result = {1}')

