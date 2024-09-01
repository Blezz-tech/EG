f = open('26.txt')
n = int(f.readline())
a=[]
for i in f:
    a.append(int(i))
f.close()
a.sort()
a=a[::-1]
l={}
maxi=0
n=0
for i in a:
    f=0
    for j in l:
        if l[j][0] >= i+5:
            l.update({j: [i, l[j][1]+1]})
            maxi=max(l[j][1], maxi)
            f=1
            break
    if f==0:
        l.update({n: [i,0]})
        n+=1
print(len(l), maxi+1)

# f = open('26.txt')
# n = f.readline()
# cubes = sorted([int(i) for i in f], reverse=True)
# cklad=[]
# while len(cubes)>0:
#     block = [cubes.pop(0)]
#     for i in range(len(cubes)):
#         if (block[-1]-cubes[i])>=5:
#             block.append(cubes[i])
#             cubes[i]=''
#     cubes=[x for x in cubes if x!='']
#     cklad.append(block)
# print(len(cklad),max(len(c) for c in cklad))