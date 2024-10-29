def neighbors(coord):
    (x,y,z,w) = coord
    ret = set()
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                for l in range(-1,2):
                    ret.add((x+i,y+j,z+k,w+l))
    ret.remove(coord)
    return ret

with open('input.txt') as inp:
    s = inp.read()

active = set()

y = 0
for line in s.split('\n'):
    x = 0
    for c in line:
        if c == '#':
            active.add((x,y,0,0))
        x += 1
    y += 1

for i in range(0,6):
    inactive = set()
    for cell in active:
        for neighbor in neighbors(cell):
            if neighbor not in active:
                inactive.add(neighbor)
    nextActive = set()
    
    for cell in active:
        numNeighbor = 0
        for neighbor in neighbors(cell):
            if neighbor in active:
                numNeighbor += 1
        if numNeighbor == 2 or numNeighbor == 3:
            nextActive.add(cell)

    for cell in inactive:
        numNeighbor = 0
        for neighbor in neighbors(cell):
            if neighbor in active:
                numNeighbor += 1
        if numNeighbor == 3:
            nextActive.add(cell)
    active = nextActive.copy()

print(len(active))