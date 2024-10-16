import ipaddress
ip1 = ipaddress.ip_address("125.28.160.73")
for m in range(15,31):
    net = ipaddress.ip_network(f"125.28.160.73/{m}",0)
    print(net,net.netmask,ip1 in net.hosts(),2**(32 - m)-2)

print(2 **4)
print(2 ** 5)
print(2**6)
