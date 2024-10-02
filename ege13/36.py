import ipaddress
x = -1
net = ipaddress.ip_network("132.126.150.18/255.255.240.0",0)
for ip in net:
    x += 1
    if str(ip) == "132.126.150.18":
        print(x,ip)

    #if ip == ipaddress.ip_adress("132.126.150.18")