import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

def getMostCaloriesElf(puzzle):
    mostCalories = 0
    counting = 0
    
    for line in puzzle:
        line = line.replace("\n", "")
        if line == "":
            if counting > mostCalories:
                mostCalories = counting
            counting = 0
        else:
            counting += int(line)
    
    return mostCalories

def getTopThreeMostCaloriesElves(puzzle):
    elves = []
    counting = 0
    for line in puzzle:
        line = line.replace("\n", "")
        if line == "":
            elves.append(counting)
            counting = 0
        else:
            counting += int(line)
    
    elves.sort(reverse=True)
    return sum(elves[:3])


# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", getMostCaloriesElf(puzzle))
print("Part-Two Answer:", getTopThreeMostCaloriesElves(puzzle))