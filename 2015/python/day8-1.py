import re

f = open(r"2015/python/day8-input.txt", "r")

chars = 0
bytes = 0 
escaped = 0

for line in f:
    line = line.strip()
    chars += len(line)
    escaped += len(line) + line.count("\"") + line.count("\\") + 2
    print(re.escape("\"" + line + "\""))
    line = re.sub(r"\\x[a-f0-9]{2}", "x", line)
    line = line.replace("\\\"", "\"")
    line = line.replace("\\\\", "\\")
    bytes += len(line[1:-1])
print(chars)
print(bytes)
print(chars - bytes)

print(escaped)
print(escaped - chars)