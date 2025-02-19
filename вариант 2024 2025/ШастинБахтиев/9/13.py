import ipaddress
k = 0

net = ipaddress.ip_network(f"111.233.75.16/255.255.255.224",0)
print(net,net.netmask)
for ip in net:
    k+=1


print(k)

#255.255.255.224