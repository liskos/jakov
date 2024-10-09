import ipaddress
ip1 = ipaddress.ip_address("215.118.70.47")
ip2 = ipaddress.ip_address("215.118.64.0")
for m in range(5,31):
    net = ipaddress.ip_network(f"215.118.64.0/{m}",0)
    if ip1 in net and ip2 in net:
        print(net,net.netmask)

print(bin(248)[2:])

