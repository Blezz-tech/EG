# Нужно успользовать fnmatch см 6 номер

for i in range(3013, 10**10, 3013):
    if (str(i)[-1] == '5') and (str(i)[2:6] == '3948') and (str(i)[0] == '1'):
        print(i)