from setup_solutions import getPuzzleInput

puzzleInput = getPuzzleInput("2015", "Day_10.txt")
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
print("Advent of Code - 2015: Day Ten")
print("Part-One Answer:", playGameNTimes(40))
print("Part-Two Answer:", playGameNTimes(50))