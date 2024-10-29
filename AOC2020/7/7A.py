numbers = ['0','1','2','3','4','5','6','7','8','9'] #old, bad way to find this

with open('test.txt') as inp:
    tree = {}
    for l in inp:
        line = l.replace('bags', '')
        line = line.replace('bag', '')
        line = line.replace(' .\n','')
        left,right = line.split('  contain ')
        value = []
        for v in right.split(' , '):
            if v[0] in numbers:
                amt = int(v[0])
                name = v[2:]
            else:
                amt = 0
                name = 'EMPTY'
            value.append((amt,name))
        tree[left] = value

print(tree)
print()

answer = 0
magic = 'shiny gold'
for k in tree.keys():
    queue = [k]
    while len(queue) > 0:
        val = queue.pop(0)
        contains = tree[val]
        found = False
        for item in contains:
            if item[0] == 0:
                break
            if item[1] == magic:
                found = True
            else:
                queue.append(item[1])
        if found:
            answer += 1
            break
print(answer)