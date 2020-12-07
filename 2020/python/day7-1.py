f = open(r"2020\python\day7-input.txt", "r")

adjacency = {}

for line in f:
    split = line.strip().split(" contain ")
    # Drop "bags" from key
    key = " ".join(split[0][:-5].split()[0:2])
    rawValues = split[1].split(", ")
    # Drop "." from the end
    rawValues[-1] = rawValues[-1][:-1]
    values = []
    for value in rawValues:
        if value == "no other bags":
            continue
        splitValue = value.split()
        num = int(splitValue[0])
        # Drop bags from the end
        color = " ".join(splitValue[1:3])
        values.append([color, num])
    adjacency[key] = values
    
queue = []
for v in adjacency.keys():
    queue.append([v, []])

visited = set()
paths = set()
canContain = set()
while len(queue) > 0:
    v = queue.pop(0)
    key = v[0]
    path = v[1]
    if key == "shiny gold":
        for p in path:
            canContain.add(p)
    visited.add(key)
    if key in path:
        continue
    path.append(key)
    if str(path) in paths:
        continue
    paths.add(str(path))
    for t in adjacency[key]:
        queue.append([t[0], path.copy()])

print(len(canContain))

total = 0
for v in adjacency["shiny gold"]:
    queue.append(v)
    total += v[1]

while len(queue) > 0:
    v = queue.pop(0)
    key = v[0]
    num = v[1]
    for w in adjacency[key]:
        queue.append([w[0], w[1]*num])
        total += w[1]*num

print(total)
            

