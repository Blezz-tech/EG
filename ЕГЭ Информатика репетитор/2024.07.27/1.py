f = open('1.txt')
s = int(f.readline().split()[0])
a = [int(i) for i in f]
a.sort()
s1 = 0
for i in range(0,len(a)):
    if s1 + a[i] > s: break
    s1 += a[i]
    i1 = i
s2 = s1 - a[i1]
for j in range(i1, len(a)):
    if s2 + a[j] > s: break
    p = a[j]
print(i1 + 1,p)