import ipaddress
k = 0
net = ipaddress.ip_network("204.16.168.0/255.255.248.0",0)

for ip in net:
    if ip.__format__("o").count("0") % 5 != 0:
        print(ip.__format__("oct"))