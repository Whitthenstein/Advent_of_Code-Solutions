from setup_solutions import getPuzzleInput

year = "2015"
day = "11"
puzzleInput = getPuzzleInput(f"{year}", f"Day_{day}.txt")
puzzle = puzzleInput[0]

alphabetDict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5,
                "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
                "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
                "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
                "y": 24, "z": 25}

alphabetList = ["a", "b", "c", "d", "e", "f",
                "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x",
                "y", "z"]

def incrementLetter(letter: str):
    letterIndex = alphabetDict[letter]
    if letterIndex == 25:
        return alphabetList[0]
    else:
        return alphabetList[letterIndex + 1]

def ruleOfIncreasingThree(password: str):
    for i in range(len(password) - 2):
        if password[i+1] == incrementLetter(password[i]) and password[i+2] == incrementLetter(incrementLetter(password[i])):
            pattern = password[i] + incrementLetter(password[i]) + incrementLetter(incrementLetter(password[i]))
            if pattern in ["zab", "yza"]:
                return False
            return True
    return False

def cannotContainIOL(password: str):
    if "i" in password or "o" in password or "l" in password:
        return False
    else:
        return True

def twoDifferentPairsOfLetters(password: str):
    firstPairLetter = ""
    pairsFound = 0
    for i in range(len(password) - 1):
        if password[i] == password[i+1] and firstPairLetter != password[i]:
            if firstPairLetter == "":
                firstPairLetter = password[i]
            pairsFound += 1
        if pairsFound == 2:
            return True
    
    return False

def isValidPassword(password: str):
    if ruleOfIncreasingThree(password) and cannotContainIOL(password) and twoDifferentPairsOfLetters(password):
        return True
    else:
        return False

def incrementPassword(password: str):
    incrementedLetter = "a"
    index = len(password) - 1
    incrementedPassword  = password
    while incrementedLetter == "a":
        if index == -1:
            index = len(password) - 1
        incrementedLetter = incrementLetter(incrementedPassword[index])
        incrementedPassword = incrementedPassword[:index] + incrementedLetter + incrementedPassword[index+1:]
        index -= 1

    return incrementedPassword

def findPassword(password: str):
    newPassword = password
    while not isValidPassword(newPassword):
        newPassword = incrementPassword(newPassword)

    return newPassword

# Script runs here
print(f"Advent of Code - {year}: Day {day}")
print("Part-One Answer:", findPassword(puzzle))
print("Part-Two Answer:", findPassword(incrementPassword(findPassword(puzzle))))
