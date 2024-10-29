letters = []
for i in range(97,97+26):
    letters.append(chr(i))

with open('input.txt') as inp:
    s = inp.read()

sets = s.split('\n\n')

total = 0
for s in sets:
    x = []
    answers = s.split('\n')
    print(answers)
    for l in letters:
        good = True
        for a in answers:
            if len(a) == 0:
                continue
            if l not in a:
                good = False
        if good:
            total += 1

print(total)