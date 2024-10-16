import ipaddress
k = 0
net = ipaddress.ip_network("211.48.136.64/255.255.255.224",0)
for ip in net:
    if ip.__format__("b")[-2] == "0" and ip.__format__("b")[-1] == "0":
        k+=1
print(k)