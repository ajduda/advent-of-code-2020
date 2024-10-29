with open('input.txt') as inp:
    for line in inp:
        strNumbers = line.split(',')
    offset = 0
    numbers = []
    last = {}  # index of last usage of a number
    for n in strNumbers:
        last[int(n)] = offset
        offset += 1
        numbers.append(int(n))

holding = numbers.pop()

n = len(numbers)
while len(numbers) < 2020:
    if holding in last:
        temp = n - last[holding]
        last[holding] = n
        numbers.append(holding)
        holding = temp
    else:
        last[holding] = n
        numbers.append(holding)
        holding = 0
    n += 1

    #print(numbers)




#print(last)
print(numbers[-1])