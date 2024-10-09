import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"120.120.120.35/{m}",0)
    print(net,net.netmask)

print(bin(248)[2:])