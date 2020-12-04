f = open("day1-input1.txt", "r")
values = []
for line in f:
    val = int(line)
    if (2020 - val) in values:
        print((val * (2020-val)))
        exit
    values.append(val)
