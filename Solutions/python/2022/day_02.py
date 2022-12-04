import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = "2022"
day = "02"
puzzleInput = getPuzzleInput(f"{year}", f"Day_{day}.txt")
puzzle = puzzleInput

points = {"Rock": 1, "Paper": 2, "Scissors": 3}
strategy_one = {"A": "Rock", "X": "Rock", "B": "Paper",
                "Y": "Paper", "C": "Scissors", "Z": "Scissors"}
strategy_two = {
    "X": "Lose",
    "Y": "Draw", "Z": "Win"
}
beats = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}
loses = {
    "Rock": "Paper",
    "Scissors": "Rock",
    "Paper": "Scissors"    
}

def getAllPlays(input):
    plays = []
    for line in input:
        line = line.replace("\n", "")
        one, two = line.split(" ")
        plays.append([one, two])
    
    return plays

def calculateScoreForFirstStrategy(puzzle):
    plays = getAllPlays(puzzle)
    total = 0

    for play in plays:
        player_one = strategy_one[play[0]]
        player_two = strategy_one[play[1]]

        if player_one == player_two:
            total += 3
        elif player_two == "Rock" and player_one == "Scissors" \
            or player_two == "Scissors" and player_one == "Paper" \
                or player_two == "Paper" and player_one == "Rock":
            total += 6
        
        total += points[player_two]
    
    return total

def calculateScoreForSecondStrategy(puzzle):
    plays = getAllPlays(puzzle)
    total = 0

    for play in plays:
        player_one = strategy_one[play[0]]
        player_two = strategy_two[play[1]]

        if player_two == "Win":
            total += 6 + points[loses[player_one]]
        elif player_two == "Draw":
            total += 3 + points[player_one]
        else:
            total += points[beats[player_one]]
    
    return total

# Script runs here
print(f"Advent of Code - {year}: Day {day}")
print("Part-One Answer:", calculateScoreForFirstStrategy(puzzle))
print("Part-Two Answer:", calculateScoreForSecondStrategy(puzzle))