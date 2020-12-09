import math
f = open(r"2020/python/day9-input.txt", "r")

lines = [int(i.strip()) for i in f.readlines()]
numlist = []
target = None

for value in lines:
    if len(numlist) < 25:
        numlist.append(value)
        continue
    
    found = False
    for v in numlist:
        if (value - v) in numlist:
            found = True
    if not found:
        print(value)
        target = value
        break
    numlist.pop(0)
    numlist.append(value)

current = 0
earliest = 0
i = 0
while True:
    if current < target:
        current += lines[i]
        i += 1
    elif current > target:
        current -= lines[earliest]
        earliest += 1
    else:
        break

print(min(lines[earliest:i+1])+max(lines[earliest:i+1]))
    
