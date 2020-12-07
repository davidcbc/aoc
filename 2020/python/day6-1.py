f = open(r"2020\python\day6-input.txt", "r")

questions = set()
total = 0
for line in f:
    line = line.strip()
    if line == "":
        total += len(questions)
        questions = set()
        continue
    for c in line:
        questions.add(c)

total += len(questions)
print(total)
