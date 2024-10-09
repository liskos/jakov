import ipaddress
x = -1
net = ipaddress.ip_network("10.18.134.220/255.255.255.192",0)
for ip in net:
    x += 1
    if str(ip) == "10.18.134.220":
        print(x,ip)

    #if ip == ipaddress.ip_adress("132.126.150.18")