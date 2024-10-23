
import ipaddress
for m in range(0,255):
    net = ipaddress.ip_network(f"196.233.{m}.52/255.255.255.248",0)
    if all(ip.__format__("b")[:16].count("1") > ip.__format__("b")[16:].count("1") for ip in net):
        print(net,m)
