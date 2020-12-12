f = open(r"2020/python/day12-input.txt", "r")

def rotate(wx, wy, dir, degrees):
    turns = degrees//90
    for i in range(turns):
        tx = wx
        wx = wy
        wy = tx
        if dir == 'R':
            wy *= -1
        else:
            wx *= -1
    return wx, wy

instructions = [[x[0], int(x[1:])] for x in f]

wx = 10
wy = 1
currDir = 'E'
x = 0
y = 0
for inst in instructions:
    dir = inst[0]
    if dir == 'F':
        x += (wx * inst[1])
        y += (wy * inst[1])
    if dir == 'R' or dir == 'L':
        wx, wy = rotate(wx, wy, dir, inst[1])
    if dir == 'N':
        wy += inst[1]
    if dir == 'E':
        wx += inst[1]
    if dir == 'S':
        wy -= inst[1]
    if dir == 'W':
        wx -= inst[1]

print(abs(x) + abs(y))