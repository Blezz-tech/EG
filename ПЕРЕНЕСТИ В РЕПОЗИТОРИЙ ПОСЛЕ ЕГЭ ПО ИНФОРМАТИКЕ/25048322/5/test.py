for n in range(2000, 1, -1):
    s = ""
    n1 = n
    while n1 != 0:
        s += str(n1 % 7)
        n1 //= 7
    
    s = s[::-1]
    if (s.count("2") % 2 == 0):
        s += "5" * 3
    else:
        s += "1"
    
    r = int(s, 7)
    print(s, n)
    if(r < 3799):
        print(n)
        break