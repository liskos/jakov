import ipaddress
ip1 = ipaddress.ip_address("121.171.ege15.149")
ip2 = ipaddress.ip_address("121.171.ege15.143")
for m in range(5,31):
    net = ipaddress.ip_network(f"121.171.ege15.143/{m}",0)
    if ip1 in net and ip2 in net:
        print(net,net.netmask)
        
print(2**(32-27))