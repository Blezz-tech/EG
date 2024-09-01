for x in range(174457, 174505+1):
    k = 0
    s = 0
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            s = i
            k += 1
    if k == 2:
        print(x // s, s)