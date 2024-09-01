def f(start, end, k):
    if start > end + 1:
        return 0
    if start == end:
        return 1
    else:
        if k == 1:
            return f(start * 2, end, k - 1) + f(start + 3, end, k - 1)
        else:
            return f(start - 1, end, k + 1) + f(start * 2, end, k) + f(start + 3, end, k)

print(f(4, 14, 0))