with open('input.txt') as inp:
    numbers = []
    for line in inp:
        numbers.append(int(line))
numbers.sort()

print(numbers)
l = 0
r = len(numbers) - 1

while numbers[l] + numbers[r] != 2020:
    if numbers[l] + numbers[r] < 2020:
        l += 1
    else:
        r -= 1
    if r <= l:
        print("This broke, blame Justin")
        exit()

print(numbers[l] * numbers[r])