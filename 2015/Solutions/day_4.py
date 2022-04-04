from setup_solutions import getPuzzleInput
import hashlib

puzzleInput = getPuzzleInput("Day_4.txt")
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
print("Advent of Code - 2015: Day Four")
print("Part-One Answer:", findNum(puzzle, numZeroes))
print("Part-Two Answer:", findNum(puzzle, numZeroes+1))