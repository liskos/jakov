import ipaddress
x = -1
net = ipaddress.ip_network("112.154.133.208/255.255.248.0",0)
for ip in net:
    x += 1
    if str(ip) == "112.154.133.208":
        print(x,ip)

    #if ip == ipaddress.ip_adress("132.126.150.18")