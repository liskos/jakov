import ipaddress
ip1 = ipaddress.ip_address("193.138.70.47")
ip2 = ipaddress.ip_address("193.138.64.0")
for m in range(5,31):
    net = ipaddress.ip_network(f"193.138.70.47/{m}",0)
    if ip1 in net and ip2 in net:
        print(net,net.netmask)

print(bin(240)[2:])

