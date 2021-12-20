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
alg = inputFile.readline().strip()
inputFile.readline()

img = []
for line in inputFile.readlines():
    img.append(line.strip())
inputFile.close()

dbgPrint(alg)
dbgPrint()
for i in img:
    dbgPrint(i)

def valToNum(val):
    num = 0
    power = 0
    for i in reversed(range(0,9)):
        if val[i] == '#':
            num += 2**power
        power+=1

    return num


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:

    lastImg = copy.deepcopy(img)
    numIters = 2
    lastImgW = len(img[0])
    lastImgH = len(img)
    oobVal = '.'
    for i in range(0,numIters):
        newImgW = len(lastImg[0]) + 2
        newImgH = len(lastImg) + 2

        newImg = [['x' for x in range(newImgW)] for y in range(newImgH)]

        for y in range(0,newImgH):
            for x in range(0,newImgW):
                coords = []

                coords.append( (x-1-1, y-1-1) )
                coords.append( (x  -1, y-1-1) )
                coords.append( (x+1-1, y-1-1) )
                coords.append( (x-1-1, y  -1) )
                coords.append( (x  -1, y  -1) )
                coords.append( (x+1-1, y  -1) )
                coords.append( (x-1-1, y+1-1) )
                coords.append( (x  -1, y+1-1) )
                coords.append( (x+1-1, y+1-1) )
                
                val = ''
                for c in coords:
                    if c[0] < 0 or c[0] > (lastImgW - 1):
                        val += oobVal
                        continue
                    if c[1] < 0 or c[1] > (lastImgH - 1):
                        val += oobVal
                        continue
                    
                    val += lastImg[c[1]][c[0]]

                newImg[y][x] = alg[valToNum(val)]

        dbgPrint('================')
        count = 0
        for n in newImg:
            dbgPrint("".join(n))
            for char in n:
                if char == '#':
                    count+=1

        lastImg = newImg
        lastImgW = newImgW
        lastImgH = newImgH
        oobVal = alg[valToNum(oobVal*9)]

    print(f'Result = {count}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    lastImg = copy.deepcopy(img)
    numIters = 50
    lastImgW = len(img[0])
    lastImgH = len(img)
    oobVal = '.'
    for i in range(0,numIters):
        newImgW = len(lastImg[0]) + 2
        newImgH = len(lastImg) + 2

        newImg = [['x' for x in range(newImgW)] for y in range(newImgH)]

        for y in range(0,newImgH):
            for x in range(0,newImgW):
                coords = []

                coords.append( (x-1-1, y-1-1) )
                coords.append( (x  -1, y-1-1) )
                coords.append( (x+1-1, y-1-1) )
                coords.append( (x-1-1, y  -1) )
                coords.append( (x  -1, y  -1) )
                coords.append( (x+1-1, y  -1) )
                coords.append( (x-1-1, y+1-1) )
                coords.append( (x  -1, y+1-1) )
                coords.append( (x+1-1, y+1-1) )
                
                val = ''
                for c in coords:
                    if c[0] < 0 or c[0] > (lastImgW - 1):
                        val += oobVal
                        continue
                    if c[1] < 0 or c[1] > (lastImgH - 1):
                        val += oobVal
                        continue
                    
                    val += lastImg[c[1]][c[0]]

                newImg[y][x] = alg[valToNum(val)]

        dbgPrint('================')
        count = 0
        for n in newImg:
            dbgPrint("".join(n))
            for char in n:
                if char == '#':
                    count+=1

        lastImg = newImg
        lastImgW = newImgW
        lastImgH = newImgH
        oobVal = alg[valToNum(oobVal*9)]

    print(f'Result = {count}')


