input = [2,5,3,1,4,9,8,6,7]

#input = [3,8,9,1,2,5,4,6,7]

i = 0
for _ in range(100):
    pickedUp = input[1:4]
    temp = [input[0]]
    temp.extend(input[4:])
    v = temp[0]-1
    while v not in temp:
        v-=1
        if v <= 0:
            v = 9 
    index = temp.index(v)
    input = temp[:index+1]
    input.extend(pickedUp)
    input.extend(temp[index+1:])
    input.append(input.pop(0))
    i += 1
    i %= len(input)


print("".join(str(c) for c in input[input.index(1)+1:]) + "".join(str(c) for c in input[:input.index(1)]))
