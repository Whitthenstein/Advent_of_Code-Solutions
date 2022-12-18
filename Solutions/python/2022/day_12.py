import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "SetupSolutions")))

from SetupSolutions import getPuzzleInput

year = os.path.basename(os.path.dirname(__file__))
day = os.path.basename(__file__).split(".")[0].capitalize()
puzzleInput = [line for line in getPuzzleInput(f"{year}", f"{day}.txt")]
puzzle = puzzleInput

sample = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]

import math

def dijkstra(graph, source, target):
    # Initialize distances and create a queue
    distances = {source: 0}
    queue = [(0, source)]

    # Create a set to track visited nodes
    visited = set()

    # Loop until the queue is empty
    while queue:
        # Get the next node with the smallest distance
        distance, node = queue.pop(0)

        # If the node has not been visited yet, process it
        if node not in visited:
            visited.add(node)

            # Update the distances of its neighbors
            for neighbor in graph[node]["neighbors"]:
                new_distance = distance + 1
                if (neighbor not in distances or new_distance <= distances[neighbor]):
                    distances[neighbor] = new_distance
                    queue.append((new_distance, neighbor))

    # Return the shortest distance to the target node
    return (distances[target] if target in distances else math.inf)

def isValidNeighbor(currentLetter, nextLetter):
    return ord(nextLetter) <= (ord(currentLetter) + 1)

def getNeighbors(row, col, lenRow, lenCol, graph):
    all = []
    if row == 0 :
        all.append((1, col))
    if row > 0 and row < lenRow-1:
        all.append((row - 1, col))
        all.append((row + 1, col))
    if row == lenRow - 1:
        all.append((lenRow - 2, col))
    if col == 0:
        all.append((row, 1))
    if col > 0 and col < lenCol - 1:
        all.append((row, col - 1))
        all.append((row, col + 1))
    if col == lenCol - 1:
        all.append((row, lenCol - 2))

    return all

def getGraph(puzzle):
    lenRows = len(puzzle)
    lenCols = len(puzzle[0])
    start = None
    end = None
    graph = {}
    for i, line in enumerate(puzzle):
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)
                c = "a"
            elif c == "E":
                end = (i, j)
                c = "z"
            neighbors = [neighbor for neighbor in getNeighbors(i, j, lenRows, lenCols, graph) if isValidNeighbor(c, puzzle[neighbor[0]][neighbor[1]])]
            graph[(i,j)] = {"neighbors": neighbors}

    return start, end, graph

def getShortestPathOne(puzzle):
    start, end, graph = getGraph(puzzle)

    return dijkstra(graph, start, end)

def getShortestPathTwo(puzzle):
    start, end, graph = getGraph(puzzle)

    starts = []
    for i, line in enumerate(puzzle):
        for j, c in enumerate(line):
            if c == "a":
                starts.append((i, j))
    starts.append(start)

    results = [dijkstra(graph, s, end) for s in starts]
    results.sort()
    return results[0]

# Script runs here
print(f"Advent of Code - {year}: {day.replace('_', ' ')}")
print("Part-One Answer:", getShortestPathOne(puzzle))
print("Part-Two Answer:", getShortestPathTwo(puzzle))