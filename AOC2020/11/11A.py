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
    #printNice(seats)
    didChange = False
    changes = []
    for seatrow in seats:
        changes.append(seatrow.copy())
    for i in range(0,maxI):
        for j in range(0,maxJ):
            if seats[i][j] == '.':
                continue
            nearbyOccupied = 0
            if i > 0:
                nearbyOccupied += 1 if seats[i-1][j] == '#' else 0
            if i > 0 and j > 0:
                nearbyOccupied += 1 if seats[i-1][j-1] == '#' else 0
            if j > 0:
                nearbyOccupied += 1 if seats[i][j-1] == '#' else 0
            if j > 0 and i < maxI-1:
                nearbyOccupied += 1 if seats[i+1][j-1] == '#' else 0
            if i < maxI-1:
                nearbyOccupied += 1 if seats[i+1][j] == '#' else 0
            if i < maxI - 1 and j < maxJ - 1:
                nearbyOccupied += 1 if seats[i+1][j+1] == '#' else 0
            if j < maxJ - 1:
                nearbyOccupied += 1 if seats[i][j+1] == '#' else 0
            if i > 0 and j < maxJ - 1:
                nearbyOccupied += 1 if seats[i-1][j+1] == '#' else 0
            
            if nearbyOccupied == 0 and seats[i][j] == 'L':
                changes[i][j] = '#'
                didChange = True
            if nearbyOccupied > 3 and seats[i][j] == '#':
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

print(ans)
