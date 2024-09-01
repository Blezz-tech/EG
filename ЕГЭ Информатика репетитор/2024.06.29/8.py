def f(start, end):
    if start == 14:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    else:
        return f(start + 1, end) + f(start + 2, end)

print(f(2, 9) * f(9, 18))