import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

import functools

def comparator(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        elif type(y) == list:
            return comparator([x], y)
    else:
        if type(y) == int:
            return comparator(x, [y])

    for a, b in zip(x, y):
        v = comparator(a, b)
        if v:
            return v
    
    return len(x) - len(y)


def getSumOfRightOrderPairs(puzzle):
    puzzle = [line for line in puzzle if line != ""]
    pairs = []
    for i in range(0, len(puzzle), 2):
        left = eval(puzzle[i])
        right = eval(puzzle[i+1])

        pairs.append((left, right))
    
    count = 0
    for i, (l, r) in enumerate(pairs):
        if comparator(l, r) < 0:
            count += i + 1
    
    return count

def getMultiplierOfDividerPacketsPositions(puzzle):
    puzzle = [line for line in puzzle if line != ""]
    pairs = []
    for i in range(0, len(puzzle), 2):
        left = eval(puzzle[i])
        right = eval(puzzle[i+1])

        pairs += [left, right]
    
    pairs += [[[2]], [[6]]]

    pairs.sort(key=functools.cmp_to_key(comparator))
    
    return (pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1)

# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", getSumOfRightOrderPairs(puzzle))
print("Part-Two Answer:", getMultiplierOfDividerPacketsPositions(puzzle))