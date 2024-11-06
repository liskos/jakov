import ipaddress
b = []
net = ipaddress.ip_network("172.16.128.0/255.255.192.0",0)
for ip in net:
    if ip.__format__("b").count("1") % 2 != 0:
        b.append(ip)
print(len(b))