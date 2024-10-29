with open('input.txt') as inp:
    s = inp.read()



tiles = s.split('\n\n')
tileById = {}
for tile in tiles:
    lines = tile.split('\n')
    if len(lines[-1]) == 0:
        lines.pop()
    key = int(lines[0][5:-1])
    sides = []
    sides.append(lines[1])
    s1 = ""
    s2 = ""
    for i in range(1,len(lines)):
        s1 += lines[i][0]
        s2 += lines[i][-1]
    sides.append(s1[::-1])
    sides.append(lines[-1][::-1])
    sides.append(s2)
    tileById[key] = sides

sideCount = {}

for tile in tileById.values():
    for side in tile:
        if side in sideCount:
            sideCount[side] += 1
        elif side[::-1] in sideCount:
            sideCount[side[::-1]] += 1
        else:
            sideCount[side] = 1
print(tileById)
print(sideCount)

lonelyEdges = set()
for k in sideCount.keys():
    if sideCount[k] == 1:
        lonelyEdges.add(k)
edgeIds = {}
for edge in lonelyEdges:
    for k in tileById.keys():
        if edge in tileById[k] or edge[::-1] in tileById[k]:
            if k in edgeIds:
                edgeIds[k] += 1
            else:
                edgeIds[k] = 1

ans = 1
for k in edgeIds.keys():
    if edgeIds[k] == 2:
        ans *= k

print(ans)