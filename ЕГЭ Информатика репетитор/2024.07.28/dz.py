f = open('dz.txt')
N, M = f.readline().split()
N, M = int(N), int(M)

A = []
B = []

for i in f:
    price, count, c = i.split()
    price, count = int(price), int(count)

    for l in range(count):
        if c == 'A':
            A.append(price)
        elif c == 'B':
            B.append(price)

A.sort()
B.sort()

d = []
flag = True

for x in B:
    if sum(d) + x <= M:
        d.append(x)
    else:
        flag = False
        break

count = 0
if flag:
    for x in A:
        if sum(d) + x <= M:
            count += 1
            d.append(x)
        else:
            break

print(count, M - sum(d))

# 7165 245