import ipaddress
ip1 = ipaddress.ip_address("193.45.192.104")
ip2 = ipaddress.ip_address("193.45.206.210")
for m in range(15,31):

    net1 = ipaddress.ip_network(f"193.45.192.104/{m}",0)
    net2 = ipaddress.ip_network(f"193.45.206.210/{m}",0)
    if ip1 not in net2 and ip2 not in net1:
        if ip1 in list(net1)[1:-1] and ip2 in list(net2)[1:-1]:
               print(net1,net1.netmask)