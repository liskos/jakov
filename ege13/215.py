import ipaddress
ip1 = ipaddress.ip_address("211.188.211.49")
ip2 = ipaddress.ip_address("211.188.200.115")
for m in range(15,31):
    net = ipaddress.ip_network(f"211.188.211.49/{m}",0)
    if ip2 in list(net)[1:-1] and ip1 in list(net)[1:-1]:
        k = 0
        for ip in net:
            if ip.__format__("b").count("1") % 2 != 0:
                k+= 1
        print(net,k)