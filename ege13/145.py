import ipaddress
ip1 = ipaddress.ip_address("198.75.95.31")
ip2 = ipaddress.ip_address("198.75.96.13")
for m in range(5,31):
    net1 = ipaddress.ip_network(f"198.75.95.31/{m}",0)
    net2 = ipaddress.ip_network(f"198.75.96.13/{m}",0)
    if ip1 not in net2 and ip2 not in net1:
        if ip1 in net1.hosts() and ip2 in net2.hosts():
            print(net1,net2,net1.netmask)