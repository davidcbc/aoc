f = open("day1-input1.txt", "r")
values = []
for line in f:
    values.append(int(line))

for val in values:
    need = 2020 - val
    for val2 in values:
        if (need - val2) in values:
            print (val*val2*(need-val2))
            exit
        