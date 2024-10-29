with open('input.txt') as inp:
    s = inp.read()

fields,myTicket,nearbyTicket = s.split('\n\n')

ranges = []
for line in fields.split('\n'):
    r = line.split(' ')
    r1 = r[-3]
    r2 = r[-1]
    a,b = r1.split('-')
    ranges.append((int(a),int(b)))
    a,b = r2.split('-')
    ranges.append((int(a),int(b)))


print(ranges)
ans = 0
for line in nearbyTicket.split('\n')[1:]:
    for strVal in line.split(','):
        if len(strVal) == 0:
            continue
        val = int(strVal)
        valid = False
        for bound in ranges:
            if bound[0] <= val and val <= bound[1]:
                valid = True
                break
        if not valid:
            ans += val

print(ans)