import ipaddress

net = ipaddress.ip_network("192.168.32.160/255.255.255.240",0)
b = set()
for ip in net:
    if ip.__format__("b").count("0") > 21:
        b.add(ip)

print(len(b))