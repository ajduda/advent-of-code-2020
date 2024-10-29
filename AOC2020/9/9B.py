preamble = 25

with open('input.txt') as inp:
    numbers = []
    for line in inp:
        numbers.append(int(line))

for i in range(preamble, len(numbers)):
    valid = False
    for j in range(i-preamble,i):
        for k in range(i-preamble,i):
            if j == k:
                continue
            if numbers[i] == numbers[j] + numbers[k]:
                valid = True
    if valid == False:
        invalid = numbers[i]
        break

print(invalid)

for j in range(0,i):
    for k in range(j+1,i):
        if invalid == sum(numbers[j:k]):
            print(min(numbers[j:k]))
            print(max(numbers[j:k]))
            print((min(numbers[j:k]) + max(numbers[j:k])))