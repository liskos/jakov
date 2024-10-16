import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"229.117.114.172/{m}",0)
    print(net,net.netmask)