import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"90.155.69.100/{m}",0)
    print(net,net.netmask)