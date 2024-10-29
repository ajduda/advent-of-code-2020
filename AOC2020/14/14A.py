mem = {}

with open('input.txt') as inp:
    for l in inp:
        line = l.strip()
        if len(line) == 0:
            break
        if line[0:4] == 'mask':
            mask = line.split(' = ')[1]
            mask1 = 0
            mask0 = 0
            for i in range(0,36):
                j = 35 - i
                if mask[j] == '1':
                    mask1 |= (1 << i)
                if mask[j] == '0':
                    mask0 |= (1 << i)


        elif line[0:3] == 'mem':
            lBound = line.index('[') + 1
            rBound = line.index(']')
            addr = int(line[lBound:rBound])
            val = int(line.split(' = ')[1])
            val &= ~mask0
            val |= mask1
            mem[addr] = val
        else:
            print('ERROR!')
            print(l)
            print('ERROR!')


print(mem)
ans = 0
for v in mem.values():
    ans += v

print(ans)
