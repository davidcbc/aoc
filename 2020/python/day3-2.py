f = open("day3-input.txt", "r")
slope = f.readlines()
right = [1,3,5,7,1]
down = [1,1,1,1,2]
i = 0
result = 0

for r in right:
    tree = 0
    d = down[i]
    i = i+1
    lc = 1
    x = 0
    for line in slope:
        lc += 1
        if lc < d:
            continue
        else:
            lc = 0
        line = line.strip()
        if line[x] == '#':
            tree += 1
        x = (x + r) % len(line)
    print(tree)
    if result == 0:
        result = tree
    else:
        result *= tree
    

print(result)