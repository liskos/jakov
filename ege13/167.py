import ipaddress
net = ipaddress.ip_network("140.19.96.0/255.255.248.0",0)
b = set()
for ip in net:
    if ((ip.__format__("b")[:8].count("1") == ip.__format__("b")[9:16].count("1") and ip.__format__("b")[:8].count("1") == ip.__format__("b")[17:24].count("1") and ip.__format__("b")[:8].count("1") == ip.__format__("b")[25:32].count("1"))):
        b.add(ip)

print(len(b))