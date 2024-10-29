def coordinates(s):  # x is normal, y is positvely sloped
    i = 0
    x = 0
    y = 0
    while i < len(s):
        if s[i] == 'e':
            x += 1
            i += 1
        elif s[i] == 'w':
            x -= 1
            i += 1
        elif s[i:i+2] == 'se':
            x += 1
            y -= 1
            i += 2
        elif s[i:i+2] == 'sw':
            y -= 1
            i += 2
        elif s[i:i+2] == 'ne':
            y += 1
            i += 2
        elif s[i:i+2] == 'nw':
            x -= 1
            y += 1
            i += 2
        else:
            print('ERROR')
            return (0,0)

    return (x,y)


def adjacent(coord):
    ret = set()
    x, y = coord
    ret.add((x+1,y))
    ret.add((x-1,y))
    ret.add((x,y+1))
    ret.add((x,y-1))
    ret.add((x+1,y-1))
    ret.add((x-1,y+1))
    return ret

with open('input.txt') as inp:
    lines = inp.read()

flipped = set()

for line in lines.split('\n'):
    tile = coordinates(line)
    if tile in flipped:
        flipped.remove(tile)
    else:
        flipped.add(tile)


#Now to begin the game of life part
for i in range(0, 100):
    possible = flipped.copy()
    for tile in flipped:
        possible = possible.union(adjacent(tile))
    nextFlipped = set()
    for tile in possible:
        neiughbors = adjacent(tile)
        touching = 0
        for neiughbor in neiughbors:
            if neiughbor in flipped:
                touching += 1
        if touching == 2:
            nextFlipped.add(tile)
        if touching == 1 and tile in flipped:
            nextFlipped.add(tile)
    flipped = nextFlipped

print(len(flipped))