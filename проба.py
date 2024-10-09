import ipaddress

net = ipaddress.ip_network("151.172.115.156/30")
print(*net)
for ip in net:
    print(ip.__format__("b"), ip)