import ipaddress
k = 0
net = ipaddress.ip_network("5.2.5.0/255.255.0.0",0)
for ip in net:
    if ip.__format__("b").count("0") % 25 == 0:
        k += 1

print(k)