f = open(r"2020/python/day14-input.txt", "r")

def getAddresses(fluctmask, i, addresses):
    if i > 35:
        return addresses
    if (fluctmask >> i) & 1 == 1:
        newAddresses = []
        for address in addresses:
            newAddress = address
            newAddress = newAddress & ~(1 << i)
            newAddresses.append(newAddress)
            newAddress = address
            newAddress = newAddress | (1 << i)
            newAddresses.append(newAddress)
        return getAddresses(fluctmask, i+1, newAddresses)
    else:
        return getAddresses(fluctmask, i+1, addresses)



onmask = 0b0
offmask = 0b0
fluctmask = 0b0
addresses = {}
addressesp2 = {}
addresslist = []
for line in f:
    tokens = line.strip().split(" = ")
    if tokens[0] == "mask":
        onmask = 0b0
        offmask = 0b0
        fluctmask = 0b0
        for c in tokens[1]:
            if c == "X":
                onmask = onmask << 1
                offmask = (offmask << 1) + 1
                fluctmask = (fluctmask << 1) + 1
            if c == "1":
                onmask = (onmask << 1) + 1
                offmask = (offmask << 1) + 1
                fluctmask = fluctmask << 1
            if c == "0":
                onmask = onmask << 1
                offmask = offmask << 1
                fluctmask = fluctmask << 1
    else:
        address = int(tokens[0].split(']')[0][4:])
        addresses[address] = int(tokens[1])
        addresses[address] = addresses[address] & offmask
        addresses[address] = addresses[address] | onmask

        address = address | onmask
        newAddresses = sorted(getAddresses(fluctmask, 0, [address]))
        for a in newAddresses:
            addressesp2[a] = int(tokens[1])
            addresslist.append(a)

print(sum(addresses.values()))
print(sum(addressesp2.values()))