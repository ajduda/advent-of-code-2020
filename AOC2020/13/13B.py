with open('input.txt') as inp:
    s = inp.read().split('\n')
    nums = []
    bigs = []
    i = 0
    for x in s[1].split(','):
        if x != 'x':
            nums.append((int(x),i))
        i += 1

interval = 1
ans = 0
for i in range(0, len(nums)):
    while (ans + nums[i][1]) % nums[i][0] != 0:
        ans += interval
    interval *= nums[i][0]
    print(ans)

print(ans)







#Brute forces below
"""
n = big - nums[i][1]
while True:
    valid = True
    for i in nums:
        if(n + i[1]) % i[0] != 0:
            valid = False
            break
    if valid:
        print(n)
        exit()
    n += big
    print(n)
"""


"""n = 2
while True:
    valid = True
    for i in nums:
        if (n + i[1]) % i[0] != 0:
            valid = False
            break
    if valid:
        print(n)
        exit()
    n += 1
"""