with open('input.txt') as inp:
    s = inp.read()

fields,myTicket,nearbyTicket = s.split('\n\n')

ranges = {}
rangesList = []
for line in fields.split('\n'):
    name = line.split(':')[0]
    r = line.split(' ')
    r1 = r[-3]
    r2 = r[-1]
    a,b = r1.split('-')
    c,d = r2.split('-')
    ranges[name] = ((int(a),int(b)), (int(c),int(d)))
    rangesList.append((int(a),int(b)))
    rangesList.append((int(c),int(d)))

print(ranges)

colOptions = []
for i in range(0, len(ranges)):
    colOptions.append(list(ranges.keys()))

rowFields = {} #Will hold the finished solution order, name -> index


tickets = [[]]
for val in myTicket.split('\n')[1].split(','): 
    tickets[0].append(int(val))

for line in nearbyTicket.split('\n')[1:]:
    tickets.append([])
    for val in line.split(','):
        if len(val) > 0:
            tickets[-1].append(int(val))

ticketsToRemove = []
for ticket in tickets:
    for val in ticket:
        valid = False
        for bound in rangesList:
            if bound[0] <= val and val <= bound[1]:
                valid = True
                break
        if not valid:
            ticketsToRemove.append(ticket)
            break

for ticket in ticketsToRemove:
    tickets.remove(ticket)

while len(rowFields) < len(ranges):
    for i in range(0, len(tickets)):
        ticket = tickets[i]
        for j in range(0,len(ticket)):
            fieldsToRemove = []
            for field in colOptions[j]:
                (x,y) = ranges[field]
                (a,b) = x
                (c,d) = y
                val = ticket[j]
                if (val < a or b < val) and (val < c or d < val):
                    fieldsToRemove.append(field)
            for field in fieldsToRemove:
                colOptions[j].remove(field)
            if len(colOptions[j]) == 1:
                knownField = colOptions[j][0]
                rowFields[knownField] = j
                for col in colOptions:
                    if knownField in col:
                        col.remove(knownField)

print(rowFields)

ans = 1

for name in rowFields.keys():
    if name[0:9] == 'departure':
        ans *= tickets[0][rowFields[name]]

print(ans)