f = open(r"2020/python/day10-input.txt", "r")

adapters = [int(i.strip()) for i in f.readlines()]
adapters.append(0)
adapters = sorted(adapters)
adapters.append(adapters[len(adapters)-1] + 3)        

steps = [0] * len(adapters)
steps[0] = 1
steps[1] = 1
steps[2] = 2
i = 3
print(len(adapters))
while i < len(adapters):
    if adapters[i] - adapters[i-1] <= 3:
        steps[i] += steps[i-1]
    if adapters[i] - adapters[i-2] <= 3:
        steps[i] += steps[i-2]
    if adapters[i] - adapters[i-3] <= 3:
        steps[i] += steps[i-3]
    i += 1

print(steps[len(adapters)-1])

