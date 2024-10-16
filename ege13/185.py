import ipaddress
b = set()
net = ipaddress.ip_network("99.165.134.0/255.255.254.0",0)
for ip in net:
    if ip.__format__("b").count("1") % 3 == 0:
        b.add(ip)
print(len(b))