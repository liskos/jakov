import ipaddress
ip1 = ipaddress.ip_address("175.122.80.13")
for m in range(5,31):
    net = ipaddress.ip_network(f"175.122.80.13/{m}",0)
    print(net,net.netmask)

print(2**7)
print(2**8)
print(2**9)
print(2**10)
