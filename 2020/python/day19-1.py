import re
f = open(r"2020/python/day19-input.txt", "r")

everything = f.read().split("\n")

for i in range(len(everything)):
    line = everything[i].strip()
    if line == "":
        break
    tokens = line.split(": ")
    everythingString = "\n".join(everything)
    everything = re.sub(" " + tokens[0] + "(\\b)", " ( " + tokens[1] + " )", everythingString).split("\n")

rulesString = "\n".join(everything[0:137]).replace("( \"a\" )", "a").replace("( \"b\" )", "b").replace(" ", "")

print(rulesString)

rules = {}
for line in rulesString.split("\n"):
    tokens = line.split(":")
    rules[tokens[0]] = tokens[1]

count = 0
for i in range(138,len(everything)):
    if re.match("^" + rules["0"] + "$", everything[i]):
        count += 1
print(count)
