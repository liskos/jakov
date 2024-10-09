import ipaddress
for m in range(5,31):
    net = ipaddress.ip_network(f"217.138.127.144/{m}",0)
    print(net,net.netmask)