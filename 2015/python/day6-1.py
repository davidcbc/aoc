f = open(r"2015/python/day6-input.txt", "r")

grid = [[0]*1000 for i in range(1000)]
grid2 = [[0]* 1000 for i in range(1000)]

for line in f:
    split = line.strip().split(" through ")
    tokens = split[0].split()
    command = tokens[-2]
    values = tokens[-1]
    start = values.split(',')
    end = split[1].split(',')
    x1 = int(start[0])
    y1 = int(start[1])
    x2 = int(end[0])
    y2 = int(end[1])
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if command == "on":
                grid[x][y] = 1
                grid2[x][y] += 1
            if command == "off":
                grid[x][y] = 0
                grid2[x][y] -= 1
                if grid2[x][y] < 0: grid2[x][y] = 0
            if command == "toggle":
                grid[x][y] = not grid[x][y]
                grid2[x][y] += 2

print(sum(sum(x) for x in grid))
print(sum(sum(x) for x in grid2))
            