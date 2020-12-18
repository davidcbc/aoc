f = open(r"2020\python\day18-input.txt", "r")

def doMath(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    return num1 * num2
        
def doTheThing(thing):
    print(thing)
    value = 0
    i = 0
    operator = "+"
    while i < len(thing):
        if thing[i] == '(':
            num, offset = doTheThing(thing[i+1:])
            print("i: " + str(i) + " offset: " + str(offset) + " num: " + str(num))
            i += offset + 1
            value = doMath(value, num, operator)            
        elif thing[i] == ')':
            print("returning: " + str(value) + ", " + str(i))
            return value, i
        elif thing[i] == '*' or thing[i] == '+':
            operator = thing[i]
        else:
            print("Doing math: " + str(value) + operator + thing[i])
            value = doMath(value, int(thing[i]), operator)
        i+=1
        
    return value, i             

total = 0
for line in f:
    total += doTheThing("".join(line.split()))[0]
print(total)