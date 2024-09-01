M = open('24_2.txt').readline()

k = 1
x = 1
for i in range(1, len(M)):
    if (M[i] == "X" and M[i+1] == "X"):
        k += 1
    else:
        x = max(x, k)
        k = 1

print(x)