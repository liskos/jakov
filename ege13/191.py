import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"111.7.92.52/{m}",0)
    print(net,net.netmask)

