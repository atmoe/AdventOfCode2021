#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = True
def dbgPrint(text='', endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

inputFile = open(sys.argv[1], "r")
inputFile.readline()
inputFile.readline()
firstRow = inputFile.readline().rstrip()
secondRow = inputFile.readline().rstrip()
inputFile.close()

podInit = []
podInit.append((firstRow[3], 3, 2))
podInit.append((firstRow[5], 5, 2))
podInit.append((firstRow[7], 7, 2))
podInit.append((firstRow[9], 9, 2))
podInit.append((secondRow[3], 3, 3))
podInit.append((secondRow[5], 5, 3))
podInit.append((secondRow[7], 7, 3))
podInit.append((secondRow[9], 9, 3))

class Pod:
    def __init__(self, name, x, y):
        self.n = name
        self.x = x
        self.y = y

    def __str__(self):
        return f'[{self.n}, {self.x}, {self.y}]'


class GameBoardP1:
    def __init__(self, pods):
        self.energy = 0

        self.pods = []
        for p in pods:
            self.pods.append(Pod(p[0], p[1], p[2]))

        self.board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                      ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                      ['#', '#', '#', '.', '#', '.', '#', '.', '#', '.', '#', '#', '#'],
                      [' ', ' ', '#', '.', '#', '.', '#', '.', '#', '.', '#', ' ', ' '],
                      [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ']]

        for p in self.pods:
            self.board[p.y][p.x] = p.n

    def organized(self):
        if self.board[2][3] != 'A': return False
        if self.board[3][3] != 'A': return False
        if self.board[2][5] != 'B': return False
        if self.board[3][5] != 'B': return False
        if self.board[2][7] != 'C': return False
        if self.board[3][7] != 'C': return False
        if self.board[2][9] != 'D': return False
        if self.board[3][9] != 'D': return False
        return True


    def printBoard(self):
        for b in self.board:
            print("".join(b))

    def positionHash(self):
        hashStr = ""
        #for p in self.pods:
        #    hashStr += "_"
        #    hashStr += str(p.x)
        #    hashStr += "_"
        #    hashStr += str(p.y)
        #    hashStr += "_"
        hashStr += "".join(self.board[1])
        hashStr += "".join(self.board[2])
        hashStr += "".join(self.board[3])
        return hashStr


    def pathIsClear(self, start, end):
        sx = start[0]
        sy = start[1]
        ex = end[0]
        ey = end[1]

        pathClear = True

        if sy == 1: # hall -> room
            curY=sy
            curX=sx

            # move to room entry
            if sx > ex:
                while sx > ex:
                    sx-=1
                    if not self.board[sy][sx] == '.':
                        pathClear = False

            elif sx < ex:
                while sx < ex:
                    sx+=1
                    if not self.board[sy][sx] == '.':
                        pathClear = False

            if not pathClear: return False

            # move into room
            while sy < ey:
                sy+=1
                if not self.board[sy][sx] == '.':
                    pathClear = False

            return pathClear

        else:
            # move out of room
            while sy > ey:
                sy-=1
                if not self.board[sy][sx] == '.':
                    pathClear = False

            if not pathClear: return False

            # move to hall position
            if sx > ex:
                while sx > ex:
                    sx-=1
                    if not self.board[sy][sx] == '.':
                        pathClear = False

            elif sx < ex:
                while sx < ex:
                    sx+=1
                    if not self.board[sy][sx] == '.':
                        pathClear = False

            return pathClear


    def possibleMoves(self):
        # move = (podNum, newX, newY)
        moves = []
        for podNum, p in enumerate(self.pods):
            if   p.n == 'A': roomIdx = 3
            elif p.n == 'B': roomIdx = 5
            elif p.n == 'C': roomIdx = 7
            elif p.n == 'D': roomIdx = 9

            st = (p.x, p.y)

            # in Hall
            if p.y == 1:
                if self.board[2][roomIdx] == '.' and self.board[3][roomIdx] == '.':
                    if self.pathIsClear(st, (roomIdx,3) ): moves.append([podNum, p.n, st, (roomIdx, 3)])
                elif self.board[2][roomIdx] == '.' and self.board[3][roomIdx] == p.n:
                    if self.pathIsClear(st, (roomIdx,2) ): moves.append([podNum, p.n, st, (roomIdx, 2)])
            

            else: # in Room
                #if in correct room but blocking incorrect
                blocking = p.x == roomIdx and p.y == 2 and self.board[3][roomIdx] != p.n
                needMove = blocking or p.x != roomIdx

                if needMove: 
                    if self.pathIsClear(st, ( 1,1) ): moves.append([podNum, p.n, st, (1, 1)]) 
                    if self.pathIsClear(st, ( 2,1) ): moves.append([podNum, p.n, st, (2, 1)]) 
                    if self.pathIsClear(st, ( 4,1) ): moves.append([podNum, p.n, st, (4, 1)]) 
                    if self.pathIsClear(st, ( 6,1) ): moves.append([podNum, p.n, st, (6, 1)]) 
                    if self.pathIsClear(st, ( 8,1) ): moves.append([podNum, p.n, st, (8, 1)]) 
                    if self.pathIsClear(st, (10,1) ): moves.append([podNum, p.n, st, (10, 1)]) 
                    if self.pathIsClear(st, (11,1) ): moves.append([podNum, p.n, st, (11, 1)]) 

        return moves
                    


    def move(self, podNum, newPos):
        p = self.pods[podNum]
        self.board[p.y][p.x] = '.'
        
        if p.n == 'A': scale = 1
        if p.n == 'B': scale = 10
        if p.n == 'C': scale = 100
        if p.n == 'D': scale = 1000

        self.energy += scale * (abs(p.x - newPos[0]) + abs(p.y - newPos[1]))

        # Update
        p.x = newPos[0]
        p.y = newPos[1]
        self.board[p.y][p.x] = p.n

        return



print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    boards = [GameBoardP1(podInit)]
    boardEnergies = {}

    boardEnergies[boards[0].positionHash()] = boards[0].energy

    count = 0
    while len(boards) > 0:
        print("-------------------------------------------")
        print(len(boards))

        minBoard = boards.pop()

        minBoard.printBoard()
        print(minBoard.energy)
        if minBoard.organized():
            break

        moves = minBoard.possibleMoves()

        for m in moves:
            newBoard = copy.deepcopy(minBoard)
            newBoard.move(m[0], m[3])

            if newBoard.positionHash() not in boardEnergies.keys():
                boards.append(newBoard)
                boardEnergies[newBoard.positionHash()] = newBoard.energy
            else:
                if newBoard.energy < boardEnergies[newBoard.positionHash()]:
                    boards.append(newBoard)
                    boardEnergies[newBoard.positionHash()] = newBoard.energy

        boards.sort(key=lambda x: x.energy, reverse=True)

        #count+=1
        #if count > 20: break


    print(f'Result = {minBoard.energy}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:

    print(f'Result = {1}')
