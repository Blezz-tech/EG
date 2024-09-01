f = open('4.txt')
n = f.readline() # количество товаров
a = [int(i) for i in f]
a.sort()
ksum = 0
while a[0] <= 100:
    ksum += a[0]
    del a[0]
for i in range(len(a) // 2):
    ksum += a[i] * 0.7
    ksum += a[-i - 1]
print(int(ksum) + 1, a[len(a) // 2 - 1])