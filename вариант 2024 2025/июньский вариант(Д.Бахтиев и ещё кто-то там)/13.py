import ipaddress
b = set()
k = 0
for m in range(0,33):
    net = ipaddress.ip_network(f"192.214.116.184/{m}",0)
    print(net[0], net[0].__format__("b").count("1"))

