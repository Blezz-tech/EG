m = 100000000000000000
E = [i for i in range(18, 43)]
V = [i for i in range(11, 18)]

for a_min in range(1, 101):
    for a_max in range(a_min+1, 101):
        s = 1
        A = [i for i in range(a_min, a_max)]
        for x in range(1, 101):
            f = (x in E) <= (not (x in V) and (x in A))
            if not f:
                s = 0
                break
        if s == 1:
            m = min(m, a_max - a_min)
            break
print(m)