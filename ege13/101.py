import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"220.127.169.27/{m}",0)
    print(net,net.netmask)

print(bin(224)[2:])