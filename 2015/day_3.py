"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

"""
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