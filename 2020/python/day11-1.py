import copy

f = open(r"2020/python/day11-input.txt", "r")

def adjacentSeatsEmpty(seats, x, y):
    return adjacentSeatsTakenCount(seats, x, y) == 0
    
def adjacentSeatsTakenCount(seats, x, y):
    return sum([not seatEmpty(seats, x-1, y-1),
                 not seatEmpty(seats, x-1, y), 
                not seatEmpty(seats, x-1, y+1),
                not seatEmpty(seats, x, y-1),
                not seatEmpty(seats, x, y+1),
                not seatEmpty(seats, x+1, y-1),
                not seatEmpty(seats, x+1, y),
                not seatEmpty(seats, x+1, y+1)])

def seatEmpty(seats,x,y):
    if x < 0 or y < 0 or x == len(seats) or y == (len(seats[x])):
        return True
    return seats[x][y] != 'X'


    

seats = [[c for c in line.strip()] for line in f]
changed = True
count = 0
while changed:
    changed = False
    count = 0
    newSeats = copy.deepcopy(seats)
    for x in range(len(newSeats)):
        for y in range(len(newSeats[x])):
            # print(seats[x][y], end='')
            if seats[x][y] == 'L' and adjacentSeatsEmpty(seats, x, y):
                changed = True
                newSeats[x][y] = 'X'
            if seats[x][y] == 'X' and adjacentSeatsTakenCount(seats, x, y) >= 4:
                changed = True
                newSeats[x][y] = 'L'
            if newSeats[x][y] == 'X':
                count += 1
        #print("")
    seats = copy.deepcopy(newSeats)
    #print("\n\n")
    #input("Press Enter to continue")

print(count)
    
            
