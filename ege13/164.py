import ipaddress
k=0
net = ipaddress.ip_network("202.75.38.152/255.255.255.248",0)
for ip in net:
    if "111" not in ip.__format__("b"):
        k+=1
print(k)