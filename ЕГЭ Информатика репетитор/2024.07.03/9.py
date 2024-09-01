
for x in range(312614, 312651+1):
    k = 0
    s = []
    for i in range(1, x+1):
        if x % i == 0:
            s.append(i)
            k += 1
    if k == 6:
        print(sorted(s))