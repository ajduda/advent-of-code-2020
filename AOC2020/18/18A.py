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
    ans = 0
    adding = True
    for item in expr.split(' '):
        if len(item) == 0:
            continue
        elif item == '+':
            adding = True
        elif item == '*':
            adding = False
        else:  # Number
            n = int(item)
            if adding:
                ans += n
            else:
                ans *= n
            #print(ans)

    return ans



with open('input.txt') as inp:
    sum = 0
    for line in inp:
        sum += evaluate(line.strip())

print(sum)