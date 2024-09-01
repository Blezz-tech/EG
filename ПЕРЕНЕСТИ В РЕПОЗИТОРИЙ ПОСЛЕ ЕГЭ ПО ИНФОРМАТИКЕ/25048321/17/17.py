def func_1(item):
    if len(str(abs(item))) == 4 and item % 2 == 0:
        return 1
    else:
        return 0

def func_2(lst):
    return (func_1(lst[0]) + func_1(lst[1]) + func_1(lst[2])) < 2

def func_3(lst, max121):
    return (lst[0] + lst[1] + lst[2]) <= max121

def check121(x):
    return abs(x) > 99 and str(x)[-3:] == "121"

def maximum121(lst):
    lst1 = []

    for i in lst:
        if check121(i):
            lst1.append(i)

    return max(lst1)

with open("17.txt") as f:
    count = 0

    text = f.read().splitlines()
    lst = list(map((lambda x: int(x)), text))
    max121 = maximum121(lst)

    lst1 = []
    for index, item in enumerate(lst):
        if (index == len(lst) - 2):
            break
        lst1.append([item, lst[index+1], lst[index+2]])

    lst3 = []
    for lst in lst1:
        if func_2(lst) and func_3(lst, max121):
            count = count + 1
            lst3.append(lst)

    lst4 = list(map((lambda x: sum(x)), lst3))
    print(count)
    print(max(lst4))
