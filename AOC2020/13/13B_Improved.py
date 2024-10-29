with open('input.txt') as inp:
    s = inp.read().split('\n')
    nums = []
    bigs = []
    i = 0
    for x in s[1].split(','):
        if x != 'x':
            nums.append((int(x),i))
        i += 1

interval = nums[0][0]
ans = int(nums[0][1])
for i in range(1, len(nums)):
    while (ans + nums[i][1]) % nums[i][0] != 0:
        ans += interval
    interval *= nums[i][0]
    print(ans)

print(ans)
