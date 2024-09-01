M = [int(x) for x in open('17_7.txt')]
D = [x for x in M if str(x)[-1] == '5']
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if str(min(x, y))[-1] == '5':
        if (x ** 2 + y ** 2) < min(D) ** 2:
            R.append(x ** 2 + y ** 2)
print(len(R), max(R))