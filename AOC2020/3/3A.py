with open('input.txt') as inp:
    l = len('.##.#.........#.....#....#...#.')
    #l = len('..##.......') #test input
    myIndex = 0
    ans = 0
    for line in inp:
        if line[myIndex % l] == '#':
            ans += 1
        myIndex += 3

print(ans)