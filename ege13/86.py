import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"156.32.140.138/{m}",0)
    print(net,net.netmask)

print(bin(240)[2:])