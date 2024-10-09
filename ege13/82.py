import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"15.51.208.15/{m}",0)
    print(net,net.netmask)
