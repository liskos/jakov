import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"117.191.88.37/{m}",0)
    print(net,net.netmask)