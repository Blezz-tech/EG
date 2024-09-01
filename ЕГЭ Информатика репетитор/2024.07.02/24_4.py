M = open("24_4.txt").readline()

k = 1
x = 0

for i in range(1, len(M)-1):
    if (M[i] != M[i+1]):
        k += 1
    else:
        x = max(x, k)
        k = 1
m = max(m, k)
print(x)