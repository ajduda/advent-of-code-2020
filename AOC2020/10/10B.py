with open('input.txt') as inp:
    numbers = [0]
    for line in inp:
        numbers.append(int(line))

numbers.sort()
numbers.append(numbers[len(numbers)-1] + 3)

ways = [1]  # ways[i] represents the number of ways to get to numbers[i]

for i in numbers[1:]:
    myWay = 0
    for j in range(i-3,i):
        if j in numbers:
            index = numbers.index(j)
            myWay += ways[index]
    ways.append(myWay)

print(numbers)
print(ways)
print()
print(ways[-1])