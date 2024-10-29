with open('input.txt') as inp:
    maxID = 0
    for line in inp:
        bits = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
        row = int(bits[:-2],2)
        col = int(bits[-2:],2)
        x = int(bits,2)
        if x > maxID:
            maxID = x

print(maxID)