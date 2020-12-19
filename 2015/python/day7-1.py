f = open(r"2015/python/day7-input.txt", "r")

def processInstruction(instructions, label, instruction, cache):
    print(str(instruction) + " -> " + label)
    if label in cache:
        return cache[label]
    elif len(instruction) == 1:
        if instruction[0].isdigit():
            return int(instruction[0])
        cache[label] = processInstruction(instructions, instruction[0], instructions[instruction[0]], cache)
    elif len(instruction) == 2:
        cache[label] =  ~processInstruction(instructions, instruction[1], instructions[instruction[1]], cache)
    elif instruction[1] == "AND":
        l = 0
        if instruction[0].isdigit():
            l = int(instruction[0])
        else:
            l = processInstruction(instructions, instruction[0],instructions[instruction[0]], cache)
        cache[label] = l & processInstruction(instructions, instruction[2],instructions[instruction[2]], cache) 
    elif instruction[1] == "OR":
        cache[label] =  processInstruction(instructions, instruction[0], instructions[instruction[0]], cache) | processInstruction(instructions, instruction[2],instructions[instruction[2]], cache) 
    elif instruction[1] == "RSHIFT":
        cache[label] =  processInstruction(instructions, instruction[0],instructions[instruction[0]], cache) >> int(instruction[2])
    elif instruction[1] == "LSHIFT":
        cache[label] =  processInstruction(instructions, instruction[0],instructions[instruction[0]], cache) << int(instruction[2])
    return cache[label]

instructions = {}
for l in f:
    tokens = l.strip().split(" -> ")
    instructions[tokens[1]] = tokens[0].split()

instruction = instructions['a']

cache = {}
a = processInstruction(instructions, 'a', instruction, cache)
instructions['b'] = [str(a)]
print(a)
cache = {}
a = processInstruction(instructions, 'a', instruction, cache)
print(a)

