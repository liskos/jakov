import ipaddress
b = set()
net = ipaddress.ip_network(f"213.0.0.0/255.192.0.0",0)
for ip in net:
    print(ip.__format__("b")[:3])
    if ip.__format__("b")[:3] == "111":
        b.add(ip)
print(len(b),b)