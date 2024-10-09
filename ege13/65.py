import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"220.128.114.142/{m}",0)
    print(net,net.netmask)