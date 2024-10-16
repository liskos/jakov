import ipaddress
b = set()
net = ipaddress.ip_network(f"213.0.0.0/255.192.0.0",0)
for ip in net:
    if "111" in ip.__format__("b"):
        b.add(ip)
print(len(b),b)