with open('input.txt') as inp:
    s = inp.read()

foods = set()
allergens = set()
lines = []

for line in s.split('\n'):
    if len(line) == 0:
        continue
    lines.append([set(),set()])
    l,r = line.split(' (contains ')
    r = r[:-1]

    for food in l.split(' '):
        foods.add(food)
        lines[-1][0].add(food)
    for allergen in r.split(', '):
        allergens.add(allergen)
        lines[-1][1].add(allergen)

safeFoods = foods.copy()

for allergen in allergens:
    possibleFoods = set()
    for line in lines:
        if allergen in line[1]:
            if len(possibleFoods) == 0:
                possibleFoods = line[0]
            else:
                possibleFoods = possibleFoods.intersection(line[0])
    for food in possibleFoods:
        if food in safeFoods:
            safeFoods.remove(food)


for food in safeFoods:
    for line in lines:
        if food in line[0]:
            line[0].remove(food)

known = {}
while len(known) < len(allergens):
    for allergen in allergens:
        if allergen in known:
            continue
        possibleFoods = set()
        for line in lines:
            if allergen in line[1]:
                if len(possibleFoods) == 0:
                    possibleFoods = line[0]
                else:
                    possibleFoods = possibleFoods.intersection(line[0])
        if len(possibleFoods) == 1:
            food = possibleFoods.pop()
            known[allergen] = food
            for line in lines:
                if food in line[0]:
                    line[0].remove(food)
                if allergen in line[1]:
                    line[1].remove(allergen)

answer = []
for key in known.keys():
    answer.append((key, known[key]))

answer.sort()
s = ''
for item in answer:
    s += item[1]
    s += ','

print(s[:-1])