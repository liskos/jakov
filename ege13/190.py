import ipaddress
b = 0
net = ipaddress.ip_network("124.8.0.0/255.248.0.0",0)
for ip in net:
    if ip.__format__("b").count("0") > b:
        b = ip.__format__("b").count("0")
print((b))