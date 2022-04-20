from setup_solutions import getPuzzleInput
import numpy as np

puzzleInput = getPuzzleInput("Day_6.txt")
puzzle = puzzleInput

#matrix
matrix = np.zeros((1000, 1000))

# Part - One
def getStrInListAsInt(l: list):
    return (int(el) for el in l)

def turnOn(x: int, y: int):
    matrix[x][y] = 1

def turnOff(x: int, y: int):
    matrix[x][y] = 0

def toggle(x: int, y: int):
    if matrix[x][y] == 1:
        turnOff(x, y)
    else:
        turnOn(x, y)

def processInstruction(order: str, start: str, end: str):
    start_x, start_y = getStrInListAsInt(start.split(","))
    end_x, end_y = getStrInListAsInt(end.split(","))

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if order == "turn on":
                turnOn(x, y)
            elif order == "turn off":
                turnOff(x, y)
            elif order == "toggle":
                toggle(x, y)

def handleLightInstruction(instruction: str):
    parts = instruction.split(" ")

    # handle space between "turn on" and "turn off"
    if len(parts) == 5:
        parts = [ f"{parts[0]} {parts[1]}", parts[2], parts[3], parts[4]]
    
    processInstruction(parts[0], parts[1], parts[3])   

def countLights():
    count = 0
    for x in matrix:
        for y in x:
            count += y
    
    return int(count)

def howManyLights(puzzle: list):
    for el in puzzle:
        handleLightInstruction(el)
    
    return countLights()

# Part - Two
def turnOn2(x: int, y: int):
    matrix[x][y] += 1

def turnOff2(x: int, y: int):
    matrix[x][y] -= 1
    if matrix[x][y] < 0:
        matrix[x][y] = 0

def toggle2(x: int, y: int):
    matrix[x][y] += 2

def processInstruction2(order: str, start: str, end: str):
    start_x, start_y = getStrInListAsInt(start.split(","))
    end_x, end_y = getStrInListAsInt(end.split(","))

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if order == "turn on":
                turnOn2(x, y)
            elif order == "turn off":
                turnOff2(x, y)
            elif order == "toggle":
                toggle2(x, y)

def handleLightInstruction2(instruction: str):
    parts = instruction.split(" ")

    # handle space between "turn on" and "turn off"
    if len(parts) == 5:
        parts = [ f"{parts[0]} {parts[1]}", parts[2], parts[3], parts[4]]
    
    processInstruction2(parts[0], parts[1], parts[3])

def howManyLights2(puzzle: list):
    for el in puzzle:
        handleLightInstruction2(el)
    
    return countLights()

# Script runs here
print("Advent of Code - 2015: Day Six")
print("Part-One Answer:", howManyLights(puzzle))

# reset matrix for part two
matrix = np.zeros((1000, 1000))

print("Part-Two Answer:", howManyLights2(puzzle))
