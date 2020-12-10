f = open(r"2020/python/day10-test.txt", "r")

adapters = [int(i.strip()) for i in f.readlines()]
adapters.append(0)
adapters = sorted(adapters)
adapters.append(adapters[len(adapters)-1] + 3)        
prev = 0
ones = 0
threes = 0
for x in adapters:
    if x - prev == 1: ones += 1
    if x - prev == 3: threes += 1
    prev = x
print(ones)
print(threes)
print((ones*threes))

