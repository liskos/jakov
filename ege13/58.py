import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"134.92.108.145/{m}",0)
    print(net,net.netmask)