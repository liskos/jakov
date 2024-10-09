import ipaddress
x = -1
net = ipaddress.ip_network("162.198.0.157/255.255.255.224",0)
for ip in net:
    x += 1
    if str(ip) == "162.198.0.157":
        print(x,ip)

    #if ip == ipaddress.ip_adress("132.126.150.18")