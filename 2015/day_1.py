# puzzle input for the challenge
puzzle = ""

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
print("Advent of Code - 2015: Day One")
print("Part-One Answer:", getFloor(puzzle))
print("Part-Two Answer:", getFirstTimeBasement(puzzle))