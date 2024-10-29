with open('input.txt') as inp:
    s = inp.read()

sets = s.split('\n\n')

total = 0
for s in sets:
    x = set()
    chars = s.replace('\n','')
    for char in chars:
        x.add(char)
    total += len(x)
print(total)