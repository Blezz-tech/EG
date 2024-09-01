def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    else:
        return\
            f1(start + 1, end) +\
            f1(start + 2, end) +\
            f2(start * 2, end) +\
            f2(start * 3, end)

def f1(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    else:
        return\
            f2(start * 2, end) +\
            f2(start * 3, end)

def f2(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    else:
        return\
            f1(start + 1, end) +\
            f1(start + 2, end)

print(f(1, 24))