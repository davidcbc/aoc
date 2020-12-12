import copy

f = open(r"2020/python/day11-input.txt", "r")

def adjacentSeatsEmpty(seats, x, y):
    return adjacentSeatsTakenCount(seats, x, y) == 0
    
def adjacentSeatsTakenCount(seats, x, y):
    return sum([not seatEmpty(seats, x-1, y-1, 'NW'),
                 not seatEmpty(seats, x-1, y, 'W'), 
                not seatEmpty(seats, x-1, y+1, 'SW'),
                not seatEmpty(seats, x, y-1, 'N'),
                not seatEmpty(seats, x, y+1, 'S'),
                not seatEmpty(seats, x+1, y-1, 'NE'),
                not seatEmpty(seats, x+1, y, 'E'),
                not seatEmpty(seats, x+1, y+1, 'SE')])

def seatEmpty(seats,x,y,dir):
    if x < 0 or y < 0 or x == len(seats) or y == (len(seats[x])):
        return True
    if seats[x][y] == 'X':
        return False
    if seats[x][y] == 'L':
        return True
    nextX = x
    nextY = y
    if 'N' in dir:
        nextY -= 1
    if 'S' in dir:
        nextY += 1
    if 'E' in dir:
        nextX += 1
    if 'W' in dir:
        nextX -= 1
    return seatEmpty(seats, nextX, nextY, dir)


seats = [[c for c in line.strip()] for line in f]
changed = True
count = 0
while changed:
    changed = False
    count = 0
    newSeats = copy.deepcopy(seats)
    for x in range(len(newSeats)):
        for y in range(len(newSeats[x])):
            if seats[x][y] == 'L' and adjacentSeatsEmpty(seats, x, y):
                changed = True
                newSeats[x][y] = 'X'
            if seats[x][y] == 'X' and adjacentSeatsTakenCount(seats, x, y) >= 5:
                changed = True
                newSeats[x][y] = 'L'
            if newSeats[x][y] == 'X':
                count += 1
    seats = copy.deepcopy(newSeats)

print(count)
    
            
