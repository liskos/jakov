import ipaddress
ip1 = ipaddress.ip_address("154.28.80.25")
ip2 = ipaddress.ip_address("154.28.90.25")
for m in range(5,31):
    net = ipaddress.ip_network(f"154.28.80.25/{m}",0)
    if ip1 in net and ip2 in net:
        print(net,net.netmask)

print(bin(224)[2:])

