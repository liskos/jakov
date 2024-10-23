import ipaddress
ip1 = ipaddress.ip_address("211.188.211.49")
ip2 = ipaddress.ip_address("211.188.200.115")
for m in range(15,31):

    net1 = ipaddress.ip_network(f"211.188.211.49/{m}",0)
    net2 = ipaddress.ip_network(f"211.188.200.115/{m}",0)
    if ip1 not in net2 and ip2 not in net1:
        if ip1 in list(net1)[1:-1] and ip2 in list(net2)[1:-1]:
               print(net1,net1.netmask)