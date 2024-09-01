x = 81**1314 + 9**2769 - 3**3942 + 10
s = ""

while x != 0:
    s = s + str(x % 3)
    x //= 3

s = s[::-1]

print(s.count("2"))