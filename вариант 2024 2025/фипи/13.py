import ipaddress
k = 0
net = ipaddress.ip_network("122.159.136.144/255.255.255.248",0)
for ip in net:
    if ip.__format__("b").count("1") % 4 != 0:
        k+=1

print(k)