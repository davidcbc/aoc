import re
import collections

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def validRange(value, min, max):
    return int(value) >= min and int(value) <= max

def validate(passport, part2=False):
    requiredCount = 0
    for field in required:
        if field in passport:
            requiredCount += 1
    isValid = requiredCount == len(required)
    if part2==False or not isValid:
        return isValid

    
    isValid = (validRange(passport["byr"], 1920, 2002)
      and validRange(passport["iyr"], 2010, 2020)
      and validRange(passport["eyr"], 2020, 2030)
      and passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
      and re.match("^[0-9]{9}$", passport["pid"]) != None
      and re.match("^#[0-9a-f]{6}$", passport["hcl"]) != None)

    unit = passport["hgt"][-2:]
    isValid = isValid and unit in ["cm", "in"]
    if unit == "cm":
        isValid = isValid and validRange(passport["hgt"][0:-2], 150, 193)
    elif unit == "in":
        isValid = isValid and validRange(passport["hgt"][0:-2], 59, 76)
    else:
        isValid = False
    
    return isValid
    

f = open(r"2020\python\day4-input.txt", "r")

passport = {}
valid = 0
valid2 = 0
for line in f:
    line = line.strip()
    if line == "":
        if validate(passport):
            valid += 1
        if validate(passport, True):
            valid2 += 1
        passport = {}
        continue
    currentFields = line.split()
    for field in currentFields:
        currentField = field.split(":")
        if currentField[0] in required:
            passport[currentField[0]] = currentField[1]

if validate(passport):
    valid += 1
if validate(passport, True):
    valid2 += 1
print(valid)
print(valid2)