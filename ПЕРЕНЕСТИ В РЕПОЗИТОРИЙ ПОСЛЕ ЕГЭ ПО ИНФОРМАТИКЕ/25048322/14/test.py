for x in range(0, 10000):
    number =\
        int(f"11{x}73") +\
        int(f"94662{x}53{x}") +\
        int(f"6{x}41") +\
        int(f"31{x}77") +\
        int(f"9{x}82{x}{x}181")
    if number % 15 == 0:
        print(x)
        break
