f = open(r"2015\python\day2-input.txt", "r")

total = 0
ribbon = 0
for line in f:
    dims = line.split("x")
    l = int(dims[0])
    w = int(dims[1])
    h = int(dims[2])
    print(dims)
    total += (2*l*w + 2*w*h + 2*h*l)
    total += min(l*w,w*h,h*l)
    ribbon += min((2*l+2*w), (2*w+2*h), (2*l+2*h)) + l*w*h

print(total)
print(ribbon)