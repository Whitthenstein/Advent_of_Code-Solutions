import os

def getPuzzleInput(text: str):
    inputPath = os.path.join("..", "Inputs", text)
    scriptInDirectory = os.path.dirname(os.path.realpath(__file__))
    puzzlePath = os.path.join(scriptInDirectory, inputPath)

    with open(puzzlePath) as file:
        puzzle = file.readlines()
    
    return puzzle