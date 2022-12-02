from setup_solutions import getPuzzleInput

year = "2022"
day = "01"
puzzleInput = getPuzzleInput(f"{year}", f"Day_{day}.txt")
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
print(f"Advent of Code - {year}: Day {day}")
print("Part-One Answer:", getMostCaloriesElf(puzzle))
print("Part-Two Answer:", getTopThreeMostCaloriesElves(puzzle))