# puzzle input for the challenge
puzzle = ""

def getDimensionsStrings(string: str):
    dimensions = string.splitlines()
    dimensions.remove('')
    return dimensions

def getSquareFeet(l: int, w: int, h: int):
    area1 = l*w
    area2 = w*h
    area3 = h*l
    return 2*area1 + 2*area2 + 2*area3 + min(area1, area2, area3)

def getFeetOfRibbon(l: int, w: int, h: int):
    maxToCut = max(l,w, h)
    feetOfRibbon = 2*l + 2*w + 2*h - 2*maxToCut
    return feetOfRibbon + l*w*h

def getSquareFeetTotal(pzl: str):
    total = 0
    dimensions = getDimensionsStrings(pzl)
    for element in dimensions:
        dims = element.split('x')
        total += getSquareFeet(int(dims[0]), int(dims[1]), int(dims[2]))

    return total

def getFeetRibbonTotal(pzl: str):
    total = 0
    dimensions = getDimensionsStrings(pzl)
    for element in dimensions:
        dims = element.split('x')
        total += getFeetOfRibbon(int(dims[0]), int(dims[1]), int(dims[2]))

    return total

# Script runs here
print("Advent of Code - 2015: Day Two")
print("Part-One Answer:", getSquareFeetTotal(puzzle))
print("Part-Two Answer:", getFeetRibbonTotal(puzzle))