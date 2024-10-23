
import ipaddress
for m in range(16,25):
    net = ipaddress.ip_network(f"108.8.190.123/{m}",0)
    if all(ip.__format__("b")[:16].count("1") <= ip.__format__("b")[16:].count("1") for ip in net):
        print(net.netmask)
