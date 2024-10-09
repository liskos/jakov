import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"111.91.200.28/{m}",0)
    print(net,net.netmask)

print(bin(240)[2:])