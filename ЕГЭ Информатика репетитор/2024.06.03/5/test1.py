for n in range(100, 1, -1):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += "00"
    else:
        s += "11"
    k = int(s, 2)
    if k <= 71:
        print(n)
        break