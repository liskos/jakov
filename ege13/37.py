import ipaddress
x = -1
net = ipaddress.ip_network("206.158.124.67/255.255.224.0",0)
for ip in net:
    x += 1
    if str(ip) == "206.158.124.67":
        print(x,ip)