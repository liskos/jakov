import ipaddress
x = -1
net = ipaddress.ip_network("156.132.ege15.138/255.255.252.0",0)
for ip in net:
    x += 1
    if str(ip) == "156.132.ege15.138":
        print(x,ip)

    #if ip == ipaddress.ip_adress("132.126.150.18")