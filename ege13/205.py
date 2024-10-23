import ipaddress
ip1 = ipaddress.ip_address("211.188.211.49")
ip2 = ipaddress.ip_address("211.188.200.115")
for m in range(5,31):
    net = ipaddress.ip_network(f"211.188.211.49/{m}",0)
    if ip1 in net and ip2 in net:
        print(net,net.netmask)