import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"153.209.23.240/{m}",0)
    print(net,net.netmask)