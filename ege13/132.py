import ipaddress
ip1 = ipaddress.ip_address("112.117.107.70")
ip2 = ipaddress.ip_address("112.117.121.80")
for m in range(5,31):
    net = ipaddress.ip_network(f"112.117.121.80/{m}",0)
    if ip1 in net and ip2 in net:
        print(net,net.netmask)
print(2**(32-19))