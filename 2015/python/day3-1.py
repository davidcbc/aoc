f = open(r"2015/python/day3-input.txt", "r")
dirs = [c for c in f.readline().strip()]

x = 0
y = 0
cords = set()
cords.add(str([x,y]))
for dir in dirs:
    if dir == '>':
        x += 1
    if dir == '<':
        x -= 1
    if dir == '^':
        y += 1
    if dir == 'v':
        y -= 1
    cords.add(str([x,y]))
print(len(cords))

cords = set()
x1 = 0
y1 = 0
x2 = 0
y2 = 0
cords.add(str([x1,y1]))
santa = True
for dir in dirs:
    if santa:
        if dir == '>':
            x1 += 1
        if dir == '<':
            x1 -= 1
        if dir == '^':
            y1 += 1
        if dir == 'v':
            y1 -= 1
        cords.add(str([x1,y1]))
        santa = False
    else:
        if dir == '>':
            x2 += 1
        if dir == '<':
            x2 -= 1
        if dir == '^':
            y2 += 1
        if dir == 'v':
            y2 -= 1 
        cords.add(str([x2,y2]))
        santa = True

print(len(cords))