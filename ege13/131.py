import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"156.133.216.35/{m}",0)
    print(net,net.netmask,net[0])
print(2**(32-26))