with open('input.txt') as inp:
    instrs = []
    for l in inp:
        line = l.strip()
        op,val = line.split(' ')
        instrs.append((op,int(val)))

target = len(instrs)

for j in range(0, target):
    changeBack = ''
    op = instrs[j][0]
    if op == 'nop':
        instrs[j] = ('jmp',instrs[j][1])
        changeBack = 'nop'
    elif op == 'jmp':
        instrs[j] = ('nop',instrs[j][1])
        changeBack = 'jmp'
    else:
        continue

    visited = set()
    i = 0
    acc = 0
    while i not in visited:
        if i == target:
            print(acc)
            exit()

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
    if len(changeBack) > 0:
        instrs[j] = (changeBack,instrs[j][1])
