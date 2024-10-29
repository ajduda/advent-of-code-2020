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

with open('input.txt') as inp:
    lines = inp.read()

flipped = set()

for line in lines.split('\n'):
    tile = coordinates(line)
    if tile in flipped:
        flipped.remove(tile)
    else:
        flipped.add(tile)

print(len(flipped))
