import ipaddress

for m in range(10,33):
    net = ipaddress.ip_network(f"222.190.122.24/{m}",0)
    print(net)

print(2**11-3)