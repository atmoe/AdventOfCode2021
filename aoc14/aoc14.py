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

template = inputFile.readline().strip()
inputFile.readline() # new line

rules = {}
for line in inputFile.readlines():
    ruleRe = re.match('^(\w+) -> (\w+)', line)
    rules[ruleRe.group(1)] = ruleRe.group(2)

inputFile.close()


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:

    numSteps = 10
    poly = copy.deepcopy(template)
    for i in range(1, numSteps+1):
        newPoly = poly[0]
        for idx in range(0,len(poly)-1):
            pair = f'{poly[idx]}{poly[idx+1]}'
            if pair not in rules:
                print('not found!')
                quit()
            
            newPoly += rules[pair] + poly[idx+1]
        poly = newPoly
        #print(len(poly))
        #print(poly)
    
    resultHash = {}
    for char in poly:
        if char not in resultHash:
            resultHash[char] = 1
        else:
            resultHash[char] += 1

    maxVal = 0
    minVal = 10000000000
    for r in resultHash:
        if resultHash[r] > maxVal:
            maxVal = resultHash[r]
        if resultHash[r] < minVal:
            minVal = resultHash[r]

    print(f'Result = {maxVal - minVal}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:

    resultHash = {}
    pairHash = {}
    for i in range(0, len(template)-1):
        pair = f'{template[i]}{template[i+1]}'
        if pair not in pairHash:
            pairHash[pair] = 1
        else:
            pairHash[pair] += 1

        if pair[0] not in resultHash:
            resultHash[pair[0]] = 1
        else:
            resultHash[pair[0]] += 1

    lastLet = template[-1]
    if lastLet not in resultHash:
        resultHash[lastLet] = 1
    else:
        resultHash[lastLet] += 1

    numSteps = 40
    for step in range(1,numSteps+1):
        newHash = {}
        for pair in pairHash:
            rule = rules[pair]
            count = pairHash[pair]
            newPair1 = pair[0] + rule
            newPair2 = rule + pair[1]

            if newPair1 not in newHash:
                newHash[newPair1] = count
            else:
                newHash[newPair1] += count

            if newPair2 not in newHash:
                newHash[newPair2] = count
            else:
                newHash[newPair2] += count

            if rule not in resultHash:
                resultHash[rule] = count
            else:
                resultHash[rule] += count

        pairHash = newHash


    maxVal = 0
    minVal = 100000000000000000000
    for r in resultHash:
        if resultHash[r] > maxVal:
            maxVal = resultHash[r]
        if resultHash[r] < minVal:
            minVal = resultHash[r]

    print(f'Result = {maxVal - minVal}')



#######################
#### Recursive ########
#######################
# Runs too long
def addToResult(r, letter):
    if letter not in r:
        r[letter] = 1
    else:
        r[letter] += 1

def goStep(l0, l1, step, results):
    pair = f'{l0}{l1}'
    if pair not in rules:
        print('not found!')
        quit()
    rule = rules[pair]

    addToResult(results, rule)

    if step+1 <= 40:
        goStep(l0, rule, step+1, results)
        goStep(rule, l1, step+1, results)

doPart2_recursive = False
if doPart2_recursive:

    resultHash = {}

    for i in range(0, len(template)-1):
        print('here')
        addToResult(resultHash, template[i])
        goStep(template[i], template[i+1], 1, resultHash)

    addToResult(resultHash, template[-1])

    maxVal = 0
    minVal = 10000000000
    for r in resultHash:
        if resultHash[r] > maxVal:
            maxVal = resultHash[r]
        if resultHash[r] < minVal:
            minVal = resultHash[r]

    print(f'Result2 = {maxVal - minVal}')




#######################
#### Linked List ######
#######################
# Runs too long
class PolyNode:
    def __init__(self, name):
        self.name = name
        self.neighbor = None

    def addNeighbor(self, neighbor):
        self.neighbor = neighbor


def printPoly(curr):
    print(curr.name, end='')
    while curr.neighbor != None:
        curr = curr.neighbor
        print(curr.name, end='')
    print()


doPart2_linkedlist= False
if doPart2_linkedlist:
    polyStart = PolyNode(template[0])
    curr = polyStart
    for idx in range(1,len(template)):
        node = PolyNode(template[idx])
        curr.addNeighbor(node)
        curr = curr.neighbor

    numSteps = 40
    for i in range(1, numSteps+1):
        print(f'Step {i}')
        #printPoly(polyStart)

        curr = polyStart
        while curr.neighbor != None:
            nbr  = curr.neighbor
            pair = f'{curr.name}{nbr.name}'

            if pair not in rules:
                print('not found!')
                quit()
            
            newNode = PolyNode(rules[pair])
            newNode.addNeighbor(nbr)
            curr.addNeighbor(newNode)

            #print('-------')
            #print(f'{curr.name} {curr.neighbor}')
            #print(f'{newNode.name} {newNode.neighbor}')


            curr = nbr

    resultHash = {}
    curr = polyStart
    while curr != None:
        if curr.name not in resultHash:
            resultHash[curr.name] = 1
        else:
            resultHash[curr.name] += 1
        curr = curr.neighbor

    maxVal = 0
    minVal = 10000000000
    for r in resultHash:
        if resultHash[r] > maxVal:
            maxVal = resultHash[r]
        if resultHash[r] < minVal:
            minVal = resultHash[r]

    print(f'Result = {maxVal - minVal}')


#######################
#### Depth First ######
#######################
# Tries to limit the number of arrays created by going depth first
# and only generating the string for pairs of initial input
# Runs too long
def getStr(s, numSteps):
    p = copy.deepcopy(s)
    for i in range(1, numSteps+1):
        print(i)
        newPoly = p[0]
        for idx in range(0,len(p)-1):
            pair = f'{p[idx]}{p[idx+1]}'
            if pair not in rules:
                print('not found!')
                quit()
            
            newPoly += rules[pair] + p[idx+1]
        p = newPoly
    return p

doPart2_depthfirst = False
if doPart2_depthfirst:
    resultHash = {}

    numSteps = 40
    poly = copy.deepcopy(template)
    for i in range(0, len(poly)-1):
        print(f'{i}/{len(poly)}')
        newStr = getStr(poly[i:i+2], numSteps)
        for char in newStr:
            if char not in resultHash:
                resultHash[char] = 1
            else:
                resultHash[char] += 1

    maxVal = 0
    minVal = 10000000000
    for r in resultHash:
        if resultHash[r] > maxVal:
            maxVal = resultHash[r]
        if resultHash[r] < minVal:
            minVal = resultHash[r]

    print(f'Result = {maxVal - minVal}')



