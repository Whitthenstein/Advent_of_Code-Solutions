from setup_solutions import getPuzzleInput
import numpy as np

year = "2015"
day = "07"
puzzleInput = getPuzzleInput(f"{year}", f"Day_{day}.txt")
puzzle = puzzleInput

instructions = []
results = {}

# Part - One
def getInstructionFormatted(line: str):
    instruction, out = line.split(" -> ")
    return instruction, out.replace("\n", "")

def doInstruction(instruction: str, operand_1: str, operand_2: str):
    if instruction == "AND":
        return operand_1 & operand_2
    elif instruction == "OR":
        return operand_1 | operand_2
    elif instruction == "LSHIFT":
        return operand_1 << operand_2
    elif instruction == "RSHIFT":
        return operand_1 >> operand_2

def has3LeftArgs(l: list):
    return len(l) == 3

def getValue(val: str):
    if val.isdigit():
        return int(val)
    else:
        return results[val]

def getInstructionResult(instruction: str):
    left_list = instruction.split(' ')
    if len(left_list) == 1:
        return getValue(left_list[0])

    if "NOT" in left_list:
        return ~ getValue(left_list[1])

    if has3LeftArgs(left_list):
        operand_1 = getValue(left_list[0])
        inst = left_list[1]
        operand_2 = getValue(left_list[2])
        return doInstruction(inst, operand_1, operand_2)

def isProcessable(instruction: str):
    left_list = instruction.split(' ')
    if len(left_list) == 1:
        if left_list[0].isdigit() or left_list[0] in results:
            return True
        else:
            return False

    if "NOT" in left_list:
        if left_list[1].isdigit() or left_list[1] in results:
            return True
        else:
            return False

    if has3LeftArgs(left_list):
        if (left_list[0].isdigit() or left_list[0] in results) and (left_list[2].isdigit() or left_list[2] in results):
            return True
        else:
            return False

def findAndProcessInstruction():
    for index, instruction in enumerate(instructions):
        inst, out = getInstructionFormatted(instruction)
        if isProcessable(inst):
            return index, out, getInstructionResult(inst)

def buildCircuit():
    for el in puzzle:
        instructions.append(el)
    
    while len(instructions) > 0:
        instructionIndex, out_var, result = findAndProcessInstruction()
        results[out_var] = result
        del instructions[instructionIndex]
        
    return np.uint16(results['a'])
    
# Part - Two
def buildCircuit2():
    for el in puzzle:
        _, out = getInstructionFormatted(el)

        # override wire b to the signal received in part 1
        if out == "b":
            el = "46065 -> b\n"
        instructions.append(el)

    while len(instructions) > 0:
        instructionIndex, out_var, result = findAndProcessInstruction()
        results[out_var] = result
        del instructions[instructionIndex]
        
    return np.uint16(results['a'])
    

# Script runs here
print(f"Advent of Code - {year}: Day {day}")
print("Part-One Answer:", buildCircuit())
instructions = []
results = {}
print("Part-Two Answer:", buildCircuit2())