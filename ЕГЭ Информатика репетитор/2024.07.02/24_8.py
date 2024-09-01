s = open('24_8.txt').read()
p = []
for i in range(len(s)-2):
    if s[i] == s[i+2]:
        p.append(s[i+1])
print(max(p,key=p.count))