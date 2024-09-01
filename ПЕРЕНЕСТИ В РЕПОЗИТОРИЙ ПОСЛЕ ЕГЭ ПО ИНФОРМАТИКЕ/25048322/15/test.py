for a in range(300, 0, -1):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if ((x + 2*y) > a) or (y < x) or (x < 30):
                k += 1
    if k == 300*300:
        print(a)
        break
    