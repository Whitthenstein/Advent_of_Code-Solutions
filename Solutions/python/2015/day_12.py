import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput
import numbers
import json

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput[0]

def sumNumbers1(element: object):
    if isinstance(element, numbers.Number):
        return element

    total = 0
    if isinstance(element, list):
        for obj in element:
            total += sumNumbers1(obj)
        
        return total
    
    if isinstance(element, dict):
        elementsList = list(element.values())
        for obj in elementsList:
            total += sumNumbers1(obj)
    
        return total

    return 0
    
def sumNumbers2(element: object):
    if isinstance(element, numbers.Number):
        return element

    total = 0
    if isinstance(element, list):
        for obj in element:
            total += sumNumbers2(obj)
        
        return total
    
    if isinstance(element, dict):
        elementsList = list(element.values())
        if "red" in elementsList:
            return 0
        for obj in elementsList:
            total += sumNumbers2(obj)
    
        return total

    return 0


# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")

# load puzzle JSON
JSON = json.loads(puzzle)
print("Part-One Answer:", sumNumbers1(JSON))
print("Part-One Answer:", sumNumbers2(JSON))