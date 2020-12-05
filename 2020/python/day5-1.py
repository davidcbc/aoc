import math

f = open(r"2020\python\day5-input.txt", "r")

max = 0
seats = []

for line in f:
    line = line.strip()
    rowBsp = line[0:-3]
    colBsp = line[-3:]
    rowMax = 127
    rowMin = 0
    for c in rowBsp:
        mid = (rowMax + rowMin) / 2
        if c == "F":
            rowMax = math.floor(mid)
        else:
            rowMin = math.ceil(mid)
    colMax = 7
    colMin = 0
    for c in colBsp:
        mid = (colMax + colMin) / 2
        if c == "L":
            colMax = math.floor(mid)
        else:
            colMin = math.ceil(mid)
    
    seat = rowMin*8 + colMin
    if seat > max:
        max = seat
    seats.append(seat)
print(max)

seats = sorted(seats)
prevSeat = seats[0]
for seat in seats[1:]:
    if seat - prevSeat > 1:
        print(seat - 1)
    prevSeat = seat
