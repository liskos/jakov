import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"120.216.74.153/{m}",0)
    print(net,net.netmask)

print(2**19)