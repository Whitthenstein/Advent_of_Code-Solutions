from setup_solutions import getPuzzleInput
import numpy as np

puzzleInput = getPuzzleInput("2015", "Day_8.txt")
puzzle = puzzleInput

#puzzle = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']

totalCharsOfStringCode = 0
totalCharsInMem = 0

# Part - One
def countCharsInCode(string: str):
    return len(string)
    

def countCharsInMem(string: str):
    return len(eval(string))

def countChars(string: str):
    global totalCharsOfStringCode
    global totalCharsInMem

    totalCharsOfStringCode += countCharsInCode(string)
    totalCharsInMem += countCharsInMem(string)

def countTotalChars():
    for line in puzzle:
        countChars(line.replace("\n", ""))

def getTotalNumberCharacters1():
    countTotalChars()
    return totalCharsOfStringCode - totalCharsInMem

# Part - Two
def getTotalNumberCharacters2():
    countTotalChars()
    return totalCharsOfStringCode - totalCharsInMem
    

# Script runs here
print("Advent of Code - 2015: Day Eight")
print("Part-One Answer:", sum(len(s.replace("\n", "")) - len(eval(s.replace("\n", ""))) for s in puzzle))
print("Part-Two Answer:", sum(2+s.replace("\n", "").count('\\')+s.replace("\n", "").count('"') for s in puzzle))
