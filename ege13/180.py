import ipaddress
b = set()
net = ipaddress.ip_network("98.116.0.0/255.252.0.0",0)
for ip in net:
    if ip.__format__("b").count("0") % 2 == 0:
        b.add(ip)
print(len(b))