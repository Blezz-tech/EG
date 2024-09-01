# Нужно успользовать fnmatch см 6 номер

for i in range(3023, 10**10, 3023):
    if (str(i)[-2:] == '21') and (str(i)[2:5] == '954') and (str(i)[0] == '1'):
        print(i)