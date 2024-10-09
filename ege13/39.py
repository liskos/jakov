import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"{m}/255.255.254.0",0)
    print(net, net.netmask)

#11111111 11111111 11111110 00000000

