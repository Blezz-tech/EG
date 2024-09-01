s = "1" + "5" * 112

while ("15" in s or "255" in s or "355" in s):
    if "15" in s:
        s = s.replace("15", "2", 1)
    elif "255" in s:
        s = s.replace("255", "3", 1)
    else:
        s = s.replace("355", "1", 1)

print(s)