f = open(r"2015/python/day5-input.txt", "r")

def count(counts, c):
    if c not in counts: return 0
    return counts[c]

def p1nice(line):
    double = False
    prev = ""
    counts = {}
    for c in line:
        if prev != "":
            if (prev+c) in counts:   
                counts[prev+c] += 1
            else: counts[prev+c] = 1
        if c in counts:
            counts[c] += 1
        else: counts[c] = 1
        if prev == c:
            double = True
        prev = c
    return (double and (sum([count(counts,'a'), 
                            count(counts,'e'), 
                            count(counts,'i'), 
                            count(counts,'o'), 
                            count(counts,'u')]) >= 3) 
                        and ('ab' not in counts and 
                             'cd' not in counts and 
                             'pq' not in counts and 
                             'xy' not in counts))

def p2nice(line):
    counts = {}
    i = 0
    double = False
    duplicatePair = False
    for c in line:
        if i-1 >= 0:
            if (line[i-1]+c) in counts:
                if i - line.find(line[i-1]+c) > 2:
                    duplicatePair = True
                counts[line[i-1]+c] += 1         
            else: counts[line[i-1]+c] = i
        if i-2 >= 0 and line[i-2] == c:
            double = True
        i += 1
    
    return double and duplicatePair

nicep1 = 0
nicep2 = 0
for line in f:
    line = line.strip()
    if p1nice(line):
        nicep1 += 1
    if p2nice(line):
        nicep2 += 1
print(nicep1)
print(nicep2)