for a in range(0, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (y - 3*x < a) or (x > 15) or (y > 10):
                k = k + 1
    if k == 300*300:
        print(a)
        break