import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"111.81.208.27/{m}",0)
    print(net,net.netmask)
