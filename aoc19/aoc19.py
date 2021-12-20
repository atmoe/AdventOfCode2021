#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False
def dbgPrint(text='', endChar='\n'):
    if dbgEn:
        print(text, end=endChar)

scanners = []
currScanner = -1
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    scanRe = re.match('--- scanner (\d+) ---', line)
    beacRe = re.match('(-*\d+),(-*\d+),(-*\d+)', line)

    if scanRe:
        currScanner = int(scanRe.group(1))
        scanners.append([])

    if beacRe:
        scanners[currScanner].append([int(beacRe.group(1)), int(beacRe.group(2)), int(beacRe.group(3))])

inputFile.close()

def orient(coord, direction, degrees):
    dirCoord = [0,0,0]
    if direction == 'z':
        # x,  y,  z
        dirCoord[0] = coord[0]
        dirCoord[1] = coord[1]
        dirCoord[2] = coord[2]
    elif direction == '-z':
        # -x,  y, -z
        dirCoord[0] = -coord[0]
        dirCoord[1] =  coord[1]
        dirCoord[2] = -coord[2]
    elif direction == 'y':
        # x, -z,  y
        dirCoord[0] =  coord[0]
        dirCoord[1] = -coord[2]
        dirCoord[2] =  coord[1]
    elif direction == '-y':
        # x,  z, -y
        dirCoord[0] =  coord[0]
        dirCoord[1] =  coord[2]
        dirCoord[2] = -coord[1]
    elif direction == 'x':
        #-z,  y,  x
        dirCoord[0] = -coord[2]
        dirCoord[1] =  coord[1]
        dirCoord[2] =  coord[0]
    elif direction == '-x':
        # z,  y, -x
        dirCoord[0] =  coord[2]
        dirCoord[1] =  coord[1]
        dirCoord[2] = -coord[0]

    rotCoord = [0,0,0]
    if degrees == 0:
        rotCoord[0] =  dirCoord[0]
        rotCoord[1] =  dirCoord[1]
        rotCoord[2] =  dirCoord[2]
    elif degrees == 90:
        rotCoord[0] =  dirCoord[1]
        rotCoord[1] = -dirCoord[0]
        rotCoord[2] =  dirCoord[2]
    elif degrees == 180:
        rotCoord[0] = -dirCoord[0]
        rotCoord[1] = -dirCoord[1]
        rotCoord[2] =  dirCoord[2]
    elif degrees == 270:
        rotCoord[0] = -dirCoord[1]
        rotCoord[1] =  dirCoord[0]
        rotCoord[2] =  dirCoord[2]

    return rotCoord

def commonBeacons(s0, s1):
    for b0 in s0:
        for b1 in s1:
            
            # check that b0 and b1 are the same

            for d in ['z', '-z', 'y', '-y', 'x', '-x']:
                for r in [0, 90, 180, 270]:
                    count = 1
                    orientedB1 = orient(b1, d, r)

                    for b in s1:
                        # check if the other beacons in s1 line up with s0
                        if b == b1: continue

                        orientedB  = orient(b, d, r)

                        xOff = orientedB[0] - orientedB1[0]
                        yOff = orientedB[1] - orientedB1[1]
                        zOff = orientedB[2] - orientedB1[2]

                        bInB0Space = [b0[0] + xOff, b0[1] + yOff, b0[2] + zOff]
                        if bInB0Space in s0:
                            count+=1

                    if count == 12:
                        s1Loc = [0,0,0]
                        s1Loc[0] = bInB0Space[0]-orientedB[0]
                        s1Loc[1] = bInB0Space[1]-orientedB[1]
                        s1Loc[2] = bInB0Space[2]-orientedB[2]

                        # change all s1 coords to be oriented the same as s0
                        for i in range(0, len(s1)):
                            s1[i] = orient(s1[i], d, r)

                        return (True, s1Loc)

    return (False, None)


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = True
if doPart1:

    scannerLoc = [[0,0,0]] * len(scanners)
    remScanners = list(range(1,len(scanners)))

    knownScanners = [0]
    checkedPairs = []
    while len(remScanners) > 0:
        for r in remScanners:
            rtn = False
            for k in knownScanners:
                alreadyChecked = False
                for pair in checkedPairs:
                    if r == pair[0] and k == pair[1]:
                        alreadyChecked = True 

                if alreadyChecked:
                    continue

                checkedPairs.append((r,k))

                print(f'checking {r} {k}...')

                (rtn, loc) = commonBeacons(scanners[k], scanners[r])
                if rtn:
                    thisLoc = [0,0,0]
                    thisLoc[0] = loc[0] + scannerLoc[k][0]
                    thisLoc[1] = loc[1] + scannerLoc[k][1]
                    thisLoc[2] = loc[2] + scannerLoc[k][2]
                    print(f'scanner {r} = {thisLoc}')

                    scannerLoc[r] = thisLoc
                    knownScanners.append(r)
                    remScanners.remove(r)
                    break
            if rtn:
                break

    numBeacons = 0
    beaconHash = {}
    for s in range(0,len(scanners)):
        for b in scanners[s]:
            sLoc = scannerLoc[s]
            bLoc = [0,0,0]
            bLoc[0] = b[0] + sLoc[0]
            bLoc[1] = b[1] + sLoc[1]
            bLoc[2] = b[2] + sLoc[2]
            key = ''
            for c in bLoc:
                key+=str(c)
                key+='x'
            beaconHash[key] = True

    print(f'Result = {len(beaconHash.keys())}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
doPart2 = True
if doPart2:
#    scannerLoc = []
#    inputFile = open(sys.argv[1], "r")
#    for line in inputFile.readlines():
#        bRe = re.match('\[(-*\d+), (-*\d+), (-*\d+)\]', line)
#
#        scannerLoc.append( (int(bRe.group(1)), int(bRe.group(2)), int(bRe.group(3)) ) )

#    inputFile.close()
    
    maxDist = 0
    for b1 in scannerLoc:
        for b2 in scannerLoc:
            if b1 == b2: continue

            thisDist  = b2[0] - b1[0]
            thisDist += b2[1] - b1[1]
            thisDist += b2[2] - b1[2]

            if thisDist > maxDist:
                maxDist = thisDist


    print(f'Result = {maxDist}')


