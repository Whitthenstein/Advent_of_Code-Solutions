import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput[0]

def allDifferentChars(s: str):
    existing_chars = set()
    for char in s:
        if char in existing_chars:
            return False
        else:
            existing_chars.add(char)
    
    return True

def getStartOfMarker(puzzle, interval):

    for i in range(0, len(puzzle)):
        latest = i + interval
        snip = puzzle[i:latest]

        if allDifferentChars(snip):
            return latest


# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", getStartOfMarker(puzzle, 4))
print("Part-Two Answer:", getStartOfMarker(puzzle, 14))