
for x in range(210235, 210300+1):
    k = 0
    s = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            s.append(i)
            k += 1
    if k == 4:
        print(sorted(s))