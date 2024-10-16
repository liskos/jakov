import ipaddress
b = 10000
net = ipaddress.ip_network("135.221.128.0/255.255.128.0",0)
for ip in net:
    if ip.__format__("b").count("1") < b:
        b = ip.__format__("b").count("1")
print((b))