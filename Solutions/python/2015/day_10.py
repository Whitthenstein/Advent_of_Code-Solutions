import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput[0]

def lookAndSay(string: str):
    foundChar = ""
    pattern = ""
    finalString = ""
    for char in string:
        if char != foundChar:
            if len(pattern) > 0:
                finalString += str(len(pattern)) + foundChar
            foundChar = char
            pattern = char
        else:
            pattern += char

    return finalString + str(len(pattern)) + foundChar
        
def playGameNTimes(n: int):
    string = puzzle
    for _ in range(n):
        string = lookAndSay(string)

    return len(string)

# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", playGameNTimes(40))
print("Part-Two Answer:", playGameNTimes(50))