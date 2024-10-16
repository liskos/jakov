import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"151.168.147.193/{m}",0)
    print(net,net.netmask)