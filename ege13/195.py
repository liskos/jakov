import ipaddress
for m in range(16,25):
    net = ipaddress.ip_network(f"117.157.2.8/{m}",0)
    f = True
    for ip in net:
        if ip.__format__("b")[:16].count("1") < ip.__format__("b")[16:].count("1"):
            f = False
    if f:
        print(net.netmask)

# import ipaddress
# for m in range(16,25):
#     net = ipaddress.ip_network(f"117.157.2.8/{m}",0)
#     if all(ip.__format__("b")[:16].count("1") >= ip.__format__("b")[16:].count("1") for ip in net):
#         print(net.netmask)
