x = int(bin(213)[2:] + bin(55)[2:] + bin(160)[2:] + bin(20)[2:])
count = 0
for i in range(0, 64):
    y = bin(x + i)[2:]
    if y.count("1") % 3 == 0:
        count += 1

print(count)