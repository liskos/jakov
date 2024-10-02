import ipaddress
net = ipaddress.ip_network("145.92.137.88/255.255.240.0",0)

print(net)
print(len(list(net)))
print(len(list(net.hosts())))

