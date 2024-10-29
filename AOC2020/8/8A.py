with open('input.txt') as inp:
    instrs = []
    for l in inp:
        line = l.strip()
        op,val = line.split(' ')
        instrs.append((op,int(val)))

visited = set()
i = 0
acc = 0
while i not in visited:
    op = instrs[i][0]
    if op == 'nop':
        visited.add(i)
        i += 1
    elif op == 'acc':
        acc += instrs[i][1]
        visited.add(i)
        i += 1
    elif op == 'jmp':
        visited.add(i)
        i += instrs[i][1]
    else:
        print('error!')
        exit()

print(acc)