import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"154.112.144.160/{m}",0)
    print(net,net.netmask)

print(bin(254)[2:])