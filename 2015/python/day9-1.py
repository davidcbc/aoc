import math

f = open(r"2015/python/day9-input.txt", "r")

graph = {}

for line in f:
    line = line.strip()
    tokens = line.split(" = ")
    cities = tokens[0].split(" to ")
    if cities[0] not in graph:
        graph[cities[0]] = []
    if cities[1] not in graph:
        graph[cities[1]] = []
    graph[cities[0]].append((cities[1], int(tokens[1])))
    graph[cities[1]].append((cities[0], int(tokens[1])))



def FindMinDistance(graph, visited, node):
    minimum = 9999999999999
    visited.add(node)
    if len(graph) == len(visited):
        visited.remove(node)
        return 0
    for next in graph[node]:
        if next[0] in visited:
            continue
        minimum = min(minimum, FindMinDistance(graph, visited, next[0]) + next[1])
    visited.remove(node)
    return minimum

def FindMaxDistance(graph, visited, node):
    maximum = 0
    visited.add(node)
    if len(graph) == len(visited):
        visited.remove(node)
        return 0
    for next in graph[node]:
        if next[0] in visited:
            continue
        maximum = max(maximum, FindMaxDistance(graph, visited, next[0]) + next[1])
    visited.remove(node)
    return maximum

minimum = 9999999999999
maximum = 0

for n in graph.keys():
    minimum = min(minimum, FindMinDistance(graph, set(), n))
    maximum = max(maximum, FindMaxDistance(graph, set(), n))

print(minimum)
print(maximum)