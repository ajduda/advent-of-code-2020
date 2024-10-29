with open('input.txt') as inp:
    ans = 0
    for line in inp:
        l = line.split(' ')
        password = l[2]
        letter = l[1][0] #Just the letter in x:
        bounds = l[0].split('-')
        lower = int(bounds[0])
        upper = int(bounds[1])
        count = 0
        
        for c in password:
            if c == letter:
                count += 1
        if count >= lower and count <= upper:
            ans += 1
    print(ans)