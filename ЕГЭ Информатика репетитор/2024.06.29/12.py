def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    else:
        x = start
        if str(start)[0] != "9":
            x = int(str(int(str(start)[0]) + 1) + str(start)[1:])
        return f(start + 1, end) + f(x, end)

print(f(35, 57))