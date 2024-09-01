for n in range(1, 100):
    s = bin(n)[2:]
    s += str(s.count("1") % 2)
    s += str(s.count("1") % 2)
    k = int(s, 2)
    if (k > 83):
        print(k)
        break