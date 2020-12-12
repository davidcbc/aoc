f = open(r"2020/python/day12-input.txt", "r")

def rotate(start, dir, degrees):
    dirs = ['N','E','S','W']
    turns = degrees//90
    if dir == 'L': turns *= -1
    v = (dirs.index(start) + turns) % len(dirs)
    return dirs[v]


instructions = [[x[0], int(x[1:])] for x in f]

x = 0
y = 0
currDir = 'E'
for inst in instructions:
    dir = inst[0]
    if dir == 'F':
        dir = currDir
    if dir == 'R' or dir == 'L':
        currDir = rotate(currDir, dir, inst[1])
    if dir == 'N':
        y += inst[1]
    if dir == 'E':
        x += inst[1]
    if dir == 'S':
        y -= inst[1]
    if dir == 'W':
        x -= inst[1]

print(abs(x) + abs(y))