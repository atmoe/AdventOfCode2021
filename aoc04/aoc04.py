#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = True
def dbgPrint(text):
    if dbgEn:
        print(text)

class Board:
    def __init__(self, boardStrs, boardID):
        self.board = []
        self.id = boardID
        for i in range(0,5):
            self.board.append(boardStrs[i].split())

        self.entryHash = {}
        x = 0
        y = 0
        for i in self.board:
            for j in i:
                self.entryHash[j] = (x,y)

                x+=1
            x=0
            y+=1

    def markEntry(self, val):
        if val in self.entryHash:
            (x,y) = self.entryHash[val]
            self.board[y][x] = 'x'

    def printBoard(self):
        for b in self.board:
            print(b)

    def boardWon(self):
        # check rows
        for b in self.board:
            if b == ['x', 'x', 'x', 'x', 'x']:
                return True

        # check cols
        for i in range(0,5):
            if self.board[0][i] == 'x' and \
               self.board[1][i] == 'x' and \
               self.board[2][i] == 'x' and \
               self.board[3][i] == 'x' and \
               self.board[4][i] == 'x':
                   return True

        return False

    def boardScore(self, val):
        total = 0
        for i in range(0,5):
            for j in range(0,5):
                if self.board[i][j] == 'x':
                    continue
                else:
                    total += int(self.board[i][j])
        return total * int(val)



selections = []
inputFile = open(sys.argv[1], "r")
selections = inputFile.readline().rstrip("\n").split(",")

boards = []
newBoard = False
counter = 0
board = []
boardNum = 0
for line in inputFile.readlines():
    if line == "\n":
        counter = 0
        boardNum += 1
        board = []
    else:
        board.append(line.rstrip('\n'))
        
        if counter == 4:
            boards.append(Board(board, boardNum))

        counter += 1

inputFile.close()


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:
    winner = False
    for s in selections:
        for b in boards:
            b.markEntry(s)

        for b in boards:
            if b.boardWon():
                print(f'winnerID = {b.id}')
                print(f'score = {b.boardScore(s)}')
                winner = True

        if winner:
            break

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
    loser = False
    lastS = ""
    for s in selections:
        for b in boards:
            b.markEntry(s)

        for b in boards:
            if b.boardWon():
                if len(boards) == 1:
                    loser = True
                    lastS = s
                    print(f'winnerID = {b.id}')
                    print(f'score = {b.boardScore(s)}')

                boards.remove(b)
        if loser:
            break

    #print(f'result = {boards[0].id} score = {boards[0].boardScore(lastS)}')

