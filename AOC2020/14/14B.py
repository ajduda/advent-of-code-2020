def xAddrs(mask, addr):
    for i in range(0,36):
        j = 35 - i
        if mask[j] == '1':
            addr |= (1 << i)
        if mask[j] == 'X':  #We'll make all cases later
            addr &= ~(1 << i)
    xDict = {}
    n = 1
    for i in range(0,36):
        if mask[i] == 'X':
            xDict[n] = 35 - i
            n *= 2
    if n == 1:
        return [addr]
    ret = []
    for i in range(0, n):
        addrToChange = addr
        for (k,v) in xDict.items():
            if k & i > 0:
                addrToChange |= 1 << v
        ret.append(addrToChange)
    return ret





mem = {}

with open('input.txt') as inp:
    for l in inp:
        line = l.strip()
        if len(line) == 0:
            break
        if line[0:4] == 'mask':
            mask = line.split(' = ')[1]

        elif line[0:3] == 'mem':
            lBound = line.index('[') + 1
            rBound = line.index(']')
            addr = int(line[lBound:rBound])
            val = int(line.split(' = ')[1])
            for xaddr in xAddrs(mask,addr):
                mem[xaddr] = val


print(mem)
ans = 0
for v in mem.values():
    ans += v

print(ans)
