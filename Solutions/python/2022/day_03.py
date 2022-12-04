import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = "2022"
day = "03"
puzzleInput = getPuzzleInput(f"{year}", f"Day_{day}.txt")
puzzle = puzzleInput

def getCommonItems(rucksack_1, rucksack_2):
    common = []
    for letter in rucksack_1:
        if letter in rucksack_2 and letter not in common:
            common.append(letter)
    
    return common

def getCommonItemsThree(rucksack_1, rucksack_2, rucksack_3):
    common = []
    for letter in rucksack_1:
        if letter in rucksack_2 and letter not in common and letter in rucksack_3:
            common.append(letter)
    
    return common

def getItemTypePriority(item):
    value = ord(item)

    if value >= ord("A") and value <= ord("Z"):
        return value - 38
    else:
        return value- 96

def sumOfPrioritiesOfCommonItems(puzzle):
    all_letters = []
    lines = [line for line in puzzle][:3]
    for line in puzzle:
        line = line.replace("\n", "")
        middlePoint = int(len(line) / 2)
        common = getCommonItems(line[0:middlePoint], line[middlePoint:])
        all_letters += [getItemTypePriority(letter) for letter in common]

    return sum(all_letters)

def sumOfPrioritiesOfElfGroups(puzzle):
    all_letters = []
    groups_of_three = [puzzle[i:i + 3] for i in range(0, len(puzzle), 3)]
    for group in groups_of_three:
        common = getCommonItemsThree(group[0].replace("\n", ""), group[1].replace("\n", ""), group[2].replace("\n", ""))
        all_letters += [getItemTypePriority(letter) for letter in common]
    
    return sum(all_letters)
# Script runs here
print(f"Advent of Code - {year}: Day {day}")
print("Part-One Answer:", sumOfPrioritiesOfCommonItems(puzzle))
print("Part-Two Answer:", sumOfPrioritiesOfElfGroups(puzzle))