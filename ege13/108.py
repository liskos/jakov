import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"218.217.212.15/{m}",0)
    print(net,net.netmask)

print(bin(254)[2:])