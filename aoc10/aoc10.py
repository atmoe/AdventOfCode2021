#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text):
    if dbgEn:
        print(text)

lines = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    lines.append(line.strip())
inputFile.close()

def charIsOpen(char):
    return char == '(' or char == '[' or char == '{' or char == '<'

def charIsClose(char):
    return char == ')' or char == ']' or char == '}' or char == '>'

def charsOpenAndClose(o, c):
    return (o == '(' and c == ')') or \
           (o == '{' and c == '}') or \
           (o == '[' and c == ']') or \
           (o == '<' and c == '>')


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
incompleteLines = []
if doPart1:
    errorSum = 0
    for l in lines:
        corruptLine = False
        stack = []
        for char in l:
            if charIsOpen(char):
                stack.append(char)
            else:
                popChar = stack.pop()
                if not charsOpenAndClose(popChar, char):
                    dbgPrint(f'{popChar} did not expect {char}')
                    if char == ')': errorSum += 3
                    if char == ']': errorSum += 57
                    if char == '}': errorSum += 1197
                    if char == '>': errorSum += 25137
                    corruptLine = True
                    break

        if not corruptLine:
            incompleteLines.append(l)

    print(f'Result = {errorSum}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    scores = []
    for l in incompleteLines:
        stack = []
        score = 0
        for char in l:
            if charIsOpen(char):
                stack.append(char)
            else:
                popChar = stack.pop()
                if not charsOpenAndClose(popChar, char):
                    dbgPrint(f'Should not be here!!1')
                    break

        while len(stack) > 0:
            char = stack.pop()
            score *= 5    
            if char == '(':
                score += 1
            if char == '[':
                score += 2
            if char == '{':
                score += 3
            if char == '<':
                score += 4

        scores.append(score)

    scores.sort()

    print(f'Result = {scores[int(len(scores)/2)]}')


