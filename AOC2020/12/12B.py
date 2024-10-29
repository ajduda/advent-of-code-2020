with open('input.txt') as inp:
    directions = []
    for line in inp:
        directions.append((line[0],int(line[1:])))

x = 0
y = 0
wayX = 10
wayY = 1
for d in directions:
    if d[0] == 'F':
        x += wayX * d[1]
        y += wayY * d[1]
    elif d[0] == 'L':
        for i in range(0,int(d[1] / 90)):
            t = wayX
            wayX = wayY * -1
            wayY = t
    elif d[0] == 'R':
        for i in range(0,int(d[1] / 90)):
            t = wayX
            wayX = wayY
            wayY = t * -1
    elif d[0] == 'N':
        wayY += d[1]
    elif d[0] == 'S':
        wayY -= d[1]
    elif d[0] == 'E':
        wayX += d[1]
    elif d[0] == 'W':
        wayX -= d[1]
    else:
        print('ERROR!')
        exit()

print(abs(x) + abs(y))
