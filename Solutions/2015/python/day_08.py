from setup_solutions import getPuzzleInput

year = "2015"
day = "08"
puzzleInput = getPuzzleInput(f"{year}", f"Day_{day}.txt")
puzzle = puzzleInput
    
# Script runs here
print(f"Advent of Code - {year}: Day {day}")
print("Part-One Answer:", sum(len(s.replace("\n", "")) - len(eval(s.replace("\n", ""))) for s in puzzle))
print("Part-Two Answer:", sum(2+s.replace("\n", "").count('\\')+s.replace("\n", "").count('"') for s in puzzle))
