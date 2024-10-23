import ipaddress
ip1 = ipaddress.ip_address("193.45.192.104")
ip2 = ipaddress.ip_address("193.45.206.210")
for m in range(5,31):
    net = ipaddress.ip_network(f"193.45.192.104/{m}",0)
    if ip1 in net and ip2 in net:
        for ip in net:
            if ip.__format__("b").count("1") % 2 == 0:
                print(net,net.netmask)