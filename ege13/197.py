
import ipaddress
for m in range(16,25):
    net = ipaddress.ip_network(f"134.97.250.117/{m}",0)
    if all(ip.__format__("b")[:16].count("0") >= ip.__format__("b")[16:].count("0") for ip in net):
        print(net.netmask)
