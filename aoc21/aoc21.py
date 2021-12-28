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
for line in inputFile.readlines():
    break
inputFile.close()


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = False
if doPart1:
    p1_pos = 7 - 1
    p2_pos = 1 - 1
    p1_score = 0
    p2_score = 0

    turn = 1
    dieVal = 0
    num_rolls = 0
    while p1_score < 1000 and p2_score < 1000 :

        roll = 0
        for i in range(0,3):
            dieVal+=1
            roll+=dieVal

        num_rolls += 3

        if turn == 1:
            p1_pos += roll
            p1_pos = p1_pos % 10

            p1_score += (p1_pos+1)

            print(f'P1: {p1_pos+1}  {roll}  {p1_score}')
            turn = 2
        else:
            p2_pos += roll
            p2_pos = p2_pos % 10

            p2_score += (p2_pos + 1)

            print(f'P2: {p2_pos+1}  {roll}  {p2_score}')
            turn = 1

    result = num_rolls
    if p2_score >= 1000:
        result *= p1_score
    elif p1_score >= 1000:
        result *= p2_score


    print(f'Result = {result}')

print("------------------")
print("---- PART 2 ------")
print("------------------")

def playTurn(p1, p2, turn, p1_wins, p2_wins):
    for r0 in [1, 2, 3]:
        for r1 in [1, 2, 3]:
            for r2 in [1, 2, 3]:
                if turn == 1:
                    roll = r0+r1+r2
                    p1_pos   = (p1[0] + roll) % 10
                    p1_score = p1[1] + p1_pos + 1
                    newP1 = (p1_pos, p1_score)

                    if p1_score >= 21:
                        p1_wins[0] += 1
                        if p1_wins[0] % 1000000 == 0:
                            print(p1_wins)
                    else:
                        playTurn(newP1, p2, 2, p1_wins, p2_wins)

                elif turn == 2:
                    roll = r0+r1+r2
                    p2_pos   = (p2[0] + roll) % 10
                    p2_score = p2[1] + p2_pos + 1
                    newP2 = (p2_pos, p2_score)
                    
                    if p2_score >= 21:
                        p2_wins[0] += 1
                    else:
                        playTurn(p1, newP2, 1, p2_wins, p2_wins)

doPart2 = True
if doPart2:
    p1_wins = [0]
    p2_wins = [0]
   
    p1 = (4-1,0)
    p2 = (8-1,0)
    
    playTurn(p1, p2, 1, p1_wins, p2_wins)

    print(f'Result = {p1_wins}')
    print(f'Result = {p2_wins}')
