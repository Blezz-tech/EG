f = open("2.txt")
M = list(map(int,f))

ns = set(M)

count = 0
max_number = 0
for i in range(len(M) - 1):
    for j in range(i+1, len(M)):
        if M[j] % 2 == 1 and M[i] % 2 == 1:
            x = (M[i] + M[j]) // 2
            if x in ns:
                count += 1
                max_number = max(max_number, x)

print(count, max_number)