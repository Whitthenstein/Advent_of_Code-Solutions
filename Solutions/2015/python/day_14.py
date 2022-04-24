from setup_solutions import getPuzzleInput
from math import floor

year = "2015"
day = "14"
puzzleInput = getPuzzleInput(f"{year}", f"Day_{day}.txt")
puzzle = puzzleInput

seconds = 2503
distances = []
reinDeersInfo = {}
allReindeer = []

def calculateDistance(duration: int, restDuration: int, velocity: int, sec: int):
    remainderFlyingSeconds = min(sec % (duration + restDuration), duration)

    return velocity * ((floor(sec / (duration + restDuration)) * duration) + remainderFlyingSeconds )

def getReindeerDetails(line: str):
    infoList = line.split(" ")
    return infoList[0], int(infoList[3]), int(infoList[6]), int(infoList[-2])

def getDistance(line: str):
    _, velocity, duration, restDuration = getReindeerDetails(line)

    return calculateDistance(duration, restDuration, velocity, seconds)

def getDistances(puzzle: list):
    for line in puzzle:
        distances.append(getDistance(line))

    return max(distances)

def findLeadingReindeer(l: list):
    greaterDistance = 0
    reindeer = ""
    for tup in l:
        if tup[1] > greaterDistance:
            reindeer = tup[0]
            greaterDistance = tup[1]
    
    return reindeer

def getPoints(puzzle: list):
    points = {}
    for line in puzzle:
        name, velocity, duration, restDuration = getReindeerDetails(line)
        allReindeer.append(name)
        points[name] = 0
        reinDeersInfo[name] = {"name": name, "velocity": velocity, 
                                "duration": duration, "restDuration": restDuration}
    
    for i in range(1, seconds + 1):
        nameDistance = []
        for reindeer in allReindeer:
            distance = calculateDistance(reinDeersInfo[reindeer]["duration"], reinDeersInfo[reindeer]["restDuration"], reinDeersInfo[reindeer]["velocity"], i)
            nameDistance.append((reindeer, distance))
        
        points[findLeadingReindeer(nameDistance)] += 1

    return max(points[r] for r in allReindeer)



# Script runs here
print(f"Advent of Code - {year}: Day {day}")
print("Part-One Answer:", getDistances(puzzle))
print("Part-One Answer:", getPoints(puzzle))