import ipaddress

for m in range(1,33):
    net = ipaddress.ip_network(f"222.190.122.24/{m}",0)
    if net.network_address == "222.190.120.0":
        print(net.netmask)