M = open("24_7.txt").readline()

k = x = 0
for i in range(1, len(M)- 1):
    if (M[i] == "D" and M[i+1] == "D"):
        x += 1
    else:
        k = max(k, x)
        x = 1

print(k)