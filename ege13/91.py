import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"108.87.113.106/{m}",0)
    print(net,net.netmask)

print(bin(240)[2:])