f = open(r"2020\python\day8-input.txt", "r")

instructions = []
for line in f:
    tokens = line.strip().split()
    instructions.append([tokens[0], int(tokens[1])])


inst = instructions[0]
acc = 0
i = 0
visited = set()
while True:
    print(inst)
    if i in visited:
        print(acc)
        break
    visited.add(i)
    if inst[0] == "acc":
        acc += inst[1]
        i+=1
        inst = instructions[i]
        continue
    if inst[0] == "jmp":
        i += inst[1]
        inst = instructions[i]
        continue
    if inst[0] == "nop":
        i += 1
        inst = instructions[i]
