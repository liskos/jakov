import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"118.105.136.60/{m}",0)
    print(net,net.netmask)

print(bin(248)[2:])