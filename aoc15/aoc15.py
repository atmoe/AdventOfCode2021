#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text='', endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

class Node:
    def __init__(self, cost):
        self.dist    = 100000000000
        self.cost    = cost
        self.visited = False
        self.neighbors = []

    def addNeighbor(self, n):
        self.neighbors.append(n)

    def removeNeighbors(self):
        self.neighbors = []

grid = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    row = []
    for r in list(line.strip()):
        node = Node(int(r))
        row.append(node)
    grid.append(row)
inputFile.close()


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    p1Grid = copy.deepcopy(grid)
    gridW = len(grid[0])
    gridH = len(grid)
    for y in range(0, gridH):
        for x in range(0, gridW):
            nbrs = []
            nbrs.append((x+1, y))
            nbrs.append((x-1, y))
            nbrs.append((x, y+1))
            nbrs.append((x, y-1))
            for n in nbrs:
                if n[0] < 0 or n[0] >= gridW:
                    continue
                if n[1] < 0 or n[1] >= gridH:
                    continue
    
                p1Grid[y][x].addNeighbor(p1Grid[n[1]][n[0]])


    currNode = p1Grid[0][0]
    currNode.dist = 0

    while not p1Grid[gridH-1][gridW-1].visited:

        for n in currNode.neighbors:
            if n.visited:
                continue

            if n.dist > currNode.dist + n.cost:
                n.dist = currNode.dist + n.cost

        currNode.visited = True

        tmpDist = 100000000000
        for y in range(0, gridH):
            for x in range(0, gridW):
                if p1Grid[y][x].visited:
                    continue
                else:
                    if p1Grid[y][x].dist < tmpDist:
                        currNode = p1Grid[y][x]
                        tmpDist = currNode.dist

    print(f'Result = {p1Grid[gridH-1][gridW-1].dist}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    p2Grid = []
    for yBlock in range(0,5):
        for xBlock in range(0,5):
            scale = xBlock+yBlock
            gridBlock = copy.deepcopy(grid)
            for y in range(0, gridH):
                for x in range(0, gridW):
                    gridBlock[y][x].cost += scale
                    if gridBlock[y][x].cost > 9:
                        gridBlock[y][x].cost -= 9

            
            y = gridH * yBlock
            for g in gridBlock:
                if xBlock == 0:
                    p2Grid.append(g)
                else:
                    p2Grid[y] = p2Grid[y] + g

                y+=1

    gridH = len(p2Grid)
    gridW = len(p2Grid[0])

    if dbgEn:
        for g in p2Grid:
            for n in g:
                print(n.cost, end='')
            print()


    # redo neighbors
    for y in range(0, gridH):
        for x in range(0, gridW):
            nbrs = []
            nbrs.append((x+1, y))
            nbrs.append((x-1, y))
            nbrs.append((x, y+1))
            nbrs.append((x, y-1))

            p2Grid[y][x].removeNeighbors()
            for n in nbrs:
                if n[0] < 0 or n[0] >= gridW:
                    continue
                if n[1] < 0 or n[1] >= gridH:
                    continue
    
                p2Grid[y][x].addNeighbor(p2Grid[n[1]][n[0]])

    nodes = set()
    currNode = p2Grid[0][0]
    currNode.dist = 0
    nodes.add(currNode)

    while not p2Grid[gridH-1][gridW-1].visited:

        for n in currNode.neighbors:
            if n.visited:
                continue

            if n.dist == 100000000000:
                nodes.add(n)

            if n.dist > currNode.dist + n.cost:
                n.dist = currNode.dist + n.cost

        currNode.visited = True
        nodes.remove(currNode)

        tmpDist = 100000000000
        for n in nodes:
            if n.dist < tmpDist:
                currNode = n
                tmpDist = currNode.dist

    print(f'Result = {p2Grid[gridH-1][gridW-1].dist}')


