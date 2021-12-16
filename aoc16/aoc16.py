#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text='', endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

binary = ''
inputFile = open(sys.argv[1], "r")
line = inputFile.readline().strip()

for h in line:
    if h == '0': binary+='0000'
    if h == '1': binary+='0001'
    if h == '2': binary+='0010'
    if h == '3': binary+='0011'
    if h == '4': binary+='0100'
    if h == '5': binary+='0101'
    if h == '6': binary+='0110'
    if h == '7': binary+='0111'
    if h == '8': binary+='1000'
    if h == '9': binary+='1001'
    if h == 'A': binary+='1010'
    if h == 'B': binary+='1011'
    if h == 'C': binary+='1100'
    if h == 'D': binary+='1101'
    if h == 'E': binary+='1110'
    if h == 'F': binary+='1111'
inputFile.close()

dbgPrint(binary)



# make this return the pointer to the end of the packet
def decodePkt(p, vSum):
    dbgPrint(f'--- Decoding Packet {p} ---')

    version = binary[p:p+3]
    pType   = binary[p+3:p+6]

    vSum[0] += int(version,2)

    dbgPrint(f'v = {version}')
    dbgPrint(f't = {pType}')

    if pType == '100':  # Literal
        curr = p+6
        indicator = binary[curr]
        literal = binary[curr+1:curr+1+4]
        while indicator != '0':
            curr += 5
            indicator = binary[curr]
            literal += binary[curr+1:curr+1+4]
        dbgPrint(f'literal = {int(literal,2)}')

        return (curr+5, int(literal,2))

    else:  # operator
        curr = p+6 # point to length ID
        lenID = binary[curr]

        results = []
        if lenID == '0': # count bits
            curr+=1 # point to start of length
            lenInBits = int(binary[curr:curr+15],2)
            dbgPrint(f'len = {lenInBits}')

            curr += 15

            decodedBits = 0
            while decodedBits < lenInBits:
                (nextPtr, r) = decodePkt(curr, vSum)
                results.append(r)
                decodedBits += nextPtr-curr
                curr = nextPtr

        else: # count packets
            curr+=1 # point to start of num pkts 
            lenInPkts = int(binary[curr:curr+11],2)
            dbgPrint(f'pkts = {lenInPkts}')

            curr += 11

            decodedPkts = 0
            while decodedPkts < lenInPkts:
                (nextPtr, r) = decodePkt(curr, vSum)
                results.append(r)
                decodedPkts += 1
                curr = nextPtr


        if pType == '000': # sum
            opResult = sum(results)

        if pType == '001': # product
            opResult = 1
            for r in results:
                opResult *= r

        if pType == '010': # minimum
            opResult = results[0]
            for r in results:
                if r < opResult:
                    opResult = r

        if pType == '011': # maximum
            opResult = results[0]
            for r in results:
                if r > opResult:
                    opResult = r

        if pType == '101': # GT
            if results[0] > results[1]:
                opResult = 1
            else:
                opResult = 0

        if pType == '110': # GT
            if results[0] < results[1]:
                opResult = 1
            else:
                opResult = 0

        if pType == '111': # EQ
            if results[0] == results[1]:
                opResult = 1
            else:
                opResult = 0

        return (curr, opResult)



print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    vSum = [0]
    (ptr, result) = decodePkt(0, vSum)

    print(f'Result = {vSum[0]}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    print(f'Result = {result}')

