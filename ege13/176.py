import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"180.2.252.76/{m}",0)
    print(net,net.netmask)