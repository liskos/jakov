import ipaddress
ip1 = ipaddress.ip_address("111.3.161.27")
for m in range(5,31):
    net = ipaddress.ip_network(f"111.3.161.27/{m}",0)
    print(net,net.netmask)

