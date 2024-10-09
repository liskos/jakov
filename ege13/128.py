import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"108.133.75.91/{m}",0)
    print(net,net.netmask)

print(2**(32-26))