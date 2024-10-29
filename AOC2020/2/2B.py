with open('input.txt') as inp:
    ans = 0
    for line in inp:
        l = line.split(' ')
        password = l[2]
        letter = l[1][0] #Just the letter in x:
        bounds = l[0].split('-')
        lower = int(bounds[0]) - 1
        upper = int(bounds[1]) - 1
        count = 0
        
        if password[lower] == letter:
            count += 1
        if password[upper] == letter:
            count += 1
        if count == 1:
            ans += 1
    print(ans)