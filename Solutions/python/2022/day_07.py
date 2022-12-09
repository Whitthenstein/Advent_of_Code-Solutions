import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

def setValueInsideCurrentDir(currentPath:list, directoryTree:dict, value:str):
    dir = directoryTree
    for val in currentPath:
    
        dir = dir["dirs"][val]

    val1, val2 = value.split(" ")
    if val1 == "dir":
        dir["dirs"][val2] = {"dirs" : {}, "files": []}
    else:
        dir["files"].append({"name": val2, "size": val1})

    return directoryTree

def populateTree(lines:list, directoryTree:dict, currentPath:list):
    for line in lines:
        directoryTree = setValueInsideCurrentDir(currentPath, directoryTree, line)

    return directoryTree

def processCDCommand(arg:str, currentPath:list):
    if arg == "/":
        currentPath = ["/"]
    elif arg == "..":
        currentPath.pop()
    else:
        currentPath.append(arg)

    return currentPath

def printDirectoryTree(dT:dict, level:int):
    if len(dT) == 0:
        return
    
    for key, value in dT.items():
        print(f'{"-" * level}{key}')
        if "files" in value.keys():
            for file in value["files"]:
                print(f'{"-" * (level+1)}{file["name"]} -> {file["size"]}')
        if "dirs" in value.keys():
            printDirectoryTree(value["dirs"], level+1)

def getFilesSize(filesList:list):
    total = 0
    for file in filesList:
        total += int(file["size"])

    return total

def getDirectorySize(dir:dict, l:list):
    total = getFilesSize(dir["files"])
    for d in dir["dirs"].values():
        total += getDirectorySize(d, l)

    l.append(total)
    
    return total

def getDirectorySizeExternal(dir:dict, l:list):
    getDirectorySize(dir, l)

    return l

def parseCommandsList(puzzle:list):
    currentlyProcessing = []
    directoryTree = {"dirs": {"/": {"dirs": {}, "files": []}}}
    currentPath = []
    for line in puzzle:
        if line[0] == "$":
            if len(currentlyProcessing) > 0:
                directoryTree = populateTree(currentlyProcessing, directoryTree, currentPath)
                currentlyProcessing = []
            separated = line.split(" ") # get input in command
            if separated[1] == "cd":
                currentPath = processCDCommand(separated[2], currentPath)
        else:
            currentlyProcessing.append(line)
    
    if len(currentlyProcessing) > 0:
        directoryTree = populateTree(currentlyProcessing, directoryTree, currentPath)

    allDirectories = getDirectorySizeExternal(directoryTree["dirs"]["/"], [])
    allDirectories.sort()
    availableSpace = 70000000 - allDirectories[-1]
    necessarySpace = 30000000 - availableSpace

    solutionOneList = []
    for size in allDirectories:
        if size <= 100000:
            solutionOneList.append(size)

    solutionTwo = 0
    for size in allDirectories:
        if size >= necessarySpace:
            solutionTwo = size
            break

    return sum(solutionOneList), solutionTwo

# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
partOneSolution, partTwoSolution = parseCommandsList(puzzle)
print("Part-One Answer:", partOneSolution)
print("Part-Two Answer:", partTwoSolution)