import sys
f = open(r"2020\python\day8-input.txt", "r")

instructions = []
for line in f:
    tokens = line.strip().split()
    instructions.append([tokens[0], int(tokens[1])])

for instruction in instructions:
    if instruction[0] == "nop":
        instruction[0] = "jmp"
    elif instruction[0] == "jmp":
        instruction[0] = "nop"
    inst = instructions[0]
    acc = 0
    i = 0
    visited = set()
    while True:
        if i in visited:
            break
        visited.add(i)
        if inst[0] == "acc":
            acc += inst[1]
            i+=1
            if i >= len(instructions):
                print(acc)
                sys.exit()
            inst = instructions[i]
            continue
        if inst[0] == "jmp":
            i += inst[1]
            if i >= len(instructions):
                print(acc)
                sys.exit()
            inst = instructions[i]
            continue
        if inst[0] == "nop":
            i += 1
            if i >= len(instructions):
                print(acc)
                sys.exit()
            inst = instructions[i]
    if instruction[0] == "nop":
        instruction[0] = "jmp"
    elif instruction[0] == "jmp":
        instruction[0] = "nop"
