import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput
import hashlib

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput[0]

numZeroes = 5

def allZeroes(s: str):
    for el in s:
        if el != '0':
            return False
    
    return True

def verifyHash(s: str, nZeroes: int):
    hash = hashlib.md5(s.encode("utf-8")).hexdigest()
    firstFive = hash[:nZeroes]

    return allZeroes(firstFive)

def findNum(s:str, nZeroes: int):
    n = 0
    attempt = s + str(n)
    while(not verifyHash(attempt, nZeroes)):
        n += 1
        attempt = s + str(n)
    
    return n


# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", findNum(puzzle, numZeroes))
print("Part-Two Answer:", findNum(puzzle, numZeroes+1))