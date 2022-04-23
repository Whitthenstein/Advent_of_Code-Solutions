from setup_solutions import getPuzzleInput
from itertools import permutations


puzzleInput = getPuzzleInput("2015", "Day_9.txt")
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
print("Advent of Code - 2015: Day Nine")
allPossibleRoutes()
print("Part-One Answer:", getShortestDistance())
print("Part-Two Answer:", getLongestDistance())