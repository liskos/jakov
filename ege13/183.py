import ipaddress
b = set()
net = ipaddress.ip_network("99.64.0.0/255.192.0.0",0)
for ip in net:
    if ip.__format__("b")[-2] == "1" and ip.__format__("b")[-1] == "1":
        b.add(ip)
print(len(b))