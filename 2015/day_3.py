# puzzle input for the challenge
puzzle = ""

def getTupleCoordinate(s: str):
    if s == '^':
        return (0,1)
    if s == '>':
        return (1,0)
    if s == '<':
        return (-1,0)
    if s == 'v':
        return (0, -1)
    
def getNumberOfHouses(pzl: str):
    houseCoordinatesSet = {(0,0)}
    currentCoordinates = [0,0]

    for letter in pzl:
        coor = getTupleCoordinate(letter)
        currentCoordinates[0] += coor[0]
        currentCoordinates[1] += coor[1]
        houseCoordinatesSet.add((currentCoordinates[0], (currentCoordinates[1])))
    
    return len(houseCoordinatesSet)

def getNumberOfHousesRoboAndSanta(pzl: str):
    santaCoordinatesSet = {(0,0)}
    roboCoordinatesSet = {(0,0)}
    santaCurrentCoordinates = [0,0]
    roboCurrentCoordinates = [0,0]

    for index, letter in enumerate(pzl):
        # santa movement
        if index % 2 == 0:
            coor = getTupleCoordinate(letter)
            santaCurrentCoordinates[0] += coor[0]
            santaCurrentCoordinates[1] += coor[1]
            santaCoordinatesSet.add((santaCurrentCoordinates[0], (santaCurrentCoordinates[1])))
        # robo movement
        else:
            coor = getTupleCoordinate(letter)
            roboCurrentCoordinates[0] += coor[0]
            roboCurrentCoordinates[1] += coor[1]
            roboCoordinatesSet.add((roboCurrentCoordinates[0], (roboCurrentCoordinates[1])))

    allHousesSet = santaCoordinatesSet.union(roboCoordinatesSet)
    return len(allHousesSet)


# Script runs here
print("Advent of Code - 2015: Day Three")
print("Part-One Answer:", getNumberOfHouses(puzzle))
print("Part-Two Answer:", getNumberOfHousesRoboAndSanta(puzzle))