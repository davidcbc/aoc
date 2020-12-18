f = open(r"2020/python/day18-input.txt", "r")
        
def doMathNoParens(statement):
    newStatement = []
    statement = doAllAddition(statement)
    v = 1
    for i in range(len(statement)):
        if statement[i] != "*":
            v *= int(statement[i])
    newStatement.append(str(v))
    return newStatement
    

def doAllAddition(statement):
    newStatement = []
    toAdd = []
    for i in range(len(statement)):
        if statement[i] == "*":
            newStatement.append(str(sum(toAdd)))
            newStatement.append("*")
            toAdd = []
        elif statement[i] != "+":
            toAdd.append(int(statement[i]))
    if len(toAdd) > 0:
        newStatement.append(str(sum(toAdd)))
    return newStatement
    
def doMath(statement):
    while '(' in statement:
        end = statement.index(')')
        snippet = statement[:end]
        snippet.reverse()
        start = end - (snippet.index('('))
        value = doMathNoParens(statement[start:end])
        statement = statement[:start-1] + value + statement[end+1:]
    return int(doMathNoParens(statement)[0])

total = 0
for line in f:
    total += doMath([c for c in "".join(line.split())])
print(total)
