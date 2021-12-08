#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = True
def dbgPrint(text):
    if dbgEn:
        print(text)

displayPatterns = []
displayOutputs= []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    temp = line.strip().split(' | ')
    patterns = temp[0].split(' ')
    outputs  = temp[1].split(' ')
    displayPatterns.append(patterns)
    displayOutputs.append(outputs)

inputFile.close()

masks = [0]*10
masks[0] = [1, 1, 1, 0, 1, 1, 1]
masks[1] = [0, 0, 1, 0, 0, 1, 0]
masks[2] = [1, 0, 1, 1, 1, 0, 1]
masks[3] = [1, 0, 1, 1, 0, 1, 1]
masks[4] = [0, 1, 1, 1, 0, 1, 0]
masks[5] = [1, 1, 0, 1, 0, 1, 1]
masks[6] = [1, 1, 0, 1, 1, 1, 1]
masks[7] = [1, 0, 1, 0, 0, 1, 0]
masks[8] = [1, 1, 1, 1, 1, 1, 1]
masks[9] = [1, 1, 1, 1, 0, 1, 1]

print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    instances = 0

    for o in displayOutputs:
        for d in o:
            if len(d) == 2: # must be 1
                instances += 1
            elif len(d) == 3: # must be 7
                instances += 1
            elif len(d) == 4: # must be 4
                instances += 1
            elif len(d) == 7: # must be 8
                instances += 1

    print(f'Result = {instances}')

def intersect(cur, nxt):
    output = []
    for c in cur:
        if c in nxt:
            output.append(c)

    return output

def remove(cur, vals):
    for v in vals:
        if v in cur:
            cur.remove(v)

    return cur


print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:

    sumOfDisplays = 0
    for i in range (0, len(displayPatterns)):
        segments = {}
        segments['a'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        segments['b'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        segments['c'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        segments['d'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        segments['e'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        segments['f'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        segments['g'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

        for r in displayPatterns[i]:
            if len(r) == 2: # must be 1
                segments['c'] = intersect(segments['c'], list(r))
                segments['f'] = intersect(segments['f'], list(r))

                segments['a'] = remove(segments['a'], list(r))
                segments['b'] = remove(segments['b'], list(r))
                segments['d'] = remove(segments['d'], list(r))
                segments['e'] = remove(segments['e'], list(r))
                segments['g'] = remove(segments['g'], list(r))

            elif len(r) == 3: # must be 7
                segments['a'] = intersect(segments['a'], list(r))
                segments['c'] = intersect(segments['c'], list(r))
                segments['f'] = intersect(segments['f'], list(r))

                segments['b'] = remove(segments['b'], list(r))
                segments['d'] = remove(segments['d'], list(r))
                segments['e'] = remove(segments['e'], list(r))
                segments['g'] = remove(segments['g'], list(r))

            elif len(r) == 4: # must be 4
                segments['b'] = intersect(segments['b'], list(r))
                segments['c'] = intersect(segments['c'], list(r))
                segments['d'] = intersect(segments['d'], list(r))
                segments['f'] = intersect(segments['f'], list(r))


                segments['a'] = remove(segments['a'], list(r))
                segments['e'] = remove(segments['e'], list(r))
                segments['g'] = remove(segments['g'], list(r))

            elif len(r) == 7: # must be 8
                segments['a'] = intersect(segments['a'], list(r))
                segments['b'] = intersect(segments['b'], list(r))
                segments['c'] = intersect(segments['c'], list(r))
                segments['d'] = intersect(segments['d'], list(r))
                segments['e'] = intersect(segments['e'], list(r))
                segments['f'] = intersect(segments['f'], list(r))
                segments['g'] = intersect(segments['g'], list(r))


        reps = {}
        remainingPatterns = copy.deepcopy(displayPatterns[i])
        while len(remainingPatterns) > 0:
            nextPatterns = []
            for d in remainingPatterns:
                if len(d) == 2:
                    reps[d] = 1
                elif len(d) == 3:
                    reps[d] = 7
                elif len(d) == 4:
                    reps[d] = 4
                elif len(d) == 7:
                    reps[d] = 8
                else:
                    possibleMasks = []
                    for letter in d:
                        possibleWires = []
                        for s in segments:
                            if letter in segments[s]:
                                possibleWires.append(s)
    
                        masksNext = []
                        if len(possibleMasks) == 0:
                            masksNext = list(possibleWires)
                        else:
                            for p in possibleMasks:
                                for w in possibleWires:
                                    masksNext.append(p + w)
    
                        possibleMasks = copy.deepcopy(masksNext)
    
                    possibleNums = {}
                    for p in possibleMasks:
                        mask = [0]*7
                        for let in p:
                            if let == 'a': mask[0] =1
                            if let == 'b': mask[1] =1
                            if let == 'c': mask[2] =1
                            if let == 'd': mask[3] =1
                            if let == 'e': mask[4] =1
                            if let == 'f': mask[5] =1
                            if let == 'g': mask[6] =1
    
                        for m in range(0, len(masks)):
                            if mask == masks[m] and m not in reps.values():
                                possibleNums[m] = True
    
                    if len(possibleNums) == 1:
                        reps[d] = list(possibleNums.keys())[0]
                    else:
                        nextPatterns.append(d)
    
                
            remainingPatterns = copy.deepcopy(nextPatterns) 

        value = 0
        for o in displayOutputs[i]:
            for r in reps.keys():
                if "".join(sorted(o)) == "".join(sorted(r)):
                    value += reps[r]
            value *= 10
        value = int(value/10)

        sumOfDisplays += value


    print(f'Result = {sumOfDisplays}')

