import ipaddress
ip1 = ipaddress.ip_address("115.53.128.88")
for m in range(5,31):
    net = ipaddress.ip_network(f"115.53.128.88/{m}",0)
    print(net,net.netmask)

print(2**7)
print(2**8)
print(2**9)
print(2**10)