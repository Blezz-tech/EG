def f(start, end):
    if start == 9 or start == 15:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    else:
        return f(start + 1, end) + f(start + 3, end) + f(start * 3, end)

print(f(3, 18))