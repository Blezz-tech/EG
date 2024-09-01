# Нужно успользовать fnmatch см 6 номер

for i in range(2023, 10**10, 2023):
    if (str(i)[-2:] == '41') and (str(i)[2:5] == '493') and (str(i)[0] == '1'):
        print(i)