import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"148.228.120.242/{m}",0)
    print(net,net.netmask)
