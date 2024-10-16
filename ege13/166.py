import ipaddress
b = set()
net = ipaddress.ip_network("139.75.100.0/255.255.252.0",0)
for ip in net:
    s = ip.packed[3]
    if s in [1,3,7,15,31,63,127,255]:
        b.add(ip)
print(len(b))