import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput
import math

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line.replace("\n", "") for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

def combinations(k, n):
  # edge case: if k is 0 or n is 0, return an empty list
  if k == 0 or n == 0:
    return []
  # base case: if k is 1, return a list with a single tuple containing the value of n
  if k == 1:
    return [(n,)]
  # initialize an empty list to store the combinations
  combos = []
  # loop through all possible values for the first number in the combination
  for i in range(n + 1):
    # get all possible combinations for the remaining numbers
    sub_combos = combinations(k - 1, n - i)
    # add i to the front of each combination and append it to the list of combinations
    for combo in sub_combos:
      combos.append((i,) + combo)
  # return the list of combinations
  return combos

def turnNegativeIntoZero(n:int):
    return 0 if n < 0 else n

def getIngredients(puzzle):
    ingredients = []
    for line in puzzle:
        _, propertiesStr = line.split(":")
        ingredients.append({})
        propertiesList = propertiesStr.split(",")
        for property in propertiesList:
            _, n, q = property.split(" ")
            ingredients[-1][n] = int(q)
    return ingredients

def getBestMixOfIngredients(puzzle):
    ingredients = getIngredients(puzzle)
    combos = combinations(len(ingredients), 100)

    best_yet = {"score": 0, "combo": ()}
    for combo in combos:
        capacities = [ingredient["capacity"] * combo[count] for count, ingredient in enumerate(ingredients)]
        durability = [ingredient["durability"] * combo[count] for count, ingredient in enumerate(ingredients)]
        flavor = [ingredient["flavor"] * combo[count] for count, ingredient in enumerate(ingredients)]
        texture = [ingredient["texture"] * combo[count] for count, ingredient in enumerate(ingredients)]

        total = math.prod([turnNegativeIntoZero(sum(capacities)), 
                            turnNegativeIntoZero(sum(durability)), 
                            turnNegativeIntoZero(sum(flavor)), 
                            turnNegativeIntoZero(sum(texture))])
        if total >= best_yet["score"]:
            best_yet["score"] = total
            best_yet["combo"] = combo

    return best_yet["score"]

def getBestMixOfIngredientsFor500Calories(puzzle):
    ingredients = getIngredients(puzzle)
    combos = combinations(len(ingredients), 100)

    best_yet = {"score": 0, "combo": ()}
    for combo in combos:
        capacities = [ingredient["capacity"] * combo[count] for count, ingredient in enumerate(ingredients)]
        durability = [ingredient["durability"] * combo[count] for count, ingredient in enumerate(ingredients)]
        flavor = [ingredient["flavor"] * combo[count] for count, ingredient in enumerate(ingredients)]
        texture = [ingredient["texture"] * combo[count] for count, ingredient in enumerate(ingredients)]
        calories = [ingredient["calories"] * combo[count] for count, ingredient in enumerate(ingredients)]

        if sum(calories) == 500:
            total = math.prod([turnNegativeIntoZero(sum(capacities)), 
                                turnNegativeIntoZero(sum(durability)), 
                                turnNegativeIntoZero(sum(flavor)), 
                                turnNegativeIntoZero(sum(texture))])
            if total >= best_yet["score"]:
                best_yet["score"] = total
                best_yet["combo"] = combo

    return best_yet["score"]

# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", getBestMixOfIngredients(puzzle))
print("Part-One Answer:", getBestMixOfIngredientsFor500Calories(puzzle))