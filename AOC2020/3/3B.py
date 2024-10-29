def treeCount(input, right, down):
    x = 0
    y = 0
    l = len(input[0])
    depth = len(input)
    ans = 0
    while y < depth:
        if input[y][x] == '#':
            ans += 1
        x += right
        x %= l
        y += down
    return ans

with open('input.txt') as inp:
    strinp = []
    for line in inp:
        strinp.append(line.strip())

a = []
a.append(treeCount(strinp, 1, 1))
a.append(treeCount(strinp, 3, 1))
a.append(treeCount(strinp, 5, 1))
a.append(treeCount(strinp, 7, 1))
a.append(treeCount(strinp, 1, 2))

print(a)
answer = 1
for val in a:
    answer *= val
print(answer)
    