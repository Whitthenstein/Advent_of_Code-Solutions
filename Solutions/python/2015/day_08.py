import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput
    
# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", sum(len(s.replace("\n", "")) - len(eval(s.replace("\n", ""))) for s in puzzle))
print("Part-Two Answer:", sum(2+s.replace("\n", "").count('\\')+s.replace("\n", "").count('"') for s in puzzle))
