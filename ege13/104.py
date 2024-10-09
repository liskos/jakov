import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"192.168.104.15/{m}",0)
    print(net,net.netmask)

print(bin(248)[2:])