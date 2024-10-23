import ipaddress
ip1 = ipaddress.ip_address("176.213.225.119")
ip2 = ipaddress.ip_address("176.213.195.58")
for m in range(5,31):
    net = ipaddress.ip_network(f"176.213.225.119/{m}",0)
    if ip1 in net and ip2 in net:
        print(net,net.netmask)