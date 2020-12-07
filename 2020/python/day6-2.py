f = open(r"2020\python\day6-input.txt", "r")

questions = set()
total = 0
first = True
for line in f:
    line = line.strip()
    if line == "":
        total += len(questions)
        print(len(questions))
        first = True
        continue
    if first:
        first = False
        questions = set(line)
    else:
        lineSet = set(line)
        questions = questions.intersection(lineSet)

total += len(questions)
print(total)
