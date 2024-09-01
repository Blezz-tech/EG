import ipaddress

lst = []
for a in range(0, 256):
    flag = False
    for subnetwork_step in range(0, 64):
        ip = ipaddress.ip_address(f"223.167.{a}.{167 + subnetwork_step}")
        ip = bin(int(ip))[2:]
        if(ip[0:16].count('0') > ip[16:].count('0')):
            flag = True
            break
    if flag:
        continue
    print(a)