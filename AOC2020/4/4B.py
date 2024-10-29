validHex = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
validEye = ['amb','blu','brn','gry','grn','hzl','oth']

with open('input.txt') as file:
    s = file.read()

passports = s.split('\n\n')

valid = 0
for p in passports:
    lines = p.split('\n')
    fields = []
    for l in lines:
        x = l.split(' ')
        for item in x:
            fields.append(item)
    keys = []
    for f in fields:
        keys.append(f.split(':')[0])
    if not(len(keys) == 8 or (len(keys) == 7 and 'cid' not in keys)):
        continue #weed out obvious fakes
    fieldsDict = {}
    for f in fields:
        kv = f.split(':')
        if len(kv) == 1:
            continue
        fieldsDict[kv[0]] = kv[1]
    byr = int(fieldsDict['byr'])
    iyr = int(fieldsDict['iyr'])
    eyr = int(fieldsDict['eyr'])
    hgt = fieldsDict['hgt']
    hcl = fieldsDict['hcl']
    ecl = fieldsDict['ecl']
    pid = fieldsDict['pid']
    if byr < 1920 or byr > 2002:
        continue
    if iyr < 2010 or iyr > 2020:
        continue
    if eyr < 2020 or eyr > 2030:
        continue
    units = hgt[-2:]
    amt = int(hgt[0:-2])
    if units == 'cm':
        if amt < 150 or amt > 193:
            continue
    if units == 'in':
        if amt < 59 or amt > 76:
            continue
    if units != 'cm' and units != 'in':
        continue
    if hcl[0] != '#':
        continue
    good = True
    for c in hcl[1:]:
        if c not in validHex:
            good = False
    if not good:
        continue
    if ecl not in validEye:
        continue
    if len(pid) != 9:
        continue
    valid += 1


print(valid)