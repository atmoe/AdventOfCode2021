#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text='', endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

class CubeP1:
    def __init__(self, x0, x1, y0, y1, z0, z1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1

        self.pointSet = set()

        if x0 > 50 or x0 < -50 or \
           y0 > 50 or y0 < -50 or \
           z0 > 50 or z0 < -50 or \
           x1 > 50 or x1 < -50 or \
           y1 > 50 or y1 < -50 or \
           z1 > 50 or z1 < -50:
               return

        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                for z in range(z0, z1+1):
                    self.pointSet.add( (x, y, z) )

class CubeP2:
    def __init__(self, x0, x1, y0, y1, z0, z1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1
        self.xDim = (x1 - x0) + 1
        self.yDim = (y1 - y0) + 1
        self.zDim = (z1 - z0) + 1

    def overlapsWith(self, c):

        noOverlap = self.x0 > c.x1 or \
                    self.x1 < c.x0 or \
                    self.y0 > c.y1 or \
                    self.y1 < c.y0 or \
                    self.z0 > c.z1 or \
                    self.z1 < c.z0

        return not noOverlap

    def isInside(self, c):

        xInside = c.x0 <= self.x0 and self.x1 <= c.x1
        yInside = c.y0 <= self.y0 and self.y1 <= c.y1
        zInside = c.z0 <= self.z0 and self.z1 <= c.z1

        return xInside and yInside and zInside

    def largestDim(self):
        if self.xDim >= self.yDim and self.xDim >= self.zDim:  return 0
        if self.yDim >= self.xDim and self.yDim >= self.zDim:  return 1
        if self.zDim >= self.yDim and self.zDim >= self.xDim:  return 2

        return 0

    def printMe(self):
        dbgPrint(f'x={self.x0}..{self.x1}, y={self.y0}..{self.y1}, z={self.z0}..{self.z1} (vol = {self.volume()})')

    def volume(self):
        return self.xDim * self.yDim * self.zDim

commands = []
cubesP1 = []
cubesP2 = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    cubeRe = re.match('(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', line)
    cubeP1 = CubeP1(int(cubeRe.group(2)), int(cubeRe.group(3)), \
                    int(cubeRe.group(4)), int(cubeRe.group(5)), \
                    int(cubeRe.group(6)), int(cubeRe.group(7)))
    cubesP1.append(cubeP1)


    cubeP2 = CubeP2(int(cubeRe.group(2)), int(cubeRe.group(3)), \
                    int(cubeRe.group(4)), int(cubeRe.group(5)), \
                    int(cubeRe.group(6)), int(cubeRe.group(7)))
    cubesP2.append(cubeP2)

    commands.append(cubeRe.group(1))

inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:

    onPoints = set()
    for idx, cube in enumerate(cubesP1):
        command = commands[idx]
        if command == 'on':
            onPoints = onPoints | cube.pointSet
        elif command == 'off':
            onPoints = onPoints - cube.pointSet


    print(f'Result = {len(onPoints)}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:

    cubes = []
    for idx, c0 in enumerate(cubesP2):
        dbgPrint(f'--- idx = {idx} ---')
        if dbgEn: c0.printMe()
        newCubes = []
        for c1 in cubes:
            if c0.overlapsWith(c1):
                choppedCubes = [c1]

                # x-left
                x0ChoppedCubes = []
                for cube in choppedCubes:
                    if cube.xDim == 1:
                        x0ChoppedCubes.append(cube)
                        continue

                    if cube.x0 <= c0.x0 and cube.x1 >= c0.x0:
                        cube0 = CubeP2(cube.x0, c0.x0-1, cube.y0, cube.y1, cube.z0, cube.z1)
                        cube1 = CubeP2(c0.x0,   cube.x1, cube.y0, cube.y1, cube.z0, cube.z1)
                        x0ChoppedCubes.append(cube0)
                        x0ChoppedCubes.append(cube1)
                    else:
                        x0ChoppedCubes.append(cube)

                # x-right
                x1ChoppedCubes = []
                for cube in x0ChoppedCubes:
                    if cube.xDim == 1:
                        x1ChoppedCubes.append(cube)
                        continue

                    if cube.x0 <= c0.x1 and cube.x1 >= c0.x1:
                        cube0 = CubeP2(cube.x0, c0.x1,   cube.y0, cube.y1, cube.z0, cube.z1)
                        cube1 = CubeP2(c0.x1+1, cube.x1, cube.y0, cube.y1, cube.z0, cube.z1)
                        x1ChoppedCubes.append(cube0)
                        x1ChoppedCubes.append(cube1)


                        if cube0.x0 > cube0.x1:
                            print('Error:')
                            c0.printMe()
                            cube.printMe()
                            cube0.printMe()
                            quit()
                    else:
                        x1ChoppedCubes.append(cube)


                # y-left
                y0ChoppedCubes = []
                for cube in x1ChoppedCubes:
                    if cube.yDim == 1:
                        y0ChoppedCubes.append(cube)
                        continue

                    if cube.y0 <= c0.y0 and cube.y1 >= c0.y0:
                        cube0 = CubeP2(cube.x0, cube.x1, cube.y0, c0.y0-1, cube.z0, cube.z1)
                        cube1 = CubeP2(cube.x0, cube.x1, c0.y0, cube.y1,   cube.z0, cube.z1)
                        y0ChoppedCubes.append(cube0)
                        y0ChoppedCubes.append(cube1)
                    else:
                        y0ChoppedCubes.append(cube)

                # y-right
                y1ChoppedCubes = []
                for cube in y0ChoppedCubes:
                    if cube.yDim == 1:
                        y1ChoppedCubes.append(cube)
                        continue

                    if cube.y0 <= c0.y1 and cube.y1 >= c0.y1:
                        cube0 = CubeP2(cube.x0, cube.x1, cube.y0, c0.y1,   cube.z0, cube.z1)
                        cube1 = CubeP2(cube.x0, cube.x1, c0.y1+1, cube.y1, cube.z0, cube.z1)
                        y1ChoppedCubes.append(cube0)
                        y1ChoppedCubes.append(cube1)
                    else:
                        y1ChoppedCubes.append(cube)

                # z-left
                z0ChoppedCubes = []
                for cube in y1ChoppedCubes:
                    if cube.zDim == 1:
                        z0ChoppedCubes.append(cube)
                        continue

                    if cube.z0 <= c0.z0 and cube.z1 >= c0.z0:
                        cube0 = CubeP2(cube.x0, cube.x1, cube.y0, cube.y1, cube.z0, c0.z0-1)
                        cube1 = CubeP2(cube.x0, cube.x1, cube.y0, cube.y1, c0.z0,   cube.z1)
                        z0ChoppedCubes.append(cube0)
                        z0ChoppedCubes.append(cube1)
                    else:
                        z0ChoppedCubes.append(cube)

                # z-right
                z1ChoppedCubes = []
                for cube in z0ChoppedCubes:
                    if cube.zDim == 1:
                        z1ChoppedCubes.append(cube)
                        continue

                    if cube.z0 <= c0.z1 and cube.z1 >= c0.z1:
                        cube0 = CubeP2(cube.x0, cube.x1, cube.y0, cube.y1, cube.z0, c0.z1)
                        cube1 = CubeP2(cube.x0, cube.x1, cube.y0, cube.y1, c0.z1+1, cube.z1)
                        z1ChoppedCubes.append(cube0)
                        z1ChoppedCubes.append(cube1)
                    else:
                        z1ChoppedCubes.append(cube)

                for cube in z1ChoppedCubes:
                    if not cube.isInside(c0):
                        newCubes.append(cube)

            else:
                newCubes.append(c1)

        cubes = newCubes

        if commands[idx] == 'on':
            cubes.append(c0)

    totalLit = 0
    for c in cubes:
        totalLit += c.volume()

    print(f'Result = {totalLit}')
