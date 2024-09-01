from fnmatch import *
for x in range(0, 10**9, 9117):
    if fnmatch(str(x), '3*37*3?9'):
        print(x)