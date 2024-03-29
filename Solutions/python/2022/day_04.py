import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

def findFullyContainedPairs(puzzle):
    fullyContainedPairs = 0

    for line in puzzle:
        assignments = line.replace("\n", "").split(",")
        first = assignments[0].split("-")
        second = assignments[1].split("-")

        min_first = int(first[0])
        max_first = int(first[1])
        min_second = int(second[0])
        max_second = int(second[1])

        if (min_first >= min_second and max_first <= max_second) \
            or (min_second >= min_first and max_second <= max_first):
            fullyContainedPairs += 1
    
    return fullyContainedPairs

def findOverlappingPairs(puzzle):
    overlappingPairs = 0

    for line in puzzle:
        assignments = line.replace("\n", "").split(",")
        first = assignments[0].split("-")
        second = assignments[1].split("-")

        min_first = int(first[0])
        max_first = int(first[1])
        min_second = int(second[0])
        max_second = int(second[1])

        range_1 = [i for i in range(min_first, max_first + 1)]
        range_2 = [i for i in range(min_second, max_second + 1)]

        if (min_first in range_2 or max_first in range_2) \
            or (min_second in range_1 or max_second in range_1):
            overlappingPairs += 1
    
    return overlappingPairs

# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", findFullyContainedPairs(puzzle))
print("Part-Two Answer:", findOverlappingPairs(puzzle))