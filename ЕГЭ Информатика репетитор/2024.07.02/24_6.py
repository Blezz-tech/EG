f = open('24_6.txt')
a = 0
for string in f:
    if(string.count('A') < string.count('E')):
        a += 1
print(a)