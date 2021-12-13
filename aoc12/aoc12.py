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
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def addNeighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

arcs = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    arcRe = re.match('(\w*)-(\w*)', line)
    arcs.append((arcRe.group(1), arcRe.group(2)))
inputFile.close()

# Create Graph
nodes = {}
for a in arcs:
    startName = a[0]
    endName = a[1]

    if startName not in nodes:
        nodes[startName] = Node(startName)
    if endName not in nodes:
        nodes[endName] = Node(endName)

    start = nodes[startName]
    end   = nodes[endName]

    start.addNeighbor(end)
    end.addNeighbor(start)

for n in nodes:
    dbgPrint(f'{nodes[n].name} -> ', '')
    for nei in nodes[n].neighbors:
        dbgPrint(f'{nei.name}, ', '')
    dbgPrint()


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    paths = [[nodes['start']]]
    fullPaths = []

    while len(paths) > 0:
        p = paths.pop()

        for n in p[-1].neighbors:
            newPath = list(p)
            newPath.append(n)
            if n.name == 'end':
                fullPaths.append(newPath)
            elif n.name == 'start':
                continue
            elif n.name.islower():
                if n not in p:
                    paths.append(newPath)
            else:
                paths.append(newPath)
                
                

    for p in fullPaths:
        for n in p:
            dbgPrint(f'{n.name} ->', '')
        dbgPrint()

    print(f'Result = {len(fullPaths)}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    paths = [[nodes['start']]]
    fullPaths = []

    while len(paths) > 0:
        p = paths.pop()

        for n in p[-1].neighbors:
            newPath = list(p)
            newPath.append(n)
            if n.name == 'end':
                fullPaths.append(newPath)
            elif n.name == 'start':
                continue
            elif n.name.islower():
                if n not in p:
                    paths.append(newPath)
                elif p[0].name == 'Dups':
                    continue
                else:
                    dups = Node('Dups')
                    newPath.insert(0, dups)
                    paths.append(newPath)

            else:
                paths.append(newPath)
                
                

    for p in fullPaths:
        for n in p:
            dbgPrint(f'{n.name} ->', '')
        dbgPrint()

    print(f'Result = {len(fullPaths)}')


