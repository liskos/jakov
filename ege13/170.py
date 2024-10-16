import ipaddress
net = ipaddress.ip_network("174.114.120.0/255.255.252.0",0)
b = set()
for ip in net:
    if (ip.__format__("b").count("1")) % 2 == 0:
        b.add(ip)

print(len(b))