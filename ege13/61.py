import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"158.198.104.220/{m}",0)
    print(net,net.netmask)