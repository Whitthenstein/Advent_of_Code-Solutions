import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput
import math

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

def getMonkeysInfo(linesList:list):
    current = []
    monkeys = []
    for line in linesList:
        line = line.replace("\n", "")
        if line == "":
            monkeys.append(current)
            current = []
        else:
            current.append(line)
    
    monkeys.append(current)
    
    return monkeys

def getMonkeys(monkeysInfo:list):
    monkeys = []
    for info in monkeysInfo:
        items = [int(i) for i in info[1].split(": ")[1].replace(",", "").split(" ")]
        operation = info[2].split("= ")[1]
        divisible = int(info[3].split(" ")[-1])
        true = int(info[4].split(" ")[-1])
        false = int(info[5].split(" ")[-1])
        monkeys.append({"items": items, "operation": operation, "divisible": divisible, "true": true, "false": false, "inspections": 0})
    
    return monkeys

def doOperation(op:str, worryDivider, divisible):
    symbols = op.split(" ")
    result = int(symbols[0]) + int(symbols[2]) if symbols[1] == "+" else int(symbols[0]) * int(symbols[2])

    if worryDivider == 1:
        return result % divisible
    else:
        return result // 3

def countInspections(puzzle):
    monkeysInfo = getMonkeysInfo(puzzle)
    monkeys = getMonkeys(monkeysInfo)

    for i in range(20):
        for monkey in monkeys:
            count = 0
            for item in monkey["items"]:
                operation = monkey["operation"].replace("old", f"{item}")
                worry = eval(operation) // 3
                remainder = worry % monkey["divisible"]
                monkeys[monkey["true"]]["items"].append(worry) if remainder == 0 else monkeys[monkey["false"]]["items"].append(worry)
                count += 1
            monkey["items"] = monkey["items"][(count-1):-1]
            monkey["inspections"] += count

    mostActiveMonkeys = sorted([monkey["inspections"] for monkey in monkeys], reverse=True)[:2]

    return math.prod(mostActiveMonkeys)

def countInspections2(puzzle):
    monkeysInfo = getMonkeysInfo(puzzle)
    monkeys = getMonkeys(monkeysInfo)

    superModulo = math.prod([monkey["divisible"] for monkey in monkeys])

    for i in range(10000):
        for monkey in monkeys:
            count = 0
            for item in monkey["items"]:
                operation = monkey["operation"].replace("old", f"{item}")
                worry = int(eval(operation)) % superModulo
                remainder = worry % monkey["divisible"]
                monkeys[monkey["true"]]["items"].append(worry) if remainder == 0 else monkeys[monkey["false"]]["items"].append(worry)
                count += 1
            monkey["items"] = monkey["items"][(count-1):-1]
            monkey["inspections"] += count

    mostActiveMonkeys = sorted([monkey["inspections"] for monkey in monkeys], reverse=True)[:2]

    return math.prod(mostActiveMonkeys)

# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", countInspections(puzzle))
print("Part-Two Answer:", countInspections2(puzzle))