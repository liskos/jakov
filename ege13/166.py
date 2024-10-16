import ipaddress
b = set()
net = ipaddress.ip_network("139.75.100.0/255.255.252.0",0)
for ip in net:
    s = int(ip.__format__("b")[-1])
    if s == 3 or s == 7 or s == 1 or s == 15 or s == 31 or s == 63 or s == 127 or s == 255:
        b.add(ip)
print(len(b))