def findMatch(str, lIndex):
    parens = 1
    i = lIndex
    while parens > 0:
        i += 1
        if str[i] == '(':
            parens += 1
        if str[i] == ')':
            parens -= 1
    return i

def evaluate(expr):
    while '(' in expr:
        lIndex = expr.index('(')
        rIndex = findMatch(expr,lIndex)
        #print(expr[lIndex:rIndex+1])
        inner = evaluate(expr[lIndex+1:rIndex])
        #print(expr[0:lIndex])
        #print(str(inner))
        #print(expr[rIndex + 1:])
        expr = expr[0:lIndex] + str(inner) + expr[rIndex + 1:]
    line = expr.split(' ')
    while '+' in line:
        i = line.index('+')
        a = int(line.pop(i-1))
        line.pop(i-1) #The plus we already knew was there
        b = int(line.pop(i-1))
        line.insert(i-1,a+b)

    while '*' in line:
        line.remove('*')


    ans = 1
    for val in line:
        ans *= int(val)


    return ans



with open('input.txt') as inp:
    sum = 0
    for line in inp:
        sum += evaluate(line.strip())

print(sum)