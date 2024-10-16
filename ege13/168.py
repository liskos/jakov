import ipaddress
net = ipaddress.ip_network("216.130.64.0/255.255.192.0",0)
b = set()
for ip in net.hosts():
    if (ip.packed[0] % 2 == 0 and ip.packed[1] % 2 == 0 and ip.packed[2] % 2 == 0 and ip.packed[3] % 2 == 0):
        b.add(ip)

print(len(b))