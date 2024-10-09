import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"241.185.253.57/{m}",0)
    print(net,net.netmask)