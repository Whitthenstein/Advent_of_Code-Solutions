from setup_solutions import getPuzzleInput
from itertools import permutations

year = "2015"
day = "13"
puzzleInput = getPuzzleInput(f"{year}", f"Day_{day}.txt")
puzzle = puzzleInput

arrangements = {}
allNames = set()

def getChangerSignal(changer: str):
    if changer == "gain":
        return ""
    if changer == "lose":
        return "-"

def processLine(line: str):
    words = line.split(" ")
    name1, changer, points, name2 = words[0], words[2], words[3], words[-1].replace(".", "").replace("\n", "")

    changePoints = int(getChangerSignal(changer) + points)
    arrangementLabel = name1 + "->" + name2

    allNames.add(name1)
    allNames.add(name2)

    arrangements[arrangementLabel] = changePoints

def getUnitsOfPermutation(permutation: tuple):
    totalUnits = 0
    for i in range(len(permutation)):
        if i == len(permutation) - 1:
            names = [ permutation[i], permutation[0]]
        else:
            names = [ permutation[i], permutation[i + 1]]
        totalUnits += arrangements[f"{names[0]}->{names[1]}"] + arrangements[f"{names[1]}->{names[0]}"]

    return totalUnits

def getMaxPointsFromPermutations():
    allPermutations = list(permutations(allNames, len(allNames)))

    allPoints = []
    for permutation in allPermutations:
        allPoints.append(getUnitsOfPermutation(permutation))
    
    return max(allPoints)

def makeArrangements(puzzle: list):
    for line in puzzle:
        processLine(line)

    
    return getMaxPointsFromPermutations()

def makeArrangements2():
    allNames.add("me")

    for name in allNames:
        processLine(f"{name} would gain 0 happiness units by sitting next to me.")
        processLine(f"me would gain 0 happiness units by sitting next to {name}.")

    return getMaxPointsFromPermutations()

# Script runs here
print(f"Advent of Code - {year}: Day {day}")
print("Part-One Answer:", makeArrangements(puzzle))
print("Part-One Answer:", makeArrangements2())