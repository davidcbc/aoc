# order = [1,2,3]
order = [6,13,1,15,2,0]
whenSaid = {}
for i in range(len(order)):
    whenSaid[order[i]] = [i]

for i in range(30000000-len(order)):
    last = order[len(order)-1]
    if len(whenSaid[last]) == 1:
        order.append(0)
        if 0 not in whenSaid:
            whenSaid[0] = []
        whenSaid[0].append(len(order)-1)
    else:
        number = whenSaid[last][-1] - whenSaid[last][-2]
        order.append(number)
        if(number not in whenSaid):
            whenSaid[number] = []
        whenSaid[number].append(len(order)-1)
print(order[-1])
#print(len(order))
    


