import ipaddress
x = -1
net = ipaddress.ip_network("126.185.90.162/255.255.252.0",0)
for ip in net:
    x += 1
    if str(ip) == "126.185.90.162":
        print(x,ip)