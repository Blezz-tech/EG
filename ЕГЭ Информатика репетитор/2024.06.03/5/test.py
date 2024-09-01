lst = []
for n in range(1, 100):
    s = bin(n)[2:]
    s = s + s[-1]
    s += str(s.count('1') % 2)
    k = int(s, 2)
    if (k > 127):
        lst.append(k)

print(min(lst))