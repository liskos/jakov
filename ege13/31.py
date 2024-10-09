import ipaddress
x = -1
net = ipaddress.ip_network("192.168.156.235/255.255.255.240",0)
for ip in net:
    x += 1
    if str(ip) == "192.168.156.235":
        print(x,ip)

    #if ip == ipaddress.ip_adress("132.126.150.18")