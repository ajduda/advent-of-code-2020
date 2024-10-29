with open('input.txt') as inp:
    directions = []
    for line in inp:
        directions.append((line[0],int(line[1:])))

x = 0
y = 0
facing = 0 #unit circle directions, 0-1-2-3 is ENWS
for d in directions:
    if d[0] == 'F':
        if facing == 0:
            x += d[1]
        if facing == 1:
            y += d[1]
        if facing == 2:
            x -= d[1]
        if facing == 3:
            y -= d[1]
    elif d[0] == 'L':
        facing += d[1] / 90
        facing %= 4
    elif d[0] == 'R':
        facing -= d[1] / 90
        facing %= 4
    elif d[0] == 'N':
        y += d[1]
    elif d[0] == 'S':
        y -= d[1]
    elif d[0] == 'E':
        x += d[1]
    elif d[0] == 'W':
        x -= d[1]
    else:
        print('ERROR!')
        exit()

print(abs(x) + abs(y))
