import ipaddress
ip1 = ipaddress.ip_address("154.63.206.129")
ip2 = ipaddress.ip_address("154.63.100.75")
for m in range(5,31):
    net = ipaddress.ip_network(f"154.63.206.129/{m}",0)
    if ip1 in net and ip2 in net:
        print(net,net.netmask)