with open('input.txt') as inp:
    numbers = []
    for line in inp:
        numbers.append(int(line))
#numbers.sort()

a = 0
b = 0
c = 0
while a < len(numbers):
    b = 0
    while b < len(numbers):
        c = 0
        while c < len(numbers):
            if numbers[a] + numbers[b] + numbers[c] == 2020:
                print(numbers[a] * numbers[b] * numbers[c])
                exit()
            c += 1
        b += 1
    a += 1
print("It broke and it's justin's fault")