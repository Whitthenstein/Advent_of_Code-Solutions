import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

class color:
   RED = '\033[31;1;4m'
   BASE = '\033[0m'

def getSignalStrengthsOfCycles(puzzle:list, cycles:list):
    register_X = 1
    current_cycle = 1
    signal_strengths = []
    for line in puzzle:
        line:str
        splitted:list = line.split(" ")
        if splitted[0] == "noop":
            count= 1
            to_add = 0
        else:
            count = 2
            to_add = int(splitted[1])

        while count > 0:
            # print(current_cycle, register_X)
            if current_cycle in cycles:
                signal_strengths.append(current_cycle * register_X)
            current_cycle += 1
            count -= 1

        register_X += to_add


    return sum(signal_strengths)

def printCRT(crt:list):
    for l in crt:
        print(l.replace('#', color.RED + '#' + color.BASE))

def renderCRT(puzzle):
    current_cycle = 1
    register_X = 1
    CRT = []
    row = -1
    for line in puzzle:
        splitted:list = line.split(" ")

        if splitted[0] == "noop":
            count= 1
            to_add = 0
        else:
            count = 2
            to_add = int(splitted[1])

        while count > 0:
            position = (current_cycle % 40)
            if position == 1:
                CRT.append("." * 40)
                row += 1

            down = register_X
            up = register_X + 2
            if position >= down and position <= up:
                CRT[row] = CRT[row][:position-1] + "#" + CRT[row][position:]
            current_cycle += 1
            count -= 1

        register_X += to_add
    
    return CRT

# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", getSignalStrengthsOfCycles(puzzle, [20, 60, 100, 140, 180, 220]))
print("Part-Two Answer:")
printCRT(renderCRT(puzzle))