import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"151.181.88.129/{m}",0)
    print(net,net.netmask)

print(bin(254)[2:])