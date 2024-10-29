with open('input.txt') as inp:
    s = inp.read()

deckA = []
deckB = []

s1,s2 = s.split('\n\n')
s1 = s1.split('\n')[1:]
s2 = s2.split('\n')[1:]

for card in s1:
    deckA.append(int(card))

for card in s2:
    if len(card) > 0:
        deckB.append(int(card))

while len(deckA) > 0 and len(deckB) > 0:
    A = deckA.pop(0)
    B = deckB.pop(0)
    if A > B:
        deckA.append(A)
        deckA.append(B)
    else:
        deckB.append(B)
        deckB.append(A)
    #print(deckA)

if len(deckA) > 0:
    winner = deckA
else:
    winner = deckB

print(winner)

ans = 0
i = len(winner)
for j in range(0,len(winner)):
    ans += i * winner[j]
    i -= 1

print(ans)