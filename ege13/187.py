import ipaddress
b = 0
net = ipaddress.ip_network("204.252.0.0/255.255.0.0",0)
for ip in net:
    if ip.__format__("b").count("1") > b:
        b = ip.__format__("b").count("1")
print((b))