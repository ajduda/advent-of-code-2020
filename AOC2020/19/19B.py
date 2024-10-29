DEPTH = 12#The max depth a recurring tree can go

global tree
tree = {}
global endpoints
endpoints = set()
global recurring 
recurring = set()
global possiblities
possiblities = {}
global depends8
global depends11
depends8 = set()
depends11 = set()

# Rather hardcoded version to solve this problem, since general solutions wasn't working

def buildPossibilities(node):
    if node in possiblities:
        return
    strs = set()
    for option in tree[node]:
        optionStrs = set()
        for rule in option:
            if rule == 8:
                depends8.add(node)
            if rule == 11:
                depends11.add(node)
            buildPossibilities(rule)
        for possiblity in possiblities[option[0]]:
            optionStrs.add(possiblity)
        tempStrs = set()
        for i in range(1,len(option)):
            for s1 in optionStrs:
                for s2 in possiblities[option[i]]:
                    tempStrs.add(s1 + s2)
            optionStrs = tempStrs.copy()
        strs |= optionStrs

    possiblities[node] = strs



def isValid(chunk8,chunk11,message):
    #print(f'The message is {message}')
    num42 = 0
    num31 = 0
    i = 0
    while message[i:i+chunk8] in possiblities[42]:
        i += chunk8
        num42 += 1
    while message[i:i+chunk8] in possiblities[31]:
        i += chunk8
        num31 += 1
    if i != len(message):
        return False
    return num42 > num31





with open('input.txt') as inp:
    s = inp.read()
    rules,tests = s.split('\n\n')

    for line in rules.split('\n'):
        l,r = line.split(': ')
        k = int(l)
        if r[0] == '"':
            tree[k] = [r[1]]
            endpoints.add(k)
            continue
        v = []
        for s in r.split(' | '):
            v.append([])
            for num in s.split(' '):
                v[-1].append(int(num))
                if int(num) == k:
                    recurring.add(k)
        tree[k] = v



print(tree)
total = 0
for rule in endpoints:
    possiblities[rule] = tree[rule]

print(possiblities)

buildPossibilities(0)

for possiblity in possiblities[8]:
    eightChunk = len(possiblity)
    break

for possiblity in possiblities[11]:
    elevenChunk = len(possiblity)
    break

for possiblity in possiblities[8]:
    if len(possiblity) != eightChunk:
        print('ERROROROROR!')
        exit()

for possiblity in possiblities[11]:
    if len(possiblity) != elevenChunk:
        print('ERROROROROR 2!')
        exit()



print(eightChunk)
print(elevenChunk)

for message in tests.split('\n'):
    if len(message) == 0:
        continue
    if len(message) % eightChunk != 0:
        continue
    if message in possiblities[0]:
        #print(f'{message} -> True A')
        total += 1
    elif message[0:eightChunk] in possiblities[8] and message[-1*eightChunk:] in possiblities[31]:
        if isValid(eightChunk,elevenChunk,message):
            #print(f'{message} -> True B')
            total += 1
    else:
        pass
        #print(f'{message} -> False')

            

print(total)