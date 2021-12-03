#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

entries = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    entries.append(line.rstrip('\n'))
inputFile.close()


print("------------------")
print("---- PART 1 ------")
print("------------------")

gamma   = 0
epsilon = 0
index = 0
for idx in reversed(range(0, len(entries[0]))):
    zeros = 0
    ones  = 0
    for n in range(0, len(entries)):
        if entries[n][idx] == '0':
            zeros += 1
        else:
            ones += 1

    if ones > zeros:
        gamma += 2**index
    else:
        epsilon += 2**index

    index+=1

print(f'g = {gamma}')
print(f'e = {epsilon}')

print(f'result = {gamma*epsilon}')

print("------------------")
print("---- PART 2 ------")
print("------------------")

oxyEntries = copy.deepcopy(entries)
idx = 0
while len(oxyEntries) > 1:
    zeros = 0
    ones  = 0
    for e in oxyEntries:
        if e[idx] == '0':
            zeros += 1
        else:
            ones += 1

    nextOxyEntries = []
    for e in oxyEntries:
        if zeros > ones and e[idx] == '0':
            nextOxyEntries.append(e)
        elif zeros <= ones and e[idx] == '1':
            nextOxyEntries.append(e)

    oxyEntries = copy.deepcopy(nextOxyEntries)

    idx+=1
print(f'oxy = {oxyEntries[0]}')

co2Entries = copy.deepcopy(entries)
idx = 0
while len(co2Entries) > 1:
    zeros = 0
    ones  = 0
    for e in co2Entries:
        if e[idx] == '0':
            zeros += 1
        else:
            ones += 1

    nextCO2Entries = []
    for e in co2Entries:
        if zeros <= ones and e[idx] == '0':
            nextCO2Entries.append(e)
        elif zeros > ones and e[idx] == '1':
            nextCO2Entries.append(e)

    co2Entries = copy.deepcopy(nextCO2Entries)

    idx+=1
print(f'co2 = {co2Entries[0]}')

co2 = 0
oxy = 0
for i in range(0,len(co2Entries[0])):
    idx = len(co2Entries[0]) - i - 1
    if oxyEntries[0][idx] == '1':
        oxy += 2**i
    if co2Entries[0][idx] == '1':
        co2 += 2**i

print(oxy)
print(co2)

print(co2*oxy)


print(f'')
