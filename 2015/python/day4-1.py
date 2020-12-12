import hashlib

f = open(r"2015/python/day4-input.txt", "r")

input = f.readline().strip()
hash = hashlib.md5(input.encode()).hexdigest()
counter = 0
while hash[0:6] != "000000":
    counter += 1
    hash = hashlib.md5((input + str(counter)).encode()).hexdigest()
print(counter)