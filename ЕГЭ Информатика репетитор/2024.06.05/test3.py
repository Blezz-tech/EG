s = "2" * 129

while "222" in s or "444" in s:
    if "222" in s:
        s = s.replace("222", "44", 1)
    else:
        s = s.replace("4444", "2", 1)

print(s)