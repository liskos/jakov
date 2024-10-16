import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"190.120.251.78/{m}",0)
    print(net,net.netmask)

print((32-24))