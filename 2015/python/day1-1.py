f = open(r"2015\python\day1-input.txt", "r")
line = f.readline()
floor = 0
i = 0
basement = None
for c in line:
    i += 1
    if c == "(":
        floor += 1
    if c == ")":
        floor -= 1
    if basement == None and floor < 0:
        basement = i
print(floor)
print(basement)