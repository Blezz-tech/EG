def task_1():
    def f(n):
        if n == 0:
            return 0
        if n > 0 and n % 2 == 0:
            return f(n/2)
        if n % 2 == 1:
            return 1 + f(n - 1)
    
    k = 0
    for n in range(1, 1001):
        if f(n) == 3:
            k += 1
    print(k)

def task_2():   
    def f(n):
        if n <= 1:
            return 0
        if n > 1 and n % 2 == 1:
            return f(n-1) + 3 * (n**2)
        if n > 1 and n % 2 == 0:
            return n/2 + f(n-1) + 2
    
    print(f(49))


def task_3():
    def f(n):
        if n == 1:
            return 1
        if n > 1:
            return n * f(n-1)

    print(f(2023)/f(2020))


def task_4():
    def f(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n > 2 and n % 2 == 0:
            return int((4 * n - f(n - 3)) / 8)
        if n > 2 and n % 2 == 1:
            return int((4 * n - f(n - 1) + f(n - 2)) / 8)
    
    print(f(52) - f(38))


def task_5():
    def f(n):
        if n == 1:
            return 1
        if n == 2:
            return 3
        if n > 2:
            return f(n - 1) * n + f(n - 2) * (n - 1)
    
    print(f(5))


def task_6():
    def f(n):
        if n == 1: return 1
        if n == 2: return 1
        if n > 2: return f(n - 2) + f(n - 1)

    print(f(8))


def task_7():
    def f(n):
        if n == 1: return 0
        if n == 2: return 1
        if n == 3: return 1
        if n > 3: return f(n - 3) + f(n - 2) + f(n - 1)

    print(f(11))


def task_8():
    def f(n):
        if n == 0: return 0
        if n > 0 and n % 2 == 0: return f(n / 2)
        if n % 2 == 1: return 1 + f(n - 1)
    
    k = 0
    for n in range(1, 901):
        if f(n) == 9:
            k += 1
    print(k)


def task_9():
    def f(n):
        if n >= 1000: return 1000
        if n < 1000 and n % 2 == 1: return n * f(n + 1)
        if n < 1000 and n % 2 == 0: return n * f(n + 1) / 2
    
    print(f(998) / f(1001))


def task_10():
    def f(n):
        if n == 1: return 1
        if n > 1: return f(n - 1) * n
    print(f(5))


def task_11():
    def f(n):
        if n == 1: return 1
        if n > 1: return 2 * g(n - 1) + 5 * n
    
    def g(n):
        if n == 1: return 1
        if n > 1: return f(n - 1) + 2 * n

    print(f(4) + g(4))


def task_12():
    # def f(n):
    #     if n == 0:
    #         return 0
    #     return f(n - 1) + n
    
    # k = 0
    # for n in range(237567892, 1134567004 + 1):
    #     if f(n) % 3 == 0:
    #         k += 1
    # print(k)
    a,b = 237567892,1134567004
    print(((b-1)//3*3-(a+1)//3*3)//3+1)













def task_13():
    a,b = 765432010,1542613234
    print(((b-1)//3*3-(a+1)//3*3)//3+1)


# task_1()
# task_2()
# task_3()
# task_4()
# task_5()
# task_6()
# task_7()
# task_8()
# task_9()
# task_10()
# task_11()
# task_12()
task_13()