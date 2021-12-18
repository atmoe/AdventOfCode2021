#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text='', endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

numbers = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    number = []
    for char in line.strip():
        if char == ',':
            continue
        elif char == '[' or char == ']':
            number.append(char)
        else:
            number.append(int(char))

    numbers.append(number)

inputFile.close()

def add(n1, n2):
    return ['['] + n1 + n2 + [']']

def explode(n, idx): # idx points at left parenthesis
    lVal = n[idx+1] 
    rVal = n[idx+2] 

    for i in range(idx+4,len(n)):
        if n[i] != ']' and n[i] != '[':
            n[i] += rVal
            break

    for i in range(idx-1, -1, -1):
        if n[i] != ']' and n[i] != '[':
            n[i] += lVal
            break

    return n[0:idx] + [0] + n[idx+4:]

def split(n, idx): # idx points at the number to be split
    lVal = n[idx] >> 1
    rVal = (n[idx] + 1) >> 1

    return n[0:idx] + ['[', lVal, rVal, ']'] + n[idx+1:]


def getMagnitude(n):
    dbgPrint('--- getting magnitude ---')
    newN = copy.deepcopy(n)
    while len(newN) > 1:
        dbgPrint(newN)
        for i in range(0,len(curr_num)):
            if newN[i] == ']':
                val = newN[i-2]*3 + newN[i-1]*2

                if len(newN) == 4:
                    newN = [val]
                    break

                nextN = []
                # construct start
                if i-4 == 0: # this value is becoming first number
                    nextN = [newN[0]]
                else: 
                    nextN = newN[0:i-3]

                nextN += [val] + newN[i+1:]

                newN = nextN
                # construct end
                #newN = newN[0:i-4] + [val] + newN[i+1:]

                break

    return newN[0]

print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    curr_num = numbers[0]
    for n in numbers[1:]:
        dbgPrint(curr_num)
        curr_num = add(curr_num, n)

        numModified = True
        while numModified:
            numModified = False
            
            # Check for explodes first
            parenDepth = 0
            for i in range(0,len(curr_num)):
                if curr_num[i] == '[':
                    parenDepth += 1
                if curr_num[i] == ']':
                    parenDepth -= 1
    
                if parenDepth == 5:
                    curr_num = explode(curr_num, i)
                    numModified = True
                    dbgPrint(curr_num)
                    break
    
            if numModified:
                continue
    
            for i in range(0,len(curr_num)):
                if curr_num[i] == '[':
                    continue
                elif curr_num[i] == ']':
                    continue
                elif curr_num[i] > 9:
                    curr_num = split(curr_num, i)
                    numModified = True
                    dbgPrint(curr_num)
                    break
    
            if numModified:
                continue
    
    dbgPrint(curr_num)
    mag = getMagnitude(curr_num)
    print(f'Result = {mag}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    maxMag = 0
    
    for n1 in numbers:
        for n2 in numbers:
            if n1 == n2:
                continue

            curr_num = add(n1, n2)
    
            numModified = True
            while numModified:
                numModified = False
                
                # Check for explodes first
                parenDepth = 0
                for i in range(0,len(curr_num)):
                    if curr_num[i] == '[':
                        parenDepth += 1
                    if curr_num[i] == ']':
                        parenDepth -= 1
        
                    if parenDepth == 5:
                        curr_num = explode(curr_num, i)
                        numModified = True
                        dbgPrint(curr_num)
                        break
        
                if numModified:
                    continue
        
                for i in range(0,len(curr_num)):
                    if curr_num[i] == '[':
                        continue
                    elif curr_num[i] == ']':
                        continue
                    elif curr_num[i] > 9:
                        curr_num = split(curr_num, i)
                        numModified = True
                        dbgPrint(curr_num)
                        break
        
                if numModified:
                    continue
        
            dbgPrint(curr_num)
            mag = getMagnitude(curr_num)
            if mag > maxMag:
                maxMag = mag
    

    print(f'Result = {maxMag}')


