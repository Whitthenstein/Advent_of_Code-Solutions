from setup_solutions import getPuzzleInput

puzzleInput = getPuzzleInput("2015", "Day_5.txt")
puzzle = puzzleInput

# Part - One
def hasAtLeastNumVowels(s: str, n: int):
    vowels = ['a', 'e', 'i', 'o', 'u']
    has = 0
    for char in s:
        if char in vowels:
            has += 1

    return True if has >= n else False
    
def letterTwiceInRow(s: str):
    length = len(s) - 1
    for index, char in enumerate(s):
        if index < length:
            if s[index+1] == char:
                return True
    
    return False

def notContainCertainStringsStrings(s: str):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for ss in forbidden:
        if ss in s:
            return False

    return True

def checkString(s: str):
    if (hasAtLeastNumVowels(s, 3) and letterTwiceInRow(s) and notContainCertainStringsStrings(s)):
        return 1
    else:
        return 0

def howManySrings(l: list):
    # a if condition else b
    totalWords = 0
    for word in l:
        totalWords += checkString(word)
    
    return totalWords

# Part - Two

def pairAnyTwoLetters(s: str):
    length = len(s)
    for index, char in enumerate(s):
        if index < length - 2:
            pair = char + s[index+1]
            if s.find(pair, index+2) != -1:
                return True
    
    return False

def oneLetterRepeatsWithOneLetterInMiddle(s: str):
    length = len(s)
    for index, char in enumerate(s):
        if index < length - 2:
            if char == s[index + 2]:
                return True
    
    return False

def checkStringTwo(s: str):
    if (pairAnyTwoLetters(s) and oneLetterRepeatsWithOneLetterInMiddle(s)):
        return 1
    else:
        return 0

def howManySringsTwo(l: list):
    # a if condition else b
    totalWords = 0
    for word in l:
        totalWords += checkStringTwo(word)
    
    return totalWords

# Script runs here
print("Advent of Code - 2015: Day Five")
print("Part-One Answer:", howManySrings(puzzle))
print("Part-Two Answer:", howManySringsTwo(puzzle))