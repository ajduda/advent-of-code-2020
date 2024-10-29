def isValid(tree,node,message,index,endpoints):
    #print('in rule ' + str(node) + ' with index ' + str(index))
    if node in endpoints:
        #print(message[index])
        #print(tree[node])
        return (message[index] == tree[node], index + 1)
    for option in tree[node]:
        tempIndex = index
        good = True
        for rule in option:
            ret,newIndex = isValid(tree,rule,message,tempIndex,endpoints)
            if not ret:
                good = False
                break
            #if newIndex > len(message):
                #good = False
                #break
            tempIndex = newIndex
            if newIndex == len(message):
                return (True, newIndex)
        if good:
            return (True,newIndex)
    #print('failed at index ' + str(tempIndex))
    return (False,index)



with open('input.txt') as inp:
    s = inp.read()
    rules,tests = s.split('\n\n')

    tree = {}
    endpoints = set()

    for line in rules.split('\n'):
        l,r = line.split(': ')
        k = int(l)
        if r[0] == '"':
            tree[k] = r[1]
            endpoints.add(k)
            continue
        v = []
        for s in r.split(' | '):
            v.append([])
            for num in s.split(' '):
                v[-1].append(int(num))
        tree[k] = v



print(tree)
print(endpoints)
total = 0
for message in tests.split('\n'):
    if len(message) == 0:
        continue
    ret,length = isValid(tree,0,message,0,endpoints)
    if ret and length == len(message):
        total += 1


print(total)