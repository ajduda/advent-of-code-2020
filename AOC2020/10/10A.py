with open('input.txt') as inp:
    numbers = [0]
    for line in inp:
        numbers.append(int(line))

numbers.sort()
numbers.append(numbers[len(numbers)-1] + 3)

diff = [0,0,0,0]

for i in range(0,len(numbers)-1):
    diff[numbers[i+1] - numbers[i]] += 1

print(diff)
print()
print(diff[1] * diff[3])