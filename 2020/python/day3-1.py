f = open("day3-input.txt", "r")
x = 0
tree = 0
for line in f:
    line = line.strip()
    print(line)
    print(x)
    if line[x] == '#':
        tree += 1
    x = (x + 3) % len(line)
    
print(tree)