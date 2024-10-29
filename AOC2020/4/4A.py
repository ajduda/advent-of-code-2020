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
    if len(keys) == 8 or (len(keys) == 7 and 'cid' not in keys):
        valid += 1
print(valid)