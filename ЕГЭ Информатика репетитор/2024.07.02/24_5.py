M = open("24_5.txt").readline()
k = m = 0
for i in range(1, len(M)):
    if (M[i] == "A" and k%2 == 0) or (M[i] == "B" and k%2 == 1):
        k += 1
        m = max(m, k)
    elif M[i] == 'A': k = 1
    else: k = 0
print(m)
