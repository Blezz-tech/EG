M = open("dz.txt").readline()
k = m = 0
for i in range(len(M)):
    if (M[i] == "L" and k % 3 == 0) or\
        (M[i] == "D" and k % 3 == 1) or\
        (M[i] == "R" and k % 3 == 2):
        k += 1
        m = max(m, k)
    elif M[i] == 'L': k = 1
    else: k = 0
print(m)

# 14