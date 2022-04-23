from setup_solutions import getPuzzleInput

puzzleInput = getPuzzleInput("2015", "Day_8.txt")
puzzle = puzzleInput
    
# Script runs here
print("Advent of Code - 2015: Day Eight")
print("Part-One Answer:", sum(len(s.replace("\n", "")) - len(eval(s.replace("\n", ""))) for s in puzzle))
print("Part-Two Answer:", sum(2+s.replace("\n", "").count('\\')+s.replace("\n", "").count('"') for s in puzzle))
