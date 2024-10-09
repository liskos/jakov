import ipaddress
x = -1
net = ipaddress.ip_network("156.128.0.227/255.255.255.248",0)
for ip in net:
    x += 1
    if str(ip) == "156.128.0.227":
        print(x,ip)

    #if ip == ipaddress.ip_adress("132.126.150.18")