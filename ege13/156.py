import ipaddress
ip1 = ipaddress.ip_address("188.214.176.25")
for m in range(5,31):
    net = ipaddress.ip_network(f"188.214.176.25/{m}",0)
    print(net,net.netmask)

print(2**5)
print(2**6)
print(2**7)
print(2**10)

8