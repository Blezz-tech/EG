for x in "0123456789A":
    x1 = int("21"+x+"17", 11) + int("2"+x+"160", 11)
    if x1 % 10 == 0:
        print(x1//10)
        break