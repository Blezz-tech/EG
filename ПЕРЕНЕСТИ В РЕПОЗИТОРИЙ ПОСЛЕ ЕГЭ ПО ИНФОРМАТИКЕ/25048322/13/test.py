import ipaddress

lst = []
for i in range(0, 256):
    ip = ipaddress.ip_address(f"223.167.{i}.167")
    ip = bin(int(ip))[2:]
    if(ip[0:16].count('0') == ip[16:].count('0')):
        lst.append(i)

print(max(lst))