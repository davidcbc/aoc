f = open("day2-input1.txt", "r")
valid = 0
for line in f:
    split = line.split()
    range = split[0].split('-')
    min = int(range[0])
    max = int(range[1])
    letter = split[1][0]
    password = split[2]

    print(str(min) + " " + str(max) + " " + letter + " " + password)
    count = password.count(letter)
    if count >= min and count <= max:
        valid += 1

print(valid)