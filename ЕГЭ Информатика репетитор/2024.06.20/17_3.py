f = open('17_3.txt')
a = [int(i) for i in f]
s = 0
mx = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[j] - a[i]) % 2 == 0) and (a[j] % 31 == 0 or a[i] % 31 == 0):
            s += 1
            mx = max(mx, a[i] + a[j])
print(s, mx)