import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput
from itertools import permutations

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

allLocations = set()
allDistances = {}
allPossibleRoutes = []
calculatedRoutes = {}

def allPossibleRoutes():
    for line in puzzle:
        locations, distance = line.split(" = ")
        location1, location2 = locations.split(" to ")

        allLocations.add(location1)
        allLocations.add(location2)

        allDistances[f"{location1} -> {location2}"] = int(distance)
        allDistances[f"{location2} -> {location1}"] = int(distance)

    allPossibleRoutes = list(permutations(allLocations, len(allLocations)))

    for route in allPossibleRoutes:
        routeLabel = " -> ".join(route)
        routeDistance = 0
        for i in range(len(route) -1 ):
            miniRoute = f"{route[i]} -> {route[i + 1]}"
            routeDistance += allDistances[miniRoute]

        calculatedRoutes[routeLabel] = routeDistance

def getShortestDistance():
    return min(calculatedRoutes.values())

def getLongestDistance():
    return max(calculatedRoutes.values())

# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
allPossibleRoutes()
print("Part-One Answer:", getShortestDistance())
print("Part-Two Answer:", getLongestDistance())