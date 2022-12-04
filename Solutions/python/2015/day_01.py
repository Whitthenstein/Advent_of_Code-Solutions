import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = "2015"
day = "01"
puzzleInput = getPuzzleInput(f"{year}", f"Day_{day}.txt")
puzzle = puzzleInput[0]

def getValue(v: str):
    if v == '(':
        return 1
    if v == ')':
        return -1

def getFloor(pzl: str):
    floor = 0
    for element in pzl:
        floor += getValue(element)
    return floor

def getFirstTimeBasement(pzl:str):
    floor = 0
    for ind, element in enumerate(pzl):
        floor += getValue(element)
        if floor == -1:
            return ind + 1


# Script runs here
print(f"Advent of Code - {year}: Day {day}")
print("Part-One Answer:", getFloor(puzzle))
print("Part-Two Answer:", getFirstTimeBasement(puzzle))