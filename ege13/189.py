import ipaddress
b = 10000
net = ipaddress.ip_network("94.159.76.0/255.255.255.128",0)
for ip in net:
    if ip.__format__("b").count("0") < b:
        b = ip.__format__("b").count("0")
print((b))