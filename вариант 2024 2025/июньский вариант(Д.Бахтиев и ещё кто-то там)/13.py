import ipaddress
b = set()
for m in range(1,33):
    net = ipaddress.ip_network(f"192.214.116.184/{m}",0)
    for ip in net:
        if ip.__format__("b").count("1") % 5 == 0:
            b.add(net.netmask)
            break
print(len(b),b)
