import ipaddress
net = ipaddress.ip_network("216.130.64.0/255.255.192.0",0)
b = set()
for ip in net:
    print(ip.__format__("b"))
    if (ip.__format__("b")[7] == 0 and ip.__format__("b")[15] == 0 and ip.__format__("b")[23] == 0 and ip.__format__("b")[31] == 0):
        b.add(ip)

print(len(b))