def createTouple(deckA,deckB):
    ret = []
    for e in deckA:
        ret.append(e)
    ret.append(-1) #divider
    for e in deckB:
        ret.append(e)
    return tuple(ret)

def play(deckA,deckB):  # Returns true if player 1 wins, and false if player 2 wins
    #print(f'Starting a game, here are the decks: {deckA} {deckB}')
    history = []
    while len(deckA) > 0 and len(deckB) > 0:
        state = createTouple(deckA,deckB)
        if state in history:
            #print(history)
            return True
        history.append(state)
        A = deckA.pop(0)
        B = deckB.pop(0)
        if A <= len(deckA) and B <= len(deckB):
            if play(deckA[0:A],deckB[0:B]): #Player 1 wins the subgame
                deckA.append(A)
                deckA.append(B)
            else:
                deckB.append(B)
                deckB.append(A)
        elif A > B:
            deckA.append(A)
            deckA.append(B)
        else:
            deckB.append(B)
            deckB.append(A)

    return len(deckA) > 0

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

ret = play(deckA,deckB)

if ret:
    winner = deckA
else:
    winner = deckB

ans = 0
i = len(winner)
for j in range(0,len(winner)):
    ans += i * winner[j]
    i -= 1

print(ans)