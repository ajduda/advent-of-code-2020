with open('input.txt') as inp:
    s = inp.read().split('\n')
    early = int(s[0])
    nums = []
    for x in s[1].split(','):
        if x != 'x':
            nums.append(int(x))
close = 9999999

for n in nums:
    val = (early // n) + 1
    if n*val - early < close:
        close = n*val - early
        best = n

print(best * close)