f = open('dz.txt')
M = [int(i) for i in f]
D = [x for x in M if str(x)[-1] == '3']

s = 0
mx = 0
for i in range(len(M) - 1):
        x, y = M[i], M[i+1]
        z = str(min(x, y)) 

        if z[-1] == "3" and (x ** 2 + y ** 2) < min(D) ** 2:
            s += 1
            mx = max(mx, x ** 2 + y ** 2)
print(s, mx)
# 355 99033293
