f = open(r"2020/python/day22-input.txt", "r")

player1 = []
player2 = []

f.readline()

for line in f:
    if line.strip() == "":
        break
    player1.append(int(line.strip()))

f.readline()
for line in f:
    if line.strip() == "":
        break
    player2.append(int(line.strip()))


print(player1)
print(player2)

while len(player1) > 0 and len(player2) > 0:
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    else:
        player2.append(p2)
        player2.append(p1)

winner = player1
winner.extend(player2)

print(winner)
total = 0
for i in range(len(winner)):
    total += winner[i]*(len(winner)-i)

print(total)