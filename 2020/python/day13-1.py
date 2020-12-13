f = open(r"2020/python/day13-input.txt", "r")

start = int(f.readline())
buses = f.readline().strip().split(",")

min = 9999999
minBus = 9999999
for bus in buses:
    if bus == 'x':
        continue
    minutes = int(bus)
    minutesTilNext = minutes - (start%minutes)
    if minutesTilNext < min:
        min = minutesTilNext
        minBus = minutes

print(minBus*min)

bnum = []
brem = []
for i in range(len(buses)):
    if buses[i] == 'x':
        continue
    bnum.append(int(buses[i]))
    brem.append(int(buses[i])-i)
    while brem[len(brem)-1] < 0:
        brem[len(brem)-1] += int(buses[i])

# Borrowed code that implements Chinese Remainder Theorem using
# modular inverses.
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def findMinX(num, rem) :
    prod = 1
    for i in range(0, len(num)) : 
        prod = prod * num[i] 
    result = 0
    for i in range(0,len(num)): 
        pp = prod // num[i] 
        result = result + rem[i] * modinv(pp, num[i]) * pp  
    return result % prod 

print(findMinX(bnum, brem))

    


