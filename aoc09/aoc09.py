#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = True
def dbgPrint(text):
    if dbgEn:
        print(text)

grid = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    row = []
    for p in line.strip():
        row.append(int(p))

    grid.append(row)

inputFile.close()

gridH = len(grid)
gridW = len(grid[0])

print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True

sumRisk = 0
if doPart1:
    for y,row in enumerate(grid):
        for x,val in enumerate(row):
            yCheck = False
            if y==0:
                if grid[y+1][x] > val:
                    yCheck = True
            elif y==gridH-1:
                if grid[y-1][x] > val:
                    yCheck = True
            else:
                if grid[y-1][x] > val and grid[y+1][x] > val:
                    yCheck = True

            xCheck = False
            if x==0:
                if grid[y][x+1] > val:
                    xCheck = True
            elif x==gridW-1:
                if grid[y][x-1] > val:
                    xCheck = True
            else:
                if grid[y][x-1] > val and grid[y][x+1] > val:
                    xCheck = True

            if xCheck and yCheck:
                sumRisk += (val+1)


    print(f'Result = {sumRisk}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:

    basins = []
    for y,row in enumerate(grid):
        for x,val in enumerate(row):
            yCheck = False
            if y==0:
                if grid[y+1][x] > val:
                    yCheck = True
            elif y==gridH-1:
                if grid[y-1][x] > val:
                    yCheck = True
            else:
                if grid[y-1][x] > val and grid[y+1][x] > val:
                    yCheck = True

            xCheck = False
            if x==0:
                if grid[y][x+1] > val:
                    xCheck = True
            elif x==gridW-1:
                if grid[y][x-1] > val:
                    xCheck = True
            else:
                if grid[y][x-1] > val and grid[y][x+1] > val:
                    xCheck = True

            if xCheck and yCheck:
                basins.append((y,x))
  
    basinSums = []
    for b in basins:
        basinHash = {}
        basinHash[b] = True

        curPoints = [b]

        basinSum = 0
        while len(curPoints) > 0:
            nxtPoints = []
            for c in curPoints:
                basinSum += 1

                coords = []
                coords.append((c[0], c[1]+1))
                coords.append((c[0], c[1]-1))
                coords.append((c[0]+1, c[1]))
                coords.append((c[0]-1, c[1]))

                for coord in coords:
                    x = coord[1]
                    y = coord[0]
                    if x < 0 or x > gridW-1:
                        continue
                    if y < 0 or y > gridH-1:
                        continue
                    if coord in basinHash.keys():
                        continue

                    if grid[y][x] != 9:
                        nxtPoints.append(coord)
                        basinHash[coord] = True

            curPoints = nxtPoints

        basinSums.append(basinSum)

    basinSums.sort()
    basinMul = 1
    for s in basinSums[-3:]:
        basinMul *= s


    print(f'Result = {basinMul}')


