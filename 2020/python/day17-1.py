import copy
f = open(r"2020\python\day17-input.txt", "r")

def surroundingNumActive(grid, x, y, z):
    count = 0
    for z1 in range(z-1, z+2):
        for y1 in range(y-1, y+2):
            for x1 in range(x-1, x+2):
                if (x1, y1, z1) == (x, y, z):
                    continue
                if (x1, y1, z1) in grid:
                    count += 1
    return count

def printGrid(grid, xmin, xmax, ymin, ymax, zmin, zmax, counts=False):
    for z in range(zmin, zmax):
        print("\nz=" + str(z))
        for y in range(ymin, ymax):
            line = ""
            for x in range(xmin, xmax):
                if(counts):
                    line += str(surroundingNumActive(grid, x, y, z))
                else:
                    line += "#" if (x,y,z) in grid else "."
            print(line)

grid = set()

x = 0
y = 0
z = 0

xmax = 0
ymax = 0
zmax = 1
xmin = 0
ymin = 0
zmin = 0
for line in f:
    for c in line.strip():
        if c == '#':
            grid.add((x,y,z))
        x += 1
    xmax = x
    
    y += 1
    x = 0
ymax = y

printGrid(grid, xmin, xmax, ymin, ymax, zmin-1, zmax+1, counts=True)
initialGrid = copy.deepcopy(grid)

for i in range(6):
    newGrid = copy.deepcopy(grid)

    for z in range(zmin-1, zmax+1):
        for y in range(ymin-1, ymax+1):
            for x in range(xmin-1, xmax+1):
                count = surroundingNumActive(grid, x, y, z)
                if (x,y,z) in grid:
                    if count != 2 and count != 3:
                        newGrid.remove((x,y,z))
                else:
                    if count == 3:
                        newGrid.add((x,y,z))

    grid = copy.deepcopy(newGrid)
    xmin -= 1
    ymin -= 1
    zmin -= 1
    xmax += 1
    ymax += 1
    zmax += 1
    printGrid(grid, xmin, xmax, ymin, ymax, zmin, zmax)


print(len(grid))    