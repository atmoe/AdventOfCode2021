#!/usr/bin/python

import sys
import re
import copy
import math

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text='', endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

program = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    program.append(line.strip().split(' '))
inputFile.close()

#for instr in program:
#    print(instr)


class ALU:
    def __init__(self, prog):
        self.program = prog
        self.state = {}
        self.state['w'] = 0
        self.state['x'] = 0
        self.state['y'] = 0
        self.state['z'] = 0

    def printZ(self,z):
        zBuckets = []
        while z > 0:
            zBuckets.append(z%26)
            z=int(math.floor(z/26))

        print(zBuckets)

    def execute(self, inputVal):
        inputPtr = 0
        for instr in self.program:
            dbgPrint('----------------------')
            dbgPrint(instr)
            for s in self.state:
                dbgPrint(f'{s}:{self.state[s]} ', '')
            dbgPrint(' | ', '')

            arg1 = self.state[instr[1]]

            arg2 = -10000000000
            if len(instr) == 3:
                if instr[2] not in ['w', 'x', 'y', 'z']:
                    arg2 = int(instr[2])
                else:
                    arg2 = self.state[instr[2]]

            if instr[0] == 'inp':
                dbgPrint(f"new input(p={inputPtr} {inputVal[inputPtr]})\tz = {self.state['z']},\tx = {self.state['x']},\ty = {self.state['y']}")

                dbgPrint(f'inp {instr[1]} <= {inputVal[inputPtr]}')
                self.state[instr[1]] = int(inputVal[inputPtr])
                inputPtr+=1

                z = self.state['z']
                print(f"{inputPtr-1:2d}: z = {z}\t", end='')
                self.printZ(z)
                #if inputPtr==6:
                #    quit()


            elif instr[0] == 'add':
                dbgPrint(f'add {instr[1]} <= {arg1} + {arg2}')
                self.state[instr[1]] =  arg1 + arg2

            elif instr[0] == 'mul':
                dbgPrint(f'mul {instr[1]} <= {arg1} * {arg2}')

                self.state[instr[1]] = arg1 * arg2

            elif instr[0] == 'div':
                if arg2 == 0:
                    print('zero divide')
                    quit()

                dbgPrint(f'div {instr[1]} <= {arg1} / {arg2}')
                self.state[instr[1]] = int(math.floor(arg1 / arg2))

            elif instr[0] == 'mod':
                if arg1 < 0 or arg2 <= 0:
                    print('negative mod')
                    quit()

                dbgPrint(f'mod {instr[1]} <= {arg1} % {arg2}')
                self.state[instr[1]] = arg1 % arg2

            elif instr[0] == 'eql':
                dbgPrint(f'eql {instr[1]} <= {arg1} == {arg2}')
                if arg1 == arg2:
                    self.state[instr[1]] = 1
                else:
                    self.state[instr[1]] = 0
            else:
                print('invalid instruction!')
                quit()

        z = self.state['z']
        print(f"{inputPtr:2d}: z = {z}\t", end='')
        self.printZ(z)
        #print('-------------')
        #for s in self.state:
        #    print(f'{s} = {self.state[s]}')

        return self.state['z']

    def reset(self):
        self.state['w'] = 0
        self.state['x'] = 0
        self.state['y'] = 0
        self.state['z'] = 0

print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    alu = ALU(program)

    # I just brute forced it
    result = alu.execute('39999698799429')

    print(f'Result = {result}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    alu = ALU(program)

    # I just brute forced it by hantd
    result = alu.execute('18116121134117')

    print(f'Result = {result}')

