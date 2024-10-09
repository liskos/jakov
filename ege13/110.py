import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"18.168.250.32/{m}",0)
    print(net,net.netmask)

print(bin(254)[2:])