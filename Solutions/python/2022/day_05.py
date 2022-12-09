import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

def getCratesForWhichStacks(cratesList: list):
    stackNum = 1
    emptyElCounter = 0
    tuplesList = []
    for el in cratesList:
        if el != "":
            tuplesList.append((el[1], stackNum))
            stackNum += 1
        elif el == "":
            if emptyElCounter == 3:
                stackNum += 1
                emptyElCounter = 0
            else:
                emptyElCounter += 1
    
    return tuplesList

def getStacks(stackRepresentation: list):
    stacks = {}
    stackRepresentation = stackRepresentation[:-1]
    cratesLists = [line.split(" ") for line in stackRepresentation]

    for l in cratesLists:
        cratesForStacks = getCratesForWhichStacks(l)
        for tup in cratesForStacks:
            if tup[1] in stacks:
                stacks[tup[1]].append(tup[0])
            else:
                stacks[tup[1]] = [tup[0]]

    return stacks

def getOrders(ordersRepresentationList: list):
    orders = []
    for line in ordersRepresentationList:
        l = line.split(" ")
        orders.append([int(l[1]), int(l[3]), int(l[5])])
    
    return orders

def reArrangeStacksForCrateMover9000(puzzle):
    separatorIndex = puzzle.index("")
    stackRepresentation = puzzle[:separatorIndex]
    ordersRepresentationList = puzzle[separatorIndex+1:]
    
    stacks = getStacks(stackRepresentation)
    ordersList = getOrders(ordersRepresentationList)

    for order in ordersList:
        for _ in range(order[0]):
            stacks[order[2]].insert(0, stacks[order[1]].pop(0))

    topCrates = []
    for i in range(1, len(stacks) + 1):
        topCrates.append(stacks[i][0])
        
    return "".join(topCrates)

def reArrangeStacksForCrateMover9001(puzzle):
    separatorIndex = puzzle.index("")
    stackRepresentation = puzzle[:separatorIndex]
    ordersRepresentationList = puzzle[separatorIndex+1:]
    
    stacks = getStacks(stackRepresentation)
    ordersList = getOrders(ordersRepresentationList)

    for order in ordersList:
        stacks[order[2]] = stacks[order[1]][:order[0]] + stacks[order[2]]
        stacks[order[1]] = stacks[order[1]][order[0]:]

    topCrates = []
    for i in range(1, len(stacks) + 1):
        topCrates.append(stacks[i][0])
        
    return "".join(topCrates)
        
# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", reArrangeStacksForCrateMover9000(puzzle))
print("Part-Two Answer:", reArrangeStacksForCrateMover9001(puzzle))