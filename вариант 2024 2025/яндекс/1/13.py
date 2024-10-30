import ipaddress
a = []
net = ipaddress.ip_network("10.112.0.0/255.248.0.0",0)

for ip in net.hosts():
    if (ip.__format__("b")).count("1") % 3 == 0:
        a.append(ip)

print(len(a))