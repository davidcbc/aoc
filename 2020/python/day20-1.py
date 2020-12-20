import copy
import math
f = open(r"2020/python/day20-input.txt", "r")

input = f.read().split("\n")

BASE = 2
UP = 2
RIGHT = 3
DOWN = 4
LEFT = 5

def checkSeamonster(grid, x, y):
    seamonster = [list("                  # "),
                  list("#    ##    ##    ###"),
                  list(" #  #  #  #  #  #   ")]
    if (len(grid[y]) < x + len(seamonster[0]) or
        len(grid) < y + 3):
        return False

    for i in range(len(seamonster)):
        for j in range(len(seamonster[i])):
            if seamonster[i][j] == " ":
                continue
            if grid[y+i][x+j] == ".":
                return False
    for i in range(len(seamonster)):
        for j in range(len(seamonster[i])):
            if seamonster[i][j] == " ":
                continue
            grid[y+i][x+j] = 'O'
    
    return True

def rotateSides(sides):
    sides[LEFT-BASE] = rotateInt(sides[LEFT-BASE])
    sides[RIGHT-BASE] = rotateInt(sides[RIGHT-BASE])
    return [sides[LEFT-BASE], sides[UP-BASE], sides[RIGHT-BASE], sides[DOWN-BASE]]

def rotateInt(n):
    return int(format(n, "#012b")[2:][::-1], 2)

def rotateGrid(original):
    grid = zip(*original[::-1])
    new = []
    for l in grid:
        new.append(list(l))
    return new

def flipGrid(original):
    new = []
    for y in range(len(original)):
        new.append([])
        for x in range(len(original[y])-1, -1, -1):
            new[y].append(original[y][x])
    return new

def printTile(tile):
    for line in tile[1]:
        print(line)

def lineToNumber(line):
    number = 0
    for c in line:
        number = number << 1
        if c == '#':
            number += 1
    return number

def findCorrectPermutation(tiles, x, y, permutation, used, dimensions):
    for row in permutation:
        line = ""
        for tile in row:
            line += str(tile[0]) + " "
    if x == dimensions and y == dimensions - 1:
        return permutation
    if x == dimensions:
        x = 0
        y += 1
    for tile in tiles:
        if (tile[0] in used or
            (x != 0 and permutation[y][x-1][RIGHT] != tile[LEFT]) or
            (y != 0 and permutation[y-1][x][DOWN] != tile[UP])):
            continue
        if x == 0:
            permutation.append([])
        permutation[-1].append(tile)
        used.add(tile[0])
        fullPermutation = findCorrectPermutation(tiles, x+1, y, permutation, used, dimensions)
        if fullPermutation:
            return fullPermutation
        used.remove(tile[0])
        permutation[-1].pop()
        if x == 0:
            permutation.pop()
    return None

tiles = []
grid = []
tile = ""
i = 0
while i < len(input):
    if input[i][:4] == "Tile":
        tile = int(input[i].split()[1][:-1])
    elif input[i] == "":
        u = lineToNumber(grid[0])
        d = lineToNumber(grid[len(grid)-1])
        l = lineToNumber(row[0] for row in grid)
        r = lineToNumber(row[len(row)-1] for row in grid)
        for j in range(4):
            tiles.append((tile, 
                        copy.deepcopy(grid), 
                        u,r,d,l))
            u,r,d,l = rotateSides([u,r,d,l])
            grid = rotateGrid(grid)
        
        u = rotateInt(u)
        t = r
        r = l
        l = t
        d = rotateInt(d)
        grid = flipGrid(grid)
        for j in range(4):
            tiles.append((tile, 
                        copy.deepcopy(grid), 
                        u,r,d,l))
            u,r,d,l = rotateSides([u,r,d,l])
            grid = rotateGrid(grid)
        tile = ""
        grid = []
        
    else:
        grid.append([c for c in input[i]])
    i += 1

dim = int(math.sqrt(len(tiles)/8))
p = findCorrectPermutation(tiles, 0,0, [], set(), dim)

print(p[0][0][0] * p[0][dim-1][0] * p[dim-1][0][0] * p[dim-1][dim-1][0])

newGrid = []

for i in range(len(p)):
    for k in range(1,len(p[i][0][1])-1):
        line = ""
        for j in range(len(p[i])):
            line += "".join(p[i][j][1][k][1:-1])
        newGrid.append(list(line))


for i in range(4):
    for y in range(len(newGrid)):
        for x in range(len(newGrid[y])):
            checkSeamonster(newGrid, x, y)
    newGrid = rotateGrid(newGrid)

newGrid = flipGrid(newGrid)
for i in range(4):
    for y in range(len(newGrid)):
        for x in range(len(newGrid[y])):
            checkSeamonster(newGrid, x, y)
    newGrid = rotateGrid(newGrid)

count = 0
for l in newGrid:
    count += "".join(l).count("#")

print(count)
           