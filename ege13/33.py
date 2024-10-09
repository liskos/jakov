import ipaddress
x = -1
net = ipaddress.ip_network("122.191.12.189/255.255.255.128",0)
for ip in net:
    x += 1
    if str(ip) == "122.191.12.189":
        print(x,ip)

    #if ip == ipaddress.ip_adress("132.126.150.18")