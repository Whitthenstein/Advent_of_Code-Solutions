import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput
import math

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

def movement(move:str, grid:dict):
    head = grid[0]
    if move == "R":
        head[0] +=1
    elif move == "L":
        head[0] -=1
    elif move == "U":
        head[1] +=1
    elif move == "D":
        head[1] -=1
    
    for i in range(0, grid["knots"]-1):
        head = grid[i]
        tail = grid[i+1]


        delta_x = head[0] - tail[0]
        delta_y = head[1] - tail[1]
        if abs(delta_x) > 1 or abs(delta_y) > 1:
            tail[0] += math.floor(delta_x / 2) if delta_x <= 0 else math.ceil(delta_x / 2)
            tail[1] += math.floor(delta_y / 2) if delta_y <= 0 else math.ceil(delta_y / 2)
        
    grid["tailHistory"].add((tail[0],tail[1]))
    
    return grid
    
def positionOfTailOfRope(puzzle:list, grid:dict):

    for line in puzzle:
        move, unit = line.split(" ")
        unit = int(unit)
        while unit != 0:
            grid = movement(move, grid)
            unit-=1
            
    return len(grid["tailHistory"])

grid_one:dict = {0: [0, 0], 1: [0, 0], "tailHistory": set(), "knots": 2}
grid_two:dict = {0: [0, 0], 
                    1: [0, 0], 
                    2: [0, 0], 
                    3: [0, 0], 
                    4: [0, 0], 
                    5: [0, 0], 
                    6: [0, 0], 
                    7: [0, 0], 
                    8: [0, 0], 
                    9: [0, 0], 
                    "tailHistory": set(),
                    "knots": 10
}

# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", positionOfTailOfRope(puzzle, grid_one))
print("Part-Two Answer:", positionOfTailOfRope(puzzle, grid_two))