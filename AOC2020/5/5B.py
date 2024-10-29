with open('input.txt') as inp:
    IDs = []
    for line in inp:
        bits = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
        row = int(bits[:-2],2)
        col = int(bits[-2:],2)
        x = int(bits,2)
        IDs.append(x)

for i in range(0,883):
    if i not in IDs and i+1 in IDs and i-1 in IDs:
        print(i)
        exit()