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

#print(foods)
#print(allergens)
#print(lines)

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
    #print(f'allergen: {allergen}   possible foods: {possibleFoods}')

#print(safeFoods)

ans = 0

for food in safeFoods:
    for line in lines:
        if food in line[0]:
            ans += 1

print(ans)