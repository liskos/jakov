import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"203.155.64.98/{m}",0)
    print(net,net.netmask)

print(bin(128)[2:])