def printNice(active):
    maxX = -1000
    minX = 1000
    maxY = -1000
    minY = 1000
    maxZ = -1000
    minZ = 10
    for coord in active:
        (x,y,z) = coord
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y
        if z < minZ:
            minZ = z
        if z > maxZ:
            maxZ = z
    diffX = maxX - minX + 1
    diffY = maxY - minY + 1
    diffZ = maxZ - minZ + 1
    for z in range(minZ,maxZ+1):
        print('z=' + str(z))
        for y in range(minY,maxY+1):
            s = ''
            for x in range(minX, maxX+1):
                if (x,y,z) in active:
                    s += '#'
                else:
                    s += '.'
            print(s)
        print()


def neighbors(coord):
    (x,y,z) = coord
    ret = set()
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                ret.add((x+i,y+j,z+k))
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
            active.add((x,y,0))
        x += 1
    y += 1


for i in range(0,6):
    #print('cycle ' + str(i) + '\n')
    #printNice(active)
    #print('\n\n')
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

#printNice(active)

print(len(active))