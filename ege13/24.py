import ipaddress
net = ipaddress.ip_network("12.16.196.10/255.255.224.0", 0)
print(net)
print(list(net))
for ip in net:
    print(ip.packed[0].__format__("b"), ip.packed[1], ip.packed[2], ip.packed[3])