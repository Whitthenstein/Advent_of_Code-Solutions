import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput
import math

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

sample = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390"
]

def isVisible(row, col, puzzle):
    treeHeight = int(puzzle[row][col])
    visible = [True, True, True, True]

    # up
    for i in range(row-1, -1, -1):
        proc = int(puzzle[i][col])
        if proc >= treeHeight:
            visible[0] = False
            break
    # down
    for i in range(row+1, len(puzzle), 1):
        proc = int(puzzle[i][col])
        if proc >= treeHeight:
            visible[1] = False
            break
    # left
    for i in range(col-1, -1, -1):
        proc = int(puzzle[row][i])
        if proc >= treeHeight:
            visible[2] = False
            break 
    # right
    for i in range(col+1, len(puzzle[0]), 1):
        proc = int(puzzle[row][i])
        if proc >= treeHeight:
            visible[3] = False
            break 
        
    for val in visible:
        if val:
            return True
    
    return False

def getTreeScore(row, col, puzzle):
    treeHeight = int(puzzle[row][col])
    visible = [0, 0, 0, 0]

    # up
    for i in range(row-1, -1, -1):
        proc = int(puzzle[i][col])
        visible[0] += 1
        if proc >= treeHeight:
            break
    # down
    for i in range(row+1, len(puzzle), 1):
        proc = int(puzzle[i][col])
        visible[1] += 1
        if proc >= treeHeight:
            break
    # left
    for i in range(col-1, -1, -1):
        proc = int(puzzle[row][i])
        visible[2] += 1
        if proc >= treeHeight:
            break 
    # right
    for i in range(col+1, len(puzzle[0]), 1):
        proc = int(puzzle[row][i])
        visible[3] += 1
        if proc >= treeHeight:
            break 
    
    return math.prod(visible)

def getVisibleTrees(puzzle):
    linesNum = len(puzzle)
    columnsNum = len(puzzle[0])

    totalVisible = columnsNum*2 + (linesNum*2 - 4)

    for i in range(1, linesNum-1):
        for j in range(1, columnsNum-1):
            if isVisible(i, j, puzzle):
                totalVisible += 1
    
    return totalVisible


def getHeighestScenicScore(puzzle):
    linesNum = len(puzzle)
    columnsNum = len(puzzle[0])
    scenicScores = []

    for i in range(0, linesNum):
        for j in range(0, columnsNum):
            scenicScores.append(getTreeScore(i, j, puzzle))
    
    return max(scenicScores)
            


# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", getVisibleTrees(puzzle))
print("Part-Two Answer:", getHeighestScenicScore(puzzle))