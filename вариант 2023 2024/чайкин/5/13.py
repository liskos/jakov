import ipaddress
ip1 = ipaddress.ip_address("92.149.25.164")
ip2 = ipaddress.ip_address("92.149.37.2")
for m in range(5,31):
    net = ipaddress.ip_network(f"92.149.37.2/{m}",0)
    if ip1 in net and ip2 in net:
        print(net,net.netmask)

print(bin(192)[2:])