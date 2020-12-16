f = open(r"2020\python\day16-input.txt", "r")

line = f.readline().strip()
rules = {}
while line != "":
    tokens = line.split(": ")
    ranges = tokens[1].split(" or ")
    range1 = ranges[0].split("-")
    range2 = ranges[1].split("-")
    rules[tokens[0]] = [(int(range1[0]), int(range1[1])), (int(range2[0]), int(range2[1]))]
    line = f.readline().strip()

f.readline()
tickets = [f.readline().strip().split(",")]
f.readline()
f.readline()

print(tickets)
invalid = 0
for line in f:
    values = line.strip().split(",")
    ticketValid = True
    for v in values:
        valid = False
        for rule in rules.items():
            for r in rule[1]:
                if int(v) >= r[0] and int(v) <= r[1]:
                    valid = True
        if not valid:
            ticketValid = False
            invalid += int(v)
    if ticketValid:
        tickets.append(values)

print(invalid)

print(len(tickets))

fields = {}
for i in range(len(tickets[0])):
    fields[i] = []
    for j in range(len(rules)):
        fields[i].append(j)

for ticket in tickets:
    for i in range(len(ticket)):
        for j in range(len(rules)):
            rule = list(rules.values())[j]
            valid = False
            for r in rule:
                if int(ticket[i]) >= r[0] and int(ticket[i]) <= r[1]:
                    valid = True
            if not valid:
                if j in fields[i]:
                    fields[i].remove(j)

done = False
while not done:
    done = True
    for i in range(len(fields)):
        if len(fields[i]) != 1:
            done = False
            continue
        v = fields[i][0]
        for j in range(len(fields)):
            if i == j:
                continue
            if v in fields[j]:
                fields[j].remove(v)
print(fields)

final = 0
for i in range(len(tickets[0])):
    if "departure" in list(rules.items())[fields[i][0]][0]:
        if final == 0:
            final = int(tickets[0][i])
        else:
            final *= int(tickets[0][i])
print(final)
        


