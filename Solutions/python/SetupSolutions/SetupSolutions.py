import os

def getPuzzleInput(year: str, day: str):
    print(os.getcwd())
    inputPath = os.path.join("..", "..", "..", "Inputs", year, day)
    scriptInDirectory = os.path.dirname(os.path.realpath(__file__))
    puzzlePath = os.path.join(scriptInDirectory, inputPath)

    with open(puzzlePath) as file:
        puzzle = file.readlines()
    
    return puzzle