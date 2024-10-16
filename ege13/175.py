import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"134.73.209.97/{m}",0)
    print(net,net.netmask)