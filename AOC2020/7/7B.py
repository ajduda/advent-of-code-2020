with open('kyle_input.txt') as inp:
    tree = {}
    for l in inp:
        line = l.replace('bags', '')
        line = line.replace('bag', '')
        line = line.replace(' .\n','')
        left,right = line.split('  contain ')
        value = []
        for v in right.split(' , '):
            if v[0] != 'n':   # if it's 'no other' bags, make it [0,'EMPTY']
                amt = int(v[0])
                name = v[2:]
            else:
                amt = 0
                name = 'EMPTY'
            value.append((amt,name))
        tree[left] = value

print(tree)

#make a dict of how many bags each bag contains
bagAmt = {}
lines = len(tree)
#print(lines)
keyArray = list(tree.keys())
i = 0
while len(bagAmt) < lines:
    i = (i + 1) % lines
    key = keyArray[i]
    if key in bagAmt:
        continue
    valid = True
    for item in tree[key]:
        if item[0] != 0 and item[1] not in bagAmt:
            valid = False
            break
    if not valid:
        continue
    #we're good to compute this one
    bagVal = 1
    for item in tree[key]:
        if item[0] != 0:
            bagVal += item[0] * bagAmt[item[1]]
    bagAmt[key] = bagVal

print(bagAmt['shiny gold'] - 1) #don't count the bag in what's inside it