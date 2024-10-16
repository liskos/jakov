import ipaddress
b = set()
net = ipaddress.ip_network("154.233.0.0/255.255.0.0",0)
for ip in net:
    if ip.__format__("b")[-1] == "0":
        b.add(ip)
print(len(b))