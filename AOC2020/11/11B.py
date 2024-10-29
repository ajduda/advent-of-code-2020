def printNice(l):
    s = ''
    for a in l:
        for b in a:
            s += b
        s += '\n'
    print()
    print(s)
    print()

with open('input.txt') as inp:
    seats = []
    for line in inp:
        seats.append([])
        for char in line.strip():
            seats[-1].append(char)

didChange = True
maxI = len(seats)
maxJ = len(seats[0])
while didChange:
    didChange = False
    changes = []
    for seatrow in seats:
        changes.append(seatrow.copy())
    for i in range(0,maxI):
        for j in range(0,maxJ):
            if seats[i][j] == '.':
                continue
            visible = 0
            
            a = i - 1
            b = j
            while a >= 0:
                if seats[a][b] == 'L':
                    break
                if seats[a][b] == '#':
                    visible += 1
                    break
                a -= 1

            a = i - 1
            b = j - 1
            while a >= 0 and b >= 0:
                if seats[a][b] == 'L':
                    break
                if seats[a][b] == '#':
                    visible += 1
                    break
                a -= 1
                b -= 1

            a = i
            b = j - 1
            while b >= 0:
                if seats[a][b] == 'L':
                    break
                if seats[a][b] == '#':
                    visible += 1
                    break
                b -= 1

            a = i + 1
            b = j - 1
            while a < maxI and b >= 0:
                if seats[a][b] == 'L':
                    break
                if seats[a][b] == '#':
                    visible += 1
                    break
                a += 1
                b -= 1

            a = i + 1
            b = j
            while a < maxI:
                if seats[a][b] == 'L':
                    break
                if seats[a][b] == '#':
                    visible += 1
                    break
                a += 1

            a = i + 1
            b = j + 1
            while a < maxI and b < maxJ:
                if seats[a][b] == 'L':
                    break
                if seats[a][b] == '#':
                    visible += 1
                    break
                a += 1
                b += 1

            a = i
            b = j + 1
            while b < maxJ:
                if seats[a][b] == 'L':
                    break
                if seats[a][b] == '#':
                    visible += 1
                    break
                b += 1

            a = i - 1
            b = j + 1
            while a >= 0 and b < maxJ:
                if seats[a][b] == 'L':
                    break
                if seats[a][b] == '#':
                    visible += 1
                    break
                a -= 1
                b += 1


            if visible == 0 and seats[i][j] == 'L':
                changes[i][j] = '#'
                didChange = True
            if visible > 4 and seats[i][j] == '#':
                changes[i][j] = 'L'
                didChange = True
    
    #print('saving new seats')
    seats = []
    for changeRow in changes:
        seats.append(changeRow.copy())

ans = 0

for i in range(0,maxI):
    for j in range(0, maxJ):
        if seats[i][j] == '#':
            ans += 1

printNice(seats)

print(ans)
